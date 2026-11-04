# Proposal

## Why

Four paginated operations have no `@returns`, so the client returns `None` and their page iterators yield `Any`:
- **`planner_index`, `planner_index_for_users`** (List planner items): render `planner_item_json`. The item envelope is stable: context fields, `plannable_id`, `plannable_type`, `plannable_date`, `planner_override`, `new_activity`, `submissions`, `html_url`. But `plannable` is the raw attributes of one of ten object kinds, and `submissions` is `false` or a status object.
- **`users_todo_items`, `courses_todo_items`** (List the TODO items, Course TODO items): render `todo_item_json`. These have context fields, `type` (`grading` or `submitting`), `ignore`/`ignore_permanently` URLs, `html_url`, `needs_grading_count`, and either an `assignment` (`assignment_json`) or a `quiz` (`quiz_json`).

These are the dashboard feeds a student or parent app reads first, so typing the envelope is worthwhile even where the payload stays polymorphic.

## What Changes

- **Controller docs (canvas-lms fork), one upstreamable commit:**
  - `planner_controller.rb`:
    - add `@model PlannerItem` and `@returns [PlannerItem]`
    - `plannable` and `submissions` stay untyped, because their shape depends on `plannable_type` and on the submission state
    - `planner_override` references `PlannerOverride`
  - `users_controller.rb`: add `@model TodoItem` and `@returns [TodoItem]` on List the TODO items. `assignment` references `Assignment` and `quiz` references `Quiz`.
  - `courses_controller.rb`: add `@returns [TodoItem]` on Course TODO items.
- **Seed script (fork, never committed):** a new `--todo-items` option creates, in course 5:
  - an assignment due in the next week, which shows as a planner item and a `submitting` todo for the student
  - a submitted-but-ungraded submission, which shows as a `grading` todo for the course's teacher
  - a planner note for the student

  It prints a teacher token reference only if one already exists. Otherwise the grading todo is checked through the student's course list.
- **Client:**
  - Regenerate. The four operations yield `PlannerItem` / `TodoItem` and gain `_all` iterators.
  - They leave the undocumented allowlist.
  - Offline tests use captured payloads, and integration tests use the student and observer tokens.
- **BREAKING (client):** these operations return models instead of `None`. The client is unreleased, so this isn't documented.

## Capabilities

### New Capabilities
<!-- None. -->

### Modified Capabilities
- `paginated-list-responses`: planner items and todo items yield typed items.

## Impact

- **canvas-lms (fork):**
  - Docs: `app/controllers/planner_controller.rb`, `users_controller.rb`, `courses_controller.rb`.
  - Not committed: the seed script and the regenerated `public/doc/openapi/canvas.openapi.yaml`.
- **canvas-lms-python-client:**
  - Regenerated `api/planner_api.py`, `users_api.py` and `courses_api.py`; new models `PlannerItem` and `TodoItem`.
  - `test/custom/unit/test_paginated_response_types.py`, a new `test/custom/unit/test_planner_and_todo_models.py` and its fixtures, and `test/custom/integration/test_paginated_models.py`.
- **Order:** apply last of the four undocumented-list changes. All of them edit the allowlist and the seed script.
- **Needs:** a working `CANVAS_STUDENT_API_TOKEN` (see `type-discussion-entries-and-recipients`, task 1.1).
- **Risk inherited:** `TodoItem.assignment` uses the existing `Assignment` model. If that model mismatches what `assignment_json` sends, the integration run surfaces it as a `ValidationError`, and it's fixed in this change's doc commit.
