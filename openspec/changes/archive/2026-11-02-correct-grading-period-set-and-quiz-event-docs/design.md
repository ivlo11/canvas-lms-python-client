# Design

## Context

- Motivation: see proposal.md, "Why". Requirements: `specs/paginated-list-responses/spec.md` and `specs/typed-operation-responses/spec.md`.
- **The generator is ready.** `type-inline-returns-objects` (archived) turns a brace `@returns` whose entries are all `[Model]`, `Model`, a primitive or a literal into a `<Resource><Action>Response` wrapper with optional properties. Anything else becomes a plain object. This change only edits controller docs.
- **What Canvas returns,** from its code, its specs and the dev instance:
  - Grading period sets:
    - `GET /accounts/:id/grading_period_sets` returns `{ "grading_period_sets": [ ... ], "meta": { "pagination": { ... } } }` (live; Canvas spec `grading_period_sets_controller_spec.rb:46`).
    - `POST` returns `{ "grading_period_set": { ... } }` with status 201 (Canvas spec `:93`).
    - `update` and `destroy` return 204.
    - A set, from `GradingPeriodSetSerializer`, has `id`, `title`, `weighted`, `display_totals_for_all_grading_periods`, `account_id`, `course_id`, `grading_periods` (each a `GradingPeriodSerializer`), `permissions` and `created_at`. `stringify!` makes the set's own `*_id` values strings. Whether nested grading period ids are strings is **unverified**, because the seeded instance has no sets.
  - Quiz submission events:
    - `GET .../submissions/:id/events` returns `{ "quiz_submission_events": [ { "id": "<string>", "event_type", "event_data", "created_at" } ] }`, paginated by `Api.paginate`.
    - It returns 400 unless `quiz_log_auditing` (a course setting) is on.
    - It lists only events of the current attempt created after `started_at`.
    - `event_data` is a list of answers for `question_answered` (`log_auditing/event_aggregator.rb:109`), an object for `question_flagged` (`:80`), and null for page focus and blur events.
- **How Canvas's HTML docs read these tags** (`doc/api/documentation_helpers.rb:61`, `doc/api/tags/setup.rb#returns`):
  - Models are indexed by the `@model` tag's name, so the JSON `"id"` is ignored.
  - For `@returns`, the renderer takes the name inside `[...]` and links "Returns a list of X objects", or it links a bare `X`.
  - So the brace form renders a correct link upstream, and the HTML docs don't need generator support. **Apply finding:** only when the model sits inside `[...]`. A bare model in braces (`{ "grading_period_set": GradingPeriodSets }`) renders no Returns line, so create stays unlinked in the HTML docs, as it was before.
- Both controller files are identical to the local `upstream/master` ref (dated 2026-04-30).

## Goals / Non-Goals

**Goals:**
- Controller doc edits that are correct for upstream readers and that our generator types as written.
- Field types confirmed against live data, not inferred.

**Non-Goals:**
- Documenting `meta` (decided). Renaming `@model GradingPeriodSets` (decided).
- Generator changes, or a PR to instructure/canvas-lms (decided: commit only).
- The quiz submission events `create` (204) and the grading period set `update`/`destroy` (204) responses.

## Decisions

### D1: Doc text
Grading period sets controller:
```
index:   @returns { "grading_period_sets": [GradingPeriodSets] }
         @example_response  { "grading_period_sets": [GradingPeriodSets] }
create:  @returns { "grading_period_set": GradingPeriodSets }
         @example_response  { "grading_period_set": GradingPeriodSets }
```

Quiz submission events API controller, index:
```
@returns { "quiz_submission_events": [QuizSubmissionEvent] }   (example kept as is)
```

- `@returns` is added rather than relying on change 2's example inference. The tag documents the contract for upstream readers. It also lets the quiz events keep their sample-value example. And because change 2 only runs when there is no `@returns`, both endpoints take the same path.
- The grading period set examples are corrected anyway, because their singular key, list shape and `GradingPeriodGroup` reference are wrong for upstream readers.
- *Alternative: fix only the examples (change 2's path).* That leaves upstream without a return-type link, and the quiz example would lose its values.

### D2: `GradingPeriodSets` model fields, typed from live data
The model adds `id`, `account_id`, `course_id`, `grading_periods` (`"type": "array", "items": { "$ref": "GradingPeriod" }`), `permissions` (`object`) and `created_at` (`datetime`). The existing `"id": "GradingPeriodGroup"` JSON id is left as is: Canvas ignores it, and changing it is a rename in all but name.

Types come from task 1.2's live response, not from reading the code. The expectations are:
- `id` and `*_id`: string
- `account_id` / `course_id`: null on the other context
- `permissions`: a map of booleans

### D3: `GradingPeriod` corrected to the live types
Correct `GradingPeriod`'s `@model` in `grading_periods_controller.rb` to the types task 1.3 recorded, and include the file in the same commit. The nested set response and the grading period endpoints agree on every field:
- `id`: integer → string
- `weight`: integer → number (example `33.33`)
- add `grading_period_group_id` (string) and `permissions` (an object of booleans), which Canvas sends and the model lacks

Fields that already match are left alone. The course include's different shape moves to its own model (D7), so `GradingPeriod` can follow these endpoints.
- *Alternative: correct them from the serializer code.* `stringify!` applies to top-level keys, and nesting goes through a different path, so reading the code isn't conclusive.

### D4: `event_data` has no `type`
Remove `"type": "object"` from `QuizSubmissionEvent.event_data` and describe the shape per `event_type`.
- The adapter's `convert_property_type` returns early when there's no `type`, so the property has no schema type and the generator emits `Optional[Any]`. Task 2.3 verifies that.
- *Alternative: `"type": ["array", "object", "null"]`.* The adapter's union handling keeps only the first non-null type, so it would still reject one of the shapes.
- *Alternative: `"type": "array"`.* That's wrong for flagged events.

Add `"id": { "type": "string", ... }` to the model.

### D5: Seed additions (uncommitted)
Add two helpers to `spec/manual_seeding/large_gradebook_seeds.rb`, both called from the main flow:
- **`create_grading_period_set(account:)`:** find or create, by title, a `GradingPeriodGroup` on the root account with two `GradingPeriod`s (for example 60/40 weights, and at least one fractional weight such as 33.33 to expose `weight`'s type), linked to the default term. Find-or-create keeps reruns from multiplying sets. Linking it to the default term affects grading in the default term's courses, which is acceptable for a dummy dev instance.
- **`create_quiz_submission_events(course:, quiz_submission:)`:** enable `quiz_log_auditing` on the course, then create three `Quizzes::QuizSubmissionEvent`s on one seeded submission's current attempt, each with `created_at` after `started_at`:
  - `question_answered` with `[{ "quiz_question_id": "<id>", "answer": "1" }]`
  - `question_flagged` with `{ "quiz_question_id": "<id>", "flagged": true }`
  - `page_blurred` with `nil`

It's run as before (`bin/rails runner spec/manual_seeding/large_gradebook_seeds.rb` in the web container). The file is never committed, and neither is the regenerated spec.

### D6: One upstream-format commit
The commit contains only the controller files. Its message follows `CONTRIBUTING.md` (subject, why, `Test Plan:`) and the fork's `CLAUDE.md` rules:
- lines under 60 characters
- `flag=none`
- no JIRA key, since there's no ticket
- no `closes gh-…` unless the user files an issue

This makes it cherry-pickable onto upstream `master` unchanged.

### D7: Separate model for the course include
*Decided by the user after task 1.3.* `GradingPeriod` serves two shapes that can't share one type for `id`:
- `GradingPeriod` (nested in sets, `/accounts/self/grading_periods`, `/courses/:id/grading_periods`): `GradingPeriodSerializer`, with `id` and `grading_period_group_id` as strings and `weight` as a float.
- `Course.grading_periods` (`include[]=grading_periods`): `Api::V1::Course` renders `api_json(gp, only: %w[id title start_date end_date workflow_state])`. That gives an integer `id`, plus `workflow_state` and no `weight`, for every period in the term's set, deleted ones included.

So `courses_controller.rb` gains `@model CourseGradingPeriod` with those five fields, typed from the live capture:
- `id`: integer
- `title`: string
- `start_date` / `end_date`: datetime
- `workflow_state`: string

`Course.grading_periods.items` changes from `$ref GradingPeriod` to `$ref CourseGradingPeriod`. The edit is limited to that `$ref` and the new `@model` block. The full model keeps the public name `GradingPeriod`, and the partial shape gets its own model, following the `WhatIfSubmission`/`WhatIfGrade` precedent.
- *Alternative: a `string|integer` union for `GradingPeriod.id`.* That keeps one model, but the adapter only unions `string|Model`, and the course include would still be typed with fields it never sends.

## Risks / Trade-offs

- [Seeding a grading period set on the default term changes grade calculation in seeded courses] → Dummy data. The set is created once (find-or-create), and a set with only future or past periods could be used if it disturbs other integration tests.
- [Upstream reviewers object to the brace `@returns` form] → Canvas already uses it (`account_calendars_api`, `what_if_grades_api`), and its renderer links the model.
- [The live check finds nested types that differ between the set and grading periods endpoints] → `GradingPeriod` is one model, so a mismatch would need a union, which D3 doesn't cover. If it happens, record it and stop before editing `GradingPeriod`; it needs a decision. (It happened with the course include, not between those two endpoints, and was decided as D7.)
- [`event_data` as `Any` is untyped for callers] → It's correct for a field whose shape depends on `event_type`, and it's lossless.

## Migration Plan

1. Fork: seed and confirm the types, edit the docs, regenerate (not committed), check the spec diff, then make one commit with the controller files only.
2. Client: regenerate, update the tests, then commit.

Rollback: revert both commits.
