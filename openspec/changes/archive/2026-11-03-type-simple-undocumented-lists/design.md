# Design

## Context

- Motivation: see proposal.md, "Why". Requirements: `specs/paginated-list-responses/spec.md`.
- **Serializers:**
  - **`pseudonym_json`:** `id`, `user_id`, `account_id`, `unique_id`, `created_at`, `workflow_state`, `declared_user_type`, `authentication_provider_id`
    - `sis_user_id` and `integration_id` only with SIS rights
    - `authentication_provider_type` only when a provider is linked
    - live for user 1: ids are integers, `created_at` is ISO
  - **`conversation_batch_json`:** `id`, `workflow_state` (`only`), `completion` (float), `recipient_count` (integer), `message` (`conversation_message_json`), `tags` (string list).
  - **`bulk_user_progress`:** `user_display_json(user, course)` (`id`, `anonymous_id`, `display_name`, `avatar_image_url`, `html_url`, `pronouns`, and `fake_student` for test students) merged with `progress: CourseProgress#to_json`. That is `{requirement_count, requirement_completed_count, next_requirement_url, completed_at}`, or `{error: {message}}` when the user's progress can't be evaluated. If the course isn't module-based, the whole response is `{"error": …}` (the 400-style body seen live).
  - **`multiple_gradeable_students`:** `user_display_json(student, course)` plus `assignment_ids` (assignment ids from the visibility service, integers).
  - **`PaceContextsPresenter.as_json`:**
    - `name`, `type` (`Course`, `CourseSection` or `StudentEnrollment`), `item_id`
    - `associated_section_count`, `associated_student_count` (null for non-courses)
    - `applied_pace` (`{name, type, duration, last_modified}`, or null)
    - `on_pace` (boolean, or null for non-students)

    The response is `{pace_contexts: [...], total_entries}`.
- **Existing models:**
  - `CourseProgress` matches `to_json`'s success shape.
  - `UserDisplay` documents `short_name`, not `display_name`, so it's reused nowhere here (follow-up).
  - No `Login`, `ConversationBatch`, `PaceContext` or conversation message model exists.
- **Live data today:** logins exist. Course 5 bulk progress errors (not module-based), pace contexts 404 (pacing off), and the admin has no batches.

## Goals / Non-Goals

**Goals:**
- The six operations return models matching what Canvas sends, checked against live payloads.

**Non-Goals:**
- Fixing `UserDisplay` (`display_name`, `anonymous_id`, `pronouns`). It's referenced by many operations and is a separate change.
- A `ConversationMessage` model for `ConversationBatch.message`.
- `CourseProgress`'s `{error}` variant beyond keeping it optional (see D3).

## Decisions

### D1: `@model Login`
Add it in `pseudonyms_controller.rb`, with the fields listed in Context:
- ids are `integer`, `created_at` is `datetime`, the rest are `string`
- all optional except `id`, `user_id`, `account_id` and `unique_id`

`@returns [Login]` on List user logins. The name follows Canvas's own wording ("logins").
- *Alternative: `Pseudonym`.* Rejected: the API calls them logins everywhere (`/logins`, "List user logins").

### D2: `@model ConversationBatch`
`id` (integer), `workflow_state` (string), `completion` (number), `recipient_count` (integer), `message` (`object`, no properties), `tags` (array of string). `@returns [ConversationBatch]`.

### D3: `@model UserProgress`
The user display fields as Canvas sends them (`id`, `anonymous_id`, `display_name`, `avatar_image_url`, `html_url`, `pronouns`, `fake_student`) plus `progress` (`$ref CourseProgress`). All `CourseProgress` fields are already optional, so a per-user `{error: …}` progress deserializes with every field unset. `@returns [UserProgress]`.
- *Alternative: extend `UserDisplay` through composition.* The adapter has no `allOf`, and `UserDisplay` itself is wrong.

### D4: `@model MultipleGradeableStudent`
The same user display fields plus `assignment_ids` (array of integer). `@returns [MultipleGradeableStudent]`. Task 1.2 confirms that the ids are integers.

### D5: `@model PaceContext` and `@model AppliedPace`
- `PaceContext`: `name`, `type` (string, the three values in the description), `item_id` (integer), `associated_section_count`, `associated_student_count` (integer), `applied_pace` (`$ref AppliedPace`) and `on_pace` (boolean).
- `AppliedPace`: `name`, `type` (string), `duration` (integer), `last_modified` (datetime).
- `@returns { "pace_contexts": [PaceContext], "total_entries": integer }` generates `PaceContextsApiIndexResponse` through the existing inline-returns support.

Using `$ref AppliedPace` instead of a nested `properties` block avoids depending on `type-nested-object-properties`.

### D6: Seed options
Each is standalone, idempotent and never committed:
- **`--module-progress`:** in course 5, find or create a published module with one assignment item and a `must_submit` completion requirement, then run the progressions. Print the module id.
- **`--course-pacing`:** enable the `course_paces` feature on the account, set `course.enable_course_paces = true` on course 5, and find or create a published course pace. Print the pace id.
- **`--conversation-batch`:** create a `ConversationBatch` for the admin in the `created` state (in progress), with a root message to two seeded students, without running its job. Print the batch id. If the model's validations prevent that, capture the JSON by calling `conversation_batch_json` in a runner and use it only as an offline fixture. Then make the integration test skip, and record which path was used.

### D7: Tests
- **Offline:** `test/custom/unit/test_simple_list_models.py`, with fixtures in `test/custom/unit/fixtures/simple_lists/`, captured live. Each payload deserializes and its key fields equal the JSON. A synthetic `UserProgress` item has `progress: {"error": {...}}`.
- **Allowlist:** the six operations leave `UNDOCUMENTED_PAGINATED_OPERATIONS`.
- **Live:** `test_paginated_models.py` gets one test per operation with the admin token, each skipping with its seed hint when data is missing.

## Risks / Trade-offs

- [Duplicate user display fields across two new models] → This mirrors what Canvas sends. They can be consolidated if `UserDisplay` is fixed later.
- [Bulk progress on a non-module course returns an error body with a non-2xx status] → The client raises an API exception, as it does for any error, and this change doesn't alter that.
- [The batch seed may not be possible without running jobs] → D6's fallback keeps the offline coverage.

## Migration Plan

1. Fork:
   1. seed and capture (uncommitted)
   2. docs, regenerate (uncommitted), diff, then commit in upstream format
2. Client: regenerate, add tests and fixtures, run the suites, then commit.

Rollback: revert the commits.
