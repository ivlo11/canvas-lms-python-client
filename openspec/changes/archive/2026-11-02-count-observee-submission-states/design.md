# Design

## Context

- Motivation: see proposal.md, "Why". Requirements: `specs/observee-academic-data/spec.md`.
- **Model collection:** `CanvasAdapter.collect_model_schemas!` parses every controller and stores each `@model` under its sanitized name (`@canvas_schemas[name] = schema`). A later definition with the same name overwrites the earlier one without a warning.
  - Of 259 `@model` names, 14 are defined more than once.
  - `Submission` is defined in `submissions_api_controller.rb` (29 properties, no `id`), `lti/submissions_api_controller.rb` (13) and `what_if_grades_api_controller.rb` (2: `id`, `student_entered_score`).
  - The spec and the client currently hold the what-if definition.
- **Where each definition is used:**
  - The what-if `Submission` is referenced only by `what_if_grades#update`'s `@returns {"grades": [Grades], "submission": Submission}`. Its render is `submission: { id:, student_entered_score: }`.
  - The LTI plagiarism detection API isn't in the generated spec, and no `@returns` references its `Submission`.
  - Every other `Submission` reference (`@returns [Submission]` across the submissions API, `Grades`-adjacent docs and similar) means the full model.
- **Observer access (live, seeded instance):**
  - The observer token sees 1 observee (168), with 1 course (5).
  - `GET /api/v1/courses/5/students/submissions?student_ids[]=168` returns 50 submissions, all `unsubmitted`.
  - Each has 26 keys, including `id` (int), `assignment_id`, `user_id`, `workflow_state` and `submission_type` (null).
  - The client exposes this as `SubmissionsApiApi.submissions_api_for_students[_all|_paginated]`, returning `List[Submission]`.
- **The full model's enums:** `workflow_state` (`graded|submitted|unsubmitted|pending_review`), `submission_type` (six values) and `read_status`. The generated pydantic validators reject values outside an enum. `None` is accepted because the fields are optional.

## Goals / Non-Goals

**Goals:**
- `Submission` in the client is Canvas's full submission model.
- A live test of observer, observees, courses, submissions and the state counts, with seeded data covering several states.

**Non-Goals:**
- The other 13 duplicated model names, and a generator-level duplicate guard (follow-ups).
- Changing the full `Submission` model beyond adding `id`.
- Typing `grouped=true` responses.

## Decisions

### D1: Rename the partial models; the full one keeps the name
- `what_if_grades_api_controller.rb`: `@model Submission` / `"id": "Submission"` become `WhatIfSubmission`, and `update`'s `@returns` uses `"submission": WhatIfSubmission`.
- `lti/submissions_api_controller.rb`: becomes `@model Lti::Submission` (`"id": "Lti::Submission"`), following the namespaced model names the LTI controllers already use (`Lti::Deployment`, `Lti::Registration`). The generator sanitizes it to `Lti_Submission`.
- Upstream, Canvas's HTML docs index models by tag name, so the full model's anchor (`submissions.html#Submission`) is unchanged and only the two partial models' anchors move.
- *Alternative: a generator rule (keep the largest, or namespace by controller).* That's a larger change. It wouldn't fix upstream's own docs, where these definitions also collide, and it was deferred by decision.
- *Alternative: delete the partial models.* The what-if response really is a two-field object, and its `@returns` needs a model.

### D2: Add `id` to the full `Submission`
`"id": { "description": "The submission's id", "example": 1, "type": "integer" }`, because Canvas sends an integer `id` (live). Without it, D1 would drop `id` from the client's `Submission`.

### D3: Seed varied states for existing observees (`--observee-states`)
Add a `CreateHelpers.vary_observee_submission_states` helper, run by a new `--observee-states` option that skips the bulk course creation, so it can be run on its own:
- For each active `UserObservationLink` on the account, pick one of the student's active courses that has assignments.
- If the student already has at least one `graded` and one `submitted` submission there, skip it. That makes reruns idempotent.
- Otherwise:
  - Submit 2 assignments (`assignment.submit_homework(student, submission_type: "online_text_entry", body: ...)`) → `submitted`.
  - Grade 1 of them (`assignment.grade_student(student, grade: ..., grader: course teacher)`) → `graded`.
  - Leave the rest `unsubmitted`.
- **Pending review, where feasible:** add an essay-question quiz to that course, then generate and complete a submission for the student. An ungraded essay leaves the quiz's assignment submission `pending_review`. If that state doesn't come out, record it and continue; the test doesn't require `pending_review`.

It runs with `bin/rails runner spec/manual_seeding/large_gradebook_seeds.rb --observee-states` in the web container. It's never committed (per the standing rule).
- *Alternative: seed new observers.* `CANVAS_API_TOKEN` belongs to an existing observer, so new links wouldn't be visible to the test without changing the environment.

### D4: The test
Add `test_observee_submission_workflow_states(canvas_api_client)` to `test/custom/integration/test_observees.py`, reusing `list_observees` and `list_courses`:
- For each observee and course: `collect(SubmissionsApiApi(c).submissions_api_for_students_all(course_id=..., student_ids=[str(observee.id)], per_page=10))`. A small `per_page` makes 50 submissions span 5 pages.
- Assert that each item is a `Submission`, that `user_id == observee.id`, and that ids are unique per observee.
- Build `counts[observee.id] = Counter(s.workflow_state for s in submissions)`. Assert that each sum equals that observee's number of submissions, and that every key is in the documented set.
- If no observee has two or more states, `pytest.skip` with the seeded-data reason. Otherwise assert it.
- Print the per-observee counts (shown with `-s` / `-v`), so the run reports them.

### D5: Offline payload test
Save the observee submissions response from the seeded instance, after D3, to `test/custom/unit/fixtures/submissions/observee_submissions.json`. Add `test/custom/unit/test_submission_model.py`, which deserializes each item with `Submission.from_dict` and asserts that `workflow_state`, `assignment_id`, `user_id`, `submitted_at` and `grade` equal the JSON. This catches a model regression, such as another collision, without needing Canvas.

### D6: One upstream-format commit
The commit contains only the three controller files, in `CONTRIBUTING.md` format plus the fork's rules (lines under 60 characters, `flag=none`, `Test Plan:`). It's not a PR.

## Risks / Trade-offs

- [The full model's enums reject a real value. Seeded `online_text_entry` is in the list; others such as `basic_lti_launch` aren't] → The test and payload test would fail with a `ValidationError` naming the field. Record it as a follow-up (a doc correction for `submission_type`), rather than loosening the model here.
- [Renaming `Lti::Submission` while that API's other duplicate (`File`) still collides] → Out of scope; listed among the 13 follow-ups.
- [The seed changes grades in a dummy dev course] → Acceptable for seeded data; the change is idempotent.
- [Upstream reviewers prefer other names than `WhatIfSubmission` / `Lti::Submission`] → Doc-only, so it's easy to rename at review time.

## Migration Plan

1. Fork: seed (uncommitted) and capture the payload, edit the docs, regenerate (uncommitted), check the spec diff, then commit the controllers.
2. Client: regenerate, add the tests, run the offline and integration suites, then commit.

Rollback: revert both commits.
