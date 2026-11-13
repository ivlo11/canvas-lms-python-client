# Tasks

## 1. Ignore nested classes when building API groups (canvas-lms fork)

- [x] 1.1 Before changing any code, capture the baseline: run a throwaway script that writes `operationId → response schema (JSON)` for every operation in `public/doc/openapi/canvas.openapi.yaml` to the scratchpad. Verify that the file lists 21 ids prefixed `ServiceCredentials-`, `BadPermissionSettingError-` or `RecordAlreadyExists-`, and 0 prefixed `MetadataSaxDoc-`.
- [x] 1.2 In `spec/lib/swagger_yard/canvas_adapter_spec.rb`, add `describe "nested classes in controllers"` with the 8 cases from design D3. Use `YARD::Registry.clear` with `YARD.parse_string` fixtures, and stub `described_class.canvas_routes`. Verify with `bin/rspec spec/lib/swagger_yard/canvas_adapter_spec.rb` in the web container that cases 1–4, 6 and 8 fail (or error on the missing `nested_class?`), and that cases 5 and 7 pass under the current name-list guard. **Notes:** case 7 also failed before the fix, because its fixture has a nested class, which takes over the resource whatever the controller's namespace. Cases 1–4, 6 and 8 failed and case 5 passed, as expected.
- [x] 1.3 Implement `CanvasAdapter.nested_class?` (D1) and the `add_yard_object` short-circuit in `patch_api_group!` (D2). Delete `PROBLEMATIC_SUB_CLASSES`, its guard in `add_info`, and the guard's comment. Verify that every D3 case passes, that `bin/rspec spec/lib/swagger_yard/` passes as a whole, and that `grep -rn PROBLEMATIC_SUB_CLASSES lib spec` returns nothing.
- [x] 1.4 Run `bin/rubocop lib/swagger_yard/canvas_adapter.rb spec/lib/swagger_yard/canvas_adapter_spec.rb` and verify it is clean.
- [x] 1.5 Regenerate the spec in the web container (`bundle exec rake doc:openapi`) and run the D4 comparison against the 1.1 baseline. Verify:
  - The removed ids are exactly the 21 misnamed ids, and each has its `Users-`, `RoleOverrides-` or `LatePolicy-` counterpart.
  - Every added id belongs to `users`, `role_overrides`, `late_policy`, `external_tools`, `collaborations`, `outcome_imports_api` or `lti/ims/authorization`. At least the 37 documented actions in proposal.md are present: check by summary.
  - Every unchanged id has an identical response schema, including all `Files-*` operations.
  - No tag or schema named `ServiceCredentials`, `BadPermissionSettingError`, `RecordAlreadyExists` or `MetadataSaxDoc` remains.
  - `Users-api_index` responds `array` of `$ref User`, `Users-missing_submissions` of `$ref Assignment`, and `RoleOverrides-api_index` of `$ref Role`.

  Record the added-operation count in these notes.

  **Notes:** 1006 → 1057 operations. 72 added ids: 21 renamed counterparts and 51 new (Users 21, ExternalTools 19, OutcomeImportsApi 6, Collaborations 5), covering 36 of the 37 documented actions. The missing one is `Lti::IMS::AuthorizationController#authorize`: its route is drawn in the `/api/lti` route set, but `TokenScopes.api_routes` doesn't return it, so the generator has no route for it, before or after this fix. The stray `InvalidGrant` tag is now an empty `Authorization` tag, like the 140 other tags without operations. 17 renamed operations changed responses, all restorations: 7 RoleOverrides, `Users-api_index` and `Users-missing_submissions` regained their `$ref`s (`RoleOverrides-manageable_permissions` → `Permission`), and 10 regained their `@example_response` examples, which are also tracked by operation id.
- [x] 1.6 Commit in the fork following its commit guidelines: generator, its spec, and the regenerated YAML. Verify with `git log -1 --stat` that no controller files are included. **Notes:** committed as `fix(swagger_yard): skip nested classes in api groups` (2 files). `public/doc/` is untracked in the fork, and no earlier generator commit included the YAML, so it isn't committed.

## 2. Regenerate the client and remove orphans (canvas-lms-python-client)

- [x] 2.1 Copy `src/.openapi-generator/FILES` to the scratchpad, then regenerate the client (`openapi-generator-cli generate` with `openapi-generator-config.yaml`, `-t mustache-templates`, `-o src`). Verify that `api/users_api.py`, `role_overrides_api.py`, `late_policy_api.py`, `external_tools_api.py`, `collaborations_api.py` and `outcome_imports_api_api.py` exist.
- [x] 2.2 Delete the files listed in the old `FILES` but not the new one (D5), skipping anything matched by `src/.openapi-generator-ignore`. Verify that `api/service_credentials_api.py`, `api/bad_permission_setting_error_api.py` and `api/record_already_exists_api.py`, and their docs and generated tests, are gone, and that `git status` shows no custom file deleted or changed. **Notes:** generated tests aren't in `FILES`, so the `test_<module>.py` of each orphaned API or model was deleted too. Request models were renamed with their APIs (`BadPermissionSettingError*Request*` → `RoleOverrides*Request*`, `RecordAlreadyExistsCreateRequest*` → `LatePolicyCreateRequest*`).
- [x] 2.3 Verify the restored types in the generated code: `users_api_index_paginated` is `AsyncIterator[List[User]]`, `users_missing_submissions_paginated` is `AsyncIterator[List[Assignment]]`, and `role_overrides_api_index_paginated` is `AsyncIterator[List[Role]]`. Verify that each has an `_all` method.

## 3. Client tests and docs (canvas-lms-python-client)

- [x] 3.1 Add `test/test_api_operation_coverage.py` (custom; add it to `src/.openapi-generator-ignore` and the README list). It checks offline:
  - No API class or method name contains `service_credentials`, `bad_permission_setting_error`, `record_already_exists` or `metadata_sax_doc`.
  - `UsersApi` has `users_api_show`, `users_create` and `users_update` (the names of "Show user details", "Create a user" and "Edit a user").
  - `ExternalToolsApi`, `CollaborationsApi` and `OutcomeImportsApiApi` exist and have at least one operation each.

  Verify that it passes, and that it fails against the pre-change client: check out the old `api/__init__.py` and confirm the failure, then restore it.
- [x] 3.2 Rename `service_credentials_todo_items` → `users_todo_items` in `UNDOCUMENTED_PAGINATED_OPERATIONS`. Run `test_paginated_response_types.py`. For each newly reported undocumented paginated operation, confirm in its controller that it has no `@returns`, then add it to the allowlist with a comment naming its controller. **Notes:** no new undocumented paginated operations were reported. Verify that the guard and `test_all_iterator_only_for_list_responses` pass.
- [x] 3.3 Add an integration test, `test_users_and_roles_pages_typed` (admin client), that iterates `users_api_index_paginated(account_id="self")` and `role_overrides_api_index_paginated(account_id="self")` and asserts `User` and `Role` items. Verify with `pdm run pytest --integration -m integration -v` that it passes against the seeded instance. Record any strict-model `ValidationError` as a follow-up naming the model and field. **Notes:** passed, with no `ValidationError`.
- [x] 3.4 ~~Add the renames to the README "Breaking changes" section.~~ Superseded on 2026-11-01: the client has never been released and has no consumers, so breaking changes are not documented and the README section was removed.
- [x] 3.5 Verify that `pdm run pytest` passes offline and that `pdm run ruff check` on the new and changed test files is clean.

## 4. Final checks

- [x] 4.1 Run `openspec validate fix-nested-class-api-groups --strict` and verify it passes.

## Workflow follow-up

- Commit the client after the fork commit (task 1.6). Coordinate the regeneration order with `generalize-union-property-types` and `fix-array-query-params` (design D6).
- Follow-ups:
  - type or document newly exposed undocumented endpoints
  - any `@model` mismatches found on the new endpoints
  - `Lti::IMS::AuthorizationController#authorize` has no route in `TokenScopes.api_routes`, so it stays out of the spec
- Archive with `/opsx:archive` after review.
