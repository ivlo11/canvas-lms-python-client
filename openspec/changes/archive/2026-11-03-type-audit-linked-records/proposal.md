# Proposal

## Why

`fix-audit-compound-responses` typed the audit events but left `linked` as an untyped dict. Callers who want the side-loaded course, assignment, user or login behind an event have to read raw dicts. That change deferred typing `linked` until a `Login` model existed, and `type-simple-undocumented-lists` added one. Checks against the captured audit pages show:

| API | `linked` keys (serializer) | Do the items fit existing models? |
|---|---|---|
| Grade change | `page_views`, `assignments`, `courses`, `users` (`GradeChangeEvent#linked_json`) | Yes: `Assignment`, `Course`, `User` |
| Authentication | `logins`, `accounts`, `users`, `page_views` (`AuthenticationEvent#linked_json`) | Yes: `Login`, `Account`, `User` |
| Course audit | `page_views`, `courses`, `users` (`CourseEvent#linked_json`) | No. It calls `StringifyIds.recursively_stringify_ids`, so every `id` and `*_id` is a string (`"5"`, `"392"`), and `Course`/`User` reject that |

## What Changes

- **Controller docs (canvas-lms fork), one upstreamable commit:**
  - `grade_change_audit_api_controller.rb`:
    - add `@model GradeChangeLinkedRecords` (`page_views: [PageView]`, `assignments: [Assignment]`, `courses: [Course]`, `users: [User]`)
    - the 5 actions' `@returns` use `"linked": GradeChangeLinkedRecords` instead of `object`
  - `authentication_audit_api_controller.rb`:
    - add `@model AuthenticationLinkedRecords` (`logins: [Login]`, `accounts: [Account]`, `users: [User]`, `page_views: [PageView]`)
    - the 3 actions' `@returns` use `"linked": AuthenticationLinkedRecords`
  - `course_audit_api_controller.rb`: `@returns` unchanged. Its `linked` stays `object` because its ids are stringified, and its `@API` descriptions say so.
  - `page_views_controller.rb`: `PageView.session_id` drops `format: uuid`, because Canvas sends a Rack session id.
- **No generator change.** Inline `@returns` already accepts a bare model name as an entry value and emits a `$ref`.
- **No seed change.** `--audit-events` and the existing grade changes already produce data for every `linked` key except `page_views`, which dev Canvas doesn't record.
- **Client:**
  - Regenerate. The 8 grade change and authentication wrappers' `linked` becomes `GradeChangeLinkedRecords` or `AuthenticationLinkedRecords`.
  - Course audit wrappers keep `linked: Dict[str, Any]`.
  - Offline tests reuse the captured audit fixtures, and the integration tests assert typed `linked` records.
- **BREAKING (client):** `linked` on grade change and authentication pages is a model instead of a dict. The client is unreleased, so this isn't documented.

## Capabilities

### New Capabilities
<!-- None. -->

### Modified Capabilities
- `paginated-list-responses`: grade change and authentication audit pages carry typed `linked` records. Course audit `linked` stays an untyped mapping.

## Impact

- **canvas-lms (fork):**
  - Docs: `app/controllers/grade_change_audit_api_controller.rb`, `app/controllers/authentication_audit_api_controller.rb`, `app/controllers/course_audit_api_controller.rb`, `app/controllers/page_views_controller.rb`.
  - Not committed: the regenerated `public/doc/openapi/canvas.openapi.yaml`.
- **canvas-lms-python-client:**
  - Regenerated: the 8 grade change and authentication wrapper models, `PageView`, plus the new `GradeChangeLinkedRecords` and `AuthenticationLinkedRecords` models.
  - `test/custom/unit/test_audit_responses.py` and `test/custom/integration/test_paginated_models.py`.
- **Order:**
  - Apply after `type-discussion-entries-and-recipients` and `type-planner-and-todo-items` have landed. All of them edit `test_paginated_models.py`.
  - Archive after `fix-audit-compound-responses`. This change's delta modifies the requirement that change adds.
