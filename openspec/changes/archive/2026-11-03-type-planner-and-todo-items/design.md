# Design

## Context

- Motivation: see proposal.md, "Why". Requirements: `specs/paginated-list-responses/spec.md`.
- **`planner_item_json`** (`lib/api/v1/planner_item.rb`):
  - `context_data(item)`: `context_type` plus `<context>_id` (`course_id`, `group_id` or `user_id`, integer)
  - `plannable_id`, `planner_override` (`planner_override_json`, or nil), `plannable_type` (a key of `PlannerHelper::PLANNABLE_TYPES`: `discussion_topic`, `announcement`, `quiz`, `assignment`, `wiki_page`, `planner_note`, `calendar_event`, `assessment_request`, `sub_assignment`, `peer_review_sub_assignment`), `new_activity` (boolean)
  - `submissions`: `false`, or an object with `submitted`, `excused`, `graded`, `late`, `missing`, `needs_grading`, `has_feedback`, `redo_request`, …
  - per type, `plannable_date` (datetime), `plannable` (`plannable_json` of the record's raw attributes plus extra fields), `html_url`, and `context_name`/`context_image` where set
- **`todo_item_json`** (`lib/api/v1/todo_item.rb`):
  - `context_data`, `context_name`, `context_short_name`, `type` (`grading` or `submitting`), `ignore`, `ignore_permanently`, `html_url`
  - for quizzes, `quiz` (`quiz_json`)
  - otherwise `assignment` (`assignment_json` with all dates), plus `checkpoint_label` and `parent_assignment_id` for sub-assignments, and `needs_grading_count` for grading items
  - with the educator dashboard flag: `on_time_needs_grading_count`, `late_needs_grading_count`, `resubmitted_needs_grading_count`, `submitted_submissions_count`, `total_submissions_count`
- **Existing models:** `PlannerOverride`, `Assignment` and `Quiz` exist (`Quiz` was checked against live data earlier). `PlannerNote` exists, but `plannable` isn't a model of any one type.
- **Live data:** the admin's planner and todo lists are empty, and the admin isn't enrolled. Students have assignments, but whether any is due "soon" depends on seed dates.

## Goals / Non-Goals

**Goals:**
- Typed planner and todo envelopes, with typed `assignment`/`quiz` on todo items.

**Non-Goals:**
- Typing `plannable` per `plannable_type` (needs `oneOf` with a discriminator; follow-up).
- Typing `submissions` (a `false`-or-object union).
- Fixing other `Assignment` model fields beyond what this change's integration run breaks on.

## Decisions

### D1: `@model PlannerItem`
- `context_type`, `context_name`, `context_image`, `plannable_type`, `html_url` as `string`
- `course_id`, `group_id`, `user_id`, `plannable_id` as `integer`
- `plannable_date` as `datetime`
- `new_activity` as `boolean`
- `planner_override` as `$ref PlannerOverride`
- `plannable` and `submissions` with **no type**, so both are `Any` in the client: `plannable`'s fields depend on `plannable_type`, and `submissions` is `false` or an object

The descriptions list the plannable types and the submission status keys. Everything is optional except `plannable_id` and `plannable_type`. Add `@returns [PlannerItem]` to List planner items.
- *Alternative: `plannable` as `object`.* Close, but `Any` matches the existing approach for unions and costs nothing.
- *Alternative: model `submissions` as an object with the status fields.* Rejected: `false` fails a strict object field.

### D2: `@model TodoItem`
- `context_type`, `context_name`, `context_short_name`, `type`, `ignore`, `ignore_permanently`, `html_url`, `checkpoint_label` as `string`
- `course_id`, `group_id`, `parent_assignment_id`, `needs_grading_count` and the five educator-dashboard counts as `integer`
- `assignment` as `$ref Assignment`, `quiz` as `$ref Quiz`

Everything is optional except `type`. Add `@returns [TodoItem]` to both todo actions.

### D3: Seed `--todo-items`
Standalone and idempotent. Using the seeded student (the `--tokens` default) and one of their courses:
- find or create a published assignment "Seeded todo assignment" due 3 days from the run, with points
- find or create a submission for a second student in that course (submitted, ungraded), so the teacher gets a grading todo
- find or create a `PlannerNote` for the student, dated 2 days out

Print the ids, the student id, and the date range to query. It's never committed.

### D4: Tests
- **Offline:** `test/custom/unit/test_planner_and_todo_models.py`, with fixtures in `test/custom/unit/fixtures/planner/`, captured live:
  - the student's planner items: assignment and note, with `submissions` as both `false` and an object if the data allows; otherwise a synthetic variant of the captured item
  - the student's todo list (submitting)
  - a grading todo captured by a seed-run serializer call in the web container (`todo_item_json` for the course's teacher), because no teacher token exists
    - *Applied:* `todo_item_json` needs a controller context (`api_user_content`), so the grading todo was captured from `GET /courses/2/todo` with a temporary teacher access token, which was deleted after the capture

  Each deserializes, `assignment`/`quiz` are typed, and ids equal the JSON.
- **Allowlist:** the four operations leave `UNDOCUMENTED_PAGINATED_OPERATIONS`.
- **Live:** `test_paginated_models.py` gets:
  - the student's planner items in the D3 range
  - the student's todo items
  - the observer's planner items for its observee (`planner_index_for_users`)

  Each skips with its seed or token hint.

## Risks / Trade-offs

- [`Assignment` may not match `assignment_json` (all dates)] → The integration run checks it. Mismatches are fixed in this change's docs commit and noted.
- [Seed dates go stale] → The seed is relative to the run date, and the test queries the range it prints, or the default window.
- [`plannable` is untyped] → The envelope is typed and `plannable_type` tells callers what they hold. Per-type models are a follow-up.

## Migration Plan

1. Fork:
   1. seed and capture (uncommitted)
   2. docs, regenerate (uncommitted), diff, then commit in upstream format
2. Client: regenerate, add tests and fixtures, run the suites, then commit.

Rollback: revert the commits.
