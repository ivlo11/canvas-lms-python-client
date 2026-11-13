# Proposal

## Why

The main consumer of this client is a future Home Assistant integration that shows a parent (observer) their students' (observees') courses and assignments. No test runs the generated client against a real Canvas instance for that flow. A test would already have caught one bug: `AssignmentsApi.assignments_api_user_index` (`GET /users/{user_id}/courses/{course_id}/assignments`) returns `None`. The canvas-lms controller doc for that endpoint has no `@returns [Assignment]`, so the OpenAPI spec defines no response schema for it.

## What Changes

- Add opt-in integration tests to `canvas-lms-python-client` that authenticate as a seeded observer and run three steps:
  1. List the observer's observees (`UserObserveesApi.user_observees_index_all(user_id="self")`).
  2. For each observee, list their courses (`CoursesApi.courses_user_index_all(user_id=<observee.id>)`).
  3. For each observee course, list the observee's assignments (`AssignmentsApiApi.assignments_api_user_index_all(user_id=<observee.id>, course_id=<course.id>)`).
- Make the integration-test harness real: add an `--integration` pytest option (the README already documents it but nothing implements it), skip `@pytest.mark.integration` tests unless the option is passed, and add a shared async `ApiClient` fixture built from `CANVAS_BASE_URL` and `CANVAS_API_TOKEN`.
- **Cross-repo fix (canvas-lms fork):** add `# @returns [Assignment]` to the `user_index` doc block in `app/controllers/assignments_api_controller.rb`, regenerate `public/doc/openapi/canvas.openapi.yaml`, then regenerate this client. `assignments_api_user_index*` will return `List[Assignment]` instead of `None` / `AsyncIterator[Any]`.

## Capabilities

### New Capabilities
- `integration-testing`: an opt-in harness for running tests against a live Canvas instance, covering activation, credentials, a shared client fixture, and skip behavior.
- `observee-academic-data`: the client's contract for an observer reading their observees, each observee's courses, and each observee's assignments in a course, all as typed models.

### Modified Capabilities
<!-- None: openspec/specs/ is empty. -->

## Impact

- **canvas-lms-python-client**
  - New custom test module `src/canvas_lms_python_client/test/test_integration_observees.py`. It must be added to `src/.openapi-generator-ignore` and to the README's "Custom, never overwritten" list.
  - `src/canvas_lms_python_client/test/conftest.py`: adds the `--integration` option, collection-time skipping, and the `canvas_api_client` fixture.
  - Regenerated `api/assignments_api_api.py`: the return types of `assignments_api_user_index` / `_paginated` / `_all` change from `None` / `AsyncIterator[Any]` / `AsyncIterator[Any]` to `List[Assignment]` / `AsyncIterator[List[Assignment]]` / `AsyncIterator[Assignment]`. Existing callers get typed data where they previously got nothing.
  - README "Integration Tests" section: document the observer-token requirement.
- **canvas-lms (fork)**: a one-line doc annotation in `assignments_api_controller.rb`, plus the regenerated OpenAPI spec. Canvas runtime behavior does not change.
- **Test environment**: the dockerized canvas-lms with seeded data must have an observer user linked to at least one observee. That observee must be enrolled in at least one course with at least one assignment. The tests assume this data exists.
- No new runtime dependencies. `pytest-asyncio` is already in the dev extras.
