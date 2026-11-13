# Design

## Context

- Motivation: see proposal.md, "Why". Requirements: `specs/paginated-list-responses/spec.md`.
- **Today's detector** (`canvas_adapter.rb`, `method_uses_pagination?`):
  - matches `/Api\.paginate|Api::paginate|\.paginate\(/` on the method source
  - otherwise scans for `\b([a-z_][a-z0-9_]*)\s*[({]`, and recurses into methods of the same name in `yard_object.parent.children`
  - falls back to an `index`/`list` name check only when it raises
- **Why a looser regex won't do.** A census followed every bare word through controllers and `lib/api/v1`, and flagged 51 actions, nearly all false: `courses_show` because the code mentions `users`, `group_categories_export` because it mentions `groups`.
- **A stricter simulation** followed only receiverless calls, not local variables, and went from controllers into `lib/api/v1` but never back. It found the 14 operations in the proposal, plus two false hits:
  - `groups_bulk_user_tags`: `users.id` inside a SQL string, which a syntax tree excludes
  - `lti/ims/results_controller#index`: a name collision in the census's mapping to `results_index`, not a real operation

  It lost no operation that's paginated today.
- **YARD registry:** `YARD::Registry` holds only the controller being parsed, so `lib/api/v1` helpers aren't available through it.

## Goals / Non-Goals

**Goals:**
- Detect the 14 operations with no new false positives or losses, proven by a spec diff.

**Non-Goals:**
- Typing the 8 operations that join the allowlist (follow-up).
- Following `ApplicationController`, parent controllers, or modules outside `lib/api/v1`. No census hit needed them.
- Runtime detection against a live instance.

## Decisions

### D1: Follow calls using Ripper
Parse each method's source with `Ripper.sexp`, and collect receiverless calls: `:vcall`, `:fcall` and `:command` nodes. Ripper already tells local variables (`:var_ref`) and receiver calls (`:call`) apart from these, and string contents aren't identifiers, so all three false-positive sources disappear without extra rules.

If a method doesn't parse, it contributes no calls, and the existing `rescue` fallback stays as it is.
- *Alternative: a stricter regex.* Rejected: strings need a real tokenizer, and each exception would add another rule.
- *Alternative: an allowlist of helper names.* Rejected: it would miss the next helper Canvas adds without any signal.

### D2: Follow `lib/api/v1` helpers
Build a cached index, once per generation, of `lib/api/v1/**/*.rb`: method name → source. Methods are found by Ripper `:def` nodes and read by line range. A name defined in more than one module isn't followed, because it can't be resolved statically.

Resolution order for a call: the controller's own methods, then the index. Once in a `lib/api/v1` helper, the walk stays in the index and never returns to controller methods. That prevents paths like `assignment_json` → `index`. The `visited` set stays.

### D3: Recognise `Api.jsonapi_paginate`
Add it to the pattern. `Api.jsonapi_paginate` sets the same `Link` header as `Api.paginate` (`lib/api.rb`), so `AsyncPaginatedIterator` works unchanged.

### D4: Proof by spec diff
Regenerate before and after. The `x-paginated` operation set must gain exactly the 14 operations and lose none, and the only `paths` differences must be those operations' parameters and `x-paginated`. Any other difference is a false positive, and is fixed in the detector before committing.

### D5: Tests
- **Adapter spec** examples:
  - a bare same-class helper, a parenthesised helper, and a `lib/api/v1` helper through a call chain
  - `Api.jsonapi_paginate`, and `api_context.paginate(x)`
  - no detection for: a SQL string mentioning a paginating action, a local variable named like one, `@context.users`, and a helper name defined in two modules
- **Offline client test:** `test_paginated_response_types.py` gets:
  - `HELPER_PAGINATED_OPERATIONS`, the 14 operations, asserting each has `_paginated`
  - a list of single-record reads (`courses_show`, `sections_show`, `submissions_api_show`, `groups_show_for_other`), asserting none has it
  - the 8 undocumented operations added to `UNDOCUMENTED_PAGINATED_OPERATIONS`
- **Live:** `test_paginated_models.py` lists gradebook history days with `_all` and grading periods with `_paginated`, both at `per_page=1`. Each asserts more than one page, reusing `assert_pages_match` where it fits, and skips if the seeded data fits on one page. Canvas pages gradebook history by graded submission, so one date repeats across pages: that test compares the set of dates with an unpaged listing instead of checking ids.

## Risks / Trade-offs

- [`_paginated` on the 8 undocumented operations yields nothing] → That's the known behaviour of every undocumented operation, and the allowlist tracks them. Base methods are unchanged. Typing them is the follow-up.
- [A new helper outside `lib/api/v1` stays undetected] → It's no worse than today, and D5's pinned list makes regressions visible for known cases.
- [Rollups have two render paths; `aggregate=course` doesn't paginate] → Page parameters are harmless there, because a response with no `Link` header ends iteration after one page.
- [Generation gets slower] → The index is built once, from a small directory.

## Migration Plan

1. Fork, on `chore/fix-openapi-spec`: adapter and specs, regenerate (uncommitted), diff, then commit.
2. Client, on `fix/add-returns-for-paginated-models`: regenerate, add tests, run the suites, then commit.

Rollback: revert the commits.
