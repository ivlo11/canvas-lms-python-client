# Tasks

## 1. Seed and capture (canvas-lms fork, uncommitted)

- [x] 1.1 Verify that `CANVAS_STUDENT_API_TOKEN` authenticates (`GET /users/self`). If it doesn't, rerun the seed `--tokens` option and record the fix in these notes. Never write the token itself.
  - Done: `CANVAS_STUDENT_API_TOKEN` isn't set in the env. The seeded student token (user 8, "Jessie 2") authenticates on `/users/self`, so the tests ran with it set for the run only. The observer token (`CANVAS_API_TOKEN`) is user 218, observing user 168.
- [x] 1.2 Re-read `spec/manual_seeding/large_gradebook_seeds.rb` and add `--todo-items` (D3) as an additive edit. Run it twice in the web container. Verify that the first run prints the ids and date range and the second creates nothing new. Do not commit the script.
  - Done: Applies to course 2, not 5: the seed picks the student's first available course. Run twice on 2026-11-03: both runs printed the same ids and created nothing new. The ids are course 2, teacher 7, student 8, assignment 260 (due 2026-11-06), submission 13002 by user 9, planner note 1 and planner override 1, with the range 2026-11-03 to 2026-11-07.
- [x] 1.3 Capture these:
  - the student's `GET /planner/items?start_date=…&end_date=…` and `GET /users/self/todo`
  - the observer's `GET /users/<observee>/planner/items`
  - a grading todo item from a `todo_item_json` call for the course's teacher in the web container

  Record each field's JSON type next to D1/D2 in these notes, including the `assignment` fields whose type differs from the `Assignment` model.
  - Done: Captured the student's planner items (note with `submissions: false` and a `PlannerOverride`, and an assignment with a `submissions` object), the student's todo list (12 `submitting` items), and the observer's planner items for user 168 (50 assignments). **Deviation:** the grading todo was captured over HTTP with a temporary access token for teacher 7, which was deleted straight after. Calling `todo_item_json` outside a controller fails (`api_user_content` is undefined). `GET /courses/2/todo` and the teacher's `/users/self/todo` each returned 3 `grading` items, with integer `needs_grading_count`. All 70 captured items match D1/D2: `plannable` is a JSON object, `submissions` is `false` or an object, `context_image` can be null, ids are integers and dates are ISO strings. `assignment_json` validated against `Assignment` without mismatches. No personal data was found: no emails and no user 1 references.

## 2. Doc corrections (canvas-lms fork)

- [x] 2.1 Apply D1 and D2, plus any `Assignment` field fixes that 1.3 showed are needed. Verify that `git diff` shows comment lines only, and that both models' JSON parses.
  - Done: Commit `6b99bc8762e`, rebased onto the audit tip as `082f4e8b7bd`. `git diff` shows comment lines only. No `Assignment` fixes were needed.
- [x] 2.2 Regenerate (`bundle exec rake doc:openapi`, not committed) and diff. Verify:
  - `PlannerItem` and `TodoItem` exist
  - the four operations return arrays of them
  - no other operation changed, except through any `Assignment` fixes
  - Done: Generated from the worktree with `gen_wt.rb` and diffed against the main checkout's spec: the two added schemas are `PlannerItem` and `TodoItem`, no schema changed, and the only operations that changed are `Planner-index`, `Planner-index_for_users`, `Users-todo_items` and `Courses-todo_items`, each returning an array of the new model. swagger_yard specs: 176 examples, 0 failures. Rubocop: the same 18 offenses as on the unchanged controllers, none of them on the added lines.
- [x] 2.3 Commit only the edited controllers in upstream format: subject, why, `flag=none`, `Test Plan:`, every line under 60 characters. Verify that `git log -1 --stat` lists only them, and that the seed script and `public/doc/` stay uncommitted. Do not open a PR.
  - Done: Only the three controllers are committed. The seed script and `public/doc/` are still uncommitted.

## 3. Client (canvas-lms-python-client)

- [x] 3.1 Copy `src/.openapi-generator/FILES`, regenerate, and delete orphans by manifest diff (keep existing `test_*.py` entries the manifest drops). Verify:
  - `planner_index_all` yields `PlannerItem`, and its `plannable` and `submissions` are untyped
  - `users_todo_items_all` yields `TodoItem`, with `assignment: Assignment`
  - Done: Regenerated in `.worktrees/client-planner` after rebasing onto `0683c17`. `FILES` is the `LC_ALL=C sort -u` union with the pre-change manifest (no orphans). `planner_index_all` and `planner_index_for_users_all` are typed `AsyncIterator[PlannerItem]`, with `plannable` and `submissions` as `Optional[Any]`. `users_todo_items_all` and `courses_todo_items_all` are typed `AsyncIterator[TodoItem]`, with `assignment: Optional[Assignment]`.
- [x] 3.2 Add the 1.3 fixtures and `test/custom/unit/test_planner_and_todo_models.py` (D4), and drop the four operations from `UNDOCUMENTED_PAGINATED_OPERATIONS`. Verify:
  - the tests pass, and they fail against the pre-change generated files (check out the old files, confirm the failure, then restore them)
  - after this change (and the other three undocumented-list changes), only `search_all_courses` remains allowlisted; the grading period and quiz event operations were already removed by the archived `correct-grading-period-set-and-quiz-event-docs`
  - Done: Fixtures are in `fixtures/planner/`: `student_planner`, `observer_planner` (2 items), `student_todo` (2 items) and `course_todo` (3 grading items). The quiz variant is synthetic, because none was seeded. Against the pre-change generated files, the new test fails on import and the allowlist test fails as stale. With this change, `search_all_courses` and the operations of the `simple` and `discussion` changes stay allowlisted until those changes land.
- [x] 3.3 Add the integration tests (D4) and run `pdm run pytest --integration -v -k "planner or todo"` with the student and observer tokens. Verify that they pass.
  - Done: `-k "planner or todo"`: 25 passed (3 live, 22 offline).
- [x] 3.4 Verify that `pdm run pytest` passes offline, that the full `--integration` run shows no new failures, and that `pdm run ruff check src/canvas_lms_python_client/test/custom` is clean. Then commit the client.
  - Done: Offline: 3830 passed, 174 skipped. Full `--integration` run, with the student token set: 3863 passed, 141 skipped, 0 failed. Ruff check is clean. Client commit `d82f57e` on `wt/planner`.

## 4. Final checks

- [x] 4.1 Run `openspec validate type-planner-and-todo-items --strict` and verify that it passes.
  - Done after landing on 2026-11-03: rebased onto `discussion`, regenerated from the rebased fork (only `FILES` needed updating; the generated files matched), and reran the tests. Landed as fork `e0dddf2b323` and client `8299d9c`, which replace the hashes in the notes above. Allowlist conflict resolved to `search_all_courses` only. `rake doc:openapi` in the main checkout gives the same spec as the rebased worktree, and regenerating the client from it leaves only the usual `FILES` test-entry drop, which was discarded. Offline: 3872 passed, 185 skipped. Full `--integration`, before the final docs-only rebase: 3913 passed, 144 skipped, 0 failed. `openspec validate --strict` passes.

## Workflow follow-up

- Upstream: the user may cherry-pick the task 2.3 commit after signing the CLA.
- Per-type `plannable` models via a discriminator once the adapter supports `oneOf`.
- Decide whether `search_all_courses` (course catalog only) gets a `@returns`.
- Archive with `/opsx:archive` after review.
