# Design

## Context

- Motivation: see proposal.md, "Why". Requirement: `specs/typed-operation-responses/spec.md`.
- **The conversion** (`lib/swagger_yard/canvas_adapter.rb`):
  - `convert_canvas_schema_to_openapi` converts a model's top-level `properties` with `convert_properties`, which calls `convert_single_property` on each one, and copies `required`.
  - `convert_single_property`:
    - returns a sanitized `$ref` (or the `string|Model` `oneOf`)
    - otherwise sets the type (`convert_property_type`), `description`, `example` and `format`, enums from `allowableValues`, and array `items`
    - never looks at a nested `properties` or `required`, so they're dropped
  - `convert_array_items` returns object items unchanged (`convert_item_type`'s fallback), so items with `properties` reach the spec raw. The generator builds an `…Inner` model from them.
- **Survey:** I patched `parse_and_store_schema` / `convert_canvas_schema_to_openapi` in a throwaway runner (with `define_canvas_tags` called first) and walked every collected model. Results:
  - Objects with `properties`: `User.permissions` (3 fields) and `LearningObjectDates.peer_review_sub_assignment` (7 fields, including 3 `"datetime"` types and `"items": {"$ref": "AssignmentOverride"}`).
  - Array items with `properties`: `AssessmentQuestion.answers[]`, `Lti::LegacyConfiguration.extensions[]` and its `settings`. These are already typed.
  - A grep of controller `"properties"` keys also flagged `Conversation.properties`. That's a field *named* `properties`, a list of strings, not a nested object.
- **Live data:**
  - `User.permissions` is captured in `test/custom/unit/fixtures/users/users_self.json` (4 payloads; the three keys are always present).
  - `peer_review_sub_assignment` is sent by `GET /courses/:course_id/assignments/:assignment_id/date_details`. It only appears when an assignment has a peer review sub-assignment, which needs the hidden, course-level `peer_review_allocation_and_grading` flag. No seeded assignment has one today.

## Goals / Non-Goals

**Goals:**
- Both nested objects become typed client models that keep every documented field, with the same type rules as top-level properties.

**Non-Goals:**
- Converting array items with `properties` through the same path. They're already typed, and `convert_single_property` handles enums only from `allowableValues`, so it would drop the raw `enum` that `Lti::LegacyConfiguration.extensions[].privacy_level` relies on today (follow-up).
- Documenting fields for object properties that have no `properties` (`custom_fields`, `public_jwk`, `labels`, …).
- Choosing the inline model names. The generator's `InlineModelResolver` names them `<Model><Property>`.

## Decisions

### D1: Recurse in `convert_single_property`
After the existing conversion, if `prop_def["properties"]` is a Hash:
- set `converted_prop["properties"] = convert_properties(prop_def["properties"])`
- copy `required`, as an array (a string becomes a one-element array, matching `convert_canvas_schema_to_openapi`)
- set `type` to `object` if the property didn't declare one

Recursion reuses `convert_properties`, so a nested object inside a nested object works too. `$ref` properties return early as today, so a `$ref` with sibling `properties` is unaffected.
- *Alternative: hoist each nested object into a named component schema (for example `UserPermissions`) in the adapter.* That gives stable, Canvas-chosen names. But the generator already derives the same names, and hoisting would need collision handling (follow-up, if names ever clash).

### D2: Tests in the fork
Add `.convert_single_property` examples:
- an object with nested `properties` keeps them, converted (`"datetime"` becomes `string` / `date-time`, and a nested `$ref` is sanitized)
- `required` is copied
- a nested object two levels deep is converted
- a property without `properties` produces exactly today's output

### D3: Live check for `peer_review_sub_assignment`
Try to seed one, using an uncommitted seed helper:
- enable `peer_review_allocation_and_grading` on a seeded course
- enable peer reviews on an assignment so Canvas creates its peer review sub-assignment
- capture `date_details` with the admin token

If Canvas can't produce one in this instance, use the controller's documented example as the fixture, record the field as unverified in the notes, and keep the test.

**Apply result:** at the user's request, the live check was replaced with a fixture built by hand from the `@model` docs, so the field is unverified against live Canvas.

### D4: Client tests
- `test_user_model.py`: assert that `user.permissions` is a `UserPermissions` and that each of its 3 fields is a `bool` equal to the JSON. This replaces the dict assertions.
- `test_learning_object_dates_model.py` uses `fixtures/learning_object_dates/date_details.json` (from D3). It asserts that `peer_review_sub_assignment` is a `LearningObjectDatesPeerReviewSubAssignment`, that `due_at` is a `datetime` when set, and that `overrides` items are `AssignmentOverride`.
- An offline annotation check confirms that `User.model_fields["permissions"]` and `LearningObjectDates.model_fields["peer_review_sub_assignment"]` are not `Dict[str, Any]`.

### D5: Commits
- **Fork:** the adapter and its spec only, in the fork's commit format. It's not a PR.
- **Client:** the regenerated files and tests, staging only this change's files.

## Risks / Trade-offs

- [The typed nested fields reject a real payload, for example the `overrides` items or the date formats] → D3's live capture. Any `ValidationError` is fixed in the controller doc and recorded.
- [The inline model names change if the generator's naming changes] → The tests reference the generated names, so a rename fails loudly. D1's alternative is the fallback.
- [Other schemas change unexpectedly] → The spec diff check in the tasks confirms that only `User` and `LearningObjectDates` change.

## Migration Plan

1. Fork: write the examples, change the adapter, regenerate the spec (uncommitted), check the diff, then commit.
2. Client: regenerate, update and add the tests, run the offline and integration suites, then commit.

Rollback: revert both commits.
