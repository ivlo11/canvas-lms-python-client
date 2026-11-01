# Design

## Context

- See proposal.md "Why". Requirements are in `specs/api-operation-coverage/spec.md`.
- **SwaggerYard 1.1.1, `Specification#parse_controllers`:** for every controller file, `yard_class_objects_from_file` returns **all** class objects in the file, nested ones included, and `ApiGroup.from_yard_object(obj)` is called for each. Only groups that are `valid?` (meaning `@resource` is not nil) are kept.
- **`ApiGroup#add_yard_object`:** for a `:class`, it calls `add_info`, and if the group is valid, recurses into `yard_object.children` **in source order**. For a `:method`, it calls `add_path_item`.
  - `Operation#operation_id` (`"#{api_group.resource}-#{ruby_method}"`) and `#tags` are computed **when the spec is written**, from the group's final `@resource`.
- **Canvas patch, `canvas_adapter.rb#patch_api_group!`:**
  - `add_info` returns early for names in `PROBLEMATIC_SUB_CLASSES` (`%w[MetadataSaxDoc]`). Otherwise it calls `super` and sets `@resource` from **the class being processed** (its name minus `Controller`). `super` also sets `@class_name = yard_object.path`.
  - `add_path_item` → `paths_from_yard_object_canvas` builds the route key `"#{underscore(@class_name)}##{method}"` and looks it up in `CanvasAdapter.canvas_routes`, a hash of `"controller#action"` → `[{path:, method:, context:, name:}]`.
- **What a nested class does today:**
  - Through recursion, `add_info` overwrites `@resource` and `@class_name`. Every operation is renamed when the spec is written. Later methods miss their routes and are dropped. `@returns` and example tracking, which is keyed by the operation id at parse time, no longer matches the final id, so the response types are lost.
  - Through its own group, the nested class becomes a valid but empty group, so a stray tag can be emitted.
  - The `MetadataSaxDoc` guard prevents both, but only for that name.
- YARD treats `X = Struct.new(...)` as a `ClassObject` (this is why `ServiceCredentials` took over `UsersController`). Every documented controller's namespace is a module (`Lti`, `Lti::IMS`, `Polling`, `Quizzes`, `SupportHelpers`, `LiveAssessments`) or unresolved (compact `class CoursePacing::X`, `MasterCourses::X`, …). None of them is a class.

## Goals / Non-Goals

**Goals:**
- One structural rule that replaces the name list and covers both SwaggerYard paths.
- A regeneration diff that can be checked mechanically against what's expected.

**Non-Goals:**
- Typing or documenting the newly exposed endpoints beyond what their `@returns` already says.
- Patching the SwaggerYard gem itself (vendoring or forking it).
- The other untyped paginated operations (missing `@model`s, doc corrections).

## Decisions

### D1: Nested class = a class whose YARD namespace is a class
Add `SwaggerYard::CanvasAdapter.nested_class?(yard_object)`. It returns true when `yard_object.type == :class` and `yard_object.namespace` responds to `type` with `:class`. Modules (`:module`), the root (`:root`) and unresolved proxies (`:proxy`) are not classes, so every current controller counts as top level.
- *Alternative: class name doesn't end in `Controller`.* That would misclassify a nested `FooController`, and it's a naming convention rather than structure.
- *Alternative: "the first class this group saw wins".* That covers recursion but not the own-group path, so the empty `ServiceCredentials` group would stay valid.
- *Alternative: extend `PROBLEMATIC_SUB_CLASSES`.* That's the status quo, and it breaks again on the next nested class.

### D2: Short-circuit in `add_yard_object`, before `add_info`
Prepend an `add_yard_object` override to the patched `ApiGroup` that does `return self if CanvasAdapter.nested_class?(yard_object)`, and otherwise calls `super`.
- **Recursion path:** the nested class is skipped together with its whole subtree, so its methods (for example `MetadataSaxDoc#start_element`) are never considered as actions, and the group's `@resource`/`@class_name` stay those of the controller.
- **Own-group path:** `from_yard_object(nested)` returns a fresh group whose `@resource` is nil, so it is invalid and `parse_controllers` drops it.

Delete `PROBLEMATIC_SUB_CLASSES` and the guard in `add_info`, including the comment that describes the symptom. `add_info` returns to its simple behavior.
- *Alternative: guard inside `add_info` (where the current guard lives).* `add_yard_object` would still recurse into the nested class's children, because the group is already valid, so its methods would be route-checked against the controller. A nested method named like a controller action (`index`, `show`) would be emitted twice or wrongly.

### D3: Test both paths with parsed YARD fixtures
In `spec/lib/swagger_yard/canvas_adapter_spec.rb`, under `describe "nested classes in controllers"`:
- Clear `YARD::Registry` and parse small strings with `YARD.parse_string`.
- Call `install!` (already exercised by the spec) and stub `described_class.canvas_routes` with a hash for the fixture actions.

Cases:
1. A nested error class **between** two documented actions: the group's resource is `Foo`, both actions have paths, and every operation id starts with `Foo-`.
2. A nested class **before** all actions (the external-tools shape): all actions are present.
3. `X = Struct.new(:a)` nested (the users shape): same as case 1.
4. A nested class with its own `def index` documented with `@API` (the trap from D2): only the controller's `index` is emitted, once.
5. The `MetadataSaxDoc` shape (a nested class with SAX methods, after the actions): the group is unchanged.
6. `ApiGroup.from_yard_object` on the nested class itself is not `valid?`.
7. A controller inside `module Lti` with a nested class: the resource is `Foo`, unaffected.
8. `nested_class?` unit cases: module namespace, root, proxy, class namespace.

### D4: Verify the regeneration by diffing operation ids and response types
Before regenerating, save `operationId → response schema` for every operation in `canvas.openapi.yaml` with a small throwaway script. After regenerating, compare:
- removed ids must be exactly the 21 `ServiceCredentials-* / BadPermissionSettingError-* / RecordAlreadyExists-*` ids
- each must have its `Users-/RoleOverrides-/LatePolicy-` counterpart
- added ids must all belong to the 7 affected controllers
- the response type of every unchanged id must be identical

Any other difference is investigated before committing. The same comparison checks the `Files-*` operations, the requirement that replaces the name list.

### D5: Client cleanup by manifest diff
Copy `src/.openapi-generator/FILES` before regenerating. After regenerating, delete the files that were in the old manifest but not the new one, which is where `service_credentials_api.py`, its docs and its generated test live. Never delete paths listed in `.openapi-generator-ignore`.

### D6: Sequencing with other in-flight changes
`generalize-union-property-types` and `fix-array-query-params` also regenerate the client. Whichever lands second regenerates on top of the first. This change's D4 comparison runs on the canvas-lms spec only, so it isn't confused by client-template changes. The client tests in task group 3 run against whatever is regenerated last.

## Risks / Trade-offs

- [A real controller is defined inside a class, so D1 would hide it] → None exists today. The census of `@API` controllers shows only modules or unresolved namespaces. D4's "no unexpected removals" check catches one appearing later.
- [Newly exposed endpoints have inaccurate `@model`s, so strict deserialization fails at runtime] → Out of scope here. They are recorded as follow-ups when integration tests or users hit them, the same as the polling and LTI rounds.
- [Newly exposed paginated endpoints are undocumented] → The guard test fails and names them. They are added to the allowlist in task 3.3, with no silent pass.
- [Downstream code uses `ServiceCredentialsApi` and similar names] → The client is unpublished and has no consumers, so the renames are not documented. In this repo only the guard allowlist references a renamed operation.

## Migration Plan

1. In the fork: specs, then the fix, then remove the list, then the D4 diff, then commit (generator, spec file, regenerated YAML).
2. In the client: regenerate, clean up via the D5 manifest diff, update the tests and README, then commit.

Rollback: revert both commits. That restores the name list and the misnamed operations.
