# Proposal

## Why

Eight paginated operations have no `@returns`, so the client returns `None` and their page iterators yield `Any`:
- **Discussion entries:** `discussion_topics_api_entries` (List topic entries), `discussion_topics_api_replies` (List entry replies) and `discussion_topics_api_entry_list` (List entries), each also `_for_groups`. All three render `discussion_entry_api_json`, and no discussion entry model is documented.
- **Recipients:** `search_recipients` and `search_recipients_for_other` (Find recipients). They render a mix of users (`conversation_user_json`) and contexts (`SearchHelper`). The two shapes differ, and a context's `id` is an asset string (`"course_5"`) while a user's is an integer.

## What Changes

- **Controller docs (canvas-lms fork), one upstreamable commit:**
  - `discussion_topics_api_controller.rb`:
    - add `@model DiscussionEntry`, following `serialize_entry`; `recent_replies` is a list of `DiscussionEntry`
    - add `@returns [DiscussionEntry]` to the three actions
  - `search_controller.rb`:
    - add `@model Recipient`, covering both users and contexts, with every field optional and `id` untyped
    - add `@returns [Recipient]` to Find recipients
- **Seed script (fork, never committed):** a new `--discussion-entries` option creates a discussion topic in course 5 with a root entry that has an attachment, a reply, and a deleted entry. User recipients already exist for the admin. Context recipients are read with the student token.
- **Client:**
  - Regenerate. The eight operations yield `DiscussionEntry` / `Recipient` and gain `_all` iterators.
  - They leave the undocumented allowlist.
  - Offline tests use captured payloads, and integration tests cover entries, replies, the entry list and recipients.
- **BREAKING (client):** these operations return models instead of `None`. The client is unreleased, so this isn't documented.

## Capabilities

### New Capabilities
<!-- None. -->

### Modified Capabilities
- `paginated-list-responses`: discussion entry lists and recipient searches yield typed items.

## Impact

- **canvas-lms (fork):**
  - Docs: `app/controllers/discussion_topics_api_controller.rb` and `app/controllers/search_controller.rb`.
  - Not committed: the seed script and the regenerated `public/doc/openapi/canvas.openapi.yaml`.
- **canvas-lms-python-client:**
  - Regenerated `api/discussion_topics_api_api.py` and `api/search_api.py`; new models `DiscussionEntry` and `Recipient`.
  - `test/custom/unit/test_paginated_response_types.py`, a new `test/custom/unit/test_discussion_and_recipient_models.py` and its fixtures, and `test/custom/integration/test_paginated_models.py`.
- **Order:** apply after `type-simple-undocumented-lists`. All of these changes edit the allowlist and the seed script.
- **Needs:** a working `CANVAS_STUDENT_API_TOKEN`. Today it returns `401 user authorization required`. Rerun the seed `--tokens` option if it still does.
