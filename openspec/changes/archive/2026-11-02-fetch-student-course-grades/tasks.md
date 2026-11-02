# Tasks

## 1. Seed and capture (canvas-lms fork, uncommitted)

- [x] 1.1 Confirm that `seed-student-and-second-admin-tokens` is applied: its `--tokens` run prints a student token. Record which student it is in these notes; don't record the token. If it's not applied, stop and ask whether to apply it first.

  Notes: applied. `--tokens` picks student 8 ("Jessie 2"), enrolled only in course 2, not 168 as the design expected; 168 is the `CANVAS_API_TOKEN` observee, 8 is the observee of the oldest observer link.
- [x] 1.2 Re-read `spec/manual_seeding/large_gradebook_seeds.rb`. Add `enable_grading_scheme` and a standalone `--grading-scheme` option (D3), as additive edits. Run `bin/rails runner spec/manual_seeding/large_gradebook_seeds.rb --grading-scheme` twice in the web container. Verify that the first run prints a non-null letter grade for at least one course and the second run changes nothing. Do not commit the script.

  Notes: both runs print `Advanced Pokeball Mechanics (2)`: grade `"B-"`, score `80.0`. The second run leaves course 2 unchanged (`grading_standard_id` stays 0).
- [x] 1.3 Capture `courses_total_scores.json` and `enrollments_with_grades.json` (D6) with the admin token. In these notes, record each enrollment field's JSON type next to its `Enrollment` `@model` type, and confirm that `computed_current_grade` is non-null.


  Notes: captured for student 8, course 2 (`GET /users/8/courses?include[]=total_scores&include[]=current_grading_period_scores` and `GET /courses/2/enrollments?user_id=8`). Enrollment field JSON types vs. the pre-change `@model` types: `computed_current_score`/`computed_final_score` float (undocumented); `computed_current_grade`/`computed_final_grade` str (undocumented); `unposted_current_score`/`unposted_final_score` float (`string`, wrong); `unposted_*_grade` str (`string`); the eight `current_period_*` fields null (scores `number`, grades `string`; computed ones undocumented). `computed_current_grade` is `"B-"`. `grades` carries `current_score`/`final_score`/`unposted_*_score` as floats too, while the enrollments `Grade` model typed them `string`, so D1 was extended to type those four as `number` (see design D1). A student's own course list also sends `computed_current_letter_grade`, which stays undocumented (follow-up).
## 2. Doc corrections and regeneration (canvas-lms fork)

- [x] 2.1 Apply D1 to `enrollments_api_controller.rb` (`@model Enrollment`) and D2 to `what_if_grades_api_controller.rb`, placing the edit next to the existing `WhatIfSubmission` change. Verify that `git diff` shows comment lines only, and that `grep -rnE "#\s*@model Grade\s*$" app/controllers` has exactly one hit, in the enrollments controller.

  Notes: comment lines only; the one `@model Grade` hit is `enrollments_api_controller.rb:25`.
- [x] 2.2 Regenerate the spec in the web container (`bundle exec rake doc:openapi`, not committed) and diff it with the previous spec. Verify:
  - `Enrollment` has the 8 new properties, and `unposted_current_score`/`unposted_final_score` are `number`.
  - `Grade` has the enrollments properties.
  - `WhatIfGrade` exists, and `Grades.current`/`final` reference it.
  - No operation response changed.

  Notes: schema diff: `WhatIfGrade` added; `Enrollment` +8 properties and `unposted_*_score` string→number; `Grade` now has the 11 enrollment grade fields (scores `number`); `Grades.current`/`final` → `WhatIfGrade`. `paths` are identical.
- [x] 2.3 Commit only the two controller files in upstream format (D7): subject, why, `flag=none`, `Test Plan:`, every line under 60 characters. Verify that `git log -1 --stat` lists only those files, and that the seed script and `public/doc/` stay uncommitted. Do not open a PR.


  Notes: committed as `fix(canvas-lms): document enrollment grade scores`. The local `script/rlint` pre-commit step errors on the host's Ruby 2.6 bundler, but doesn't block the commit.
## 3. Client (canvas-lms-python-client)

- [x] 3.1 Copy `src/.openapi-generator/FILES`, regenerate, and delete orphans by manifest diff. Verify:
  - `models/enrollment.py` declares `computed_current_grade` (`Optional[StrictStr]`) and `unposted_final_score` (float).
  - `models/grade.py` declares `current_score` and `html_url`.
  - `models/what_if_grade.py` exists.

  Notes: no orphans. The manifest diff dropped 25 existing `test_*.py` entries (the generator lists a test only in the run that creates it), so those entries were kept. The stale `test_grade.py`/`test_grades.py` stubs built the old what-if `Grade`, so they were deleted and regenerated.
- [x] 3.2 Add the 1.3 fixtures and `test/custom/unit/test_enrollment_grades.py` (D6). Verify that it passes, and that it fails against the pre-change `models/enrollment.py` and `models/grade.py`: check out the old files, confirm the failure, then restore them.

  Notes: 4 passed; against the HEAD `enrollment.py`/`grade.py`, 3 failed (course deserialization, enrollment scores, `grades` model).
- [x] 3.3 Add the `canvas_student_api_token` and `canvas_student_api_client` fixtures to `test/custom/conftest.py`, and the README variable row and sentence (D4). Verify that, with `CANVAS_STUDENT_API_TOKEN` unset, a student-scoped test is skipped with a reason naming it while the other integration tests run.
- [x] 3.4 Add `test/custom/integration/test_student_grades.py` (D5). Run `CANVAS_STUDENT_API_TOKEN=<seeded> pdm run pytest --integration -v -s -k computed_grades` and verify that it passes and prints each course's grade and score. Record the printed grades in these notes. Record any `ValidationError` as a follow-up naming the field.

  Notes: printed `Advanced Pokeball Mechanics (2): grade B-, score 80.0`. No `ValidationError`. `UsersApi.users_api_show` returns an untyped `dict` (`@returns Schemas::Docs::User` isn't resolved), so the test reads `student["id"]` (follow-up).
- [x] 3.5 Verify that `pdm run pytest` passes offline, that the full `--integration` run (all three tokens set) shows no new failures, and that `pdm run ruff check src/canvas_lms_python_client/test/custom` is clean. Then commit the client.


  Notes: offline 3717 passed, 160 skipped. `--integration` with all three tokens: 18 passed, 6 skipped, the same seeded-data skips as before. ruff clean.
## 4. Final checks

- [x] 4.1 Run `openspec validate fetch-student-course-grades --strict` and verify that it passes.

## Workflow follow-up

- Upstream: the user may cherry-pick the task 2.3 commit onto instructure/canvas-lms `master` after signing the CLA.
- Remaining duplicated `@model` names, now 12: `Account`, `FeatureFlag`, `File`, `Module`, `ModuleItem`, `OutcomeAlignment`, `Progress`, `Report`, `ReportParameters`, `Result`, `RubricAssessment`, `RubricRating`. Plus a generator warning on redefinition.
- Document `computed_current_letter_grade`, which a student's own course list sends.
- Resolve `@returns Schemas::Docs::User` (`users_api_show`) to `User`.
- Archive with `/opsx:archive` after review.
