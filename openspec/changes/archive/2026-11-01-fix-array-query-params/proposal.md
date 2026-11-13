# Proposal

## Why

Canvas reads list query parameters only in Rails bracket form (`include[]=a&include[]=b`). The spec generator strips the `[]` from every query parameter name, and it never adds `[]` to parameters documented with an `Array` type (for example `@argument placements[Array]`). As a result, all 218 list query parameters in the spec are named without brackets. The client sends `placements=a&placements=b`, which Canvas either rejects (500) or reads as an empty list. Every list filter in the client is silently ignored or fails, including `include`, `enrollment_type` and `context_codes`. `resolve-namespaced-model-returns` found this through the LTI launch definition integration tests, which skip because Canvas returns no items.

## What Changes

- **canvas-lms generator (fork):** query parameters whose schema is an array use the bracket wire name (`name[]`). This covers both `@argument name[]` and `@argument name [Array]` / `name[Array]`. Scalar query parameters, path parameters and body parameters are unchanged. Body parameters already keep their original names.
- Regenerate the spec and the client. The client's Python argument names stay the same (`include`, `placements`). Only the wire name changes, so calls send `include[]=a&include[]=b`.
- Not a breaking change for callers: method signatures stay the same, and list filters that were silently ignored now take effect. That does change results, so it is listed in the README.

## Capabilities

### New Capabilities
- `list-query-parameters`: how the client sends list-valued query parameters so that Canvas applies them.

### Modified Capabilities
<!-- none: paginated-list-responses already expects launch definitions to yield items; this change makes that scenario pass -->

## Impact

- **canvas-lms (fork):** `lib/swagger_yard/canvas_adapter.rb` (query parameter naming), its specs in `spec/lib/swagger_yard/canvas_adapter_spec.rb`, and the regenerated `public/doc/openapi/canvas.openapi.yaml`.
- **canvas-lms-python-client:** regenerated `api/*.py` and `docs/*Api.md` for every operation with a list query parameter (wire names only). Re-enables `test_course_launch_definitions_yield_items` / `test_account_launch_definitions_yield_items`, and adds offline and integration coverage for list query parameters.
