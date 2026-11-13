# Tasks

## 1. Seed and capture (canvas-lms fork, uncommitted)

- [x] 1.1 Re-read `spec/manual_seeding/large_gradebook_seeds.rb` and add `--module-progress`, `--course-pacing` and `--conversation-batch` (D6) as additive edits. Run each twice in the web container. Verify that the first run prints its ids and the second creates nothing new. Record in these notes which path `--conversation-batch` used. Do not commit the script.
  - Done. Rerunning each option printed the same ids, so a second run creates nothing new: module 1 (item 1, course 5, 51 progressions), course pace 1 (course 5, pacing on), conversation batch 1 (`created`, user 392).
  - `--conversation-batch` used the live path, not the fallback. The batch belongs to Seeded Admin 2 (user 392), not user 1, so the captures hold no personal data. Its `queue_delivery` is stubbed, so the batch stays `created`.
- [x] 1.2 Capture these with the admin token:
  - `GET /users/1/logins`
  - `GET /conversations/batches`
  - `GET /courses/5/bulk_user_progress`
  - `GET /courses/5/assignments/gradeable_students?assignment_ids[]=…` (two ids)
  - `GET /courses/5/pace_contexts?type=course`
  - `GET /courses/5/pace_contexts?type=student_enrollment`

  Record each field's JSON type next to D1–D5 in these notes, and update D1–D5 if one disagrees.

  - Done. Logins were captured for user 8 and Seeded Admin 2 instead of user 1 (personal data). Course 5 assignments 52 and 53 were used for gradeable students. The batch was captured with Seeded Admin 2's token.
  - All types match D1–D5. Login ids are integers and `created_at` is ISO. `completion` is a float, `recipient_count` an integer and `message` an object. `assignment_ids` are integers. Pace context `associated_*_count` is an integer for `Course` and null for `StudentEnrollment`. `on_pace` is null for `Course` and a boolean for students. `applied_pace.duration` is an integer.

## 2. Doc corrections (canvas-lms fork)

- [x] 2.1 Apply D1–D5 to the five controllers. Verify that `git diff` shows comment lines only, and that every new model's JSON parses.
  - Done. The diff has comment lines only.
- [x] 2.2 Regenerate (`bundle exec rake doc:openapi`, not committed) and diff. Verify:
  - the six new schemas and `PaceContextsApiIndexResponse` exist
  - the six operations reference them (arrays for the five list operations)
  - no other operation changed
  - Done. Regenerated with `.worktrees/gen_wt.rb`.
- [x] 2.3 Commit only the five controllers in upstream format: subject, why, `flag=none`, `Test Plan:`, every line under 60 characters. Verify that `git log -1 --stat` lists only them, and that the seed script and `public/doc/` stay uncommitted. Do not open a PR.
  - Done: `bc931054ced fix(canvas-lms): document six undocumented lists` on `wt/simple` (five controllers only).

## 3. Client (canvas-lms-python-client)

- [x] 3.1 Copy `src/.openapi-generator/FILES`, regenerate, and delete orphans by manifest diff (keep existing `test_*.py` entries the manifest drops). Verify:
  - `pseudonyms_index_all` yields `Login`
  - `courses_bulk_user_progress_all` yields `UserProgress`
  - `pace_contexts_api_index_paginated` yields `PaceContextsApiIndexResponse`
  - Done. The manifest only gains the 7 models, their docs and their test stubs. Nothing is orphaned.
- [x] 3.2 Add the 1.2 fixtures and `test/custom/unit/test_simple_list_models.py` (D7), and drop the six operations from `UNDOCUMENTED_PAGINATED_OPERATIONS`. Verify that the tests pass, and that they fail against the pre-change generated files: check out the old files, confirm the failure, then restore them.
  - Done. Against an export of the pre-change files, `test_simple_list_models.py` fails to import, and 4 tests in `test_paginated_response_types.py` fail (allowlist, simple list types, and the `PaceContextsApiIndexResponse` wrapper cases).
- [x] 3.3 Add the integration tests (D7) and run `pdm run pytest --integration -v -k "logins or batches or progress or gradeable or pace"` with the admin token. Verify that they pass, or skip with their seed hint where 1.1 recorded no live data.
  - Done. Run with the admin token: 5 tests pass. The batch test skips with its seed hint, because Canvas lists only the caller's batches and user 1 has none. The batch test also passes with Seeded Admin 2's token.
  - Deviation: the account login listing returns only the caller's logins in that account (`params[:user_id]` defaults to the caller, and the client has no `user_id` parameter). User 1's login is in account 2, so the test lists logins in every account visible to the admin.
  - Hardcoded ids: course 5 and account 1 match the live instance. The tests look up courses and accounts instead of hardcoding them.
- [x] 3.4 Verify that `pdm run pytest` passes offline, that the full `--integration` run shows no new failures, and that `pdm run ruff check src/canvas_lms_python_client/test/custom` is clean. Then commit the client.
  - Done. Offline: 3778 passed, 174 skipped. `--integration`: 31 passed, 7 skipped (all existing seed or token skips, plus the batch skip above). Ruff is clean.

## 4. Final checks

- [x] 4.1 Run `openspec validate type-simple-undocumented-lists --strict` and verify that it passes.
  - Done. Landed on 2026-11-03 after rebasing onto the audit change: fork `2f6d327e254` and client `979548e`.
    - Rebase conflicts were in the two hand-written client tests only. In `test_paginated_models.py`, both sides are kept. In the `UNDOCUMENTED_PAGINATED_OPERATIONS` allowlist, both sides' removals are kept.
    - Regenerating from the rebased spec matched the commit exactly, except for the usual drop of test entries from `FILES`, which was discarded. The spec diff from the post-audit baseline is the 7 new schemas and the 6 operations only.
    - After landing, `rake doc:openapi` in the main checkout produced the same spec, and regenerating from it left no diff beyond the `FILES` drop.
    - Final counts: offline 3828 passed and 177 skipped. `--integration` 34 passed and 7 skipped. Rubocop's 18 offenses on the five controllers were already there before this change. The fork diff touches comments only.

## Workflow follow-up

- Upstream: the user may cherry-pick the task 2.3 commit after signing the CLA.
- Fix `UserDisplay` (`display_name`, `anonymous_id`, `pronouns`), then consider consolidating the user display fields.
- Document a `ConversationMessage` model for `ConversationBatch.message`.
- Archive with `/opsx:archive` after review.
