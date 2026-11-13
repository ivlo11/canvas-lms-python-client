# Tasks

## 1. Seed varied submission states (canvas-lms fork, uncommitted)

- [x] 1.1 Capture the baseline: with a throwaway script, write `operationId → response schema (JSON)` and the `Submission` schema from `public/doc/openapi/canvas.openapi.yaml` to the scratchpad. Verify that `Submission` has only `id` and `student_entered_score`. **Notes:** the committed spec was regenerated from fork HEAD first and was byte-identical. `Submission` had only `id` and `student_entered_score`.
- [x] 1.2 Add `CreateHelpers.vary_observee_submission_states` and the `--observee-states` option to `spec/manual_seeding/large_gradebook_seeds.rb` (design D3). Run `bin/rails runner spec/manual_seeding/large_gradebook_seeds.rb --observee-states` in the web container twice. Verify:
  - As the observer (`CANVAS_API_TOKEN`), `GET /api/v1/courses/<course>/students/submissions?student_ids[]=<observee>` shows at least `submitted`, `graded` and `unsubmitted`. Record in these notes whether `pending_review` appeared.
  - The second run changes nothing.

  Do not commit the seed script.

  **Notes:** the first run failed with `PG::GroupingError` because `course.submissions` has a default order; the state count uses `reorder(nil)`. 25 active observer links, in courses 5–8, were varied. Each observee now has 1 `submitted`, 1 or 2 `graded` (courses 6–8 already had a graded checkpoint quiz), 1 `pending_review` (the essay quiz) and 48 `unsubmitted`. `pending_review` appeared. The second run skipped all 25 observees.
- [x] 1.3 Save that response (all pages, `per_page=100`) to the scratchpad. In these notes, record each key's JSON types and every `submission_type`, `workflow_state` and `read_status` value seen, and compare them with the full `Submission` `@model` (D2, Risks). **Notes:** the observer token sees observee 168 in course 5. 51 submissions in one page: 48 `unsubmitted`, 1 `submitted`, 1 `graded`, 1 `pending_review`. `submission_type` values were `online_text_entry`, `online_quiz` and null, all within the enum. `read_status` was absent. Types match the model: `id`, `assignment_id`, `user_id`, `attempt` and `grader_id` are ints; `score`, `entered_score` and `points_deducted` are floats; `seconds_late` is an int (model: number); `grade`, `entered_grade`, `body`, `preview_url` and the timestamps are strings; `late`, `missing`, `excused`, `redo_request` and `grade_matches_current_submission` are booleans. Sent but undocumented: `cached_due_date`, `custom_grade_status_id`, `entered_grade`, `entered_score`, `grading_period_id` and `sticker` (dropped by the client; not in scope). Documented but not sent without includes: `assignment`, `course`, `user`, `submission_comments`, `html_url`, `assignment_visible`, `anonymous_id` and `read_status`.

## 2. Doc corrections and regeneration (canvas-lms fork)

- [x] 2.1 Apply D1 and D2:
  - `what_if_grades_api_controller.rb`: `@model WhatIfSubmission`, plus `update`'s `@returns`.
  - `lti/submissions_api_controller.rb`: `@model Lti::Submission`.
  - `submissions_api_controller.rb`: add `id` to `Submission`.

  Verify with `git diff` that only comment lines changed, and that no other `@model Submission` remains: run `grep -rnE "#\s*@model Submission\s*$" app/controllers` and expect one hit.

  **Notes:** 10 insertions and 5 deletions, all comment lines. The grep returns only `submissions_api_controller.rb:31`.
- [x] 2.2 Regenerate the spec in the web container (`bundle exec rake doc:openapi`, not committed) and compare it with the 1.1 baseline. Verify:
  - `Submission` has the full model's properties plus `id: integer`, and `workflow_state` has the four documented values.
  - `WhatIfSubmission` has `id` and `student_entered_score`, and `WhatIfGradesApiUpdateResponse.submission` references it.
  - `Lti_Submission` exists.
  - The only operation response changes are inside the what-if wrapper.

  **Notes:** schemas went from 309 to 311. No operation response changed. Only `Submission` and `WhatIfGradesApiUpdateResponse` changed, and `WhatIfSubmission` and `Lti_Submission` were added. `Submission` has 32 properties (31 documented plus `id`; the proposal's "29" was a miscount). `Lti_Submission` has 12 properties, not 13.
- [x] 2.3 Commit only the three controller files in upstream format (design D6). The message has a subject, the why, `flag=none` and a `Test Plan:`, with every line under 60 characters. Verify that `git log -1 --stat` lists only those files, and that the seed script and `public/doc/` stay uncommitted. Do not open a PR. **Notes:** canvas-lms `2ee53d74273`, "fix(canvas-lms): give each Submission @model a name", touches only the three controllers. The pre-commit hook's `script/rlint` couldn't load under the macOS system Ruby, but the commit went through.

## 3. Client regeneration and tests (canvas-lms-python-client)

- [x] 3.1 Copy `src/.openapi-generator/FILES`, regenerate the client with the usual command, and delete orphans by manifest diff. Verify:
  - `models/submission.py` declares `id`, `workflow_state`, `assignment_id`, `user_id`, `submitted_at` and `grade`.
  - `models/what_if_submission.py` and `models/lti_submission.py` exist.
  - `submissions_api_for_students_all` still yields `Submission`.

  **Notes:** used the `openapitools/openapi-generator-cli:latest` Docker image (`-i ../canvas-lms/public/doc/openapi/canvas.openapi.yaml`, `-c`, `-t mustache-templates`, `-o src`). No orphans. The new files are the `LtiSubmission` and `WhatIfSubmission` models, docs and test stubs. As before, the generator dropped 23 existing `test_*_api.py` lines from `FILES`. The manifest was rebuilt as the sorted union of the old and new lists, so only the 6 new lines are added. `Assignment` and the full `Submission` now reference each other, so the generator moved `assignment.py`'s `Submission` import below the class and added a `model_rebuild`. `submissions_api_for_students_all` still returns `AsyncIterator[Submission]`.
- [x] 3.2 Add the 1.3 capture as `src/canvas_lms_python_client/test/custom/unit/fixtures/submissions/observee_submissions.json`, and add `test/custom/unit/test_submission_model.py` (D5). Verify that it passes, and that it fails against the pre-change `models/submission.py`: check out the old file, confirm the failure, then restore it. **Notes:** 52 passed. Against the old `models/submission.py`, 51 failed (only the fixture-states check passed). The file was then restored.
- [x] 3.3 Add `test_observee_submission_workflow_states` to `test/custom/integration/test_observees.py` (D4). Verify with `pdm run pytest --integration -m integration -v -s -k workflow_states` against the seeded instance that it passes and prints each observee's state counts. Record the counts in these notes. Record any `ValidationError` as a follow-up naming the field and value. **Notes:** passed, with no `ValidationError`. Counts: observee 168 has `{'graded': 1, 'submitted': 1, 'unsubmitted': 48, 'pending_review': 1}`.
- [x] 3.4 Verify that `pdm run pytest` passes offline, that the full `--integration` run shows no new failures, and that `pdm run ruff check src/canvas_lms_python_client/test/custom` is clean. Then commit the client. **Notes:** offline, `test_inline_object_responses.py::test_what_if_grades_are_typed` failed because it expected `models.Submission`. It now asserts `models.WhatIfSubmission`, which is D1's intended type. After that: 3712 passed and 159 skipped offline; 17 passed and 6 skipped with `--integration`, with no failures; ruff is clean.

## 4. Final checks

- [x] 4.1 Run `openspec validate count-observee-submission-states --strict` and verify that it passes. **Notes:** client commit `93f004e`. Validation passed.

## Workflow follow-up

- Upstream: the user may sign the Instructure CLA and cherry-pick the task 2.3 commit onto instructure/canvas-lms `master`.
- Follow-up changes:
  - the other 13 duplicated `@model` names (`Account`, `FeatureFlag`, `File`, `Grade`, `Module`, `ModuleItem`, `OutcomeAlignment`, `Progress`, `Report`, `ReportParameters`, `Result`, `RubricAssessment`, `RubricRating`)
  - a generator warning when a `@model` name is redefined with a different schema
- Archive with `/opsx:archive` after review.
