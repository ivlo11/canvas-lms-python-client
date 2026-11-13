# Design

## Context

- Motivation: see proposal.md, "Why". Requirements: `specs/student-academic-data/spec.md` and `specs/integration-testing/spec.md`.
- **What Canvas sends.** This is the course list with `include[]=total_scores&include[]=current_grading_period_scores`, captured live for student 168, course 5, using the admin token. Each item in `enrollments` carries:
  - `computed_current_score` and `computed_final_score` (floats: 80.0 and 1.57)
  - `computed_current_grade` and `computed_final_grade` (null, because the course has no grading scheme)
  - `unposted_*_score` (floats), with `unposted_*_grade` null
  - eight `current_period_*` fields (null, with no grading periods)
  - `multiple_grading_periods_enabled`

  `courses_controller.rb` documents these fields in prose, "see Enrollment documentation", but the `Enrollment` `@model` lacks the `computed_*` and `current_period_computed_*` fields. It types `unposted_current_score`/`unposted_final_score` as `string`, while `current_period_unposted_*_score` are `number`.
- **The live failure:** deserializing that payload as `List[Course]` with today's client raises `ValidationError: unposted_final_score Input should be a valid string … input_value=1.57`. Callers with permission to see unposted scores (teachers, admins) can't list courses with total scores. Students normally don't get the `unposted_*` fields, but the same model has to serve every role.
- **`Grade` collision:**
  - `enrollments_api_controller.rb` and `what_if_grades_api_controller.rb` both define `@model Grade`, and the generator keeps the last one (what-if: `grade`, `total`, `possible`, `dropped`).
  - `Enrollment.grades` and the what-if `Grades.current`/`final` both reference `Grade`.
  - The what-if `Grade` is referenced only by `Grades` (two `$ref`s).
- **Letter grades:** Canvas computes `computed_current_grade` with `course.score_to_grade`, which returns nil unless `grading_standard_enabled?` is true. `course.grading_standard_enabled = true` sets `grading_standard_id ||= 0`, which selects Canvas's default scheme.
- **Test harness:** `test/custom/conftest.py` has `canvas_api_client` (observer) and `canvas_admin_api_client` (skips without `CANVAS_ADMIN_API_TOKEN`). The client method is `CoursesApi.courses_index_all(include=[...])`, with `include` sent as `include[]=` (from the array query parameter fix).
- **Dependencies:**
  - `seed-student-and-second-admin-tokens` (not yet applied) creates the student token. Its default student is the oldest observer link's observee, expected to be 168.
  - `count-observee-submission-states` already renamed the what-if `Submission` in the same controller.

## Goals / Non-Goals

**Goals:**
- A student-token integration test that proves courses and `computed_current_grade` come back typed and non-null.
- `Enrollment` and `Grade` models that match Canvas for every role, so the course list never fails to deserialize.

**Non-Goals:**
- The remaining 12 duplicated `@model` names, and a generator duplicate guard (follow-ups).
- Documenting `multiple_grading_periods_enabled` (deprecated upstream naming). It stays dropped.
- A full audit of the `Enrollment` model's other field types.

## Decisions

### D1: `Enrollment` model additions and type fixes
Add the following, with descriptions taken from `courses_controller.rb`'s `total_scores`/`current_grading_period_scores` text:
- `computed_current_score`, `computed_final_score`, `current_period_computed_current_score` and `current_period_computed_final_score`, as `number`
- `computed_current_grade`, `computed_final_grade`, `current_period_computed_current_grade` and `current_period_computed_final_grade`, as `string`

Change `unposted_current_score` and `unposted_final_score` to `number`, matching their `current_period_` counterparts. The enrollments `Grade` model types `current_score`, `final_score`, `unposted_current_score` and `unposted_final_score` as `string` too, while Canvas sends floats; once D2 makes it the client's `Grade`, `enrollments_with_grades.json` would fail, so those four become `number` as well (found during apply). All of them stay optional, because Canvas omits them unless `total_scores` is requested, and omits `unposted_*` without permission.
- *Alternative: a separate `CourseEnrollment` model for the course include.* That's more accurate, but upstream already points readers to `Enrollment`, and it's a larger doc change.

### D2: Rename the what-if `Grade` to `WhatIfGrade`
Rename `@model Grade` / `"id": "Grade"` to `WhatIfGrade` in `what_if_grades_api_controller.rb`, and update `Grades.current`/`final` `$ref`s. Same pattern and rationale as `WhatIfSubmission`: the enrollments model keeps the public name and upstream anchor. The edit goes next to the existing `WhatIfSubmission` change.

### D3: Seed `--grading-scheme`
Add `CreateHelpers.enable_grading_scheme(student:)`, run by a standalone `--grading-scheme` option (honouring `--student-id`, with the same default student as `--tokens`):
- For each active student course: `course.update!(grading_standard_enabled: true)` if it isn't already enabled.
- Print each course and its resulting `computed_current_grade`, read back from `enrollment.computed_current_grade`.

It's idempotent. Scores are already computed, so no recalculation is needed. The grade comes from the score at render time. It's never committed.

### D4: `canvas_student_api_client` fixture
Mirror `canvas_admin_api_client`: `canvas_student_api_token` (session) reads `CANVAS_STUDENT_API_TOKEN`. The client fixture skips with a reason naming each missing variable (`CANVAS_BASE_URL`, `CANVAS_STUDENT_API_TOKEN`), opens a `Configuration(host=..., access_token=...)` client, and closes it after the test.

README:
- add a row to the environment variable table
- add a sentence to the integration section: "student-scoped tests use `CANVAS_STUDENT_API_TOKEN`; printed by the seed script's `--tokens` option"

### D5: The integration test
New file `test/custom/integration/test_student_grades.py` (folder-marked as integration), with `test_student_courses_computed_grades(canvas_student_api_client)`:
- Call `courses_index_all(include=["total_scores"], per_page=10)` and collect the results. The test fails if the list is empty: the student has no courses.
- For each course, take the enrollments with `type == "student"` and `user_id` equal to the student, where `user_id` comes from `UsersApi.users_api_show(id="self")`. Assert that `computed_current_score` is `None` or a float, and `computed_current_grade` is `None` or a non-empty str.
- Assert that at least one course has a non-null `computed_current_grade` in Canvas's default scheme (`A`, `A-`, `B+` … `F`). If none does, skip with "no seeded course uses a grading scheme (run the seed script with --grading-scheme)", per the seeded-data rule.
- Print each course and its grade and score.

### D6: Offline payload tests
Fixtures in `test/custom/unit/fixtures/enrollments/`:
- `courses_total_scores.json`: the live course list for the seeded student, captured with the admin token so it includes `unposted_*`.
- `enrollments_with_grades.json`: `GET /courses/:id/enrollments?user_id=<student>` with the admin token, which carries `grades`.

`test/custom/unit/test_enrollment_grades.py` asserts:
- both fixtures deserialize without error
- `computed_*` and `unposted_*` scores equal the JSON as floats
- `enrollment.grades` is `Grade` with `current_score` and `html_url` equal to the JSON

Both fixtures are captured after D3, so `computed_current_grade` is non-null in them.

### D7: One upstream-format commit
The commit contains only `enrollments_api_controller.rb` and `what_if_grades_api_controller.rb`, in `CONTRIBUTING.md` format with the fork's rules. It's not a PR.

## Risks / Trade-offs

- [The `seed-student-and-second-admin-tokens` change isn't applied] → Task 1.1 checks that the token exists. Without it, the integration test skips and the rest of the change still lands.
- [Other `Enrollment` fields mismatch for other roles or courses] → The unit fixtures cover one student. Any new `ValidationError` in the integration run is recorded as a follow-up.
- [Enabling a grading scheme changes how the seeded course displays grades] → Dummy data; it's the setting being tested.
- [The default scheme's letters change in a Canvas version] → The test checks against the letters in the captured enrollment's scheme. Canvas's default scheme has been stable for years; a mismatch is reported clearly.

## Migration Plan

1. Fork: seed (uncommitted) and capture the fixtures, edit the docs, regenerate (uncommitted), check the diff, then commit the controllers.
2. Client: regenerate, add the fixture, conftest, tests and README, run the offline and integration suites, then commit.

Rollback: revert both commits, and disable the scheme from a Rails console if wanted.
