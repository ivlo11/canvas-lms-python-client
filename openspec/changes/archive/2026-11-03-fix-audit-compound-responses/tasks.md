# Tasks

## 1. Seed and capture (canvas-lms fork, uncommitted)

- [x] 1.1 Re-read `spec/manual_seeding/large_gradebook_seeds.rb` and add the standalone `--audit-events` option (D4) as an additive edit. Run it twice in the web container. Verify that the first run reports at least one course event for course 5 and the second adds none. Do not commit the script.

  Done. The option also records a login event for the seeded second admin (user 392) when it has none (D4). Both runs print `course 5 events: 1, admin 392 login events: 1`.

- [x] 1.2 Capture one page from each of these with the admin token:
  - `GET /audit/course/courses/5`
  - `GET /audit/grade_change/courses/5`
  - `GET /audit/authentication/users/392` (the seeded second admin, not user 1, to keep personal data out of fixtures)

  Record each event field's JSON type next to its current and planned (D3) doc type in these notes. If a field disagrees with D3, update D3 first.

  Done. Course 5, user 392 and account 1 confirmed live. Live type (old doc type → D3 doc type):
  - Grade change: `version_number` int (string → integer), `points_possible_before`/`after` float (missing → number), `links.course`/`assignment` int (integer), `links.student` string (integer → string), `links.grader` string or null (integer → string)
  - Course: `links.course`/`user`/`page_view`/`sis_batch` string (integer → string; `page_view` was already string), `event_data` object (string → object, see below)
  - Authentication: `id` string (missing → string), `links.login`/`account`/`user` int (missing → `AuthenticationEventLinks` integer), `links.page_view` null (string)

  Every field matched D3 except `CourseEvent.event_data`, documented `string` but sent as an object. The offline tests in 4.2 caught it; D3 and the proposal now cover it.

## 2. Inline `object` entries (canvas-lms fork)

- [x] 2.1 Implement D1 in `lib/swagger_yard/canvas_adapter.rb`, with the examples in `spec/lib/swagger_yard/canvas_adapter_spec.rb`. Run the adapter spec in the web container and verify that it passes. Regenerate and verify that the spec is byte-identical to before (no controller uses `object` yet).

  Done. Adapter spec: 176 examples, 0 failures. The regenerated spec was byte-identical. Rubocop: the same 14 offenses as the main checkout, none on changed lines.

- [x] 2.2 Commit the adapter and spec in the fork's format (lines under 60 characters, the why, a test plan). Verify that `git log -1 --stat` lists only those two files.

  Done: `41538941616 feat(swagger_yard): allow object in inline @returns` on `wt/audit`.

## 3. Doc corrections (canvas-lms fork)

- [x] 3.1 Apply D2 and D3 to the three audit controllers. Verify that `git diff` shows comment lines only, and that every edited model's JSON parses.

  Done. Comment lines only; all 8 models in the three controllers parse as JSON.

- [x] 3.2 Regenerate (`bundle exec rake doc:openapi`, not committed) and diff. Verify:
  - the 10 wrapper schemas exist
  - each audit operation references its own wrapper
  - the event and link schemas have the D3 types
  - no other operation changed

  Done. 11 schemas added (10 wrappers and `AuthenticationEventLinks`). `AuthenticationEvent`, `CourseEvent`, `CourseEventLink`, `GradeChangeEvent` and `GradeChangeEventLinks` changed. Only the 10 audit operations changed, each to its own wrapper.

- [x] 3.3 Commit only the three controllers in upstream format: subject, why, `flag=none`, `Test Plan:`, every line under 60 characters. Verify that `git log -1 --stat` lists only them, and that the seed script and `public/doc/` stay uncommitted. Do not open a PR.

  Done: `dc623e7cca4 fix(canvas-lms): document audit compound responses` on `wt/audit` (amended to add `event_data`).

## 4. Client (canvas-lms-python-client)

- [x] 4.1 Copy `src/.openapi-generator/FILES`, regenerate, and delete orphans by manifest diff (keep existing `test_*.py` entries the manifest drops). Verify:
  - `grade_change_audit_api_for_course_paginated` yields `GradeChangeAuditApiForCourseResponse`
  - no audit operation has an `_all` iterator
  - `AuthenticationEvent.links` is `AuthenticationEventLinks`

  Done. No orphans. Also regenerated the stale test stubs of the five changed models and of the three audit API test files, whose paginated tests still mocked list pages.

- [x] 4.2 Add the 1.2 fixtures and `test/custom/unit/test_audit_responses.py` (D5), and drop the three authentication operations from `UNDOCUMENTED_PAGINATED_OPERATIONS`. Verify that the tests pass, and that they fail against the pre-change generated files: check out the old files, confirm the failure, then restore them.

  Done. `test_audit_responses.py` has 39 tests. Against a HEAD export of the pre-change files it fails at import (`AuthenticationEventLinks`), and the allowlist test fails.

- [x] 4.3 Add the audit integration tests (D5) and run `pdm run pytest --integration -v -k audit` with the admin token. Verify that all three APIs pass, and that the course audit test skips with the `--audit-events` hint when the log is empty.

  Done. The three audit integration tests pass. They list at account level (course and authentication) or across root account courses (grade change). The empty-log skip was checked by reading the code, since the seeded log isn't empty.

- [x] 4.4 Verify that `pdm run pytest` passes offline, that the full `--integration` run shows no new failures, and that `pdm run ruff check src/canvas_lms_python_client/test/custom` is clean. Then commit the client.

  Done. Offline: 3806 passed, 171 skipped. Full `--integration` run: 345 passed, 6 skipped (main checkout: 303 passed, 6 skipped). Ruff clean. Committed `0683c17 fix(canvas_lms_python_client): type audit log compound responses` on `wt/audit`.

## 5. Final checks

- [x] 5.1 Run `openspec validate fix-audit-compound-responses --strict` and verify that it passes.

  Done. Landed by fast-forward (no rebase needed): fork `chore/fix-openapi-spec` at `dc623e7cca4`, client `fix/add-returns-for-paginated-models` at `0683c17`. After landing, `rake doc:openapi` in the main fork checkout matched the worktree spec byte for byte. Regenerating the client from it changed only the usual `FILES` test-entry drop, which was discarded. Offline `pytest` in the main checkout: 3806 passed, 171 skipped.

## Workflow follow-up

- Upstream: the user may cherry-pick the task 3.3 commit after signing the CLA. The task 2.2 commit stays in the fork.
- Type `linked` per API once `Login` exists (`type-simple-undocumented-lists`).
- Archive with `/opsx:archive` after review.
