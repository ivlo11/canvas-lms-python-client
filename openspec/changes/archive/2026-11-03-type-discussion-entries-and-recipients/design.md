# Design

## Context

- Motivation: see proposal.md, "Why". Requirements: `specs/paginated-list-responses/spec.md`.
- **`serialize_entry`** (`lib/api/v1/discussion_topics.rb`):
  - always: `id`, `created_at`, `updated_at`, `parent_id`, `rating_count`, `rating_sum`
  - `editor_id`, when the entry is deleted or edited
  - `user_id` and `user_name`, when not deleted
  - `deleted: true` or `message` (HTML)
  - `user` (`user_display_json`), when included: the default for entries and replies, and asked for by entry_list
  - `attachment` and `attachments` (`attachment_json`), when the entry has a file
  - `read_state`, `forced_read_state`
  - for root entries, `recent_replies` (up to 10, same shape, recursive) and `has_more_replies`
- **Recipients** (`search_controller#recipients`):
  - **User recipients** (`conversation_user_json`): `id` (integer), `name`, `full_name`, `pronouns`, `common_courses` and `common_groups` (maps of id to role list), `avatar_url`. Checked live with the admin token.
  - **Context recipients** (`SearchHelper`): `id` (asset string such as `course_5` or `section_3`), `name`, `avatar_url`, `type` (`"context"`), `user_count`, `permissions` (map) and `context_name`. Synthetic sub-contexts (`course_5_sections`, `course_5_groups`) carry `item_count` instead of `user_count`.
- **Model collisions:**
  - `File` is defined twice, and the 7-field LTI `File` wins.
  - `UserDisplay` documents `short_name`, but Canvas sends `display_name`.

  Neither is safe to reference here.
- **Live data:** course 5 has no discussion topics. The admin isn't enrolled anywhere, so its recipient search returns only users. Students see their course contexts.

## Goals / Non-Goals

**Goals:**
- The eight operations yield models that keep every field Canvas sends, checked against live payloads.

**Non-Goals:**
- Typing `attachment`/`user` as `File`/`UserDisplay`, which waits on the duplicate-model and `UserDisplay` fixes.
- The full discussion view (`discussion_topics_api_view`) and the GraphQL discussion API.

## Decisions

### D1: `@model DiscussionEntry`
Fields as listed in Context:
- ids and counts are `integer`, timestamps are `datetime`
- `message`, `user_name`, `read_state` are `string`
- `deleted`, `forced_read_state`, `has_more_replies` are `boolean`
- `user` and `attachment` are `object` with no properties, and `attachments` is an array of the same
- `recent_replies` is an array of `$ref DiscussionEntry`

All optional except `id`. `@returns [DiscussionEntry]` on all three actions.
- *Alternative: `$ref File` and `$ref UserDisplay`.* Rejected until those models are correct; a mapping keeps every field, and a wrong model would drop most of them.

The self-reference is fine in openapi-generator's Python output (it emits `model_rebuild`). Task 3.1 verifies a two-level payload.

### D2: `@model Recipient`
A single model covering both kinds, with every field optional:
- `id` has **no type**, so it holds a string or an integer
- `name`, `full_name`, `pronouns`, `avatar_url`, `type`, `context_name` are `string`
- `user_count`, `item_count` are `integer`
- `common_courses`, `common_groups`, `permissions` are `object` with no properties

The description explains which fields belong to users and which to contexts. `@returns [Recipient]` on Find recipients.
- *Alternative: separate `UserRecipient`/`ContextRecipient` with `oneOf`.* The adapter has no `oneOf`, and the shapes can't be told apart without a discriminator on users.
- *Alternative: type `id` as `string`.* Rejected: user ids are JSON integers, and a strict string field would fail on them.

### D3: Seed `--discussion-entries`
Standalone and idempotent. In course 5, find or create a topic "Seeded entries topic" by the course's teacher, with:
- a root entry by a student with an attached text file
- a reply to it
- a second root entry that is then destroyed (soft-deleted)

Print the topic and entry ids. It's never committed.

### D4: Tests
- **Offline:** `test/custom/unit/test_discussion_and_recipient_models.py`, with fixtures in `test/custom/unit/fixtures/discussions/`, captured live:
  - topic entries (root with replies and an attachment)
  - entries by id (`entry_list`), which is the only list that includes the deleted entry
  - replies
  - user recipients (admin token)
  - context recipients (student token), searched with `type=context&search=`: Canvas returns no contexts unless `search` is sent, even empty

  No synthetic sub-context was reachable, so a hand-written payload covers `item_count`.

  Each payload deserializes, ids and messages equal the JSON, and `id` keeps its JSON type for both recipient kinds.
- **Allowlist:** the eight operations leave `UNDOCUMENTED_PAGINATED_OPERATIONS`.
- **Live:** `test_paginated_models.py` tests entries, replies and entry_list with the admin token, and recipients with the student token (contexts) and the admin token (users). Each skips with its seed or token hint.

## Risks / Trade-offs

- [`user` and `attachment` are untyped] → All fields are preserved. Typing waits on the `UserDisplay` and `File` fixes (follow-up).
- [`Recipient.id` is `Any`] → Accurate for a mixed list. Callers check `type` to tell contexts from users.
- [The student token is invalid today] → Task 1.1 checks it first and reruns the seed `--tokens` option if needed.

## Migration Plan

1. Fork:
   1. seed and capture (uncommitted)
   2. docs, regenerate (uncommitted), diff, then commit in upstream format
2. Client: regenerate, add tests and fixtures, run the suites, then commit.

Rollback: revert the commits.
