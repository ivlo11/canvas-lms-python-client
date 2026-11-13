# Design

## Context

- See proposal.md "Why". Requirements are in `specs/paginated-list-responses/spec.md`.
- canvas-lms spec pipeline:
  1. `CanvasAdapter.install!` ends with `collect_model_schemas!`, so every `@model` schema is in `CanvasAdapter.canvas_schemas` **before** YARD parses any operation.
  2. While parsing, the patched `SwaggerYard::Operation.from_yard_object` runs `process_canvas_tags`, which calls `process_returns_tags` and then `process_example_tags`, in that order. For each `@returns` that names a model, `process_returns_tags` calls `operation.add_response_type(...)` and `track_operation_model(op_id, model, schema)`, which records `{model:, is_array:}` in `CanvasAdapter.operation_models`.
  3. `OpenApiGenerator#apply_canvas_enhancements!` then runs `add_canvas_schemas!` (copies `canvas_schemas` into `components.schemas`), `replace_responses_with_schema_refs!` (turns `operation_models` into `$ref`), `add_canvas_examples!` and `deduplicate_tags!`.
- `replace_responses_with_schema_refs!` only rewrites responses that already have `content["application/json"].schema` (`json_content?`). swagger_yard emits that content only when the operation has a response type. Undocumented operations have none, for example `{"default" => {"description" => ...}}`, so tracking a model alone does not type them; `add_response_type` is also required.
- `process_example_response_tag` sees the raw `@example_response` text before `parse_json_example`.
  - The 8 target examples are not valid JSON (`[Poll]`, and the unquoted key in outcome results).
  - The quiz submission events example is literal JSON with values, so the regex does not match it.
  - The grading period sets example names `GradingPeriodGroup`, which is not in `canvas_schemas`, so model resolution skips it.
- `canvas_schemas` keys use `::` → `_` (`sanitize_schema_name`). `model_schema_exists?` checks the name exactly as given.
- Client: `mustache-templates/api.mustache` emits `<op>`, then `<op>_paginated` and `<op>_all` inside `{{#vendorExtensions.x-paginated}}`. The `_all` signature already branches on the operation-level `{{#isArray}}`, and when the page is not a list its body yields `[page]`. `api_test.mustache` generates three `test_<op>_paginated_*` tests per paginated operation, and they actually call `<op>_all`. openapi-generator never overwrites existing test files, so the committed `test_*_api.py` files were stale from the first generation. (Corrected during implementation; see D3.)
- Generated pydantic models declare non-required properties as `Optional[...] = None`, and `from_dict` uses `obj.get(key)`, so a missing optional key deserializes to `None`.

## Goals / Non-Goals

**Goals:**
- Type the 8 operations using only what Canvas's docs say, with no edits to controller docs.
- Make the client's iterator set honest: `_all` only where items exist to iterate.

**Non-Goals:**
- Retaining undocumented keys (`additionalProperties`).
- Recognizing other example shapes, such as multiple keys, literal JSON or nested wrappers. The rule is deliberately narrow.
- Changing `_paginated`, `Link` handling, or `pagination.py`.

## Decisions

### D1: Infer the wrapper in the Canvas adapter, as an implied `@returns`
Interpreting Canvas doc tags is the adapter's job, so the inference lives in `lib/swagger_yard/canvas_adapter.rb`, next to `@returns` and `@model` handling. It treats an `@example_response` of `{ "<key>": [<Model>] }` as if the controller had written `@returns <Key>Response`. `open_api_generator.rb` is not changed: its existing `add_canvas_schemas!` and `replace_responses_with_schema_refs!` do the rest.

**Public helpers on `SwaggerYard::CanvasAdapter`** (pure, unit-testable):
- `wrapped_list_example(text)` → `[key, model_name]` or `nil`. It strips `text` and matches `WRAPPED_LIST_EXAMPLE` = `\A\{\s*"?([a-z][a-z0-9_]*)"?\s*:\s*\[\s*([A-Z][A-Za-z0-9_:]*)\s*\]\s*\}\z`. It resolves the model to a `canvas_schemas` key, trying it exactly first and then with `::` replaced by `_`, and returns `nil` if neither exists.
- `register_wrapper_schema(key, model_name)` → the wrapper name or `nil`. It adds the D2 schema to `canvas_schemas`, reuses an identical existing one, and returns `nil` with a warning (`puts`, as in `collect_model_schemas!`) if a different schema already has that name.
- The adapter records every typed operation id in `wrapped_list_operations` (reset in `load_canvas_routes!`, like the other storage), so the count can be reported.

**Hook** (in the patched `process_example_response_tag`, before `parse_json_example`, with the raw text):
1. Proceed only if the docstring has **no `@returns` tags** (`docstring.tags(:returns).empty?`). This is the parse-time version of "the response has no schema": every `@returns`, including `@returns object`, gives the operation a response type.
2. Call `wrapped_list_example(example_text)`, then `register_wrapper_schema(key, model)`. Skip if either returns `nil`.
3. Call `operation.add_response_type(SwaggerYard::Type.new("object"), <existing default response description>)`. Without this, the response has no JSON content and `replace_responses_with_schema_refs!` skips it (see Context). Keep the existing description rather than passing `nil`.
4. Call `track_operation_model(op_id, wrapper_name, "object")`, which records `{model: wrapper_name, is_array: false}` so the generator writes a plain `$ref`.

Storing the example is unchanged, so the spec keeps the example next to the new schema.

- *Alternative (implemented first, then replaced): a post-processing step on the final spec hash in `open_api_generator.rb#apply_canvas_enhancements!`.* It worked and gave the same 42/14 result, but it added a second way to register schemas and write `$ref`s, and it had to skip examples already parsed into Hashes. The original reason for rejecting the adapter hook, "components don't exist yet at parse time", was wrong: `collect_model_schemas!` runs in `install!`, before parsing.

The inference applies to every operation, paginated or not. The first regeneration matched 42 operations (14 wrappers), not just the 8 paginated targets. The other 34 are show/create/update operations that Canvas documents and returns in the same wrapped form, and keeping them was approved. Restricting the step to `x-paginated` was considered and rejected.

- *Alternative: a broader parser (multiple keys, literal JSON).* That would start guessing types from sample values, which goes against the "read Canvas's docs literally" principle.

### D2: Wrapper schema naming and sharing
The name is `<key camelized>Response`, so `poll_sessions` becomes `PollSessionsResponse` and `quiz_ip_filters` becomes `QuizIpFiltersResponse`. The schema is:
```yaml
type: object
description: "Paginated `<key>` list response (from the Canvas example response)."
properties:
  <key>:
    type: array
    items: { $ref: "#/components/schemas/<Model>" }
```
There is no `required`, because Canvas marks nothing as required. Rules:
- If a schema with that name already exists **and is identical**, reuse it. This is how the 3 poll-sessions operations share one model.
- If a schema with that name exists **and differs**, either from Canvas or from another key/model pair, skip that operation and log a warning. Never overwrite.
- *Alternative: name by operation (`PollsIndexResponse`).* That would create 3 identical poll-sessions classes, and callers would have to handle each one separately.
- *Alternative: name by model (`PollList`).* Canvas sometimes uses the same model under different keys, so names could collide. Naming by key reflects what is actually on the wire.

### D3: Gate `_all` on `isArray` in the template
Wrap the whole `@validate_call … def {{operationId}}_all … ` block in `{{#isArray}} … {{/isArray}}`, inside the existing `x-paginated` section. Simplify the now-unreachable `{{^isArray}}Any{{/isArray}}` branch of the signature, and remove the `if not isinstance(_page_data, list)` wrapper from the body, since those lines can no longer run.
- **Generated tests (added during implementation):** in `api_test.mustache`, the three paginated tests call `{{operationId}}_all` when `isArray` and `{{operationId}}_paginated` otherwise. The existing non-list assertions (one page, three pages, empty) already describe `_paginated`'s behavior. Because the generator skips existing test files, the generated `test_*_api.py` files are deleted before regeneration. This rewrote 35 files: the 44 non-list operations now test `_paginated`, and 10 stale operations that became lists in earlier changes now take the list branch.
- *Alternative: keep `_all` for wrappers and unwrap a known key.* We rejected this during exploration because it requires a vendor extension and loses sibling keys.
- *Alternative: generate `_all` but raise `TypeError` for non-list responses.* That ships a method that can never work.

### D4: Tests on both sides
- **canvas-lms** (`spec/lib/swagger_yard/canvas_adapter_spec.rb`):
  - Unit examples set `canvas_schemas` directly and call the public helpers: quoted and unquoted keys; a model with `::`; an unknown model; literal-JSON and multi-key examples; reuse of an identical wrapper; a conflicting existing name that is not overwritten; no `required` on the wrapper.
  - Hook examples, after `define_canvas_tags`/`patch_operation!`, run `process_canvas_tags` on a `YARD::Docstring`. An `@example_response` with no `@returns` tracks the wrapper in `operation_models` and gives the operation a response type. With a `@returns` present, nothing is inferred. The example is stored either way.
  - Generator wiring: an `open_api_generator`-level example feeds a tracked wrapper through `add_canvas_schemas!` and `replace_responses_with_schema_refs!` and asserts the `$ref`. This guards the `json_content?` dependency.
- **Client, offline** (`test_paginated_response_types.py`):
  - The allowlist shrinks by 8.
  - A new test checks, for every API class, that `<op>_all` exists exactly when `<op>_paginated` is annotated `AsyncIterator[List[...]]`.
  - New tests check that each of the 14 wrappers' `from_dict`/`from_json` deserializes a sample page into item models and accepts a page without the wrapper key.
- **Client, integration:** add polls and quiz submissions `_paginated` tests (admin client, skip when there is no data). They assert the wrapper type and the item model type.

## Risks / Trade-offs

- [The regex is too strict, for example comments or trailing text inside the example, so a valid case is missed] → A missed case stays untyped and allowlisted, which is safe. The guard test surfaces it, and the rule can be widened deliberately later.
- [Removing `_all` breaks downstream code that called it on non-list operations] → Those calls yielded either nothing or one wrapper per page. Call this out in the README under a "Breaking changes" note. No version bump is needed (see Open Questions).
- [Strict item models reject live data, for example `OutcomeResult` field types] → Integration tests surface this. Record mismatches as follow-ups and do not loosen the models, the same policy as the previous change.
- [Wrapper property name collides with a pydantic or BaseModel attribute] → All 6 keys are plain snake_case nouns, so no collision. The canvas-lms spec can assert that `_KEY` is not a reserved name if needed.
- [Spec regeneration brings unrelated churn] → Review the diff. Only 14 new schemas and 42 response `schema` additions are expected.

## Migration Plan

1. In the fork: adapter change plus specs, then regenerate `canvas.openapi.yaml`, then commit.
2. In the client: template change, regenerate, update tests and README, then commit.

Rollback means reverting both commits.

## Open Questions

- ~~Should `packageVersion` in `openapi-generator-config.yaml` be bumped because of the `_all` removals?~~ **Resolved: no.** The client has never been published, so it has no downstream users to signal to, and `packageVersion` stays `1.0.0`.
