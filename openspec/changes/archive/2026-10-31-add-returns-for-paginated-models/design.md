# Design

## Context

- See proposal.md "Why" for the audit and the empty-iterator failure mode. Requirements are in `specs/paginated-list-responses/spec.md` and `specs/integration-testing/spec.md`.
- Spec generation (canvas-lms `lib/swagger_yard/canvas_adapter.rb`): `process_returns_tags` → `track_operation_model` records `{model, is_array}` per operation id only when `model_schema_exists?(model_name)`. Later, `open_api_generator.rb#replace_responses_with_schema_refs!` rewrites the response schema to a `$ref`, or to `array` of `$ref`. When the model is not found, the response stays `array<object>` / `object`. When there is no `@returns` at all, the response has no `content`.
- Alias routes for one action (`RubricsApi-index` and `RubricsApi-index_for_courses`; `LtiApps-launch_definitions` and `…_for_accounts`) are emitted from a single YARD docstring and both get the `$ref`. This is already true for `RubricsApi-show` and `RubricsApi-show_for_courses`. One annotation per action is therefore enough.
- `model_schema_exists?` looks up the literal `@returns` name, while component schemas are keyed with `::` replaced by `_` (`canvas_adapter.rb:313/320`). `Lti::LaunchDefinition` is therefore never resolved.
- Shapes verified against controller bodies:
  - `appointment_groups#index` renders `groups.map { appointment_group_json }`, which is an array.
  - `#users` / `#groups` go through `participants(type)`, which renders an array of `user_json` / `group_json`, or `[]` when `participant_type` differs.
  - `rubrics_api#index` renders `rubrics_json(...)`, which is an array.
  - `lti_apps#launch_definitions` renders `AppLaunchCollator.launch_definitions(...)`, which is an array of hashes documented by `@model Lti::LaunchDefinition` in the same controller.
- The integration `CANVAS_API_TOKEN` belongs to a seeded observer (README). An observer cannot list account rubrics, account LTI launch definitions, or manageable appointment groups.

## Goals / Non-Goals

**Goals:**
- Make the 7 operations yield data, with typed models wherever the generator can resolve the model today.
- Add a guard so that a newly undocumented paginated endpoint fails the offline suite instead of shipping silently.

**Non-Goals:**
- Fixing namespaced model resolution in the generator. That needs its own change, because it also re-types every operation behind the 33 existing `@returns …Lti::…` annotations and changes their public return types.
- Wrapped and JSON-API responses, endpoints with no model, and the `users/self/todo` mis-attribution (see proposal.md "Out of scope").
- Changing the `_paginated` template to warn or raise on an empty types map. The offline test covers detection without changing runtime behavior.

## Decisions

### D1: Annotate canvas-lms controllers, then regenerate
This uses the same approach as `add-observee-integration-tests` D1. Add one `# @returns [Model]` comment line per action, as the last tag in the doc block, directly above `def`. For `RubricsApiController#index`, there is a blank (non-comment) line between the doc block and `def index`. Put the tag in the comment block and leave the blank line alone.
- *Alternative: hand-edit `canvas.openapi.yaml`.* The next `rake doc:openapi` would overwrite it.
- *Alternative: hand-edit the generated Python.* The next client regeneration would overwrite it.

### D2: Annotate LTI with the namespaced name now, even though it resolves to `object`
Write `@returns [Lti::LaunchDefinition]`, which is the model's real YARD name and matches existing usage such as `@returns [Lti::Deployment]`. Today this produces `array<object>`. That is enough to move the operation from "yields nothing" to "yields dicts". When the namespace fix lands, these operations become typed with no further controller edit.
- *Alternative: write `@returns [Lti_LaunchDefinition]` to get a typed model now.* This depends on an internal naming artifact of the generator, puts a non-Ruby name into Canvas docs, and would diverge from every other LTI annotation.
- *Alternative: leave LTI out.* The operations would stay broken (no items), and once the generator bug is fixed the annotation would still be needed.

### D3: Offline guard by inspecting generated `_paginated` methods
`test_paginated_response_types.py` imports every module in `canvas_lms_python_client.api`, finds each `*_paginated` coroutine function, and reads its source with `inspect.getsource`. It treats the operation as undocumented when the `_response_types_map` literal is empty (`{` followed only by whitespace and `}`). The test compares the set of undocumented operations with a module-level `UNDOCUMENTED_PAGINATED_OPERATIONS` frozenset in both directions:
- If an undocumented operation is not in the allowlist, the test fails and lists the operation names.
- If an allowlisted operation now has a types map, the test fails and names it as stale.

The initial allowlist is the 32 operations left after this change, keyed by method base name (for example `appointment_groups_index`).
- *Alternative: parse `canvas.openapi.yaml` in the test.* The spec lives in a sibling repo that may not be checked out, and the generated code is what users run.
- *Alternative: call each `_paginated` method against a mocked HTTP response.* This takes far more scaffolding to answer the same question.

### D4: Separate admin client fixture; integration tests skip when data is missing
Add `canvas_admin_api_client` to `conftest.py`, mirroring `canvas_api_client` but reading `CANVAS_ADMIN_API_TOKEN` and skipping with a reason that names it. `test_integration_paginated_models.py` (`pytestmark = pytest.mark.integration`) uses only the admin client:
- **Rubrics:** use the first account from `AccountsApi` list (the admin's root account) and `rubrics_api_index_all(account_id=…)`. For the course variant, use the first course from the account's courses that has a rubric.
- **Appointment groups:** call `appointment_groups_index_all(scope="manageable")`. For the first group, list `users` or `groups` according to its `participant_type`, and assert that the other participant type returns `[]`.
- **LTI:** call `lti_apps_launch_definitions_all(course_id=…)` and `…_for_accounts_all(account_id=…)`. Assert each item is a `dict` containing `definition_type` and `definition_id`.
- **Multi-page:** run each typed listing again with `per_page=1` when there are 2 or more items, and compare id sets.

When the seeded instance has none of a resource, the test calls `pytest.skip` with a reason naming the missing data.
- *Alternative: reuse the observer token and skip on 401/403.* That hides permission and seeding problems behind generic skips, and these endpoints would rarely run.
- *Alternative: seed data from the tests.* That turns the tests into writers, which goes against the read-only stance of the existing integration suite.

## Risks / Trade-offs

- [The live JSON does not match the `@model` (for example a nullable field typed as a strict non-null `StrictInt`), so the newly typed operations raise `ValidationError` where they used to return nothing] → The integration tests surface this. Record each mismatch as a follow-up against the model's `@model` doc. Do not loosen the models or drop the annotation. If a mismatch blocks one endpoint, it can be moved back to the allowlist with a comment.
- [The seeded instance has no appointment groups, LTI tools, or rubrics, so the integration tests only ever skip] → Task 4.1 records what the seed contains. If something is missing, the follow-up is a seed script, which is outside this change.
- [Spec regeneration brings unrelated churn from other canvas-lms edits] → Review the spec diff. Only the 7 operations' `responses` should change.
- [The `inspect.getsource` regex depends on template output formatting] → The templates in `mustache-templates/` are owned by this repo. Add a sanity assertion that at least 150 `_paginated` methods were found, so the test fails loudly if the template's formatting changes and the scan stops matching.

## Migration Plan

1. Commit the canvas-lms annotations and regenerated spec in the fork.
2. Regenerate the client and commit the generated changes together with the new tests.

Rollback means reverting both commits. No runtime config or data is involved.
