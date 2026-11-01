# Tasks

## 1. Correct the `@model` docs (canvas-lms fork)

- [x] 1.1 Copy the current `public/doc/openapi/canvas.openapi.yaml` to the scratchpad as the pre-change baseline. Verify that the copy exists.
- [x] 1.2 Edit the polling `@model` blocks as in design D1, D3 and D4:
  - `Poll`: `id` and `user_id` become `string`.
  - `PollChoice`: `id` and `poll_id` become `string`, and `poll_id` is removed from `required`.
  - `PollSession`: `id`, `poll_id`, `course_id` and `course_section_id` become `string`, and `poll_submissions` becomes an array of `PollSubmission`.
  - `PollSubmission`: `id`, `poll_choice_id` and `user_id` become `string`, and `required` becomes `["id", "poll_choice_id"]`.

  Use string examples for the changed fields. Verify that each edited block still parses as JSON (strip the leading `#` and run it through `JSON.parse` in the web container).
- [x] 1.3 Edit `QuizSubmission` (`score`, `kept_score`, `score_before_regrade`, `fudge_points`) and `Quiz` (`points_possible`) to `"type": "number"`, as in design D2. Verify the JSON parse the same way as 1.2.
- [x] 1.4 Regenerate the spec (`bundle exec rake doc:openapi` in the web container). Diff it against the 1.1 baseline: only the `Poll`, `PollChoice`, `PollSession`, `PollSubmission`, `QuizSubmission` and `Quiz` component schemas may differ, and each difference must be one of the edits above.

## 2. Seed poll submissions (canvas-lms fork)

- [x] 2.1 In `spec/manual_seeding/large_gradebook_seeds.rb`, extend `create_polls` (or add a helper) to publish the poll session and create one `Polling::PollSubmission` for each of the first 3 students, as in design D5. Verify by running the script (`bin/rails runner spec/manual_seeding/large_gradebook_seeds.rb` in the web container). Then check that `GET /api/v1/polls/<new id>/poll_sessions` as the admin returns a session whose `poll_submissions` has 3 entries.
- [x] 2.2 Run `bin/rubocop` on the 6 edited controllers and the seed script. Verify that it introduces no new offense types compared with HEAD (the seed script's existing `Rails/Output` pattern is acceptable).
  - (Result:) No new offense types from this change. The new seed code adds only `Rails/Output` (consistent with the script). `Lint/UnusedBlockArgument` and `Style/OptionalBooleanParameter` come from earlier uncommitted edits to the seed script.
- [x] 2.3 Commit in the fork following its commit guidelines. Verify with `git log -1 --stat`: only the six controllers and the seed script are changed, and the diff is comments plus seed code.
  - (Amended, per user:) Commit only the six controllers; `large_gradebook_seeds.rb` stays uncommitted. Committed as canvas-lms `4146c58c2bb` (6 controllers, comments only).

## 3. Regenerate and test the client (canvas-lms-python-client)

- [x] 3.1 Regenerate the client (delete the generated `test_*_api.py` files first, as in `type-wrapped-paginated-responses` D3). Verify:
  - `Poll.id` is `StrictStr`.
  - `PollChoice.poll_id` is `Optional`.
  - `PollSession.poll_submissions` is `Optional[List[PollSubmission]]`.
  - `QuizSubmission.score` and `Quiz.points_possible` accept floats.
  - No other model files change.
- [x] 3.2 Add an offline parametrized test (in `test_paginated_response_types.py`) that deserializes live-shaped payloads, captured from the seeded instance, for `Poll`, `PollChoice`, `PollSession` (with `poll_submissions` both `[]` and one submission), `QuizSubmission` (float scores) and `Quiz` (float `points_possible`). Update the minimal items for the polling wrappers to string ids. Verify that the tests pass. Then verify they fail against the pre-change model types by temporarily checking out the old `models/poll.py` and confirming a failure, and revert.
- [x] 3.3 In `test_integration_paginated_models.py`:
  - Let `assert_typed` take the expected `id` type.
  - Make `test_polls_pages_typed` expect `str`.
  - Add `test_poll_choices_pages_typed` and `test_poll_sessions_pages_typed`, the latter asserting `poll_submissions` items are `PollSubmission` with string ids.

  Verify with `pdm run pytest --integration -m integration -v` that the polls, poll choices, poll sessions and quiz submissions tests pass against the seeded instance with no `ValidationError`.
- [x] 3.4 Add a line to the README "Breaking changes" section: polling ids are strings, and quiz scores and points are floats. Verify by reading the rendered section.
- [x] 3.5 Run the full offline suite (`pdm run pytest`) and `pdm run ruff check` / `ruff format --check` on the two custom test files. Verify that everything passes.
- [x] 3.6 Run `openspec validate fix-polling-and-quiz-model-types --strict` and verify that it passes.

## Workflow follow-up

- Archive `type-wrapped-paginated-responses` before this change (it depends on that change's uncommitted client work).
- Commit the client after the fork commit (task 2.3).
- Follow-ups:
  - audit other `@model` docs for int-vs-string and int-vs-float errors
  - document `has_submitted` and `poll_session_id`
  - seed rubrics, appointment groups and LTI tools so the remaining integration tests stop skipping
- Archive with `/opsx:archive` after review.
