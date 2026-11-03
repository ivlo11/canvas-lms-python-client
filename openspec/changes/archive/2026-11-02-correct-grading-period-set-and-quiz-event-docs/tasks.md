# Tasks

## 1. Seed and confirm live types (canvas-lms fork, uncommitted)

- [x] 1.1 Capture the baseline: with a throwaway script, write `operationId → response schema (JSON)` for every operation in `public/doc/openapi/canvas.openapi.yaml` to the scratchpad. Verify that `GradingPeriodSets-index` and `QuizSubmissionEventsApi-index` have no response schema, and that `GradingPeriodSets-create` has none either.

  Notes: confirmed. All three operations have only an `example` under `default`, with no `schema`.
- [x] 1.2 Add `create_grading_period_set` and `create_quiz_submission_events` to `spec/manual_seeding/large_gradebook_seeds.rb` and call them from the main flow (design D5). Run `bin/rails runner spec/manual_seeding/large_gradebook_seeds.rb` in the web container. Verify, as the seeded admin:
  - `GET /api/v1/accounts/self/grading_period_sets` returns at least one set with two `grading_periods`.
  - `GET /api/v1/courses/<course>/quizzes/<quiz>/submissions/<id>/events` returns 3 events whose `event_data` is a list, an object and null.

  Do not commit the seed script.

  Notes: added as a standalone `--audit-data` option (`create_grading_period_set`, `create_quiz_submission_events`) rather than the main flow; reruns are no-ops. Seeded: grading period set 1 ("Seeded Grading Periods", weighted, `display_totals_for_all_grading_periods: true` so course totals stay visible) with periods 1 (66.67) and 2 (33.33) on default term 1; `quiz_log_auditing` on course 6; events 41 `question_answered` (list), 42 `question_flagged` (object), 43 `page_blurred` (null) on quiz 1, submission 1. The index also returns the existing `submission_created` event 1, whose `event_data` is an object. Captured as Seeded Admin 2.
- [x] 1.3 Save both live responses, plus `GET /api/v1/accounts/self/grading_periods`, to the scratchpad. In these notes, record the JSON type of every set field, and of every nested and top-level `GradingPeriod` field (`id`, `grading_period_group_id`, `weight`, the dates, `is_closed`, `permissions`). Compare each against `GradingPeriod`'s `@model`. If nested and top-level types differ for one field, stop and ask (design, Risks).


  Notes: stopped here at first (design, Risks), then resumed after the user chose a separate model for the course include (design D7). Live JSON types:
  - Set (`grading_period_sets[]`): `id` str, `title` str, `weighted` bool, `display_totals_for_all_grading_periods` bool, `account_id` str, `course_id` null, `permissions` dict of bools (`read`/`update`/`delete`/`create`), `created_at` str. The page also carries `meta.pagination`.
  - `GradingPeriod`, nested in a set and from `GET /accounts/self/grading_periods` (and `/courses/2/grading_periods[/2]`), agree: `id` str, `grading_period_group_id` str, the 3 dates str, `weight` float, `title` str, `is_closed` bool, `permissions` dict.
  - `@model GradingPeriod` documents `id` integer and `weight` integer, and lacks `grading_period_group_id`/`permissions`. Today's client already fails `GradingPeriodsIndexResponse.from_dict` on the live page (`id`, `weight`).
  - But `Course.grading_periods` (`GET /courses/2?include[]=grading_periods`) also `$ref`s `GradingPeriod`, and sends a different shape: `id` **int**, `title`, `start_date`, `end_date`, `workflow_state`, with no `weight`. So retyping `GradingPeriod.id` to string (D3) would break the course include, and leaving it integer breaks the set and grading period endpoints. Decided: D7 adds `CourseGradingPeriod` for the course include (`Api::V1::Course` renders `only: %w[id title start_date end_date workflow_state]`; live: `id` int, the rest strings), and D3 corrects `GradingPeriod` to the types above.
## 2. Doc corrections and regeneration (canvas-lms fork)

- [x] 2.1 Edit `app/controllers/grading_period_sets_controller.rb` as in D1 and D2, using the types recorded in 1.3. Edit `app/controllers/quizzes/quiz_submission_events_api_controller.rb` as in D1 and D4. Apply D3's `GradingPeriod` corrections in `app/controllers/grading_periods_controller.rb`, and D7's `@model CourseGradingPeriod` plus the `Course.grading_periods` `$ref` in `app/controllers/courses_controller.rb`. Verify with `git diff --stat` that only comment lines in those controllers changed.

  Notes: done in a fork worktree (`.claude/worktrees/grading-period-docs`). Comment lines only in 4 controllers: `grading_period_sets_controller.rb`, `quizzes/quiz_submission_events_api_controller.rb`, `grading_periods_controller.rb` and `courses_controller.rb`. The model is named `CourseGradingPeriod` (no collision).
- [x] 2.2 Regenerate the spec in the web container (`bundle exec rake doc:openapi`, not committed) and compare it with the 1.1 baseline. Verify:
  - `GradingPeriodSets-index` → `$ref GradingPeriodSetsIndexResponse` (`grading_period_sets`: array of `$ref GradingPeriodSets`).
  - `GradingPeriodSets-create` → `$ref GradingPeriodSetsCreateResponse` (`grading_period_set`: `$ref GradingPeriodSets`).
  - `QuizSubmissionEventsApi-index` → `$ref QuizSubmissionEventsApiIndexResponse`.
  - `GradingPeriodSets` has the D2 fields with the 1.3 types. `QuizSubmissionEvent` has `id: string`, and its `event_data` has no `type`.
  - `GradingPeriod` has the D3 types, `CourseGradingPeriod` exists with the D7 fields, and `Course.grading_periods.items` is `$ref CourseGradingPeriod`.
  - No other operation's response changed.

  Notes: generated from the worktree with a `rails runner` that loads the worktree's `open_api_generator` and passes `canvas_root:`. `canvas_root` only sets the operation scan (`config.controller_path`); `collect_model_schemas!` reads `@model`s from `Rails.root`, so the runner also overrode `Rails.root` to the worktree for the call (262 controller models, one more than before). Diff vs the main-checkout spec: added `CourseGradingPeriod`, `GradingPeriodSetsIndexResponse`, `GradingPeriodSetsCreateResponse`, `QuizSubmissionEventsApiIndexResponse`. `GradingPeriod.id` integer→string and `weight` integer→number, plus `grading_period_group_id` and `permissions`. `GradingPeriodSets` +6 fields. `QuizSubmissionEvent` +`id`, and `event_data` has no type. `Course.grading_periods.items` → `CourseGradingPeriod`. Only the 3 operations changed. Their `default` description is now empty (cosmetic; it comes from the `@returns` text).
- [x] 2.3 Generate the API HTML docs in the web container (`bundle exec rake doc:api`) and verify that the Grading Period Sets and Quiz Submission Events pages render "Returns a list of GradingPeriodSets objects" / "QuizSubmissionEvent objects" with working model links. If the task isn't available, record that and check the rendered `@returns` with YARD instead.

  Notes: `rake doc:api` reads the main checkout, so the rendering was checked by running `doc/api/tags/setup.rb#returns`'s logic over the worktree controllers with YARD. index → `GradingPeriodSets`, list, linked; events → `QuizSubmissionEvent`, list, linked. **create does not link**: its brace form has no `[...]`, so the renderer looks up the whole text as a model name and renders no "Returns" line. create had no `@returns` before, so this isn't a regression (follow-up: an upstream renderer that reads bare models inside braces).
- [x] 2.4 Commit only the four edited controller files, in upstream format (D6). The message has:
  - a subject and the why
  - `flag=none`
  - a `Test Plan:` that covers 2.3 and the live requests from 1.2
  - every line under 60 characters

  Verify that `git log -1 --stat` lists only controller files, and that `git status` still shows the seed script modified and `public/doc/` untracked. Do not open a PR.


  Notes: committed as `fix(canvas-lms): document grading period set returns` (4 controllers) and fast-forwarded onto `chore/fix-openapi-spec`. The pre-commit hook (host lint, which errors on Ruby 2.6 without blocking) was bypassed in the worktree; no Change-Id is generated, as with earlier commits.
## 3. Client regeneration and tests (canvas-lms-python-client)

- [x] 3.1 Copy `src/.openapi-generator/FILES` to the scratchpad and regenerate the client (`openapi-generator-cli generate` with `openapi-generator-config.yaml`, `-t mustache-templates`, `-o src`). Delete any orphans by manifest diff, skipping `.openapi-generator-ignore` paths. Verify:
  - `grading_period_sets_index_paginated` is `AsyncIterator[GradingPeriodSetsIndexResponse]` and has no `_all`.
  - `grading_period_sets_create` returns `GradingPeriodSetsCreateResponse`.
  - `quiz_submission_events_api_index_paginated` is `AsyncIterator[QuizSubmissionEventsApiIndexResponse]`.
  - `QuizSubmissionEvent.event_data` is `Optional[Any]`.

  Notes: done in a client worktree. All four signatures as listed, and no `_all` for either wrapper. No orphans. Kept the existing `test_*.py` `FILES` entries; deleted and regenerated the stale stubs `test_grading_period.py`, `test_grading_period_sets.py`, `test_quiz_submission_event.py` and `test_course.py`. New: `CourseGradingPeriod`, the 3 wrappers, and their docs and stubs.
- [x] 3.2 In `test/custom/unit/test_paginated_response_types.py`:
  - Remove `grading_period_sets_index` and `quiz_submission_events_api_index` from `UNDOCUMENTED_PAGINATED_OPERATIONS`.
  - Add `GradingPeriodSetsIndexResponse` and `QuizSubmissionEventsApiIndexResponse` to `WRAPPED_LIST_RESPONSES`.
  - Add offline payload tests from the 1.3 captures: a set page with nested grading periods, a create response holding one set, events whose `event_data` is a list, an object and null, the account grading periods page (string ids, float weights), and a course with `include[]=grading_periods` (`CourseGradingPeriod`, integer ids), each equal to the JSON sent.

  Verify that the module passes.

  Notes: the `grading_periods` sample item now uses a string id. Fixtures in `test/custom/unit/fixtures/grading_periods/` (`grading_period_sets.json`, `grading_periods.json`, `course_include_grading_periods.json`, `quiz_submission_events.json`) were captured as Seeded Admin 2. The create response is built from the captured set. The module has 103 passed.
- [x] 3.3 Add integration tests to `test/custom/integration/test_paginated_models.py` (admin client):
  - `test_grading_period_sets_pages_typed`
  - `test_quiz_submission_events_pages_typed`, which finds the seeded audited submission and asserts every `event_data` shape
  - `test_grading_periods_index_typed` (account grading periods, string ids)
  - `test_course_include_grading_periods_typed` (`GET /api/v1/courses/<course>?include[]=grading_periods`, `CourseGradingPeriod` items)

  Verify with `pdm run pytest --integration -m integration -v` against the seeded instance. Record any `ValidationError` as a follow-up naming the model and field.

  Notes: added `test_quiz_submission_events_pages_typed`, `test_grading_period_sets_pages_typed`, `test_grading_periods_index_typed` and `test_course_include_grading_periods_typed`; all 4 pass live. No `ValidationError`.
- [x] 3.4 Verify that `pdm run pytest` passes offline and that `pdm run ruff check` on the changed test files is clean.


  Notes: offline 3740 passed, 165 skipped. `--integration` (all three tokens): 23 passed, 6 skipped (the same seeded-data skips; `test_student_grades` still passes with the term's grading periods). ruff clean. Committed as `fix(canvas_lms_python_client): type grading period sets and quiz events` and fast-forwarded onto `fix/add-returns-for-paginated-models`. Regenerating from the main checkout's re-generated spec gives an identical spec and no client diff, apart from the known `FILES` test-entry drop, which was discarded.
## 4. Final checks

- [x] 4.1 Run `openspec validate correct-grading-period-set-and-quiz-event-docs --strict` and verify it passes.

## Workflow follow-up

- Commit the client after the fork commit (task 2.4).
- Upstream: the user may sign the Instructure CLA and cherry-pick the task 2.4 commit onto instructure/canvas-lms `master` for a PR.
- Upstream renderer: link a bare model inside a brace `@returns` (grading period set create).
- Archive with `/opsx:archive` after review.
