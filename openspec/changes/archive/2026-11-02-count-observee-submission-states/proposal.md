# Proposal

## Why

An observer, such as a parent, needs to see how each observed student's work stands: how many submissions are submitted, graded, unsubmitted or pending review. The client can't answer that today. Its `Submission` model has only `id` and `student_entered_score`, so `workflow_state` and every other submission field Canvas sends is dropped.

The cause is that Canvas documents `@model Submission` in three controllers: submissions, what-if grades, and the LTI plagiarism detection API. The spec generator keeps the last definition it reads, which is the two-field what-if model. No integration test covers observee submissions, so the gap went unnoticed.

## What Changes

- **Controller docs (canvas-lms fork), one upstreamable commit:**
  - `what_if_grades_api_controller.rb`: `@model Submission` becomes `@model WhatIfSubmission`, and its update `@returns` references `WhatIfSubmission`.
  - `lti/submissions_api_controller.rb`: `@model Submission` becomes `@model Lti::Submission`. No `@returns` references it.
  - `submissions_api_controller.rb`: the full `Submission` model gains its missing `id` (integer). The partial what-if model was the only one that had it.

  The full 29-field `Submission` then becomes the client's `Submission`, including `workflow_state` with its documented values `graded`, `submitted`, `unsubmitted` and `pending_review`.
- **Seed script (fork, never committed):** a new `--observee-states` option on `spec/manual_seeding/large_gradebook_seeds.rb`. For every existing observer link, it gives the observee submitted, graded and unsubmitted submissions in one of their courses, and a pending-review one where the seeded data allows. It's idempotent, so existing observer tokens (`CANVAS_API_TOKEN`) see the new states without reseeding.
- **Client integration test** in `test/custom/integration/test_observees.py`:
  - list the observer's observees, then each observee's courses
  - in each course, list that observee's submissions (`submissions_api_for_students_all` with `student_ids=[observee]`) across several pages
  - count submissions by `workflow_state` for each observee
  - check that every state is a documented value, that the counts add up to the submissions listed, that no submission is listed twice, and that at least one observee has more than one state
- **Client unit test:** a captured observee submissions payload deserializes into `Submission` models that keep `workflow_state` and the other fields Canvas sent.
- **BREAKING (client):**
  - `Submission` gains the full field set.
  - `WhatIfGradesApiUpdateResponse.submission` becomes a `WhatIfSubmission`.
  - A new `LtiSubmission` model is added.
  - The client has never been released, so this isn't documented.
- **Out of scope:** the other 13 duplicated `@model` names (for example `Account`, `File`, `Progress` and `Result`), and making the generator warn about duplicates. Both are recorded as follow-ups.

## Capabilities

### New Capabilities
<!-- None. -->

### Modified Capabilities
- `observee-academic-data`: adds that an observer can list each observee's submissions in a course as typed submission models carrying `workflow_state`, and count them by state.

## Impact

- **canvas-lms (fork):**
  - Docs only: `app/controllers/submissions_api_controller.rb`, `app/controllers/what_if_grades_api_controller.rb`, `app/controllers/lti/submissions_api_controller.rb`.
  - Not committed: `spec/manual_seeding/large_gradebook_seeds.rb` and the regenerated `public/doc/openapi/canvas.openapi.yaml`.
- **canvas-lms-python-client:**
  - Regenerated `models/submission.py`, new `models/what_if_submission.py` and `models/lti_submission.py`, the what-if wrapper, and `api/` docstrings.
  - `test/custom/integration/test_observees.py`.
  - A new unit test and fixture under `test/custom/unit/`.
- The untracked `scripts/openapi-client-integration-tests-large_gradebook_seeds.rb` copy in the client repo isn't edited and will fall behind the fork's seed script.
