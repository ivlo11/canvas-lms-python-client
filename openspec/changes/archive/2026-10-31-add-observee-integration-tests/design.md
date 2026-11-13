# Design

## Context

- The client is generated from `canvas-lms/public/doc/openapi/canvas.openapi.yaml`. That spec is produced by `rake doc:openapi`, which uses `lib/swagger_yard/open_api_generator.rb` and reads YARD-style `@API` / `@returns` annotations in canvas-lms controllers.
- `AssignmentsApiController#user_index` has `@API List assignments for user` but no `@returns`. Its spec operation therefore has `responses.default` with no `content`, so the generator emits `-> None` and `-> AsyncIterator[Any]`. The sibling `#index` has `@returns [Assignment]` and generates correctly.
- Every `x-paginated` operation has three generated variants. `_paginated` yields one `List[T]` per page, and `_all` yields individual `T` items. Both follow the `Link: rel="next"` header.
- `test/conftest.py` is custom (listed in `src/.openapi-generator-ignore`). It already registers the `integration` marker and has a `skip_integration_tests` fixture keyed on env vars. Nothing implements the README's `--integration` flag.
- `pytest` runs with `asyncio_mode = "auto"`, so `async def` tests and fixtures need no decorators.
- Models use `StrictInt`/`StrictStr`, so a schema mismatch in live data fails deserialization loudly. That is a useful signal for these tests.

## Goals / Non-Goals

**Goals:**
- One end-to-end test that walks observer → observees → courses → assignments through the generated client against the seeded dockerized canvas-lms.
- Focused tests for each hop, so a failure points at a specific endpoint.
- Fix the root cause of the untyped assignments endpoint in the canvas-lms annotation, not with a client-side workaround.

**Non-Goals:**
- Seeding or provisioning Canvas data. The seeded instance is assumed to contain the observer → observee → course → assignment chain.
- Starting or stopping the canvas-lms Docker stack from pytest.
- Auditing other endpoints that are missing `@returns`. That work belongs in a follow-up change.
- Running integration tests in CI.

## Decisions

### D1: Fix `@returns` in the canvas-lms controller, not in the spec YAML or the client
Add `# @returns [Assignment]` to `user_index` in `app/controllers/assignments_api_controller.rb`, run `rake doc:openapi`, then regenerate the client.
- *Alternative: hand-edit `canvas.openapi.yaml`.* The next `rake doc:openapi` would overwrite the fix.
- *Alternative: generator fallback that copies the response from the "See {api:...#index}" reference.* This is more general, but it is a heuristic over free-text descriptions, and it is too much machinery for one endpoint.
- *Alternative: call `assignments_api_index(course_id)` as the observer.* The endpoint is already typed, but its results are scoped to the caller rather than to a specific observee. That loses the per-observee semantics the Home Assistant integration needs.

### D2: Authenticate as the observer; address the observer as `self`
The token in `CANVAS_API_TOKEN` belongs to the seeded observer user. Observees are listed with `user_id="self"`. Courses and assignments are requested with the observee's id, so the test exercises the same permission path a parent's Home Assistant install will use.
- *Alternative: admin token plus `CANVAS_OBSERVER_USER_ID`.* An admin can read everything, which would hide observer-permission bugs.

### D3: Use the `_all` iterators in tests
Tests collect results with `[x async for x in api.<op>_all(..., per_page=N)]`. This covers Link-header pagination in the same call. One observee test passes `per_page=1` so the multi-page path runs whenever the observer has two or more observees.
- *Alternative: single-page calls.* These would not cover pagination, which is the client's main custom feature.

### D4: Implement `--integration` in `conftest.py` with collection-time skipping
Add `pytest_addoption("--integration")` and `pytest_collection_modifyitems`. Without the flag, add a skip marker to every item with the `integration` marker. Add an async `canvas_api_client` fixture that skips when credentials are missing, then builds `Configuration(host=CANVAS_BASE_URL, access_token=CANVAS_API_TOKEN)` and yields from `async with ApiClient(config)`. The existing `skip_integration_tests` fixture stays for backward compatibility.
- *Alternative: env vars as the only switch.* A developer who exported the token for other work would hit the network unintentionally on every `pytest` run.

### D5: Put the tests in a new custom module and protect it from regeneration
Create `test/test_integration_observees.py`, add it to `src/.openapi-generator-ignore`, and list it in the README's "Custom, never overwritten" section. Any `test_*.py` name not produced by the generator is safe, but listing it explicitly matches how `test_pagination.py` is handled.

### D6: Assert structure and invariants, not seeded values
Assert non-emptiness at the aggregate level (at least one observee, at least one course across observees, at least one assignment across courses). Also assert per-item invariants: integer ids, and `assignment.course_id == course.id`. Do not hard-code names or ids from the seed, so the tests survive a re-seed.

## Risks / Trade-offs

- [Strict models reject real Canvas payloads (for example, a field that is `null` or a different type than documented)] → Treat it as a real finding. Fix the source annotation in canvas-lms per D1, or record it in `tasks.md` as a follow-up. Do not loosen the models in the test.
- [Seed data lacks a complete observer chain] → The aggregate assertions fail with messages naming the missing hop (for example, "observer has observees but none have courses") so the seed can be fixed quickly.
- [Regenerating the client also picks up unrelated spec drift] → Regenerate from a canvas-lms commit that differs from the current one only by the annotation, and review the client diff limited to `assignments_api_api.py` and its docs.
- [Courses where the observer link does not cover the course's root account return 401/403] → The seed data should avoid this. If it shows up, the test fails clearly instead of being filtered out.

## Migration Plan

1. In canvas-lms: add the annotation, run `rake doc:openapi` (requires the DB, so run it in the docker web container), and commit both the annotation and the regenerated spec.
2. In canvas-lms-python-client: regenerate (`openapi-generator-cli generate ... -t mustache-templates -o src`), then commit the regenerated `assignments_api_api.py` together with the test and harness changes.
3. Rollback: revert both commits. The tests are opt-in, so the default suite is unaffected either way.
