# Proposal

## Why

The Canvas docs for grading period sets and quiz submission events don't match what those endpoints return, so the client can't type them:
- `grading_period_sets_index` and `quiz_submission_events_api_index` are on the undocumented allowlist and return nothing typed.
- Grading period set creation is typed as a list, but Canvas returns one object.
- The documented `QuizSubmissionEvent.event_data` is an object, but Canvas sends an array for answered questions. That would fail validation as soon as the endpoint is typed.

These are pure doc defects in Canvas, so the fix is written to be upstreamable to instructure/canvas-lms.

## What Changes

- **Controller docs (canvas-lms fork), written to be upstreamable:**
  - Grading period sets:
    - index gets `@returns { "grading_period_sets": [GradingPeriodSets] }`
    - create gets `@returns { "grading_period_set": GradingPeriodSets }`
    - both examples use the correct keys, shape and model name
    - the `GradingPeriodSets` model gains the fields Canvas sends: `id`, `account_id`, `course_id`, `grading_periods`, `permissions`, `created_at`
    - the `@model GradingPeriodSets` name is kept, and `meta` stays undocumented
  - Quiz submission events:
    - index gets `@returns { "quiz_submission_events": [QuizSubmissionEvent] }`, and its example with sample values is kept
    - `QuizSubmissionEvent` gains `id`
    - `event_data` loses its `object` type, and its description says the shape depends on `event_type`
  - `GradingPeriod` is corrected to the types Canvas sends (live check, below): `id` becomes a string, `weight` a number, and it gains `grading_period_group_id` and `permissions`.
  - Courses (`courses_controller.rb`, docs only): a new `@model CourseGradingPeriod` (`id` integer, `title`, `start_date`, `end_date`, `workflow_state`) documents the course's `include[]=grading_periods` shape, and `Course.grading_periods` references it instead of `GradingPeriod`.
- **Seed script (fork, never committed):** `spec/manual_seeding/large_gradebook_seeds.rb` seeds a grading period set with grading periods, enables `quiz_log_auditing` on the seeded course, and records quiz submission events whose `event_data` is an array, an object and null. That makes the nested id types and the `event_data` shapes checkable against live Canvas.
- **One fork commit** with only the four controller files, in upstream `CONTRIBUTING.md` format that also meets the fork's commit rules. No PR is opened. The regenerated `canvas.openapi.yaml` and the seed script are never committed.
- **Client:** regenerate. `grading_period_sets_index` and `quiz_submission_events_api_index` come off the undocumented allowlist and yield typed wrapper pages. `grading_period_sets_create` returns a wrapper holding one set.
- **BREAKING (client):** `grading_period_sets_create` no longer returns a list. `GradingPeriod.id` becomes a string, and `Course.grading_periods` items become `CourseGradingPeriod`. The client has never been released and has no consumers, so this isn't documented.

## Capabilities

### New Capabilities
<!-- None. -->

### Modified Capabilities
- `paginated-list-responses`: adds that grading period set and quiz submission event pages are typed and deserialize live Canvas data, including every `event_data` shape.
- `typed-operation-responses`: adds that creating a grading period set returns the created set as an object.

## Impact

- **canvas-lms (fork):**
  - `app/controllers/grading_period_sets_controller.rb` and `app/controllers/quizzes/quiz_submission_events_api_controller.rb` (docs only), plus `app/controllers/grading_periods_controller.rb` (`GradingPeriod` types) and `app/controllers/courses_controller.rb` (the new `CourseGradingPeriod` model and the `Course.grading_periods` `$ref`).
  - Not committed: `spec/manual_seeding/large_gradebook_seeds.rb`, the regenerated `public/doc/openapi/canvas.openapi.yaml`.
  - No generator changes. This relies on the inline-object `@returns` support from the archived `type-inline-returns-objects`.
- **canvas-lms-python-client:**
  - Regenerated `api/grading_period_sets_api.py`, `api/quiz_submission_events_api.py`, the `GradingPeriodSets` and `QuizSubmissionEvent` models, the `GradingPeriod` and `Course` models, a new `CourseGradingPeriod` model, and new wrapper models (`GradingPeriodSetsIndexResponse`, `GradingPeriodSetsCreateResponse`, `QuizSubmissionEventsApiIndexResponse`).
  - `test/custom/unit/test_paginated_response_types.py`: the two operations come off the allowlist, and the wrapper table gains entries.
  - `test/custom/integration/test_paginated_models.py`: new live tests.
- **Upstream:** the fork commit is ready to cherry-pick onto instructure/canvas-lms `master`. Signing the CLA and opening the PR are left to the user.
