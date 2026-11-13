# Tasks

Never commit `spec/manual_seeding/large_gradebook_seeds.rb` or `public/doc/openapi/canvas.openapi.yaml`, and never stash them when switching branches. Tokens appear only in reports to the user. Commit only to the branch named in each section. Don't merge back or open a PR unless asked.

## 1. Audit tooling (canvas-lms, `chore/api-docs-audit` from `chore/fix-openapi-spec` at `918a1649d21`)

- [x] 1.1 Create the branch, and verify that `git status` still shows the seed script and spec as uncommitted changes.
- [x] 1.2 Add `spec/support/api_response_recorder.rb` (D2), with specs covering the role, the string-ID mark, and that no values are recorded. Verify that specs behave the same with `API_RESPONSE_RECORD` unset.
- [x] 1.3 Add `lib/api_docs_audit/` with the docs parser and the tracer, based on the prototype. Fix the false alarms named in the design, or list each as a known limit. Add specs.
- [x] 1.4 Add `script/api_docs_audit` to merge the evidence into `tmp/` (D3). Verify that all `@API` actions get a record, and report the count.
- [x] 1.5 Run the whole spec suite with recording on (`spec/apis`, `spec/requests`, `spec/controllers`), on `canvas_test` only. Verify that `canvas_development` row counts for users and courses are unchanged. Record the time taken, the failures, and the actions with a 2xx response.
- [x] 1.6 Report measured coverage to the user. If real response coverage is under 60% of actions, stop for a decision.
- [x] 1.7 Commit in the fork's format (lines under 60 characters, the why, a test plan). Verify with `git log -1 --stat` that the commit holds only tooling files.

## 2. Contract check and probes (client, `chore/api-contract-check` from `fix/add-returns-for-paginated-models` at `61cdb56`)

- [x] 2.1 Create the branch.
- [x] 2.2 List the GET gaps from 1.5 and extend the seed script (uncommitted) to cover them, reusing the seed designs in `return-existing-models-from-reads` and `type-course-catalog-search`. Include rubrics and files. Report any action that can't be seeded, with the reason.
- [x] 2.3 Add a contract test that calls every GET through the generated client as admin, teacher, observer and student, with the teacher token read from `CANVAS_TEACHER_API_TOKEN`. It records parse failures, and which operations were reached or skipped and why. It skips session, token, download and launch routes, and never prints tokens or values.
- [x] 2.4 Add a role probe that writes key names and types for the audit. Verify that the output has no values by checking its record keys.
- [x] 2.5 Run it before any fixes. Verify that it reports the 3 crashes in proposal.md, and record the failure count as the starting point.
- [x] 2.6 Commit on `chore/api-contract-check`.

## 3. Benchmark (canvas-lms, `chore/api-docs-audit`)

- [x] 3.1 Rerun the audit with all the evidence, including the role probes, against the docs at `upstream/master`. Verify each D10 bug is found. Report any miss by name to the user before continuing.
- [x] 3.2 Rerun against `chore/fix-openapi-spec`, and report findings by type and by evidence status. Commit any tooling fixes.

## 4. Sweep (canvas-lms, `fix/api-docs-sweep` from `chore/api-docs-audit`)

- [x] 4.1 Create the branch, and apply `fix-undetected-pagination`'s generator change and specs here (D9). Verify that the `x-paginated` set gains exactly its 14 operations and loses none.
- [x] 4.2 Add the codemod (D4, D5), with specs covering each row of D4, several definitions of one model, and layout being preserved. Verify that a dry run on a copy of a controller changes only the keys it should.
- [x] 4.3 Run the codemod's automatic fixes across all controllers. Regenerate the spec (not committed), and verify that its diff contains only the expected kinds of change. Investigate any other change before continuing.
- [x] 4.4 Give the user the review list: new fields, new models, other type conflicts, and documented fields never seen. **Stop until the user has decided.** Flag fields that look sensitive. Put no values in the list.
- [x] 4.5 Apply the review decisions, and write `lib/api_docs_audit/exceptions.yml` (D6). Verify that every entry has a reason.
- [x] 4.6 Run `bin/rails doc:api` and the `spec/apis/swagger` specs, and verify that they still pass.
- [x] 4.7 Commit on `fix/api-docs-sweep`, with the codemod and the controller doc changes as separate commits. Verify that neither includes the seed script or spec.

## 5. Regenerate and verify (client, `fix/api-docs-sweep` from `chore/api-contract-check`)

- [x] 5.1 Create the branch. Copy `src/.openapi-generator/FILES`, regenerate from the swept spec, and delete orphans by manifest diff (keep existing `test_*.py` entries the manifest drops).
- [x] 5.2 Update custom tests pinned to the old types and shrink `UNDOCUMENTED_PAGINATED_OPERATIONS` to what's still undocumented. Verify that `pdm run pytest` passes offline and `pdm run ruff check src/canvas_lms_python_client/test/custom` is clean.
- [x] 5.3 Run the contract test. Verify that there are no validation errors for any role, and that skipped operations each have a reason. Fix failures in the controller docs, on `fix/api-docs-sweep` in canvas-lms, and not in the client.
- [x] 5.4 Run the full `--integration` suite, and verify that there are no new failures.
- [x] 5.5 Rerun the audit. Verify that no finding remains unresolved and missing from the exceptions file. Report the final counts by status to the user.
- [x] 5.6 Commit the client on `fix/api-docs-sweep`.

## 6. Enforcement (canvas-lms, `chore/api-docs-enforcement` from `fix/api-docs-sweep`)

- [x] 6.1 Create the branch, and add the cop to `gems/rubocop-canvas` with specs. Verify that it reports nothing new on the swept controllers, apart from entries in the exceptions file.
- [x] 6.2 Add `script/api_docs_lint`, modeled on `script/render_json_lint`, with re-checking for helpers and serializers (D7) and specs. Verify that it fails on a wrapper added to a scratch copy of a controller, and passes on the swept tree.
- [x] 6.3 Add the response check to `raw_api_call` behind `API_DOCS_CHECK`, using the recorder's comparison. Verify that it fails on a deliberately undocumented field, and that specs are unchanged with it off. Run a sample of API specs with it on, and verify that any failures are real findings.
- [x] 6.4 Agree with the user where the full audit runs. Then add the fork's GitHub Actions workflow for the lint, and a documented local hook. Add the scheduled audit job if hosted CI can run it.
- [x] 6.5 Commit on `chore/api-docs-enforcement`.

## 7. Final checks

- [x] 7.1 Run `openspec validate automate-api-docs-accuracy --strict` and verify that it passes.
- [x] 7.2 Verify that no commit on the five branches contains the seed script, the regenerated spec, tokens or response values.

## Workflow follow-up

- Ask the user whether `return-existing-models-from-reads` and `type-course-catalog-search` can be removed, based on the audit results. Answered: `return-existing-models-from-reads` removed, `type-course-catalog-search` kept.
- Ask the user whether to merge the branches back, and when.
- Archive with `/opsx:archive` after review.
