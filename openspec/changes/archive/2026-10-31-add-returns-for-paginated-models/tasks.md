# Tasks

## 1. Offline guard for undocumented paginated operations (canvas-lms-python-client)

- [x] 1.1 Create `src/canvas_lms_python_client/test/test_paginated_response_types.py` as described in design D3. It should scan every `canvas_lms_python_client.api` module for `*_paginated` methods and collect those whose `_response_types_map` literal is empty. It compares that set with a module-level `UNDOCUMENTED_PAGINATED_OPERATIONS` frozenset in both directions (unlisted undocumented operations fail; stale allowlist entries fail) and asserts at least 150 `_paginated` methods were found. Seed the allowlist with all 39 currently undocumented operations: the 32 below plus `appointment_groups_index`, `appointment_groups_users`, `appointment_groups_groups`, `rubrics_api_index`, `rubrics_api_index_for_courses`, `lti_apps_launch_definitions`, `lti_apps_launch_definitions_for_accounts`. Verify that `pdm run pytest src/canvas_lms_python_client/test/test_paginated_response_types.py` passes against the current client.
  - The 32: `authentication_audit_api_for_account`, `authentication_audit_api_for_login`, `authentication_audit_api_for_user`, `conversations_batches`, `courses_bulk_user_progress`, `courses_todo_items`, `discussion_topics_api_entries`, `discussion_topics_api_entries_for_groups`, `discussion_topics_api_entry_list`, `discussion_topics_api_entry_list_for_groups`, `discussion_topics_api_replies`, `discussion_topics_api_replies_for_groups`, `grading_period_sets_index`, `outcome_results_index`, `pace_contexts_api_index`, `planner_index`, `planner_index_for_users`, `poll_choices_index`, `poll_sessions_closed`, `poll_sessions_index`, `poll_sessions_opened`, `polls_index`, `pseudonyms_index`, `pseudonyms_index_for_users`, `quiz_ip_filters_index`, `quiz_submission_events_api_index`, `quiz_submissions_api_index`, `search_all_courses`, `search_recipients`, `search_recipients_for_other`, `service_credentials_todo_items`, `submissions_api_multiple_gradeable_students`.
- [x] 1.2 Prove that the guard detects both failure modes. Temporarily remove one entry from the allowlist and confirm the test fails naming it. Then temporarily add a typed operation (for example `history_index`) and confirm the test fails naming it as stale. Revert both edits and verify the test passes again.
- [x] 1.3 Add `test/test_paginated_response_types.py` to `src/.openapi-generator-ignore` and to the README's "Custom, never overwritten" list. Verify by grepping both files for the path.

## 2. Annotate controllers and regenerate the spec (canvas-lms fork)

- [x] 2.1 Add the `@returns` lines from proposal.md "What Changes" as the last tag of each doc block: `AppointmentGroupsController#index` (`[AppointmentGroup]`), `#users` (`[User]`), `#groups` (`[Group]`), `RubricsApiController#index` (`[Rubric]`, placed inside the comment block above the existing blank line), and `Lti::LtiAppsController#launch_definitions` (`[Lti::LaunchDefinition]`, using the module's 4-space comment indent). Verify that `git diff --stat` shows exactly 5 added comment lines across 3 files and no other changes.
- [x] 2.2 In the canvas-lms docker web container, run `bundle exec rake doc:openapi`. Verify in `public/doc/openapi/canvas.openapi.yaml` that `AppointmentGroups-index`, `-users`, `-groups`, `RubricsApi-index`, and `-index_for_courses` now have `schema: {type: array, items: {$ref: '#/components/schemas/<Model>'}}`. Also verify that both `LtiApps-launch_definitions*` operations have `type: array, items: {type: object}`, and that any other spec diff is reviewed and unrelated to these operations.
- [x] 2.3 Commit in the canvas-lms fork, following that repo's commit guidelines (lines under 60 chars, include the why). Verify with `git log -1 --stat`.

## 3. Regenerate the client (canvas-lms-python-client)

- [x] 3.1 Regenerate with `openapi-generator-cli generate` using `openapi-generator-config.yaml`, `-t mustache-templates`, and `-o src`. Verify that the base methods of `appointment_groups_index`/`_users`/`_groups` and `rubrics_api_index`/`_index_for_courses` return `List[AppointmentGroup|User|Group|Rubric]`, that `_paginated` returns `AsyncIterator[List[…]]`, and that `_all` returns `AsyncIterator[…]`. Verify that `lti_apps_launch_definitions*` return `List[object]` / `AsyncIterator[List[object]]` / `AsyncIterator[object]`. Verify that `git status` shows no change to `conftest.py`, `test_pagination.py`, `test_integration_observees.py`, `test_paginated_response_types.py`, or `pagination.py`.
- [x] 3.2 Run the guard test and confirm it fails, naming exactly the 7 fixed operations as stale allowlist entries. Remove them from `UNDOCUMENTED_PAGINATED_OPERATIONS`, leaving the 32. Verify that the test passes.
- [x] 3.3 Verify that the full offline suite passes with `pdm run pytest`, with only integration tests reported as skipped.

## 4. Admin credentials for integration tests (canvas-lms-python-client)

- [x] 4.1 In `test/conftest.py`, add a session fixture `canvas_admin_api_token` (reading `CANVAS_ADMIN_API_TOKEN`) and an async `canvas_admin_api_client` fixture that mirrors `canvas_api_client`. It skips with a reason naming each missing variable among `CANVAS_BASE_URL` and `CANVAS_ADMIN_API_TOKEN`, and otherwise yields an `ApiClient` opened with `async with`. Verify that `pdm run pytest --integration -rs` with `CANVAS_ADMIN_API_TOKEN` unset reports admin-client tests as skipped with that variable named, while observee tests still run.
- [x] 4.2 Update the README "Integration Tests" section: add `CANVAS_ADMIN_API_TOKEN` to the environment-variable table (optional; a seeded account admin's token), explain that admin-scoped tests skip without it, and add `test/test_integration_paginated_models.py` to the "Custom, never overwritten" list. Verify that the documented command and variable names match conftest.
- [x] 4.3 Add `test/test_integration_paginated_models.py` to `src/.openapi-generator-ignore`. Verify by grepping for the path.

## 5. Integration tests for the newly typed operations (canvas-lms-python-client)

- [x] 5.1 Start the seeded docker canvas-lms and, as an admin, record which test data exists: an account rubric, a course rubric, a manageable appointment group (and its `participant_type`), and an LTI tool with a launch placement in some course or account. Record the findings in this task's notes. Missing data is a follow-up for seeding, not a blocker.
  - Notes (2026-10-31, read-only `rails runner` in the web container): root accounts `Site Admin` (2) and `demo-dashboard` (1), 2 root-account admins. No rubrics in any context, no appointment groups, no active external tools. Every 5.3–5.5 test is expected to skip with a data reason until a seed script adds a rubric (account and course), an appointment group, and an LTI tool with a launch placement (follow-up).
- [x] 5.2 Create `test/test_integration_paginated_models.py` with `pytestmark = pytest.mark.integration`, using only `canvas_admin_api_client`. Add helpers that collect `_all` iterators into lists and that skip with a named reason when a listing is empty. Verify that `pdm run pytest -rs` reports the module as skipped.
- [x] 5.3 Add rubric tests: `test_account_rubrics_typed` and `test_course_rubrics_typed`. Each item must be a `Rubric` with an int `id`. Add a `per_page=1` comparison of id sets when there are 2 or more items. Verify that the tests pass, or skip with a "no rubric" reason, with `--integration`.
- [x] 5.4 Add appointment group tests: `test_appointment_groups_typed` (`scope="manageable"`, each item an `AppointmentGroup` with an int `id`) and `test_appointment_group_participants_typed` (matching participant type yields `User` or `Group` models with int `id`, the other type yields `[]`). Verify that they pass, or skip with a named reason.
- [x] 5.5 Add LTI tests: `test_course_launch_definitions_yield_items` and `test_account_launch_definitions_yield_items`. Each item must be a `dict` containing `definition_type` and `definition_id`. Verify that they pass, or skip with a named reason.
- [x] 5.6 Run `pdm run pytest --integration -m integration -v` with `CANVAS_BASE_URL`, the observer `CANVAS_API_TOKEN`, and `CANVAS_ADMIN_API_TOKEN` set. Verify that every test passes or skips with a named data reason, and that the existing observee tests still pass. Record any strict-model `ValidationError` as a follow-up naming the model and field. Do not loosen the model.
  - Notes (2026-10-31): 3 observee tests passed, `test_observees_pagination` skipped (observer has fewer than 2 observees). All 6 admin tests skipped with data reasons (no rubric, appointment group, or LTI launch placement seeded). No `ValidationError` raised. Seeding these resources is a follow-up.

## 6. Final checks

- [x] 6.1 Run `pdm run ruff check` on `conftest.py`, `test_paginated_response_types.py`, and `test_integration_paginated_models.py`, and verify it is clean.
- [x] 6.2 Run `openspec validate add-returns-for-paginated-models --strict` and verify it passes.

## Workflow follow-up

- Commit the regenerated client and tests in canvas-lms-python-client after the canvas-lms fork commit (task 2.3).
- Open follow-up changes for:
  - namespaced `@returns [Lti::…]` resolution in `canvas_adapter.rb#model_schema_exists?`
  - wrapped and JSON-API paginated responses
  - endpoints that have no `@model`
  - the `users/self/todo` operation mis-attribution
- Archive with `/opsx:archive` after review.
