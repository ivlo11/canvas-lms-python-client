# Tasks

## 1. Infer wrapped list responses in the Canvas adapter (canvas-lms fork)

- [x] 1.0 Before regenerating, copy the current `public/doc/openapi/canvas.openapi.yaml` (produced by the earlier generator-based step) to the scratchpad as the 1.5 baseline. Then revert the generator approach: restore `lib/swagger_yard/open_api_generator.rb` with `git checkout`, and delete `spec/lib/swagger_yard/open_api_generator_spec.rb`. Verify that `git status` shows neither file changed or present.
- [x] 1.1 In `spec/lib/swagger_yard/canvas_adapter_spec.rb`, add failing examples as in design D4:
  - Helpers (with `canvas_schemas` set directly):
    - `wrapped_list_example` matches a quoted key and an unquoted key (`outcome_results: [OutcomeResult]`).
    - It resolves `Lti::Thing` to `Lti_Thing`.
    - It returns `nil` for an unknown model, a literal-JSON example and a multi-key example.
    - `register_wrapper_schema` adds the D2 schema with no `required`.
    - It reuses an identical schema for a second operation.
    - It returns `nil` and does not overwrite an existing, different schema.
  - Hook (`process_canvas_tags` on a `YARD::Docstring`):
    - With no `@returns`, `operation_models[op_id]["200"]` is `{model: "<Key>Response", is_array: false}`, the operation has a response type, and the operation id is in `wrapped_list_operations`.
    - With a `@returns` present, nothing is inferred.
    - The example is still stored in `canvas_examples`.
  - Generator wiring: a tracked wrapper run through `add_canvas_schemas!` and `replace_responses_with_schema_refs!` gets a `$ref` to the wrapper.

  Verify with `bin/rspec spec/lib/swagger_yard/canvas_adapter_spec.rb` in the web container that the new examples fail because the helpers or hook are missing.
- [x] 1.2 Implement the helpers, `WRAPPED_LIST_EXAMPLE`, `wrapped_list_operations` storage (reset in `load_canvas_routes!`), and the `process_example_response_tag` hook, as in design D1 and D2. Verify that the 1.1 specs pass and that `bin/rspec spec/lib/swagger_yard/` passes as a whole.
- [x] 1.3 Run `bin/rubocop lib/swagger_yard/canvas_adapter.rb spec/lib/swagger_yard/canvas_adapter_spec.rb` and verify it is clean.
  - (Amended:) The new code adds no offenses. The 14 remaining offenses were already there at HEAD: 12 `RSpec/RepeatedDescription` and 1 `RSpec/BeforeAfterAll` in the spec, and 1 `Rails/Output` in the route-naming fallback. They are out of scope.
- [x] 1.4 Regenerate the spec in the web container (`bundle exec rake doc:openapi`). Check `public/doc/openapi/canvas.openapi.yaml`:
  - The 6 new component schemas exist: `PollsResponse`, `PollSessionsResponse`, `PollChoicesResponse`, `QuizIpFiltersResponse`, `QuizSubmissionsResponse`, `OutcomeResultsResponse`.
  - The 8 operations' success responses `$ref` them.
  - In total, there are 14 wrapper schemas and 42 `$ref`s, including the 34 non-paginated operations listed in the proposal.
  - `GradingPeriodSets-index` and `QuizSubmissionEventsApi-index` still have no `schema`.
- [x] 1.5 Compare against the 1.0 baseline and verify that the spec is semantically identical: same schemas, same response schemas, same examples. Investigate any difference, for example a response description or a `default`/`200` key. If the specs are identical, the client regenerated in section 2 does not need regenerating again.
- [x] 1.6 Commit in the fork following its commit guidelines (lines under 60 chars, include the why). Verify with `git log -1 --stat`: only `canvas_adapter.rb`, its spec, and (if tracked) the regenerated spec are changed. There should be no controller files and no `open_api_generator.rb` change.

## 2. Generate `_all` only for list responses (canvas-lms-python-client template)

- [x] 2.1 In `mustache-templates/api.mustache`, wrap the `_all` method block in `{{#isArray}}…{{/isArray}}`. Then simplify its return annotation to `AsyncIterator[{{returnProperty.items.dataType}}]` and remove the `if not isinstance(_page_data, list)` lines, as in design D3. Verify by reading the template diff: `_paginated` and the base method are untouched.
- [x] 2.2 Regenerate the client (`openapi-generator-cli generate` with `openapi-generator-config.yaml`, `-t mustache-templates`, `-o src`). Verify:
  - `polls_index`, `poll_sessions_index`/`_opened`/`_closed`, `poll_choices_index`, `quiz_ip_filters_index`, `quiz_submissions_api_index` and `outcome_results_index` return their `*Response` wrapper, and their `_paginated` returns `AsyncIterator[<Wrapper>]`.
  - None of them has `_all`.
  - `terms_api_index`, `registrations_list` and `rubrics_api_used_locations` have no `_all`.
  - `appointment_groups_index_all` still exists.
  - `git status` shows no change to the custom files in `src/.openapi-generator-ignore`.
- [x] 2.3 In `test/test_paginated_response_types.py`, add `test_all_iterator_only_for_list_responses`. For every API class, `<op>_all` must exist if and only if `<op>_paginated`'s return annotation is `AsyncIterator[List[...]]`, and the test reports offenders by name. Verify that it passes on the regenerated client. Then temporarily delete one `{{#isArray}}` guard, regenerate one API module (or monkeypatch an attribute), confirm the test fails naming it, and revert.
- [x] 2.4 Add a "Breaking changes" note to the README describing the removed `_all` methods and the replacement (iterate `_paginated` pages and read the wrapper's list attribute). Verify that the example in the note runs against the generated `PollsResponse` model in a Python snippet.

## 3. Wrapper deserialization and allowlist (canvas-lms-python-client)

- [x] 3.1 Run the guard test. Confirm it fails, naming exactly the 8 operations as stale allowlist entries. Remove them, leaving 24 including `grading_period_sets_index` and `quiz_submission_events_api_index`. Verify that the test passes.
- [x] 3.2 Add parametrized offline tests in `test_paginated_response_types.py` for the 14 wrappers (amended from 6):
  - `from_json` of a sample page (`{"<key>": [<minimal valid item>]}`) yields a list of the item model.
  - `from_json("{}")` yields a wrapper whose attribute is `None` and raises no error.

  Verify that they pass.
- [x] 3.3 Verify that the full offline suite passes with `pdm run pytest`, with only integration tests skipped.
  - (Amended:) This needed an `api_test.mustache` fix: non-list tests call `_paginated`. It also needed the generated `test_*_api.py` files to be deleted and regenerated (see design D3). The 140 existing "requires initialization parameters" skips in generated tests are unchanged from HEAD.

## 4. Integration coverage (canvas-lms-python-client)

- [x] 4.1 In `test/test_integration_paginated_models.py` (admin client), add `test_polls_pages_typed` and `test_quiz_submissions_pages_typed`. They iterate `_paginated` and assert each page is the wrapper model and each item is a `Poll`/`QuizSubmission` with an int `id` (when `id` is typed int in the model). Quiz submissions needs a course and a quiz found via the existing course listing. Skip with a named reason when there is no data. Verify with `pdm run pytest --integration -m integration -v` that each test passes or skips with its reason. Record any strict-model `ValidationError` as a follow-up naming the model and field.
  - (Result, 2026-11-01:) First run: both tests skipped, because the seeded instance had no polls or quizzes. `spec/manual_seeding/large_gradebook_seeds.rb` now also creates a poll (with choices and a session) for each account admin, and a "Checkpoint Quiz" with 5 graded submissions. It was run once, creating course 6, poll 1 and quiz 1.
  - (Result after seeding:) Both tests **fail on strict item models**. The wrapper pages deserialize correctly every time; the failures are Canvas `@model` docs that don't match live data. Following the design's Risks policy, the models are not loosened. The failures are listed under Workflow follow-up.

## 5. Final checks

- [x] 5.1 Run `pdm run ruff check src/canvas_lms_python_client/test/test_paginated_response_types.py src/canvas_lms_python_client/test/test_integration_paginated_models.py` and verify it is clean.
- [x] 5.2 Run `openspec validate type-wrapped-paginated-responses --strict` and verify it passes.

## Workflow follow-up

- ~~Decide the `packageVersion` bump~~ Resolved: no bump, because the client has never been published (design Open Questions).
- Commit the client after the canvas-lms fork commit (task 1.6).
- Follow-ups:
  - fix the GradingPeriodSets and QuizSubmissionEvent docs (key, model name, missing fields), possibly upstream to instructure/canvas-lms
  - `additionalProperties` for undocumented keys
  - wrapped endpoints without examples (pace contexts, authentication audit)
  - Canvas `@model` docs that disagree with live data, found by 4.1 (course 6, poll 1, quiz 1). Fix them in the fork's controller docs, possibly upstream:
    - `Poll.id`, `Poll.user_id`, `PollChoice.id`: documented as integer. The polling JSON-API serializer sends string ids (`"1"`).
    - `PollChoice.poll_id`: required integer, but it is `null` in `poll_choices` listings.
    - `PollSession.poll_submissions`: documented as a single `PollSubmission`, but sent as an array (`[]`).
    - `QuizSubmission.score`, `QuizSubmission.kept_score`: documented as integer, but sent as floats (`0.0`).
    - `Quiz.points_possible`: documented as integer, but sent as a float (`10.0`). This model was already typed before this change, and `test_quiz_submissions_pages_typed` fails here, while listing quizzes, before it reaches quiz submissions.
- Archive with `/opsx:archive` after review.
