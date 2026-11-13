# Tasks

## 1. Resolve namespaced `@returns` in the generator (canvas-lms fork)

- [x] 1.1 In `spec/lib/swagger_yard/canvas_adapter_spec.rb`, add failing examples for `.resolve_schema_name`:
  - `"Lti::Deployment"` returns `"Lti_Deployment"` when `canvas_schemas` has that key.
  - `"User"` returns `"User"`.
  - An unknown name returns `nil`.
  - `"Lti::Missing"` returns `nil`.

  Stub or seed `canvas_schemas` in the example, following the existing `register_wrapper_schema` examples. Verify with `bin/rspec spec/lib/swagger_yard/canvas_adapter_spec.rb` in the web container that only the new examples fail.
- [x] 1.2 Implement `CanvasAdapter.resolve_schema_name`. Make `model_schema_exists?` delegate to it, and have `track_operation_model` store the resolved name (design D1). Verify that the 1.1 examples pass and that `bin/rspec spec/lib/swagger_yard/` passes as a whole.
- [x] 1.3 Fix the `@returns` arity (design D2): `Lti::ContextControlsController#create_many` → `# @returns [Lti::ContextControl]`, and `Lti::ResourceLinksController#bulk_create` → `# @returns [Lti::ResourceLink]`. Verify that `git diff` for those two files shows exactly two changed comment lines.
- [x] 1.4 Regenerate the spec (`bundle exec rake doc:openapi`). Verify that the 32 operations in proposal.md "What Changes" now `$ref` `Lti_*` schemas (arrays for the 6 lists plus `create_many`, `bulk_create` and `overlay_history`). Verify that `Registrations-history` and the two `*_registration_update_request` operations are unchanged. Verify that no non-LTI operation's response changed (`git diff` review).
- [x] 1.5 Run `bin/rubocop lib/swagger_yard/canvas_adapter.rb spec/lib/swagger_yard/canvas_adapter_spec.rb` and verify it is clean. (Result: no new offenses. The 14 reported on these files are already on HEAD: `RSpec/RepeatedDescription` at lines 86–130, `RSpec/BeforeAfterAll` at 175, `Rails/Output` at 714.)
- [x] 1.6 Add failing examples to `spec/lib/swagger_yard/canvas_adapter_spec.rb` for `.convert_single_property` (design D5): `{"type" => "string|User", "$ref" => "User"}` → `oneOf` of `string` and the `User` `$ref`; a bare `$ref`, and `{"type" => "User", "$ref" => "User"}`, still return the bare `$ref`. Implement it in `convert_single_property`. Verify that the examples pass and that `bin/rspec spec/lib/swagger_yard/` passes.
- [x] 1.7 Add `"type": "string|User"` and the Instructure wording to `Lti::RegistrationAccountBinding.created_by` / `updated_by` in `registrations_controller.rb`. Regenerate the spec. Verify that the only schema changes are the 5 `created_by` / `updated_by` properties of `Lti_Registration`, `Lti_RegistrationAccountBinding` and `Lti_OverlayVersion` (plus the 2.4 corrections), and that rubocop has no new offenses.

## 2. Live evidence and `@model` corrections (canvas-lms fork + client)

- [x] 2.1 Add an uncommitted `create_lti` helper to `spec/manual_seeding/large_gradebook_seeds.rb` (design D3). It creates an LTI 1.3 developer key, registration and account binding, a course deployment with a `course_navigation` placement, a context control, a resource link, and a configuration overlay. Run it with `bin/rails runner spec/manual_seeding/large_gradebook_seeds.rb` in the web container. Verify that `GET /api/v1/accounts/self/lti_registrations/<id>/deployments` as the admin returns at least one deployment, and record the created ids in these notes.
  - Seeded (course "Sensory Analysis of Ales", id 8): registration 1, account deployment 1, course deployment 2 (`course_navigation`), context control 2 (course), resource link 1, overlay 1 (updated once, so 1 version).
- [x] 2.2 Regenerate the client with the 1.4 spec. Capture the admin responses of these endpoints into `src/canvas_lms_python_client/test/fixtures/lti/<operation>.json`:
  - `deployments_list`, `deployments_show`
  - `deployments_list_controls`, `context_controls_index`, `context_controls_show`
  - `lti_apps_launch_definitions` (`placements[]=course_navigation`)
  - `registrations_show`, `registrations_bind` response (or `show` with the binding included), `registrations_overlay_history`
  - `resource_links_index`, `resource_links_show`

  Add `test/fixtures/` to `src/.openapi-generator-ignore` and to the README's custom-files list. Verify that the files exist and are valid JSON.
- [x] 2.3 Write a throwaway script that deserializes each fixture with its model's `from_dict` / `from_json`. Record every `ValidationError` and every documented field whose JSON type differs from the model type, including `definition_id`. Also record fields that were null or absent and so are unverified. Verify that the list is complete by running the script to a clean exit after 2.4.
  - Mismatches: `Lti::LaunchDefinition.definition_id` (int, documented string); `Lti::OverlayVersion.diff` (array of mixed-value tuples, documented array of arrays of objects); `created_by` / `updated_by` on `Lti::Registration`, `Lti::RegistrationAccountBinding` and `Lti::OverlayVersion` (the string `"Instructure"` for site-admin users, documented as `User`; see design D5 and tasks 1.6–1.7). The first error in a nested `from_dict` hid the `diff` mismatch until `"Instructure"` was swapped for a `User` dict.
  - `registrations_bind` returned 422 (`must be inherited from Site Admin`), so the binding is verified with `registrations_show.account_binding`.
  - Unverified (null or absent in every capture): `Lti::LaunchDefinition.context_name`; `Lti::Registration.dynamic_registration`, `icon_url`, `template_registration_id`; `Lti::ResourceLink.associated_content_id`, `associated_content_type`, `lti_1_1_id`; `Lti::ToolConfiguration.public_jwk`, `tool_id`; most `Lti::Placement` / `Lti::LaunchSettings` options; most `User` fields. The `User` branch of `created_by` on registrations, bindings and overlay versions is not captured live, because the seeded admin is a site admin.
  - Undocumented keys (out of scope, see Non-Goals): for example `Lti::Deployment.root_account_deployment`, `Lti::ContextControl.registration_id`, `Lti::ResourceLink.custom` / `root_account_id`, `Lti::Registration.overlay` / `overlaid_configuration` / `developer_key_id`, `Lti::OverlayVersion.id`.
- [x] 2.4 Correct the mismatched property `type` and `example` values in the `@model` blocks of the 5 LTI controllers. At minimum, `Lti::LaunchDefinition.definition_id` → `integer`. Regenerate the spec and the client. Verify that the 2.3 script deserializes every fixture without error, and that `git diff` in the fork shows only comment lines in the controllers.
  - Done: `definition_id` → `integer` (example `123`), and `diff` inner items → `{}` (`List[List[Any]]`). The 2.3 script exits cleanly with no type or value mismatches.
- [x] 2.5 Commit in the fork following its commit guidelines: generator, its spec, the controller doc edits, and the regenerated spec YAML. The seed edit stays uncommitted. Verify with `git log -1 --stat`.
  - Committed as `fix(swagger_yard): resolve namespaced @returns` (generator, spec, 4 controllers). Following the earlier changes, the regenerated `public/doc/openapi/canvas.openapi.yaml` stays untracked: it has never been committed in the fork.

## 3. Client tests and docs (canvas-lms-python-client)

- [x] 3.1 Add `test/test_lti_model_payloads.py` (custom, added to the ignore file and the README list). It is a parametrized offline test that deserializes each `fixtures/lti/*.json` into its expected model (or into a list of it) and asserts no error, plus spot-checks such as `isinstance(definition.definition_id, int)`. Verify that it passes. Then verify that it fails on the launch-definition fixture against the pre-correction `models/lti_launch_definition.py` (`git stash` that one file), and restore it.
- [x] 3.2 Update `test_integration_paginated_models.py::assert_launch_definitions` to assert `LtiLaunchDefinition` instances with `definition_type` and an int `definition_id`. Add `test_lti_deployments_typed`, `test_lti_deployment_controls_typed`, `test_lti_account_context_controls_typed` and `test_lti_resource_links_typed`, which iterate `_all` and assert the model type and skip when there is no data. Add `test_lti_deployment_show_typed`. Verify with `pdm run pytest --integration -m integration -v` that the tests pass against the seeded instance.
  - Accepted skip (user decision): the 5 new LTI tests and the 4 poll/quiz tests pass. Both launch-definition tests skip: the client sends array query params as `placements=a&placements=b` (all 218 array query params in the spec lack `[]`). Canvas returns 500 for repeated params and `[]` for comma-joined ones. It only reads `placements[]=…`, so `_all` yields nothing even though the course has a `course_navigation` tool. The launch-definition model is verified offline by 3.1. The fix is tracked in the separate change `fix-array-query-params`.
- [x] 3.3 Add an offline assertion to `test_paginated_response_types.py` that the 6 LTI list operations' `_paginated` return annotations are `AsyncIterator[List[Lti…]]` (not `List[object]`), and that `registrations_history_paginated` is still `AsyncIterator[List[object]]`. Verify that it passes.
- [x] 3.4 Add the 32 return-type changes (dict → model) to the README "Breaking changes" section, grouped as in proposal.md. Verify that the operation names in the README match the generated method names.
- [x] 3.5 Verify that the offline suite passes (`pdm run pytest`) and that `pdm run ruff check` passes on the new and changed test files.

## 4. Final checks

- [x] 4.1 Run `openspec validate resolve-namespaced-model-returns --strict` and verify it passes.

## Workflow follow-up

- Commit the client after the fork commit (task 2.5).
- Follow-ups:
  - `@model`s for `Lti::RegistrationHistoryEntry` and `Lti::RegistrationUpdateRequest`
  - the operation mis-attribution bug (`ServiceCredentials-*`, `BadPermissionSettingError-*`, `users/self/todo`)
  - `additionalProperties`
  - generalize the `string|Model` oneOf rule to every `|` union (change `generalize-union-property-types`)
  - send list query parameters as `name[]` (change `fix-array-query-params`)
- Archive with `/opsx:archive` after review.
