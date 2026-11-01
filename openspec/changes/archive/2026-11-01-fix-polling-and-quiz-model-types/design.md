# Design

## Context

- See proposal.md "Why". The requirement is in `specs/paginated-list-responses/spec.md`.
- `@model` blocks are JSON in controller comments. `CanvasAdapter.convert_canvas_schema_to_openapi` copies `type` and `format` straight into the component schema, and turns `"$ref": "X"` and `"items": {"$ref": "X"}` into component `$ref`s. Array-of-`$ref` properties already work (for example `HelpLinks.custom_help_links`). The generated pydantic models map `integer` → `StrictInt`, `string` → `StrictStr`, and `number` → `Union[StrictFloat, StrictInt]`.
- **Polling serializers** (`app/serializers/polling/*`) inherit `Canvas::APISerialization`, whose `stringify_ids?` always returns `true`. `StringifyIds` therefore converts `id` and every `*_id` attribute to a string on every request, whatever `Accept` header is sent. `PollChoiceSerializer` declares `has_one :poll, embed: :id`, but its `filter` returns only `id`/`text`/`position`/`is_correct`, so neither `poll_id` nor `links.poll` is ever sent. `PollSessionSerializer#poll_submissions` maps the submissions to serializers, so it is always an array.
- **Quiz scores and points** are `float` columns: `quiz_submissions.score`, `kept_score`, `score_before_regrade`, `fudge_points`, `quiz_points_possible` (already documented as number), and `quizzes.points_possible`. They serialize as JSON floats (`0.0`, `10.0`).
- Live evidence: seeded course 6, poll 1 and quiz 1, from the `type-wrapped-paginated-responses` 4.1 results.

## Goals / Non-Goals

**Goals:**
- Make the six `@model` docs describe the JSON Canvas sends, so the strict generated models accept real responses.

**Non-Goals:**
- Changing serializers or any Canvas runtime behavior.
- Loosening the client templates (for example, coercing numeric strings to ints).
- Auditing `@model` docs beyond these six. That is a follow-up.

## Decisions

### D1: Correct the docs to the wire types, not the database types
Ids from the polling endpoints are documented as `"type": "string"`, even though the columns are bigint, because callers receive strings. Examples change to string form (`"1023"`).
- *Alternative: send ints by having the polling serializers stop stringifying.* That changes Canvas behavior for existing consumers (Canvas's own polling apps), and we don't own canvas-lms.
- *Alternative: make the client coerce numeric strings to int* (non-strict types, or a custom template). That hides real doc errors and diverges from the generated contract used elsewhere.

### D2: Floats are `"type": "number"`
`score`, `kept_score`, `score_before_regrade` and `fudge_points` on `QuizSubmission`, and `points_possible` on `Quiz`, become `number`. This matches the existing `QuizSubmission.quiz_points_possible`. `number` generates `Union[StrictFloat, StrictInt]`, so integer values still validate.
- The four `QuizSubmission` score fields also declared `"format": "int64"`, which contradicts `number`, so that line is removed from them. (Amended during implementation.)
- `score_before_regrade` and `fudge_points` were null in the live sample. They are included because they are float columns serialized the same way, so the next non-null value would fail.

### D3: Required lists describe what is always present
- Remove `poll_id` from `PollChoice.required`. The property stays documented (as `string`) because the model describes the resource, but it is not guaranteed in responses.
- `PollSubmission.required` changes from `["id", "poll_choice"]`, which names a non-existent property, to `["id", "poll_choice_id"]`. The serializer always emits `poll_choice_id`.
- *Alternative: delete `PollChoice.poll_id` entirely.* That is more accurate for today's serializer, but it removes documentation of a real relationship. Making it optional is the smaller, safer correction.

### D4: `poll_submissions` is an array
`PollSession.poll_submissions` becomes `{"type": "array", "items": {"$ref": "PollSubmission"}}`, and its description is kept.

### D5: Verification uses live, seeded data
- **Seed.** `large_gradebook_seeds.rb` publishes the seeded poll session and creates one `PollSubmission` for each of the first 3 students. A teacher or owner can view the results, so the admin, who owns the poll, sees the submissions.
- **Integration tests:**
  - `test_polls_pages_typed` asserts string `id`. (`assert_typed` currently checks for an int `id`, so it gains an `id_type` parameter.)
  - New `test_poll_choices_pages_typed` and `test_poll_sessions_pages_typed` follow the seeded poll from `polls_index_paginated`.
  - `test_quiz_submissions_pages_typed` passes once `Quiz` and `QuizSubmission` are fixed.
- **Offline tests:** a parametrized test feeds each corrected model the live-shaped JSON captured from the seeded instance (string ids, `poll_submissions: []` and one submission, float scores), so the type corrections are pinned without a live Canvas.

## Risks / Trade-offs

- [Other fields in these models are also wrong but weren't exercised, for example `PollSession.results` key types] → The offline payloads use the full live responses, so any extra mismatch surfaces at task time. If it does, add it to this change (same models, same rationale) and record it.
- [Regeneration churn outside the six schemas] → Diff the spec against the pre-change copy. Only the six schemas should change.
- [String ids break callers that compared poll ids to ints] → The client is unpublished. The README "Breaking changes" note gains a line about it.

## Migration Plan

1. Fork: doc edits and seed edit, `rake doc:openapi`, run the seed, commit.
2. Client: regenerate, update tests, and run the offline and integration suites. Commit together with or after `type-wrapped-paginated-responses`.

Rollback: revert both commits. The seeded rows can stay; they are test data.
