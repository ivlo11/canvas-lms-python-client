# Design

## Context

- See proposal.md "Why". Requirements are in `specs/typed-operation-responses/spec.md` and `specs/paginated-list-responses/spec.md`.
- Registration: `@model Lti::X` blocks are stored by `parse_and_store_schema` under `sanitize_schema_name(name)`, which turns `::` into `_`. `clean_schema_text` also rewrites `::` → `_` inside the schema JSON, so `$ref`s between models already use sanitized names.
- Resolution: `process_returns_tags` → `extract_model_name_from_types` (raw `Lti::X`) → `track_operation_model(op_id, model_name, …)`. That calls `model_schema_exists?(model_name)` (`canvas_schemas.key?`) and then stores `model: model_name`. Later, `open_api_generator.rb#build_schema_ref` emits `#/components/schemas/#{model}`. Both the check and the stored name use the raw name, so a fix to only one of them would still emit a broken `$ref`.
- `model_schema_exists?` and `track_operation_model` are instance methods inside a module that is prepended at install time, so they are awkward to unit-test. The `CanvasAdapter` class methods (`sanitize_schema_name`, `register_wrapper_schema`) are already tested directly in `spec/lib/swagger_yard/canvas_adapter_spec.rb`.
- The 7 resolving `@model`s are declared in `app/controllers/lti/{deployments,context_controls,lti_apps,registrations,resource_links}_controller.rb`. `registrations_controller.rb` declares 3 of them.
- LTI JSON comes from `api_json`-based helpers (`lib/api/v1/lti/*.rb`) and from `Lti::AppLaunchCollator`. `api_json` sends integer ids unless the request asks for stringified ids. The collator builds hashes by hand: `definition_id` is `tool.id` for `ContextExternalTool` (LTI 1.1 and 1.3 alike) and `message_handler.id` for LTI 2, so it is always an integer.
- The seeded instance has no LTI data (`spec/manual_seeding/large_gradebook_seeds.rb` has no LTI section).

## Goals / Non-Goals

**Goals:**
- Resolve namespaced `@returns` with a single, tested name rule shared by the existence check and the `$ref`.
- Make every newly typed operation deserialize real Canvas responses, based on live evidence.

**Non-Goals:**
- Typing undocumented keys that Canvas sends (for example `Lti::Deployment.root_account_deployment`, `Lti::ResourceLink.custom`).
- Writing `@model`s for `Lti::RegistrationHistoryEntry` or `Lti::RegistrationUpdateRequest`.
- Keeping undocumented keys (`additionalProperties`).
- The operation mis-attribution bug (`ServiceCredentials-*`, `BadPermissionSettingError-*`).
- Correcting non-LTI models.

## Decisions

### D1: One class-level resolver used for both the check and the stored name
Add `SwaggerYard::CanvasAdapter.resolve_schema_name(name)`. It returns `sanitize_schema_name(name)` when that key exists in `canvas_schemas`, and `nil` otherwise. Then:
- `model_schema_exists?(name)` becomes `!resolve_schema_name(name).nil?`.
- `track_operation_model` stores `model: resolve_schema_name(model_name)`.

Non-namespaced names sanitize to themselves, so their behavior is identical.
- *Alternative: sanitize in `extract_model_name_from_types`.* That changes a function whose output other code may log or compare, and it hides the rule in a parser.
- *Alternative: register schemas under both names.* That puts duplicate components (`Lti::X` is not a valid component name) into the spec.

### D2: Correct `@returns` arity in the docs, not in the generator
Change `create_many` and `bulk_create` to `[Lti::ContextControl]` and `[Lti::ResourceLink]`. These are 2-character doc fixes that match the code (`controls.map`, `links.map`). The user chose this option over a generator exception list.

### D3: Correct `@model` field types using live evidence
Corrections found by the captures (task 2.3): `Lti::LaunchDefinition.definition_id` → `integer`; `Lti::OverlayVersion.diff` inner items → untyped (`{}`), because each entry is a Hashdiff tuple such as `["~", "title", "old", "new"]`, not an object; `created_by` / `updated_by` → see D5.
`registrations_bind` can't be captured: Canvas only binds registrations inherited from Site Admin (422 `must be inherited from Site Admin` for a local registration). Its model is verified with the `account_binding` in the `registrations_show` capture instead.

Follow the approach of `fix-polling-and-quiz-model-types` (D5 there):
- **Seed:** add an uncommitted `create_lti` helper to `large_gradebook_seeds.rb`. It creates an LTI 1.3 developer key, registration and account binding, a deployment (a `ContextExternalTool` with a `course_navigation` placement) in the seeded course, a context control, a resource link, and an overlay (so an `OverlayVersion` exists).
- **Capture:** as the admin, call each newly typed endpoint and save the JSON under `test/fixtures/lti/*.json` in the client. These are custom files, so add them to `src/.openapi-generator-ignore`.
- **Compare:** generate the client with only D1 and D2 applied, then deserialize each captured payload into its model. Every `ValidationError`, and every documented field whose JSON type differs from the model, is a correction. Edit the corresponding `@model` property `type` (and its `example`) in the fork. The known one is `Lti::LaunchDefinition.definition_id`, which changes from `string` to `integer` (always an integer id, see Context).
- **Pin:** the captured payloads become offline tests. Each one must deserialize without error, and a test confirms it fails against the pre-correction model.

### D5: Emit `oneOf` for `string|Model` properties that carry a `$ref`
Live captures show that `created_by` / `updated_by` on `Lti::Registration`, `Lti::RegistrationAccountBinding` and `Lti::OverlayVersion` are either a `User` or the literal string `"Instructure"`. The string is sent when the user can read Site Admin (`lib/api/v1/lti/{registration,registration_account_binding,overlay_version}.rb`). `convert_single_property` returns a bare `$ref` whenever `$ref` is present, so the documented `"type": "string|User"` is dropped and the client rejects the string. The user chose to keep the `User` typing:
- In `convert_single_property`, when a property has a `$ref` and its `type` lists `string` among `|`-separated types, emit `{"oneOf" => [{"type" => "string"}, {"$ref" => …}]}`. A bare `$ref` (or a `type` without `string`) is unchanged.
- Add `"type": "string|User"` and the "If a string, … Instructure" wording to the two `Lti::RegistrationAccountBinding` fields, which document only a `$ref` today. Registration and overlay version already say `string|User`.
- The generator dedupes the 5 identical inline schemas into one shared oneOf wrapper model, `LtiRegistrationCreatedBy`, which all 5 fields use. Its `actual_instance` is a `str` or a `User`.
- `Lti::ContextControl` is unchanged: it sends a `User` or `null`, never the string (`lib/api/v1/lti/context_control.rb`).
- *Alternative: leave the fields untyped.* That is doc-only, but it loses `User` typing for the common case.

Task 1.4 verifies that the new rule changes no schema except the 5 LTI properties, because other models could also combine `string|X` with `$ref`.

### D4: Update existing client tests in place
`test_integration_paginated_models.py::assert_launch_definitions` changes from dict checks to `isinstance(..., LtiLaunchDefinition)` with attribute checks. Add integration tests, which skip when there is no data, for `deployments_list_all`, `deployments_list_controls_all`, `context_controls_index_all` and `resource_links_index_all`, plus one single-object call (`deployments_show`), using the seeded ids.

## Risks / Trade-offs

- [Other mismatched fields hide in the parts of a response the seed didn't fill, for example optional nested `overlay` fields] → The seed fills every relation it can. Fields that are absent or null in the captures are recorded as unverified in the task notes, not guessed.
- [A field's JSON type varies by request, for example stringified ids when `Accept: application/json+canvas-string-ids` is sent] → The generated client never sends that header. Document the default shape only, the same policy as before.
- [The resolver change also affects non-LTI namespaced models that weren't counted] → The change is limited to `Lti::` today (all 34 namespaced `@returns` are `Lti::`). Task 1.4 verifies that the regenerated spec diff only touches the expected operations.
- [32 public return types change at once] → The client is unpublished, so there's no version bump. List the changes in the README "Breaking changes" section.

## Migration Plan

1. In the fork: resolver and specs, then the 2 `@returns` fixes. Regenerate the spec, seed the LTI data, capture payloads, make the `@model` corrections, and regenerate again. Commit only the generator, its spec, the controllers and the spec YAML. The seed edit stays uncommitted.
2. In the client: regenerate, add fixtures and tests, update the README, then commit.

Rollback: revert both commits. The seeded rows are test data and can stay.

