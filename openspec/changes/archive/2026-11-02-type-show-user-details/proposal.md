# Proposal

## Why

`UsersApi.users_api_show` (`GET /api/v1/users/:id`, "Show user details") returns a raw `dict`, so callers write `student["id"]` instead of `student.id`. It's the usual way to find out who the token belongs to (`id="self"`), and `test_student_grades.py` already has to work around it.

The cause is a generator bug, not a missing model:
- `users_controller.rb#api_show` documents `# @returns Schemas::Docs::User`. It's the only `@returns` that names a Ruby schema class rather than a `@model`.
- The generator loads `lib/schemas/docs/user.rb` and registers it under the schema's `id`, `User`. That's the same `User` schema 47 other `$ref`s already use.
- When it resolves `@returns`, it sanitizes the raw name to `Schemas_Docs_User`, finds no such schema, and falls back to `type: object`.

Canvas's own doc tooling strips the `Schemas::Docs::` prefix (`doc/api/documentation_helpers.rb`, `controller_view.rb`, `return_view.rb`, `tags/setup.rb`). The OpenAPI adapter doesn't.

Typing the response would also drop fields the operation's own docs promise: `permissions` (always returned), `effective_locale` (always returned for `self`) and `uuid` (`include[]=uuid`). They're missing from `Schemas::Docs::User`.

## What Changes

- **canvas-lms generator (fork):** `CanvasAdapter.resolve_schema_name` strips a leading `Schemas::Docs::` before sanitizing, so `@returns Schemas::Docs::User` resolves to `User`. Other names resolve exactly as before.
- **canvas-lms docs (fork):** `lib/schemas/docs/user.rb` gains these optional properties:
  - `permissions`: an object with the booleans `can_update_name`, `can_update_avatar` and `limit_parent_app_web_access`
  - `effective_locale`: a string
  - `uuid`: a string

  These edits and the generator fix go in one upstream-format commit.
- **Regenerate** the spec and the client. `users_api_show` returns `User`. Its `_with_http_info` and `_without_preload_content` variants change with it.
- **Client tests:**
  - an offline payload test for `users/self` captured as the observer, student and admin
  - an integration test that `users_api_show(id="self")` returns a `User` whose `id` and `name` match the caller
  - `test_student_grades.py` uses `student.id` instead of the dict workaround
- **BREAKING (client):** `users_api_show` returns `User` instead of `object`, and `User` gains three fields. The client is unreleased, so this isn't documented.
- **Not in scope:**
  - other fields `api_show` sends that the shared `User` schema lacks: `created_at`, `account_uuid`, `past_uuid`, `confirmation_url`
  - other `User`-returning operations, which are already typed

## Capabilities

### New Capabilities
<!-- None. -->

### Modified Capabilities
- `typed-operation-responses`: an operation documented with a schema class name (`Schemas::Docs::<Model>`) returns that model, as one documented with a `@model` name does.

## Impact

- **canvas-lms (fork):**
  - `lib/swagger_yard/canvas_adapter.rb`, plus examples in `spec/lib/swagger_yard/canvas_adapter_spec.rb`
  - `lib/schemas/docs/user.rb`
  - Not committed: the regenerated `public/doc/openapi/canvas.openapi.yaml`
- **canvas-lms-python-client:**
  - Regenerated `api/users_api.py`, `models/user.py` (and a nested permissions model if the generator emits one), and their docs
  - A new `test/custom/unit/test_user_model.py` with fixtures in `test/custom/unit/fixtures/users/`
  - A new integration test, and the `test_student_grades.py` update
- **Dependencies:** builds on `fetch-student-course-grades` (applied), which added `test_student_grades.py` and the student token.
