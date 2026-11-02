# Design

## Context

- Motivation: see proposal.md, "Why". Requirement: `specs/typed-operation-responses/spec.md`.
- **How the adapter loads schema classes** (`lib/swagger_yard/canvas_adapter.rb`):
  - `collect_schemas` collects every controller `@model` first, then calls `collect_schemas_from_lib`.
  - `load_schema_from_file` loads each `lib/schemas/docs/**/*.rb` and stores the class's schema under `sanitize_schema_name(schema["id"] || class_name)`. For `user.rb`, that key is `User`.
  - No controller defines `@model User`, so `lib/schemas/docs/user.rb` is the only source of the `User` schema.
- **How `@returns` resolves:**
  - `resolve_schema_name(name)` returns `sanitize_schema_name(name)` (`::` → `_`) if that key exists, and nil otherwise.
  - `model_schema_exists?` and `track_operation_model` both go through it. It was added by `resolve-namespaced-model-returns`.
  - For `Schemas::Docs::User`, it looks up `Schemas_Docs_User`, finds nothing, and the operation stays `type: object`.
- **Scope:** `grep -rn "@returns.*Schemas::" app/controllers` finds one hit, `users_controller.rb:1484`. `lib/schemas/docs/` holds one file, `user.rb`.
- **What `api_show` sends** (`api_show_includes`, `lib/api/v1/user.rb`):
  - Always: `first_name`, `last_name`, `locale`, `avatar_url`, `permissions`, `email`, `effective_locale` (for `self` only).
  - With `include[]`: `uuid` (plus `account_uuid` and `past_uuid`), `last_login`, `avatar_state`, `confirmation_url`.
  - Captured live for the observer, the student (8), the admin, and the admin reading user 8: no field's JSON type conflicts with `User`. The fields `User` lacks are `permissions` (a dict of 3 booleans), `effective_locale`, `uuid`, `account_uuid` and `created_at`.

## Goals / Non-Goals

**Goals:**
- `users_api_show` returns `User`, with the fields its operation docs promise.

**Non-Goals:**
- Documenting every key `user_json` can emit, such as `created_at`, `account_uuid`, `past_uuid` and `confirmation_url` (follow-up).
- Resolving other Ruby schema namespaces (`Schemas::Lti::…`). They aren't used in any `@returns`.

## Decisions

### D1: Strip `Schemas::Docs::` in `resolve_schema_name`
`resolve_schema_name` removes a leading `Schemas::Docs::` and then sanitizes as before. The existence check and the `$ref` name both use it, so they stay consistent.

This matches Canvas's own doc tooling, which uses `.sub("Schemas::Docs::", "")` in four places. It also matches how `load_schema_from_file` derives `class_name` (the path under `lib/schemas/docs/`).

- *Alternative: register an alias for each loaded class (`Schemas_Docs_User` → `User`).* That's more general if a schema's `id` ever differs from its class name. But no such schema exists, and it adds a second lookup table.
- *Alternative: change the controller to `@returns User`.* That's simpler, but it changes upstream Canvas docs to suit the fork's generator, and Canvas's HTML docs rely on the `Schemas::Docs::` form to inline the schema.

### D2: Document `permissions`, `effective_locale` and `uuid` on `Schemas::Docs::User`
Add them as optional properties, with descriptions taken from the `api_show` docs and `user_json`:
- `permissions`: `type: object`, with `can_update_name`, `can_update_avatar` and `limit_parent_app_web_access` as `boolean` properties
- `effective_locale`: `string`
- `uuid`: `string`

`User` is shared by 47 `$ref`s, but the additions are optional, so the other operations are unaffected.

If `convert_canvas_schema_to_openapi` doesn't carry nested object `properties` through, `permissions` falls back to an untyped `object` (`Dict[str, Any]` in the client), and the apply step records that. The field is kept either way. **Apply result:** it does fall back. `permissions` is `Dict[str, Any]`, and the nested keys are documented in `user.rb` only.

### D3: Tests
- **Offline:** `test/custom/unit/fixtures/users/users_self.json` holds a list of the four captured payloads: the observer, student and second admin (Seeded Admin 2, not user 1, whose details are a real address) reading `self` with `include[]=uuid&include[]=last_login`, and the second admin reading user 8. `test_user_model.py` deserializes each item into `User` and asserts:
  - `id`, `name` and `uuid` equal the JSON
  - `permissions["can_update_name"]` equals the JSON (a dict, per D2)
  - `effective_locale` equals the JSON where it's present

  It fails against today's `models/user.py`.
- **Integration:** `test_users_api_show_self_is_typed` goes in `test/custom/integration/test_paginated_models.py`, beside the other typed-response tests. As the observer, it asserts that `users_api_show(id="self")` is a `User` with an `int` `id` and a non-empty `name`.
- `test_student_grades.py` switches to `student.id` and drops its comment.

### D4: One upstream-format commit
The fork commit contains `canvas_adapter.rb`, its spec and `lib/schemas/docs/user.rb`, following the fork's rules (subject, why, `flag=none`, `Test Plan:`, every line under 60 characters). It's not a PR.

## Risks / Trade-offs

- [Typing exposes a `ValidationError` for another caller or option] → The fixtures cover four callers. Any new integration failure is recorded and fixed in `user.rb` if the type is wrong.
- [Other `Schemas::Docs::` references start resolving] → There's only one today. The spec diff check in the tasks confirms that only `Users-api_show` and `User` change.
- [Upstream adds a `Schemas::Docs` class whose `id` differs from its class name] → It would stay untyped, as today. D1's alias alternative is the fix if that happens.

## Migration Plan

1. Fork: write the adapter examples, fix the adapter, edit `user.rb`, regenerate the spec (uncommitted), check the diff, then commit.
2. Client: regenerate, add the fixture and tests, update `test_student_grades.py`, run the offline and integration suites, then commit.

Rollback: revert both commits.
