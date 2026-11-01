# Proposal

## Why

When a Canvas controller defines a nested class, such as an error class or a `Struct.new` constant, the spec generator lets that class take over the controller's API group. The controller's endpoints are then misnamed (`ServiceCredentials-api_index` instead of `Users-api_index`) and lose their documented response types. Every endpoint defined after the nested class is silently dropped from the spec.

This affects 7 controllers today: 21 operations are misnamed, at least 37 documented endpoints are missing, and these include the entire External Tools, Collaborations and Outcome Imports APIs, as well as `Show user details`, `Create a user` and `Edit a user`.

The current guard is a hand-maintained name list, `PROBLEMATIC_SUB_CLASSES = %w[MetadataSaxDoc]`. It only covers the one case that was noticed, and any new nested class in a controller would reintroduce the bug.

## What Changes

- **canvas-lms generator (fork):** in `lib/swagger_yard/canvas_adapter.rb#patch_api_group!`, any class whose YARD namespace is itself a class is ignored when building API groups. SwaggerYard reaches such classes by two paths, and the rule covers both:
  1. **Recursion:** the controller's group walks its children in source order. A nested class it reaches must not overwrite the group's resource or class name, and its methods must not be treated as controller actions.
  2. **Own group:** SwaggerYard also builds a separate group for every class in the file. A nested class must produce an invalid group, which gets dropped.
- **Remove `PROBLEMATIC_SUB_CLASSES` and its guard.** The rule must cover `FilesController::MetadataSaxDoc`, the case the list was created for. Concretely, `Files-*` operations stay unchanged, and there is no `MetadataSaxDoc` tag, group or operation.
- Regenerate the spec and the client. Affected controllers:

  | Controller | Nested class | Effect after fix |
  |---|---|---|
  | `UsersController` | `ServiceCredentials` (Struct) | 11 ops renamed `ServiceCredentials-*` → `Users-*`; 18 missing endpoints added |
  | `RoleOverridesController` | `BadPermissionSettingError` | 7 ops renamed → `RoleOverrides-*` |
  | `LatePolicyController` | `RecordAlreadyExists` | 3 ops renamed → `LatePolicy-*` |
  | `ExternalToolsController` | `InvalidSettingsError`, `TimingMeta` | 12 missing endpoints added (whole API) |
  | `CollaborationsController` | `NoCompatibleTool` | 3 missing endpoints added (whole API) |
  | `OutcomeImportsApiController` | `InvalidContentType` | 3 missing endpoints added (whole API) |
  | `Lti::IMS::AuthorizationController` | `InvalidGrant` | 1 missing endpoint added |
  | `FilesController` | `MetadataSaxDoc` | no change (previously guarded by the name list) |

  Counts are documented `@API` actions. Generated operation counts can be higher where Canvas routes an action in several contexts.
- **Restored types:** renamed operations whose `@returns` names an existing model regain it, for example `users_api_index` → `List[User]`, `users_missing_submissions` → `List[Assignment]`, and `role_overrides_api_index` → `List[Role]`. That removes 3 of the 13 untyped (`object`) paginated operations. The renamed `users_todo_items` has no `@returns`, so it stays among the undocumented ones under its new name.
- **BREAKING (client):**
  - `ServiceCredentialsApi` → `UsersApi`, `BadPermissionSettingErrorApi` → `RoleOverridesApi` and `RecordAlreadyExistsApi` → `LatePolicyApi`. Their methods are renamed to match, for example `service_credentials_api_index` → `users_api_index`.
  - Orphaned generated files for the old names are deleted.
  - The client is unpublished, so there's no version bump, the same as previous changes.

## Capabilities

### New Capabilities
- `api-operation-coverage`: every documented Canvas API endpoint that has a route appears in the client, grouped and named by its own controller. Helper classes defined inside a controller never rename, retype or hide its endpoints.

### Modified Capabilities
<!-- None. paginated-list-responses requirements are unchanged; its undocumented allowlist is updated as data (renamed and newly added entries) under the existing "tracked" requirement. -->

## Impact

- **canvas-lms (fork):** `lib/swagger_yard/canvas_adapter.rb` (`patch_api_group!`; remove `PROBLEMATIC_SUB_CLASSES`), new examples in `spec/lib/swagger_yard/canvas_adapter_spec.rb`, and the regenerated `public/doc/openapi/canvas.openapi.yaml`. No controller edits.
- **canvas-lms-python-client:**
  - Regenerated `api/`, `models/` and `docs/`. New API modules, including `users_api.py`, `role_overrides_api.py`, `late_policy_api.py`, `external_tools_api.py`, `collaborations_api.py` and `outcome_imports_api_api.py`, plus any new models the new endpoints reference.
  - Orphaned files for the old names are removed (`api/`, `docs/`, `test/`), found by diffing `src/.openapi-generator/FILES`.
  - `test/test_paginated_response_types.py`: the allowlist renames `service_credentials_todo_items` → `users_todo_items`. Newly exposed undocumented paginated operations are added to the allowlist, and the 3 that become typed are confirmed.
- **Other in-flight changes** (`generalize-union-property-types`, `fix-array-query-params`) also regenerate the client. See the design for sequencing.
- **Newly exposed endpoints** have never passed through the strict models or the integration tests. Type mismatches found later are follow-ups, the same policy as before.
