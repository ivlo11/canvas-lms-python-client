# Tasks

## 1. Seed and capture (canvas-lms fork, uncommitted)

- [x] 1.1 Verify that `CANVAS_STUDENT_API_TOKEN` authenticates (`GET /users/self`). If it doesn't, rerun the seed `--tokens` option and record the fix in these notes. Never write the token itself into these notes.
  - Done: the student token (user 8) returns 200 on `GET /users/self`; no reseed needed. `CANVAS_STUDENT_API_TOKEN` is set in the env and authenticates as user 8.
- [x] 1.2 Re-read `spec/manual_seeding/large_gradebook_seeds.rb` and add `--discussion-entries` (D3) as an additive edit. Run it twice in the web container. Verify that the first run prints the topic and entry ids and the second creates nothing new. Do not commit the script.
  - Done: `--discussion-entries` seeded topic 3 in course 5 with entries 1 (root, attachment 2), 2 (reply to 1) and 3 (deleted root). The second run printed the same ids and created nothing.
- [x] 1.3 Capture these:
  - with the admin token: the topic's entries, a root entry's replies, and `entry_list?ids[]=…`
  - `search/recipients?search=a` with the admin token
  - `search/recipients?types[]=context` with the student token

  Record each field's JSON type next to D1/D2 in these notes, and update D1/D2 if one disagrees.
  - Done: captured to `test/custom/unit/fixtures/discussions/`. Entries match D1: ids and counts are integers or null (`rating_*` and `editor_id` are null here), timestamps are strings, `user`/`attachment` are objects, `attachments`/`recent_replies` are arrays, `deleted`/`forced_read_state`/`has_more_replies` are booleans. Entries list only active roots; the deleted entry appears only in `entry_list`. User recipients match D2 (integer `id`, `pronouns` null, `common_*` objects). **Deviation:** Canvas returns no contexts unless `search` is sent, even empty, and the client's parameter is `type`, not `types[]`; the capture used `type=context&search=` (one `course_2` context with `user_count` and empty `permissions`). No synthetic sub-contexts were reachable, so `item_count` is covered by a hand-written payload. Recaptured as Seeded Admin 2 (user 392) and the student (user 8), confirmed with `GET /users/self` first; the recapture is byte-identical to the committed fixtures.

## 2. Doc corrections (canvas-lms fork)

- [x] 2.1 Apply D1 and D2. Verify that `git diff` shows comment lines only, and that both models' JSON parses.
  - Done: fork worktree commit `28132fdaaf9`, comment lines only.
- [x] 2.2 Regenerate (`bundle exec rake doc:openapi`, not committed) and diff. Verify:
  - `DiscussionEntry` (with the self-referencing `recent_replies`) and `Recipient` exist
  - the eight operations return arrays of them
  - no other operation changed
  - Done: regenerated with `.worktrees/gen_wt.rb` from the fork worktree.
- [x] 2.3 Commit only the two controllers in upstream format: subject, why, `flag=none`, `Test Plan:`, every line under 60 characters. Verify that `git log -1 --stat` lists only them, and that the seed script and `public/doc/` stay uncommitted. Do not open a PR.
  - Done: `28132fdaaf9 fix(canvas-lms): document discussion entries, recipients` lists only the two controllers.

## 3. Client (canvas-lms-python-client)

- [x] 3.1 Copy `src/.openapi-generator/FILES`, regenerate, and delete orphans by manifest diff (keep existing `test_*.py` entries the manifest drops). Verify:
  - `discussion_topics_api_entries_all` yields `DiscussionEntry`
  - `search_recipients_all` yields `Recipient`
  - `Recipient.id` is untyped
  - a two-level `recent_replies` payload deserializes
  - Done: regenerated in `.worktrees/client-discussion`. FILES gains the 2 models, 2 docs and 2 test stubs; the generator's test-entry drop was unioned back and the stray `src/canvas_lms_python_client_README.md` removed. `_all` iterators yield `DiscussionEntry`/`Recipient`, `Recipient.id` is `Optional[Any]`, and a two-level `recent_replies` payload round-trips.
- [x] 3.2 Add the 1.3 fixtures and `test/custom/unit/test_discussion_and_recipient_models.py` (D4), and drop the eight operations from `UNDOCUMENTED_PAGINATED_OPERATIONS`. Verify that the tests pass, and that they fail against the pre-change generated files: check out the old files, confirm the failure, then restore them.
  - Done: 18 tests in `test_discussion_and_recipient_models.py`, which also checks the eight `_all` item types. Against the pre-change generated files the new file fails to import `DiscussionEntry` and the allowlist test lists the eight operations as untyped.
- [x] 3.3 Add the integration tests (D4) and run `pdm run pytest --integration -v -k "entries or replies or recipients"` with the admin and student tokens. Verify that they pass.
  - Done: 5 tests: entries, replies and entry_list (admin), user recipients (admin) and context recipients (student). The seeded topic is found by title, not by a hardcoded course id. All pass.
- [x] 3.4 Verify that `pdm run pytest` passes offline, that the full `--integration` run shows no new failures, and that `pdm run ruff check src/canvas_lms_python_client/test/custom` is clean. Then commit the client.
  - Done: offline 3776 passed, 173 skipped; `--integration` 3808 passed, 141 skipped, no failures; ruff check clean.

## 4. Final checks

- [x] 4.1 Run `openspec validate type-discussion-entries-and-recipients --strict` and verify that it passes.
  - Done. Landed on 2026-11-03 after rebasing onto the audit and simple changes: fork `46a6a91c1a0` and client `a30a62d`.
    - Rebase conflicts were in the two hand-written client tests only. In `test_paginated_models.py`, both sides are kept. In the `UNDOCUMENTED_PAGINATED_OPERATIONS` allowlist, both sides' removals are kept.
    - Regenerating from the rebased spec matched the commit exactly, except for the usual drop of test entries from `FILES`, which was discarded. The spec diff from the post-simple baseline is the 2 new schemas and the 8 operations only.
    - After landing, `rake doc:openapi` in the main checkout produced the same spec, and regenerating from it left no diff beyond the `FILES` drop.
    - Final counts: offline 3848 passed and 182 skipped. `--integration` 38 passed and 8 skipped. Adapter spec 176 examples, 0 failures, run on the landed code. Rubocop's 8 offenses on the two controllers were already there before this change. The fork diff touches comments only.
    - The integration run used an admin token belonging to Seeded Admin 2 (user 392), not user 1, so the 3 poll tests skipped (no polls owned by that user).

## Workflow follow-up

- Upstream: the user may cherry-pick the task 2.3 commit after signing the CLA.
- Type `DiscussionEntry.user`/`attachment` once `UserDisplay` and the duplicate `File` are fixed.
- Archive with `/opsx:archive` after review.
