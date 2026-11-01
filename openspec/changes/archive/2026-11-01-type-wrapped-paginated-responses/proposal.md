# Proposal

## Why

Eight paginated Canvas list endpoints return each page as a JSON object that wraps the items, for example `{"polls": [...]}`. Their controllers have no `@returns`, so the generated client has an empty response types map and the iterators finish without yielding anything. Canvas does document each wrapper, in the `@example_response`, using a regular `{ "<key>": [<Model>] }` form that names an existing model. canvas-lms is not our product, so the spec should describe these responses the way Canvas documents them, without us writing their wrapper docs. Separately, the client generates an `_all` item iterator for every paginated operation, even when a page is not a list. For the 12 operations that already return a typed wrapper (for example `terms_api_index` returns `EnrollmentTermsList`), `_all` yields the whole wrapper once per page, which misleads callers.

## What Changes

- **canvas-lms adapter (fork):** in `lib/swagger_yard/canvas_adapter.rb`, when an operation has no `@returns` and its `@example_response` is exactly the form `{ "<key>": [<Model>] }`, with `<Model>` naming a collected `@model` schema, treat the example as an implied `@returns`. The adapter registers a wrapper schema with one optional property `<key>` (an array of `$ref <Model>`), gives the operation a response type, and tracks the wrapper as the operation's model. The generator's existing schema and `$ref` steps then type the response, so `open_api_generator.rb` is unchanged. Anything that doesn't fit that pattern, or whose model doesn't resolve, is left unchanged. No controller doc is edited.
- The rule types these 8 paginated operations:

  | Operation(s) | Example | Wrapper schema |
  |---|---|---|
  | `Polls-index` | `"polls": [Poll]` | `PollsResponse` |
  | `PollSessions-index`, `-opened`, `-closed` | `"poll_sessions": [PollSession]` | `PollSessionsResponse` (shared) |
  | `PollChoices-index` | `"poll_choices": [PollChoice]` | `PollChoicesResponse` |
  | `QuizIpFilters-index` | `"quiz_ip_filters": [QuizIPFilter]` | `QuizIpFiltersResponse` |
  | `QuizSubmissionsApi-index` | `"quiz_submissions": [QuizSubmission]` | `QuizSubmissionsResponse` |
  | `OutcomeResults-index` | `outcome_results: [OutcomeResult]` | `OutcomeResultsResponse` |

- The rule is not limited to paginated operations. It also types 34 non-paginated operations whose examples use the same form. Canvas returns these wrapped too (JSON-API style). This was approved during implementation, after regeneration showed 42 matches instead of 8:

  | Wrapper schema | Additional (non-paginated) operations |
  |---|---|
  | `PollsResponse` | `Polls-create`, `-show`, `-update` |
  | `PollSessionsResponse` | `PollSessions-create`, `-show`, `-update`, `-open`, `-close` |
  | `PollChoicesResponse` | `PollChoices-create`, `-show`, `-update` |
  | `QuizSubmissionsResponse` | `QuizSubmissionsApi-create`, `-submission`, `-show`, `-update`, `-complete` |
  | `PollSubmissionsResponse` | `PollSubmissions-show`, `-create` |
  | `GradingPeriodsResponse` | `GradingPeriods-index`, `-index_for_courses`, `-show`, `-update`, `-batch_update`, `-batch_update_for_other` |
  | `QuizGroupsResponse` | `QuizGroups-index`, `-create`, `-update` |
  | `ResultsResponse` | `Results-index`, `-create` |
  | `QuizExtensionsResponse` | `QuizExtensions-create`, `CourseQuizExtensions-create` |
  | `AssignmentExtensionsResponse` | `AssignmentExtensions-create` |
  | `QuizStatisticsResponse` | `QuizStatistics-index` |
  | `QuizSubmissionQuestionsResponse` | `QuizSubmissionQuestions-index` |

  Altogether that is 42 operations and 14 wrapper schemas. These operations have no `_paginated`/`_all`, so the only client effect is that their single-call method now returns the wrapper model instead of `None`.

- **Client template:** generate `<op>_all` only when the operation's response is a list. `<op>` and `<op>_paginated` are still generated for every paginated operation. `_paginated` keeps following `Link` headers and yields each page as the documented wrapper model.
  - **BREAKING:** `_all` is removed from every paginated operation whose response is not a list. On the current client that is 44 operations: 10 that return typed wrappers (`terms_api_index`, `registrations_list`, `quiz_assignment_overrides_index`, `quiz_assignment_overrides_new_quizzes`, the 6 `learning_object_dates_show*`), the 2 `rubrics_api_used_locations*` (`object`), and 32 undocumented operations. After this change, the 8 above also have no `_all`. Undocumented operations regain `_all` automatically once they are documented as lists.
- **Client tests:** remove the 8 operations from the guard allowlist, and add offline tests for the `_all` rule and for wrapper deserialization.

## Capabilities

### New Capabilities
<!-- None. -->

### Modified Capabilities
- `paginated-list-responses`: adds two requirements. Wrapped list responses yield typed wrapper pages from the page iterator. The all-items iterator exists only for list responses. Existing requirements are unchanged.

## Impact

- **canvas-lms (fork):** `lib/swagger_yard/canvas_adapter.rb` gains the example-response inference (public helpers plus a hook in `process_example_response_tag`), with specs in `spec/lib/swagger_yard/canvas_adapter_spec.rb`. `open_api_generator.rb` is unchanged. The regenerated `public/doc/openapi/canvas.openapi.yaml` gains 14 component schemas and 42 response `$ref`s. Canvas runtime behavior does not change.
- **canvas-lms-python-client:**
  - `mustache-templates/api.mustache`: the `_all` block is now conditional.
  - Regenerated: 6 new wrapper models, and `polls_api`, `poll_sessions_api`, `poll_choices_api`, `quiz_ip_filters_api`, `quiz_submissions_api_api`, `outcome_results_api` return wrappers. `_all` is removed wherever the response is not a list. `docs/` is regenerated with the new models.
  - `test/test_paginated_response_types.py`: 8 entries leave the allowlist (32 → 24). New offline tests are added there.
- **Data not captured:** Canvas sends keys the examples don't document (`meta` for polls, `quizzes`/`submissions`/`users` for quiz submissions with `include[]`, `linked` for outcome results). The wrapper models don't include them, so they are dropped, the same as for every model today. Keeping unknown keys (`additionalProperties`) is a separate follow-up.
- **Out of scope (follow-ups):**
  - `GradingPeriodSets-index`: the example uses the wrong key (`grading_period_set` vs the actual `grading_period_sets`) and a model name that doesn't resolve (`GradingPeriodGroup`). The `GradingPeriodSets` model also lacks `id`, `grading_periods`, `account_id`, `course_id`, `permissions` and `created_at`.
  - `QuizSubmissionEventsApi-index`: the example is literal JSON rather than `[Model]`, and `QuizSubmissionEvent` lacks `id`.
  - Both need corrections to Canvas's docs, which could be upstreamed to instructure/canvas-lms. The rule skips both automatically, and they stay on the allowlist.
  - Wrapped endpoints with no example (`PaceContextsApi-index`, the 3 `AuthenticationAuditApi-*`) are not touched.
