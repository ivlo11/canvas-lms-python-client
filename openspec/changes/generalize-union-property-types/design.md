# Design

## Context

- See proposal.md "Why".
- `convert_single_property(prop_def)` (`lib/swagger_yard/canvas_adapter.rb`) has two paths:
  - With a `$ref`, it returns a bare `$ref`, or `oneOf [string, $ref]` when `type` lists `string` (added in `resolve-namespaced-model-returns`, D5 there). It ignores every other field.
  - Without a `$ref`, it goes through `convert_property_type` → `handle_single_type` / `handle_array_types` (the `["x", "null"]` form becomes `nullable`), then copies fields and handles enums and items. A pipe string such as `"integer|string"` reaches `handle_single_type`, which emits it as the literal type.
- `resolve_schema_name(name)` returns the collected schema name, or `nil` when there is none.
- The generated Python oneOf wrapper validates each variant and raises `Multiple matches found` when more than one fits (`models/lti_registration_created_by.py`). Canvas models are mostly optional fields, so any object fits any model.
- Inventory: in `app/controllers`, `lib` and `gems/plugins`, the pipe form appears only as the 5 `"string|User"` fields. The array form appears 3 times, always `[x, "null"]`.

## Goals / Non-Goals

**Goals:**
- One conversion rule for `|`-separated types, with or without `$ref`.
- Identical output for every property in today's docs.

**Non-Goals:**
- Discriminators for unions of models (Canvas docs have no field to discriminate on).
- Unions inside array `items` (`"items": {"type": "a|b"}`). Nothing uses them, so they get a follow-up if needed.
- The JSON array form with two non-null types (`["integer", "string"]`). It keeps its current first-type behavior, and the warning names it.

## Decisions

### D1: Convert each part, then collapse
Split `type` on `|`, strip whitespace, and drop empty parts. Then:
- `null` sets `nullable: true` (on the single schema, or on the `oneOf`).
- A primitive (`string integer number boolean object array datetime date-time date uuid`) becomes a schema via `handle_single_type`.
- Any other part resolves with `resolve_schema_name` to a `$ref`. When the part names the property's `$ref` model, it uses that `$ref`. A `$ref` with no matching part is still added as a variant.
- A part that resolves to nothing is dropped with a warning.

Remove duplicate variants. One variant → that schema. More than one → `{"oneOf" => variants}`. With no `|` and no `$ref`, the existing scalar path runs unchanged (extracted as `convert_scalar_property`).
- *Alternative: extend the `string` check with more primitives.* Still special-cased, and it doesn't cover models or null.

### D2: Merge primitives that share a JSON type
Before building the `oneOf`, keep a single variant per JSON type. When the variants differ only in `format` (`string` and `string`/`date-time`), keep the plain one. The wrapper would otherwise match the same JSON value twice.

### D3: Fall back on unions of several models
When two or more variants are `$ref`s, keep only the first one, together with any primitive variants, and print a warning naming the model and property. That follows the existing `puts "   Warning: …"` convention in `register_wrapper_schema`. A `oneOf` of two models would raise "Multiple matches" for every object Canvas sends.
- *Alternative: emit `anyOf`.* The Python generator's `anyOf` takes the first match, but it is less tested in this client. Revisit if a real two-model field appears.

### D4: Keep descriptions on non-`$ref` results
The `oneOf` and single primitive results keep `description` and `example` (via `copy_basic_property_fields`). A bare `$ref` stays bare, as today, because OpenAPI 3.0 ignores `$ref` siblings.

## Risks / Trade-offs

- [The refactor changes an existing property's output] → Task 1.4 requires an empty spec diff.
- [A future model union silently loses its second model] → The D3 warning prints in every `rake doc:openapi` run.
- [Primitive merging hides a documented format] → It only applies inside unions, and none exist today.

## Migration Plan

1. In the fork: specs for each D1–D3 case, then the refactor, then regenerate and require an empty spec diff. Commit.
2. In the client: regenerate and confirm no diff. If the client is unchanged, there is nothing to commit.

Rollback: revert the fork commit.
