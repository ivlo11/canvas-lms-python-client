# Proposal

## Why

The generator only adds `page`/`per_page` and `x-paginated` to an operation when `method_uses_pagination?` finds pagination in the action's source. It misses real pagination in three ways, so the client has no page iterator and callers silently get only the first page:

| Gap in the detector | Operations that lose pages |
|---|---|
| It only follows helper calls written with `(` or `{`, so a bare `user_rollups_json` or `paginated_assignments` isn't followed | `outcome_results_rollups`, `sis_api_sis_assignments` and `_for_courses` |
| It only looks in the same controller class, not in `lib/api/v1` modules | `courses_activity_stream`, `groups_activity_stream`, `users_activity_stream` and `_for_other` (`api_render_stream`); `gradebook_history_api_days`, `_day_details` and `_submissions` (`submissions_set`) |
| Its pattern doesn't match `Api.jsonapi_paginate` | `grading_periods_index` and `_for_courses`, `assessments_index`, `results_index` |

That's 14 operations. Live, `gradebook_history/days`, `outcome_rollups` and `grading_periods` with `per_page=1` all return a `Link: rel="next"` header, so more pages exist that the client can't reach.

## What Changes

- **Generator (canvas-lms fork, fork-only commit):** `method_uses_pagination?` closes all three gaps:
  - it follows calls using a parsed syntax tree, so bare calls count, while words in strings, local variables and method calls on other objects don't
  - it also follows helpers defined in `lib/api/v1`
  - it recognises `Api.jsonapi_paginate`
- **Client:**
  - Regenerate. The 14 operations gain `page`/`per_page` and `_paginated`, and the list responses (`gradebook_history_api_*`) gain `_all`.
  - An offline test pins the 14 operations as paginated, and pins representative single-record reads as not paginated.
  - Integration tests walk more than one page of gradebook history and grading periods.
- **Undocumented list grows by 8:** `courses_activity_stream`, `groups_activity_stream`, `users_activity_stream`, `users_activity_stream_for_other`, `outcome_results_rollups`, `sis_api_sis_assignments`, `sis_api_sis_assignments_for_courses` and `assessments_index` have no `@returns`, so they join `UNDOCUMENTED_PAGINATED_OPERATIONS`. Until they're typed, their `_paginated` methods yield nothing, and their base methods still return `None`. Typing them is a follow-up.
- **No controller docs change, and no new seed options.**
- **BREAKING (client):** new optional parameters and methods only. The client is unreleased, so this isn't documented.

## Capabilities

### New Capabilities
<!-- None. -->

### Modified Capabilities
- `paginated-list-responses`: an operation that paginates through a helper is exposed as paginated, and an operation that doesn't paginate isn't.

## Impact

- **canvas-lms (fork, `chore/fix-openapi-spec`):**
  - `lib/swagger_yard/canvas_adapter.rb` and `spec/lib/swagger_yard/canvas_adapter_spec.rb`.
  - Not committed: the regenerated `public/doc/openapi/canvas.openapi.yaml`.
- **canvas-lms-python-client (`fix/add-returns-for-paginated-models`):**
  - Regenerated API modules for the 14 operations, with docs and generated test stubs.
  - `test/custom/unit/test_paginated_response_types.py` and `test/custom/integration/test_paginated_models.py`.
- **Order:** independent of `type-course-catalog-search` and `return-existing-models-from-reads`, though all three edit the same test files.
