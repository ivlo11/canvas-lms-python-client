# Design

## Context

- Motivation: see proposal.md, "Why". Requirements: `specs/paginated-list-responses/spec.md`.
- **Current docs:** all 10 audit actions document `@returns { "links": object, "events": [<Event>], "linked": object }` (`fix-audit-compound-responses`, D2).
- **Generator:** `inline_object_value_schema` already turns a bare model name into a `$ref` (and `[Model]` into an array of `$ref`s). It does not parse nested braces. So a typed `linked` needs a `@model`, not a nested inline object.
- **Serializers (`lib/api/v1/`):**
  - **`grade_change_event.rb#linked_json`:** `page_views` (`page_views_json`), `assignments` (`assignments_json`), `courses` (`courses_json`), `users` (`users_json`).
  - **`authentication_event.rb#linked_json`:** `logins` (`pseudonyms_json`), `accounts` (`accounts_json`), `users`, `page_views`.
  - **`course_event.rb#linked_json`:** `page_views`, `courses`, `users`, all wrapped in `StringifyIds.recursively_stringify_ids`. The code comment says this keeps ids consistent for clients that don't send the string-ids `Accept` header.
  - Every list is always present, and may be empty.
- **Captured pages (`test/custom/unit/fixtures/audit/`), checked against the current client models:**
  - **Grade change:** 2 assignments, 1 course and 3 users, all deserializing into `Assignment`, `Course` and `User`. Every event's `links.assignment`/`links.course` id is in `linked`, and so is every student and grader id (as an integer).
  - **Authentication:** 1 login, 1 account and 1 user deserialize into `Login`, `Account` and `User`. The event's `links.login`, `links.account` and `links.user` ids match them.
  - **Course audit:** the course and the user fail with `int_type` errors on `id`, `account_id`, `root_account_id` and `enrollment_term_id` (sent as `"5"`, `"1"`, …).
  - **Unmodelled extra fields:**
    - `Account`: `default_*_quota_mb`, `default_time_zone`, `course_template_id`
    - `Course`: `homeroom_course`, `course_color`, `friendly_name`
    - `User`: `created_at`
    - `Assignment`: about 10 fields

    The models ignore them, as they do elsewhere.
- **Page views:** dev Canvas doesn't record them (`PageView.page_view_method` is false, 0 rows), so `linked.page_views` is always `[]` live. `page_view_json` sends `id` (the request id), `url`, `links: {user, context, asset, real_user, account}`, `contributed`, `app_name` and the `API_PAGE_VIEW_JSON_OPTS` columns. The existing `PageView` model (`page_views_controller.rb`) documents that serializer.

## Goals / Non-Goals

**Goals:**
- Grade change and authentication `linked` deserialize into typed records, checked against the captured pages.

**Non-Goals:**
- Typing course audit `linked`. The user chose to leave it untyped: modelling it would need string-id copies of `Course` and `User`, which would drift. Its description records why.
- Typing `links` (URL templates and `{href, type}` objects). Callers have no use for them as fields.
- Correcting the unmodelled extra fields on `Account`, `Course`, `User` or `Assignment`.
- Changing `PageView` beyond what the offline check in task 1.2 finds.

## Decisions

### D1: `@model GradeChangeLinkedRecords`
In `grade_change_audit_api_controller.rb`, next to `GradeChangeEventLinks`. Its properties are arrays with `items: {"$ref": ...}`, in the serializer's key order:
- `page_views`: `PageView`
- `assignments`: `Assignment`
- `courses`: `Course`
- `users`: `User`

Its description says these are the records referenced by the page's events.

The 5 actions' `@returns` become `{ "links": object, "events": [GradeChangeEvent], "linked": GradeChangeLinkedRecords }`.

- *Alternative: `GradeChangeEventLinked`.* Rejected: it's one letter away from `GradeChangeEventLinks`, which is easy to misread.
- *Alternative: one shared `AuditLinkedRecords` model with every key.* Rejected: it would advertise keys an API never sends, such as `logins` on grade change pages.

### D2: `@model AuthenticationLinkedRecords`
In `authentication_audit_api_controller.rb`, next to `AuthenticationEventLinks`. Its properties are:
- `logins`: `Login` (in `pseudonyms_controller.rb`)
- `accounts`: `Account`
- `users`: `User`
- `page_views`: `PageView`

The 3 actions' `@returns` become `{ "links": object, "events": [AuthenticationEvent], "linked": AuthenticationLinkedRecords }`.

### D3: Course audit stays `object`
`course_audit_api_controller.rb` gets no `@returns` change. Instead, its existing `@API` descriptions gain one sentence: the related records in `linked` have string ids. That's an upstreamable docs fact, and it explains why no model is referenced.

- *Alternative: `CourseAuditLinkedRecords` with string-id copies of `Course` and `User`.* Rejected by the user.
- *Alternative: type only `page_views`.* Rejected: `PageView`'s own ids would also be stringified.

### D4: Tests
- **Offline (`test_audit_responses.py`):**
  - For grade change and authentication operations, `response.linked` is the linked-records model. Each list's items are the expected model, and their ids equal the fixture's.
  - Every event's link ids appear in the matching `linked` list.
  - For course audit, `response.linked == page["linked"]` stays as it is.
  - A synthetic page view, built from `page_view_json`'s fields, deserializes into `PageView` inside each linked-records model.
  - The empty-page test still passes with `linked: {}`, giving a model whose lists are unset.
- **Live (`test_paginated_models.py`):** the existing grade change and authentication tests also assert typed `linked` records, and that the event link ids resolve in them. The course audit test asserts `linked` is a dict.
- **Fixtures:** the existing captured pages are reused, with no recapture. They already cover every key except `page_views`.

### D5: `PageView.session_id` is a plain string
Task 1.2 found that `session_id` is documented as `format: uuid`, but Canvas sends a Rack session id of 32 hex characters. The client's `UUID` type accepts that, but rewrites it with hyphens, so the value no longer equals what Canvas sent. Any other length fails the whole page, which the spec forbids now that page views sit inside `linked`. The fix drops `format: uuid` and replaces the example. `PageView.id` is a real UUID (`SecureRandom.uuid`) and stays as it is.

## Risks / Trade-offs

- [`PageView` may not match `page_view_json`, and dev can't produce live page views] → Task 1.2 compares the model with the serializer field by field. If it disagrees, the fix goes in the same docs commit. The synthetic offline test pins the result.
- [A linked record in production data may carry a value the shared models reject (for example, an `Assignment` field typed too narrowly)] → `linked` is now as strict as the models used by the regular list endpoints. A failure there would also affect those endpoints, and would be fixed in the model.
- [The course audit wrapper stays untyped, so `linked` is inconsistent across the three APIs] → The `@API` sentence and the model descriptions record why.

## Migration Plan

1. Fork: docs, then regenerate (uncommitted), diff, and commit in upstream format.
2. Client: regenerate, update the tests, run the suites, then commit.

Rollback: revert the commits.
