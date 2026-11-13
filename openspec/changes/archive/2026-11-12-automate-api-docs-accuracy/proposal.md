# Proposal

## Why

Spec errors have been found and fixed a few controllers at a time, and new ones keep turning up. Three client calls still crash on live data today, and none of the open changes cover them:

| Client call | Cause |
|---|---|
| `assignment_groups_index` | `group_weight` is documented as an integer, but Canvas returns `0.0` |
| `sis_imports_api_index` | Docs say a list, but Canvas returns `{"sis_imports": [...]}` |
| `conferences_for_user` | Docs say a list, but Canvas returns `{"conferences": [...]}` |

A trial on 31 of the 381 spec files compared 55 actions with the docs on `chore/fix-openapi-spec`. Of the fields it saw, 839 could be compared and 28 of those had a type conflict. Another 253 weren't documented at all. Nothing stops Canvas changes from adding more.

This change fixes the documentation for all APIs in one automated sweep, then keeps it correct with checks that run during Canvas development.

## What Changes

- **Audit tooling (canvas-lms fork):** gather evidence for every `@API` action:
  - responses recorded from the whole spec suite, which also covers writes
  - GET calls as each role against the seeded instance, with seed data added only for what the specs don't reach
  - a static trace of `render json:`, helpers and serializers
  - column types from `db/structure.sql`

  The result is one findings list, by action and field. It holds key names and types only, never values or tokens.
- **Documentation sweep (canvas-lms fork):** a codemod rewrites `@model` and `@returns` in the controllers across all APIs in one pass. There's no overlay or other correction layer. Fixes backed by evidence apply automatically, and new or sensitive-looking fields wait for one review of the whole list. Undocumented APIs are never added automatically.
- **Generator fix (canvas-lms fork):** `fix-undetected-pagination` is applied as part of the sweep, because missed pagination is a generator problem and not a documentation one.
- **Contract check (client):** a test calls every GET through the generated client as each role, and any response the client can't parse fails it.
- **Enforcement (canvas-lms fork):** three checks keep the docs correct:
  - a custom cop in `gems/rubocop-canvas`
  - `script/api_docs_lint`, which compares docs with code
  - a response check in `raw_api_call`, which compares docs with what the specs get back

  They fail on new findings only. Anything the sweep couldn't fix is listed in an exceptions file with a reason.
- **Separate branches:** the work is done on new branches, listed under Impact, and nothing merges back without being asked.
- **Open changes:** `return-existing-models-from-reads` and `type-course-catalog-search` are held. Their bugs become benchmark cases, and whether to remove them is decided after the sweep.
- **BREAKING (client):** regenerated types and return values change across many operations. The client is unreleased, so this isn't documented.

## Capabilities

### New Capabilities
- `api-docs-audit`: every documented action gets a findings record and an evidence status.
- `api-docs-sweep`: findings are fixed in the controller documentation in one pass, and every API ends up fixed or listed with a reason.
- `api-docs-enforcement`: new documentation errors are caught during Canvas development.

### Modified Capabilities
<!-- None. -->

## Impact

- **Branches (not created yet):**

  | Repo | New branch | Branches from | Holds |
  |---|---|---|---|
  | canvas-lms | `chore/api-docs-audit` | `chore/fix-openapi-spec` at `918a1649d21` | Recorder, tracer, comparison, findings |
  | canvas-lms | `fix/api-docs-sweep` | `chore/api-docs-audit` | Codemod, controller docs, generator fix |
  | canvas-lms | `chore/api-docs-enforcement` | `fix/api-docs-sweep` | Cop, lint, response check, exceptions |
  | canvas-lms-python-client | `chore/api-contract-check` | `fix/add-returns-for-paginated-models` at `61cdb56` | GET contract test and role probes |
  | canvas-lms-python-client | `fix/api-docs-sweep` | `chore/api-contract-check` | Regenerated client and updated tests |

- **canvas-lms:**
  - New: `lib/api_docs_audit/`, `script/api_docs_audit`, `script/api_docs_lint`, `spec/support/api_response_recorder.rb`, and a new cop.
  - Changed: controller documentation across `app/controllers`, `lib/swagger_yard/canvas_adapter.rb`, and `spec/apis/api_spec_helper.rb`.
  - Never committed: the seed script `spec/manual_seeding/large_gradebook_seeds.rb` and the regenerated `public/doc/openapi/canvas.openapi.yaml`.
- **canvas-lms-python-client:** regenerated models and API modules, the new contract test, and updates to existing custom tests.
- **Upstream merges:** a sweep touches many controller comments, so syncs may conflict where Instructure edits the same lines.
- **Out of scope:** adding checks to Instructure's Jenkins and Gerrit, or submitting this upstream. The scripts are written so that stays possible.
