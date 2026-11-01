# Proposal

## Why

Canvas `@model` docs write a field that can hold several types as `"type": "a|b"`. `resolve-namespaced-model-returns` handled only one shape: `string|Model` with a `$ref` becomes `oneOf [string, Model]`. Any other union gets dropped quietly. For example, `integer|string` passes through as the literal type `"integer|string"`, `Model|null` keeps only the model, and `Lti::A|Lti::B` never resolves. The client then rejects responses that match the documentation. Today only the 5 `string|User` fields use the form, so this is the right time to replace the narrow check with one rule, before new docs depend on the gaps.

## What Changes

- **canvas-lms generator (fork):** one rule converts every `|`-separated property type:
  - `null` makes the property nullable.
  - Each primitive part maps to its OpenAPI type and format. Primitives that share a JSON type merge into one plain variant (`string|DateTime` → `string`).
  - Each model part (namespaced or not) resolves to its collected schema, as does the `$ref`.
  - A single remaining variant is emitted as is. Several become `oneOf`.
- Unions the client can't tell apart, meaning two or more models, fall back to the first model with a generator warning, instead of emitting a `oneOf` that fails at runtime. Part names that resolve to nothing also get a warning.
- This replaces the `string`-only check added in `resolve-namespaced-model-returns`. Properties with a single type, and the existing `["x", "null"]` array form, produce identical output.
- Regenerate the spec. The diff must be empty, because the 5 `string|User` fields convert the same as before. If the client changes at all, regenerate it too.

## Capabilities

### New Capabilities
- `union-field-types`: model fields documented with several types accept a value of any of those types, and stay strict about everything else.

### Modified Capabilities
<!-- none -->

## Impact

- **canvas-lms (fork):** `lib/swagger_yard/canvas_adapter.rb` (`convert_single_property` and new variant helpers) and `spec/lib/swagger_yard/canvas_adapter_spec.rb`.
- **canvas-lms-python-client:** no generated change expected. Offline tests in `test_lti_model_payloads.py` keep guarding the `string|User` case.
