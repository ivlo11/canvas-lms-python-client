# Tasks

## 1. Integration test harness (canvas-lms-python-client)

- [x] 1.1 In `src/canvas_lms_python_client/test/conftest.py`, add the `--integration` option (`pytest_addoption`) and `pytest_collection_modifyitems` so that `@pytest.mark.integration` items are skipped with reason "use --integration to run" unless the flag is passed. Verify with a throwaway marked test: `pdm run pytest -rs` shows it skipped, and `pdm run pytest --integration -rs` collects it.
- [x] 1.2 Add an async `canvas_api_client` fixture that skips (naming the missing var) when `CANVAS_BASE_URL` or `CANVAS_API_TOKEN` is unset, and otherwise yields an `ApiClient` opened with `async with` using `Configuration(host=..., access_token=...)`. Keep the existing `skip_integration_tests` fixture. Verify that `pdm run pytest --integration -rs` with the env vars unset reports a skip naming them.
- [x] 1.3 Update the README "Integration Tests" section: the token must belong to a seeded observer user, show how to run `pdm run pytest --integration -m integration` against the local docker canvas-lms, and add `test/test_integration_observees.py` to the "Custom, never overwritten" list. Verify the documented command matches the conftest behavior.
- [x] 1.4 Add `test/test_integration_observees.py` to `src/.openapi-generator-ignore`. Verify by running a regeneration in task 2.3 and checking that the file is untouched (`git status`).
- [x] 1.5 Verify that the default suite is unaffected: `pdm run pytest` passes with the same pass count as before, and only integration tests are reported as skipped.

## 2. Type the "List assignments for user" endpoint (canvas-lms fork → client)

- [x] 2.1 In `canvas-lms/app/controllers/assignments_api_controller.rb`, add `# @returns [Assignment]` to the `user_index` doc block, directly above `def user_index`. Verify that the diff is a single comment line.
- [x] 2.2 Regenerate the OpenAPI spec in the canvas-lms docker web container (`bundle exec rake doc:openapi`). Verify that `/api/v1/users/{user_id}/courses/{course_id}/assignments` in `public/doc/openapi/canvas.openapi.yaml` now has `content.application/json.schema` as an array of `#/components/schemas/Assignment`, and that the rest of the spec diff is empty or unrelated churn you have reviewed.
- [x] 2.3 Regenerate the client in canvas-lms-python-client with `openapi-generator-cli generate` using `openapi-generator-config.yaml` and `-t mustache-templates -o src`. Verify that `assignments_api_user_index` returns `List[Assignment]`, that `_paginated` returns `AsyncIterator[List[Assignment]]`, that `_all` returns `AsyncIterator[Assignment]`, and that `conftest.py`, `test_pagination.py`, and `pagination.py` are unchanged.
- [x] 2.4 Verify that `pdm run pytest` (offline suite) still passes after regeneration.

## 3. Observee integration tests (canvas-lms-python-client)

- [x] 3.1 Create `test/test_integration_observees.py` with module-level `pytestmark = pytest.mark.integration`, plus small async helpers that collect `_all` iterators into lists. Verify that `pdm run pytest -rs` reports the module's tests as skipped.
- [x] 3.2 Add `test_observer_lists_observees`, which calls `UserObserveesApi.user_observees_index_all(user_id="self")`. Assert a non-empty list and that each `User` has an int `id` and a non-empty `name`. Verify that it passes with `--integration` against seeded canvas-lms.
- [x] 3.3 Add `test_observees_pagination`, which collects observees with `per_page=1` and compares the ids with the default-page-size result (same set, no duplicates). If the observer has fewer than 2 observees, call `pytest.skip` with a reason. Verify that it passes or skips with that reason.
- [x] 3.4 Add `test_observee_courses`. For each observee, call `CoursesApi.courses_user_index_all(user_id=str(observee.id))` and assert that each `Course` has an int `id`. Across all observees, assert that at least one course exists, with a message naming the missing hop. Verify that it passes with `--integration`.
- [x] 3.5 Add `test_observee_course_assignments`, the end-to-end walk. For each observee and each of their courses, call `AssignmentsApiApi.assignments_api_user_index_all(user_id=str(observee.id), course_id=str(course.id))`. Assert that each item is an `Assignment` with an int `id` and `course_id == course.id`, and that at least one assignment exists overall. Verify that it passes with `--integration`.
- [x] 3.6 Run the full integration suite against the seeded docker canvas-lms: start canvas-lms, export `CANVAS_BASE_URL` and the observer's `CANVAS_API_TOKEN`, then run `pdm run pytest --integration -m integration -v`. Verify that all tests pass. Record any strict-model deserialization failures as follow-ups instead of loosening the models.

## 4. Final checks

- [x] 4.1 Run `pdm run ruff check src/canvas_lms_python_client/test/conftest.py src/canvas_lms_python_client/test/test_integration_observees.py` and verify it is clean.
- [x] 4.2 Run `openspec validate add-observee-integration-tests --strict` and verify it passes.

## Workflow follow-up

- Commit the canvas-lms annotation and regenerated spec in the canvas-lms fork before committing the regenerated client.
- Archive the change with `/opsx:archive` after review.
