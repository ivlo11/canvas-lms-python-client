# Design

## Context

- Motivation: see proposal.md, "Why". Requirements: `specs/typed-operation-responses/spec.md` and `specs/paginated-list-responses/spec.md`.
- **How YARD parses a brace `@returns`:** YARD treats `{ ... }` like `[ ... ]`. It strips the delimiters and splits the contents on top-level commas:
  - `{ "a": [M], "b": "integer" }` becomes `tag.types == ["\"a\": [M]", "\"b\": \"integer\""]`.
  - `{Object} text` becomes `types == ["Object"]`, `text == "text"`.
  - `[Object]` also becomes `types == ["Object"]`, so braces and brackets can only be told apart in the raw docstring (`docstring.all`).
- **`canvas_adapter.rb#process_returns_tags`** builds `types = [tag.types.to_s.tr('"', "")]`. `Array#to_s` always yields a `[...]` string, so `array_type?` matches every brace `@returns` and emits `array<object>`. The client then deserializes the JSON object as `List[object]`, iterating the dict and returning its key names.
- **Change 2 (`infer_wrapped_list_response`):**
  - It runs only when an operation has **no** `@returns` tag.
  - It matches `WRAPPED_LIST_EXAMPLE` against `@example_response`.
  - It calls `register_wrapper_schema(key, schema_name)`, which names the wrapper `"#{key.camelize}Response"`, reuses an identical schema and refuses to overwrite a different one.
  - It tracks the wrapper via `track_operation_model(op_id, wrapper, "object")`, and `replace_responses_with_schema_refs!` turns that into a `$ref`.
- **Operation naming:**
  - Parse-time operation ids are `"#{api_group.resource}-#{name}"`.
  - `name` is the Rails action, with a route-context suffix (`index_for_courses`) when the action is routed more than once (`resolve_unique_name`).
  - `api_group.resource` is the controller class name minus `Controller` and its namespace (`Lti::RegistrationsController` → `Registrations`).
  - The Rails action itself is the documented method's name (`docstring.object.name`).
- **Census of `@API` actions with a brace `@returns` and a route in the spec: 20.**
  - `Lti::IMS::DynamicRegistrationController#show_configuration` is documented but has no API route, so it isn't in the spec.
  - `BrandConfigsController#create` has no `@API` tag.

## Goals / Non-Goals

**Goals:**
- No brace `@returns` ever produces a list response.
- Typed wrappers for brace `@returns` whose entries are all typeable, read as written.
- One naming rule for every generated wrapper, stable under additions and source reordering.

**Non-Goals:**
- Changing change 2's inference rule, its `@example_response` grammar, or when it runs.
- Lists of primitives (`[String]`), nested inline objects, unions, decimal literals, and `additionalProperties` on wrappers. The first four fall back to a plain object.
- Editing Canvas controller docs.

## Decisions

### D1: Detect the brace form from the raw docstring
For each `@returns` tag, find the matching `@returns` line in `docstring.all` (the n-th tag matches the n-th `@returns` line) and take its text after the tag name. If that text starts with `{`, the tag is handled by D2/D3 and never reaches the `tag.types.to_s` path. Every other `@returns` takes the existing path unchanged.
- *Alternative: rebuild from `tag.types`.* `{Object}` and `[Object]` are indistinguishable there.
- *Alternative: fix `types.to_s` generally.* That changes how every `@returns` is read, which is a larger blast radius than this change needs.

### D2: Strict, all-or-nothing inline-object grammar
```
literal   := "{" entry ("," entry)* "}" [prose]       prose must not start with "|"
entry     := key ":" value
key       := '"' ident '"' | ident                    ident = [a-z][a-z0-9_]*
value     := "[" Model "]"                             -> array of $ref
           | Model                                      -> $ref
           | primitive | '"' primitive '"'              -> that type (case-insensitive)
           | "true" | "false"                           -> boolean
           | '"' text '"'  (text not a primitive name)  -> string
           | digits                                     -> integer
primitive := integer | string | boolean | number
Model     := a name that resolve_schema_name resolves (namespaced names included)
```
- Entries are split on commas at bracket and brace depth 0.
- A bare word that is not a primitive name, `true` or `false` must resolve as a model. Otherwise the whole literal is rejected, and so is any single entry that fails.
- A rejected literal is a plain object (D3).
- This is a new parser, separate from `WRAPPED_LIST_EXAMPLE`, by decision.
- *Alternative: type whatever entries parse and drop the rest.* That yields a model that silently loses keys, which is worse than a mapping that keeps them.
- *Alternative: accept prose after the brace without the `|` rule.* That would type `validate_lti_configuration` as its first union branch only.

### D3: Emitted response per outcome
- **Parsed:** register a wrapper (D4), whose properties are built from the entries and which has no `required` and no `additionalProperties`. Then `track_operation_model(op_id, wrapper, "object")`.
- **Rejected:** add the response type `object` with no model tracking. The client returns `object`: the parsed JSON mapping, which keeps everything Canvas sent.
- Either way, a brace `@returns` counts as "has `@returns`", so change 2's example inference still doesn't run for it. That is unchanged behavior. Of the 20 brace operations, only `career_experience#enabled`, `what_if_grades#update` and `show_configuration` (not routed) have an example, and none would be typed by change 2's rule.

### D4: Wrapper name = resource + Rails action
`register_wrapper_schema` takes the wrapper name and its properties. The callers, D3 and change 2's `infer_wrapped_list_response`, build the name as `"#{api_group.resource}#{rails_action.camelize}Response"`:
- `AccountCalendarsApi` + `visible_calendars_count` → `AccountCalendarsApiVisibleCalendarsCountResponse`
- `PollSessions` + `opened` → `PollSessionsOpenedResponse`
- `QuizSubmissionsApi` + `submission` → `QuizSubmissionsApiSubmissionResponse`

Using the Rails action rather than the suffixed operation id means `index` and `index_for_courses` share `GradingPeriodsIndexResponse`. The name depends only on the operation's own controller and action, so adding actions or reordering methods never renames a wrapper. Descriptions state the source: "(from the Canvas `@returns`)" or "(from the Canvas example response)".

The reuse/refuse guard stays. An identical schema is reused, which is how route aliases share. A different schema under the same name is refused with a warning, and that operation falls back to a plain object (D3, rejected).
- *Alternative: name by key (change 2 today).* Collides for multi-key and scalar-only objects (`count`).
- *Alternative: controller name, adding the action only on a clash.* An unrelated addition would rename existing wrappers.
- *Alternative: controller plus keys.* Stable, but unwieldy names, and it still clashes on the same keys with different types.

### D5: Change 2's wrappers are renamed in place
Only the name passed to `register_wrapper_schema` changes. `WRAPPED_LIST_EXAMPLE`, `wrapped_list_example` and the "no `@returns`" trigger are untouched. Each of the 14 shared wrappers becomes one wrapper per Rails action (for example `PollsResponse` → `PollsIndexResponse`, `PollsCreateResponse`, `PollsShowResponse`, `PollsUpdateResponse`).

### D6: Verify the regeneration by diffing response schemas
As in `fix-nested-class-api-groups`, save `operationId → response schema` before and after, then check:
- The 20 brace operations change from `array of object` to a wrapper `$ref` (10) or `type: object` (10).
- Every change 2 operation changes only from the old wrapper `$ref` to its `<Resource><Action>Response` `$ref`, and the new schema's properties equal the old one's.
- No other operation's response changes.
- No schema named `<Key>Response` from change 2 remains.

### D7: Client cleanup and tests
- Remove orphaned old wrapper modules, docs and generated tests by diffing `src/.openapi-generator/FILES` before and after, skipping `.openapi-generator-ignore` paths.
- `WRAPPED_LIST_RESPONSES` in `test_paginated_response_types.py` is keyed by the new names, one entry per wrapper.
- A new custom offline test, `test/test_inline_object_responses.py`, asserts:
  - the return annotations of the 20 operations
  - that each typed wrapper deserializes the documented shape
  - that the 10 plain-object operations deserialize a JSON object to the same mapping, the regression for the key-names bug

## Risks / Trade-offs

- [Two controllers in different namespaces share a resource name and an action, and return different wrappers] → The D4 guard refuses the second with a warning, and that operation stays a mapping. D6's "no other change" check would show it. None exists today.
- [Canvas omits keys it documented, or returns extra keys it didn't] → Every property is optional, so an omitted key leaves its attribute unset. Extra keys are dropped by the model, which is accepted (no `additionalProperties`, the same as `@model`s).
- [A literal is misleading, for example `"1"` meant as an integer] → The literal rule applies to `@returns` only. The 2 literal cases today (`true`, `"eyJ..."`) are unambiguous.
- [Many identical wrapper models (about 40)] → Accepted for name stability. Each operation's return type is still exact.
- [`account_calendars_api_index` loses `_all`] → Consistent with the wrapper rule: `total_results` is a sibling of the list, so a page isn't a list.

## Migration Plan

1. Fork: specs, then the parser and naming, then regenerate, then the D6 diff, then commit (generator, spec file, regenerated YAML).
2. Client: regenerate, clean up via the D7 manifest diff, update the tests and the README wrapper example, then commit.

Rollback: revert both commits.
