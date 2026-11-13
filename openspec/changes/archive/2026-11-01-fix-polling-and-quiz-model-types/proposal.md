# Proposal

## Why

With seeded data, the live integration tests for `type-wrapped-paginated-responses` showed that wrapper pages deserialize correctly but their items do not. Several Canvas `@model` docs declare field types that don't match what Canvas actually sends:
- Polling endpoints send every id as a string.
- Quiz scores and points are floats.
- `PollSession.poll_submissions` is an array, not a single object.

The client's strict pydantic models follow those docs, so they reject the real data, and `polls_index_paginated` and `quizzes_api_index_all` raise `ValidationError`. The models are already strict, so the fix is to correct the docs so they describe what Canvas sends. Loosening the models is not the fix.

## What Changes

- **canvas-lms fork, `@model` docs only.** Correct the field types in six controller doc blocks so they match what Canvas actually sends:

  | Model (controller) | Field(s) | Documented | Actual (evidence) |
  |---|---|---|---|
  | `Poll` (`polling/polls_controller.rb`) | `id`, `user_id` | integer | string. The polling serializers always stringify `id` and `*_id` (`Canvas::APISerialization#stringify_ids?` returns `true`). |
  | `PollChoice` (`polling/poll_choices_controller.rb`) | `id`, `poll_id` | integer | string |
  | `PollChoice` | `poll_id` in `required` | required | never sent. The serializer's `filter` drops the `poll` link, and live listings omit it. |
  | `PollSession` (`polling/poll_sessions_controller.rb`) | `id`, `poll_id`, `course_id`, `course_section_id` | integer | string |
  | `PollSession` | `poll_submissions` | `$ref PollSubmission` | an array of `PollSubmission` (the serializer maps the submissions; live: `[]`) |
  | `PollSubmission` (`polling/poll_submissions_controller.rb`) | `id`, `poll_choice_id`, `user_id` | integer | string |
  | `PollSubmission` | `required: ["id", "poll_choice"]` | names a property that doesn't exist | `["id", "poll_choice_id"]`. The serializer always sends `poll_choice_id`. |
  | `QuizSubmission` (`quizzes/quiz_submissions_api_controller.rb`) | `score`, `kept_score`, `score_before_regrade`, `fudge_points` | integer | number (float columns; live `0.0`) |
  | `Quiz` (`quizzes/quizzes_api_controller.rb`) | `points_possible` | integer | number (float column; live `10.0`) |

  Descriptions and examples are updated to match, for example `"example": "1023"` for string ids. No Ruby code changes, and Canvas runtime behavior does not change.
- Regenerate `public/doc/openapi/canvas.openapi.yaml` and the client.
- **BREAKING (client types):** the affected polling id fields change from `StrictInt` to `StrictStr`, and the affected quiz score and points fields change from `StrictInt` to `StrictFloat`/`float`. The client has never been published, so `packageVersion` is not bumped.
- **Seed data:** extend `spec/manual_seeding/large_gradebook_seeds.rb` to publish the seeded poll session and add poll submissions from a few students, so `PollSession.poll_submissions` items are covered by live data.
- **Client tests:**
  - Update `test_polls_pages_typed` to expect string poll ids.
  - Add integration coverage for poll choices and poll sessions (including their submissions).
  - Add offline tests that deserialize realistic payloads for each corrected model.

## Capabilities

### New Capabilities
<!-- None. -->

### Modified Capabilities
- `paginated-list-responses`: adds one requirement. Typed items from documented list and wrapper responses must deserialize the data Canvas actually sends, including string ids from the polling endpoints and fractional scores. Existing requirements are unchanged.

## Impact

- **canvas-lms (fork):** comment-only edits to the six controllers listed above, plus the seed script. The regenerated spec changes only these six component schemas.
- **canvas-lms-python-client:**
  - Regenerated models `poll.py`, `poll_choice.py`, `poll_session.py`, `poll_submission.py`, `quiz_submission.py`, `quiz.py`, and their docs.
  - Tests: `test_integration_paginated_models.py` (poll id type, new poll choice and poll session tests). `test_paginated_response_types.py`: the minimal items for `PollChoicesResponse`, `PollSessionsResponse` and `PollsResponse` become live-shaped payloads.
- **Depends on** `type-wrapped-paginated-responses`. That change's client work, seed-script edit and integration tests are uncommitted, and this change builds on them. Archive that change first, or apply this one on the same uncommitted working tree.
- **Out of scope (follow-ups):**
  - Auditing every other `@model` for the same int-vs-string or int-vs-float mistakes. Other JSON-API serializers, and other `score`/`points` fields documented as integer, are likely candidates.
  - Undocumented keys that Canvas sends (`has_submitted` on poll sessions, `poll_session_id` on poll submissions). Strict models drop them, the same as today.
  - The rubric, appointment group and LTI integration tests still skip for lack of seed data.
