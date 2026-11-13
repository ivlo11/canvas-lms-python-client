# Design

## Context

- See proposal.md "Why".
- `extract_param_info_from_tag` (`lib/swagger_yard/canvas_adapter.rb`) returns `name: clean_name` (with `[]` removed), `original_name`, and `is_array` (true only when the name ends in `[]`). `add_query_parameter` registers the query parameter as `param_info[:name]`, so the brackets are lost. `add_body_parameter` already uses `original_name`.
- Parameters documented with an `Array` type but no brackets (`@argument placements[Array]`, `@argument x [Array]`; 16 in controllers and lib) never have `[]`, but `build_param_schema` still gives them an array schema.
- The Python client uses `multi` collection format for array query parameters, so it repeats the wire name once per value. It derives the Python argument name from the spec name by stripping characters that aren't valid in an identifier.
- The spec has 218 array query parameters, none with brackets.

## Goals / Non-Goals

**Goals:**
- One rule: a query parameter whose built schema is an array gets the wire name `<base>[]`.

**Non-Goals:**
- Nested hash query parameters (`foo[bar]`), which keep their current names.
- Body (form/JSON) parameter naming.
- Canvas endpoints that read a comma-separated string instead of `[]` (none are known). If one turns up, it gets a doc fix, not a generator exception.

## Decisions

### D1: Decide from the built schema, not from the name
Apply the rule in `add_query_parameter`. When the schema is an array (the `"array<…>"` string form or a `{"type" => "array"}` hash), use `"#{base}[]"`, where `base` is the name without a trailing `[]`. Otherwise use the name as is.
- This covers both `name[]` and `name [Array]` with one check, and it can't double the brackets.
- *Alternative: use `original_name`.* That misses the 16 `Array`-typed parameters, `placements` among them.

### D2: Keep Python argument names stable
Rely on openapi-generator's name sanitizing (`include[]` → `include`). Task 1.4 verifies that no method signature changes, by comparing parameter names before and after.
- *Alternative: add `x-python-name` vendor extensions.* Only needed if sanitizing turns out to produce different names.

## Risks / Trade-offs

- [Operations that also document a scalar parameter with the same base name (`include` and `include[]`)] → `add_or_update_parameter` treats them as different names. Task 1.4 lists any operation that ends up with both, and they are resolved in the docs.
- [Filters that were silently ignored now apply, so results change] → Callers asked for those filters. Note it in the README.
- [Python names change for some parameter] → D2 verification, with a fallback of `x-python-name`.

## Migration Plan

1. In the fork: generator change and specs, then regenerate the spec and diff the parameter names. Commit the generator and its spec.
2. In the client: regenerate, re-run the launch-definition integration tests without skips, add tests, update the README, then commit.

Rollback: revert both commits.
