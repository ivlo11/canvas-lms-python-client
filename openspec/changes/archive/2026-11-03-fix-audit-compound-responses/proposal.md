# Proposal

## Why

Canvas's three audit log APIs return a compound document, `{"links": {...}, "events": [...], "linked": {...}}`, not a plain list. In the client:
- **7 operations raise.** The course audit (`for_course`, `for_account`) and grade change audit (`for_assignment`, `for_course`, `for_student`, `for_grader`, `query`) operations are documented `@returns [CourseEvent]` / `[GradeChangeEvent]`. The client deserializes the object as a list and fails on every call. Confirmed live: `grade_change_audit_api_for_course(course_id="5")` raises `ValidationError … input_value='links'`.
- **3 operations return nothing.** The authentication audit operations (`for_account`, `for_login`, `for_user`) have no `@returns`, so they return `None` and their page iterators yield `Any`.

The event models also disagree with what Canvas sends, so they would still fail once the wrapper is right:
- **`GradeChangeEvent`:**
  - `version_number` is documented `string`, but Canvas sends an integer
  - `points_possible_before`/`points_possible_after`, `grade_current` and `course_override_grade` are missing
- **`GradeChangeEventLinks`:** `student` and `grader` are documented `integer`, but Canvas sends strings (`"172"`)
- **`CourseEventLink`:** `course`, `user`, `page_view` and `sis_batch` are documented `integer`, but Canvas stringifies them (`.to_s`, so a missing id is `""`)
- **`CourseEvent`:** `event_data` is documented `string`, but Canvas sends an object
- **`AuthenticationEvent`:** documents `pseudonym_id`, `account_id` and `user_id`, but Canvas sends `id` (a UUID), `created_at`, `event_type` and `links: {login, account, user, page_view}`

## What Changes

- **Generator (canvas-lms fork, fork-only commit):** an inline `@returns` entry may be the type name `object`. It becomes an untyped mapping and no longer makes the whole inline object a plain mapping. That's needed for `links` and `linked`, whose keys vary.
- **Controller docs (canvas-lms fork), one upstreamable commit:**
  - The 10 audit actions get `@returns { "links": object, "events": [<Event>], "linked": object }`, using `CourseEvent`, `GradeChangeEvent` or `AuthenticationEvent`.
  - `GradeChangeEvent`: `version_number` becomes integer. Add `points_possible_before`, `points_possible_after` (number), `grade_current` (string) and `course_override_grade` (boolean).
  - `GradeChangeEventLinks`: `student` and `grader` become string.
  - `CourseEventLink`: `course`, `user`, `page_view` and `sis_batch` become string. `copied_from`/`copied_to` stay integer.
  - `CourseEvent`: `event_data` becomes object.
  - `AuthenticationEvent`:
    - add `id` (string) and `links` (new `@model AuthenticationEventLinks`: `login`, `account`, `user` as integer, `page_view` as string)
    - remove `pseudonym_id`, `account_id` and `user_id`, which Canvas never sends
- **Seed script (fork, never committed):** a new `--audit-events` option records a course audit event for course 5, so course audit pages have data. Grade change and authentication events already exist.
- **Client:**
  - Regenerate. Each audit operation returns a per-action wrapper (`CourseAuditApiForCourseResponse`, `GradeChangeAuditApiQueryResponse`, `AuthenticationAuditApiForLoginResponse`, …) whose `events` are typed. Its page iterator yields those wrappers.
  - The three authentication operations leave the undocumented allowlist.
  - Offline tests use captured pages, and integration tests call all three audit APIs.
- **BREAKING (client):**
  - The audit operations return wrapper models instead of lists or `None`.
  - Several event fields change type.
  - The client is unreleased, so this isn't documented.

## Capabilities

### New Capabilities
<!-- None. -->

### Modified Capabilities
- `paginated-list-responses`: audit log queries yield compound pages whose events are typed.
- `typed-operation-responses`: an inline object entry documented as `object` is an untyped mapping and doesn't prevent a wrapper model.

## Impact

- **canvas-lms (fork):**
  - Generator: `lib/swagger_yard/canvas_adapter.rb` and `spec/lib/swagger_yard/canvas_adapter_spec.rb`.
  - Docs: `app/controllers/course_audit_api_controller.rb`, `grade_change_audit_api_controller.rb`, `authentication_audit_api_controller.rb`.
  - Not committed: the seed script and the regenerated `public/doc/openapi/canvas.openapi.yaml`.
- **canvas-lms-python-client:**
  - Regenerated `api/course_audit_api_api.py`, `grade_change_audit_api_api.py` and `authentication_audit_api_api.py`; the event, link and wrapper models.
  - `test/custom/unit/test_paginated_response_types.py`, a new `test/custom/unit/test_audit_responses.py` and its fixtures, and `test/custom/integration/test_paginated_models.py`.
- **Order:** apply this first of the four undocumented-list changes. `type-simple-undocumented-lists`, `type-discussion-entries-and-recipients` and `type-planner-and-todo-items` also edit the allowlist and the seed script.
