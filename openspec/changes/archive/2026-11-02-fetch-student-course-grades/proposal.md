# Proposal

## Why

A student, or an app acting as one, wants their courses with their current grade. Canvas returns this from the course list with `include[]=total_scores`, as `computed_current_grade` and `computed_current_score` on each of the student's course enrollments. The client can't deliver it, for three reasons:
- **The fields are dropped.** The `Enrollment` model doesn't document the `computed_*` fields, so the client discards them.
- **Deserialization fails.** `Enrollment.unposted_current_score` and `unposted_final_score` are documented as strings, but Canvas sends numbers. Deserializing a course list in which those fields are present raises a `ValidationError`. This was confirmed against a live payload, where `unposted_final_score=1.57`.
- **`Enrollment.grades` is the wrong model.** `@model Grade` is defined in both the enrollments and what-if grades controllers, and the what-if version (`grade`, `total`, `possible`, `dropped`) wins. That drops `current_grade`, `current_score` and the other enrollment grade fields.

No integration test authenticates as a student. The seeded student token comes from `seed-student-and-second-admin-tokens`.

## What Changes

- **Controller docs (canvas-lms fork), one upstreamable commit:**
  - `enrollments_api_controller.rb` `@model Enrollment`:
    - add `computed_current_score`, `computed_final_score`, `computed_current_grade`, `computed_final_grade` and the four `current_period_computed_*` fields
    - change `unposted_current_score` and `unposted_final_score` from string to number
  - `what_if_grades_api_controller.rb`: `@model Grade` becomes `@model WhatIfGrade`, and the `Grades` model's two `"$ref": "Grade"` become `WhatIfGrade`. The enrollments `Grade` (`html_url`, `current_grade`, `final_grade`, `current_score`, …) becomes the client's `Grade`.
- **Seed script (fork, never committed):** a new `--grading-scheme` option enables Canvas's default letter grading scheme on the seeded student's courses. Without a scheme, `computed_current_grade` is always null.
- **Client test harness:** a `canvas_student_api_client` fixture reads `CANVAS_STUDENT_API_TOKEN` and skips its tests when that variable is unset, like the admin fixture. The README documents the variable.
- **Client integration test** in `test/custom/integration/test_student_grades.py`:
  - list the student's courses (`courses_index_all` with `include=["total_scores"]`)
  - assert each is a `Course`
  - find the student's own enrollment
  - assert that `computed_current_grade` is a non-empty letter grade from the default scheme and `computed_current_score` is a number, in at least one course
  - assert that `grades.current_score` matches `computed_current_score` where both are present
- **Client unit test:** a captured course list with `total_scores` deserializes without error, keeps the `computed_*` and `unposted_*` values, and puts the full `Grade` in `Enrollment.grades`.
- **BREAKING (client):**
  - `Enrollment` gains fields, and its `unposted_*_score` fields become floats.
  - `Grade` becomes the enrollments grade model.
  - `Grades.current`/`final` become `WhatIfGrade`.
  - The client is unreleased, so this isn't documented.

## Capabilities

### New Capabilities
- `student-academic-data`: what a student-authenticated client can read about their own courses and grades.

### Modified Capabilities
- `integration-testing`: adds optional student credentials (`CANVAS_STUDENT_API_TOKEN`) for student-scoped integration tests.

## Impact

- **canvas-lms (fork):**
  - Docs only: `app/controllers/enrollments_api_controller.rb`, `app/controllers/what_if_grades_api_controller.rb`.
  - Not committed: `spec/manual_seeding/large_gradebook_seeds.rb` and the regenerated `public/doc/openapi/canvas.openapi.yaml`.
- **canvas-lms-python-client:**
  - Regenerated `models/enrollment.py`, `models/grade.py`, `models/grades.py`, a new `models/what_if_grade.py`, and docs.
  - `test/custom/conftest.py`, the new `test/custom/integration/test_student_grades.py`, and a new unit test and fixture.
  - `README.md`: the environment variable table and the integration section.
- **Dependencies:**
  - **Requires** `seed-student-and-second-admin-tokens` to be applied first, for the student token.
  - `count-observee-submission-states` (11/11 tasks done) also edits `what_if_grades_api_controller.rb` (`WhatIfSubmission`). This change's edit sits next to it and must be applied on top.
