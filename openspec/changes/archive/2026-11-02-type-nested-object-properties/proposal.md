# Proposal

## Why

When a model property is an object with its own documented `properties`, the spec generator drops them, and the client types the property as `Dict[str, Any]`. Callers then read `user.permissions["can_update_name"]` instead of `user.permissions.can_update_name`, with no field names, types or IDE help.

The cause is in `lib/swagger_yard/canvas_adapter.rb`. `convert_single_property` keeps only `type`, `description`, `example`, `format`, enums and array `items`, so a nested `properties` block (and its `required`) never reaches the spec.

A survey of every collected model (262 controller `@model`s plus `lib/schemas/docs`) found 2 object properties that lose their fields this way:

| Model | Property | Documented fields | Client type today |
|---|---|---|---|
| `User` | `permissions` | 3 booleans | `Dict[str, Any]` |
| `LearningObjectDates` | `peer_review_sub_assignment` | 7: `id`, `due_at`, `unlock_at`, `lock_at`, `only_visible_to_overrides`, `visible_to_everyone`, `overrides` (a list of `AssignmentOverride`) | `Dict[str, Any]` |

Array items that are objects with `properties` (`AssessmentQuestion.answers`, `Lti::LegacyConfiguration.extensions`, and the `settings` object inside it) already become inline models. That's because `convert_array_items` copies those items through unconverted.

## What Changes

- **canvas-lms generator (fork):** `convert_single_property` converts a nested `properties` block recursively, using the same conversion as top-level properties, and copies its `required`. So:
  - nested `datetime` becomes `string` / `date-time`
  - nested `$ref`s are sanitized
  - deeper objects recurse

  Properties without `properties` convert exactly as before. Array items are unchanged.
- **Regenerate** the spec and the client. The generator turns the two inline objects into models:
  - `User.permissions` becomes `UserPermissions`.
  - `LearningObjectDates.peer_review_sub_assignment` becomes `LearningObjectDatesPeerReviewSubAssignment`, whose `overrides` is `List[AssignmentOverride]` and whose dates are `datetime`.
- **Client tests:**
  - `test_user_model.py` asserts that `permissions` is a `UserPermissions` with bool fields equal to the captured JSON.
  - a new offline test deserializes a `LearningObjectDates` payload with a `peer_review_sub_assignment`
  - an offline annotation check confirms both properties are typed models, not dicts
- **BREAKING (client):** both properties change from `Dict[str, Any]` to models, so callers that indexed them must use attributes. The client is unreleased, so this isn't documented.
- **Not in scope:**
  - array items with `properties`, which already become models; converting them would also need enum handling (follow-up)
  - object properties documented without `properties`, such as `Lti::LegacyConfiguration.custom_fields`, which stay `Dict[str, Any]`

## Capabilities

### New Capabilities
<!-- None. -->

### Modified Capabilities
- `typed-operation-responses`: a model property documented as an object with its own fields is returned as a typed nested model that keeps those fields, not as an untyped mapping.

## Impact

- **canvas-lms (fork):**
  - `lib/swagger_yard/canvas_adapter.rb` and examples in `spec/lib/swagger_yard/canvas_adapter_spec.rb`. No controller or schema doc changes.
  - Not committed: the regenerated `public/doc/openapi/canvas.openapi.yaml`, and any seed helper used for live verification.
- **canvas-lms-python-client:**
  - Regenerated `models/user.py`, `models/learning_object_dates.py`, and the two new inline models with their docs and generated test stubs
  - `test/custom/unit/test_user_model.py`, a new `test/custom/unit/test_learning_object_dates_model.py` and its fixture, and an annotation check
