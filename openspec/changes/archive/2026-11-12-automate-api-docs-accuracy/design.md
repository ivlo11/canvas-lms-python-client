# Design

## Context

- Motivation: see proposal.md, "Why". Requirements: `specs/api-docs-audit/spec.md`, `specs/api-docs-sweep/spec.md`, `specs/api-docs-enforcement/spec.md`.
- **Prototype results** (scratchpad scripts, not committed), for 821 documented `@API` actions:
  - **Tracer:** found a list or object shape for 595 actions, and about 470 traces are complete. On the 44 actions scored against both, 89% of the fields it called unconditional came back live (docs: 65%), and it named 90% of the live fields (docs: 86%). It got list versus object right on all 145 actions scored.
  - **Spec traffic:** API specs name 467 actions. Of the 66 named by the sampled API spec files, 65 returned a real 2xx. Adding the GET probes gives 518, and adding controller specs gives about 618. That last count is rough and likely too low.
  - **Gaps:** 49 actions have no evidence of any kind, and API specs name only 248 of the 447 non-GET actions.
  - **Cost:** a full spec run is projected at 3.2 hours on one process.
- **False alarms seen:**
  - `lti_registrations` keys that look like they come from another model, possibly from resolving the wrong helper
  - `category` on folders and `created_at` on profile, which the tracer called unconditional but which didn't come back
  - IDs returned as strings by specs that request `application/json+canvas-string-ids`
- **Existing hooks:** `script/render_json_lint` is a static controller lint to model on. `script/rlint` runs `gems/rubocop-canvas`. `raw_api_call` in `spec/apis/api_spec_helper.rb` is the common path for API specs. `build/new-jenkins/linters/run-gergich-linters.sh` runs the linters, but only in Instructure's CI.
- **Isolation:** specs use `canvas_test` and redis DB 1, while the seeded instance uses `canvas_development`.

## Goals / Non-Goals

**Goals:**
- Audit every `@API` action, and end with each one fixed or listed with a reason.
- Make every fix in the controller documentation.
- Catch new documentation errors during development.

**Non-Goals:**
- Replacing documentation with generated output. Docs still decide what's public, model names and descriptions.
- Writing descriptions automatically.
- Scripted POST, PUT or DELETE calls against the seeded instance.
- Instructure's CI, or submitting upstream.
- Documenting APIs that have no `@API` tag.

## Decisions

### D1: Evidence order

Run the whole spec suite first, then seed only for the GET gaps it leaves, then probe GETs as each role. Seeding first would mean building data for about 500 actions that already have real responses.

Writes come only from specs. They already build valid payloads and run in `canvas_test`. Alternative rejected: scripting writes against a disposable database copy. Reconsider it only if too many writes remain on the review list after the specs have run.

### D2: Recorder

`spec/support/api_response_recorder.rb` prepends onto `ApplicationController#process_action`, and only runs when `API_RESPONSE_RECORD` is set. It covers API and controller specs without changing them. Each record holds controller, action, method, status, role, container kind, key paths and JSON type names. It holds no values, headers or tokens. Requests that ask for string IDs are marked and left out of type comparison.

### D3: Findings and evidence status

`script/api_docs_audit` merges all the evidence into one findings file under `tmp/`, which isn't committed. Each action gets one status: `verified` (real 2xx response), `static` (trace only) or `none`. The report can be filtered by role.

The role is what the responses show. The tool doesn't work out permissions from code, because object policies can't be resolved statically.

### D4: What the codemod may do

| Finding | Evidence needed | Action |
|---|---|---|
| Integer should be number | One observed float | Apply |
| Field can be null | One observed null | Apply |
| Other type conflict | Response and trace agree | Review |
| List is a wrapper, or has a root key | Response and trace agree | Apply, as inline `@returns` |
| Missing `@returns`, existing model fits | Response and trace agree | Apply |
| Missing `@returns`, no model fits | Any | Review, because a new model needs a name |
| New field | Response and trace agree | Review, because it could be internal or sensitive |
| Documented field never seen | Any | Report only |
| API with no `@API` tag | Any | Never add |

Types only ever widen. Specs only prove the types their fixtures produce, so a field seen only as whole numbers isn't narrowed to an integer.

A field accepted in review is added without a description, and the review list records that it still needs one. A field rejected in review goes in the exceptions file.

Review decision: every new field seen in a response is accepted, including fields that look sensitive, because the docs and the client describe what the API returns. A new field found only by the trace, and never seen in a response, isn't added and goes in the exceptions file as `unverifiable`.

Other review decisions: an action with no `@returns` and a nearest model gets that model, which is extended with the missing fields. An action with no fitting model gets a new model when a response shows its body, and is otherwise listed as an exception. A type conflict takes the types the responses show. A container conflict is checked against the code, and the response wins unless the code shows that response was a special case.

### D5: Codemod mechanics

The codemod edits only the keys it changes, and keeps comment layout, key order and existing descriptions. Where a model has several definitions, such as `RubricRating`, it updates all of them. A model shared by several actions takes the widest type seen. Malformed `@model` JSON is reported and not rewritten.

Alternative rejected: an OpenAPI overlay, because corrections belong in the controller docs and not in another layer.

A field documented with several types, such as `["string", "integer"]`, is generated as `anyOf`, nullable when the list includes null, so the client accepts every type the API returns. The client then wraps the field in a model, and callers read `.actual_instance`. Alternatives rejected: keeping the first type, which rejects real responses; leaving the field untyped; and a forked model template that renders inline unions, which would have to be maintained.

### D6: Exceptions file

`lib/api_docs_audit/exceptions.yml` is committed, and every entry has a reason: `internal`, `unverifiable`, `notation` or `needs_description`. Checks fail on findings that aren't listed. Entries that no longer match anything are reported so the file can shrink.

### D7: Enforcement layers

| Check | Runs | Needs a database | Catches |
|---|---|---|---|
| Cop in `gems/rubocop-canvas` | `script/rlint`, on the changed file | No | `@API` with no `@returns`, malformed `@model` JSON |
| `script/api_docs_lint` | Local hook and fork CI | No | Docs that no longer match the traced code |
| Response check on `raw_api_call` | When `API_DOCS_CHECK` is set | Yes | Wrong types and undocumented fields |

A change to a helper in `lib/api/v1` or to a serializer can affect many APIs, so the lint re-checks every action that reaches it.

All three read the docs directly, because generating the spec needs a database and is too slow for these checks.

The full audit runs manually to start, given its projected 3.2 hours. No scheduled job is added; that can be reconsidered once the manual runs show how often it's needed.

### D8: Branches

Five new branches, listed in proposal.md. The `canvas-lms` branches stack, because each stage needs the one before it. Only the first branch in each repo starts directly from `chore/fix-openapi-spec` or `fix/add-returns-for-paginated-models`. Nothing merges back unless asked, and no PRs are opened.

The seed script and regenerated spec stay uncommitted in the primary checkout. Switching branches must carry those changes across and never stash or commit them.

### D9: Open changes

- `fix-undetected-pagination` is applied on `fix/api-docs-sweep` and not on the branches its tasks name. Its allowlist additions are replaced by whatever the sweep types.
- `return-existing-models-from-reads` and `type-course-catalog-search` aren't applied, and their seed designs are reused for the gaps. After the sweep, `return-existing-models-from-reads` was removed, because every read it targets now has a `@returns`. `type-course-catalog-search` is kept: the sweep added the `course` wrapper, but the course inside is still an untyped object.

### D10: Benchmark

The audit must find these known bugs from the docs at `upstream/master`, without manual help:
- audit `{links, events, linked}` wrappers
- the `late_policy` root
- `Conversation.messages` and its 3 related fields
- `UserDisplay.display_name`
- `Grade` scores typed as strings
- `student`/`grader` strings on grade change events
- `version_number` type
- `Enrollment.unposted_*` types
- the 14 missed pagination operations
- the 3 crashes in proposal.md

The prototype missed some of these statically, so they depend on recorded responses. Any miss is investigated and reported before the sweep begins.

## Risks / Trade-offs

- **Sensitive fields become public docs** → New fields never apply automatically, and rejected ones go in the exceptions file.
- **Wrong trace produces a wrong edit** → Automatic edits need a real response, and removals are never automatic.
- **Fixtures differ from production** → Types only widen, and an unseen field is never deleted.
- **Controller comment conflicts on upstream sync** → Accepted. Rerunning the codemod after a sync should reduce the work.
- **Coverage is an estimate** → The first task measures it, and a large shortfall stops the work for a decision.
- **Spec suite failures in this environment** → 3 of 1,197 sampled examples failed. Failures are recorded and don't count as evidence.
- **Noisy checks get ignored** → They fail only on findings missing from the exceptions file, and the lint starts from the post-sweep state.
