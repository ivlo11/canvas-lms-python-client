# Proposal

## Why

Six paginated operations have no `@returns`, so the client returns `None` and their page iterators yield `Any`. Each one renders a flat, stable shape that one new model can describe:

| Operation(s) | What Canvas sends (serializer) |
|---|---|
| `pseudonyms_index`, `pseudonyms_index_for_users` (List user logins) | login objects (`pseudonym_json`), checked live |
| `conversations_batches` (Get running batches) | `conversation_batch_json`: `id`, `workflow_state`, `completion`, `recipient_count`, `message`, `tags` |
| `courses_bulk_user_progress` | user display fields plus `progress` (`CourseProgress#to_json`) |
| `submissions_api_multiple_gradeable_students` | user display fields plus `assignment_ids` |
| `pace_contexts_api_index` (List all pace contexts) | `{pace_contexts: [...], total_entries}` (`PaceContextsPresenter`) |

## What Changes

- **Controller docs (canvas-lms fork), one upstreamable commit:**
  - `pseudonyms_controller.rb`: `@model Login` and `@returns [Login]`.
  - `conversations_controller.rb`: `@model ConversationBatch` and `@returns [ConversationBatch]`. `message` stays an untyped object, because no conversation message model is documented.
  - `courses_controller.rb`: `@model UserProgress` (the user display fields plus `progress: CourseProgress`) and `@returns [UserProgress]`.
  - `submissions_api_controller.rb`: `@model MultipleGradeableStudent` (the user display fields plus `assignment_ids`) and `@returns [MultipleGradeableStudent]`.
  - `course_pacing/pace_contexts_api_controller.rb`: `@model PaceContext`, `@model AppliedPace` and `@returns { "pace_contexts": [PaceContext], "total_entries": integer }`.
- **Seed script (fork, never committed):** three new options produce data that's missing today:
  - `--module-progress`: a module with a completion requirement in course 5, so bulk progress is available
  - `--course-pacing`: enables course pacing on course 5 with a published course pace
  - `--conversation-batch`: an in-progress conversation batch for the admin

  Logins and gradeable students already have data.
- **Client:**
  - Regenerate. The five list operations yield typed items and gain `_all`; pace contexts yield `PaceContextsApiIndexResponse` pages.
  - The six operations leave the undocumented allowlist.
  - Offline tests use captured payloads, and integration tests cover each operation.
- **BREAKING (client):** these operations return models instead of `None`. The client is unreleased, so this isn't documented.

## Capabilities

### New Capabilities
<!-- None. -->

### Modified Capabilities
- `paginated-list-responses`: logins, conversation batches, bulk user progress, multiple-assignment gradeable students and pace contexts yield typed items.

## Impact

- **canvas-lms (fork):**
  - Docs: the five controllers above.
  - Not committed: the seed script and the regenerated `public/doc/openapi/canvas.openapi.yaml`.
- **canvas-lms-python-client:**
  - Regenerated `api/pseudonyms_api.py`, `conversations_api.py`, `courses_api.py`, `submissions_api_api.py` and `pace_contexts_api_api.py`.
  - New models `Login`, `ConversationBatch`, `UserProgress`, `MultipleGradeableStudent`, `PaceContext`, `AppliedPace` and `PaceContextsApiIndexResponse`.
  - `test/custom/unit/test_paginated_response_types.py`, a new `test/custom/unit/test_simple_list_models.py` and its fixtures, and `test/custom/integration/test_paginated_models.py`.
- **Order:** apply after `fix-audit-compound-responses`. Both edit the allowlist and the seed script.
