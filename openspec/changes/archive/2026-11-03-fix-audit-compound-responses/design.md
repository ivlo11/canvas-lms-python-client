# Design

## Context

- Motivation: see proposal.md, "Why". Requirements: the two spec deltas.
- **Serializers.** `lib/api/v1/course_event.rb`, `grade_change_event.rb` and `authentication_event.rb` each build `*_compound_json` → `{links: links_json, events: [...], linked: linked_json}`:
  - `links` maps `"events.<x>"` to a URL template, `nil`, or `{href, type}`.
  - `linked` maps `page_views`, `courses`, `users`, `assignments` or `logins`/`accounts` to lists of their API JSON. Course audit stringifies every id in `linked`.
- **Event JSON**, compared with the docs (live grade change and authentication events; serializer for course events):
  - **Grade change:** `version_number` is an integer, `points_possible_*` are floats, `links.student`/`links.grader` are strings, `links.course`/`links.assignment` are integers. Canvas adds `grade_current` and `course_override_grade: true` when they apply.
  - **Course:** `links` values are all strings (`""` when nil). For `copied_*`/`reset_*` events, `links` also gets `copied_from`/`copied_to`/`reset_from`/`reset_to` (integers), and `event_data` is `{}`.
  - **Authentication:** `{id, created_at, event_type, links: {login, account, user, page_view}}`.
- **Inline `@returns` parser.** `inline_object_value_schema` accepts `[Model]`, `Model`, literals and `INLINE_OBJECT_PRIMITIVES` (`integer string boolean number`). Any other entry makes `inline_object_properties` return nil, so the operation becomes a plain mapping. `links`/`linked` can't be expressed today.
- **Wrappers** are named `<Resource><Action>Response` and registered per action. A wrapped response gets a `_paginated` iterator yielding wrapper pages, and no `_all`.

## Goals / Non-Goals

**Goals:**
- All 10 audit queries deserialize live pages, with typed events.

**Non-Goals:**
- Typing `linked`, e.g. as `{logins: [Login], users: [User], …}`. It varies per API, and `Login` is introduced by `type-simple-undocumented-lists`. Follow-up.
- An `_all` iterator that flattens events across pages.
- `CreatedEventData`/`UpdatedEventData`, which aren't referenced and are left as they are.

## Decisions

### D1: `object` as an inline entry type
Add `object` to `INLINE_OBJECT_PRIMITIVES`, emitting `{"type": "object"}`. The client types that entry as `Dict[str, Any]`. Adapter spec examples:
- `{ "a": [Model], "b": object }` yields a wrapper with `b` typed object
- the quoted `"object"` form behaves the same
- existing primitives are unchanged

This is a fork-only commit, separate from the docs.
- *Alternative: define `@model`s for each `links`/`linked` shape.* Rejected: there are 6 near-identical, key-varying shapes, and link templates have no value to callers as typed fields.

### D2: Audit `@returns`
Each of the 10 actions gets one line, e.g. `@returns { "links": object, "events": [GradeChangeEvent], "linked": object }`. That replaces the existing `[GradeChangeEvent]`/`[CourseEvent]`, or is added where `@returns` is missing (authentication). The resulting wrappers are:
- `CourseAuditApi{ForCourse,ForAccount}Response`
- `GradeChangeAuditApi{ForAssignment,ForCourse,ForStudent,ForGrader,Query}Response`
- `AuthenticationAuditApi{ForAccount,ForLogin,ForUser}Response`

Canvas's HTML docs already render brace `@returns` as text, so the upstream commit reads naturally. `object` is a valid doc word there.

### D3: Event model corrections
- **`GradeChangeEvent`:**
  - `version_number` becomes `integer`
  - add `points_possible_before`/`points_possible_after` (`number`), `grade_current` (`string`) and `course_override_grade` (`boolean`)
  - keep the documented `request_id` (optional; not sent today)
- **`GradeChangeEventLinks`:** `student` and `grader` become `string`.
- **`CourseEvent`:** `event_data` becomes `object`. Canvas sends `{"name": [old, new]}` for updates and `{}` for copy/reset events. (Found by the offline tests during apply; the original design missed it.)
- **`CourseEventLink`:** `course`, `user`, `page_view` and `sis_batch` become `string`, with the description noting that ids are strings and `""` means none. `copied_from`/`copied_to` stay `integer`. Add `reset_from`/`reset_to` (`integer`).
- **`AuthenticationEvent`:**
  - add `id` (`string`, UUID) and `links` (`$ref AuthenticationEventLinks`)
  - remove `pseudonym_id`, `account_id` and `user_id`
  - new `@model AuthenticationEventLinks` with `login`, `account`, `user` (`integer`) and `page_view` (`string`)

Every change follows the live payload or the serializer, and task 1.2 re-checks each field before the docs are edited.

### D4: Seed `--audit-events`
Standalone and idempotent. For course 5:
- if it has no course audit event, call `Auditors::Course.record_updated(course, admin, {"name" => [old, new]}, source: :api)` after a no-op rename back and forth
- print the event count

It also records a login event for the seeded second admin (user 392) when it has none, so the authentication capture doesn't need user 1's personal data. Grade change events (course 5) already exist. It's never committed.

### D5: Tests
- **Offline:** `test/custom/unit/test_audit_responses.py` with captured pages in `test/custom/unit/fixtures/audit/` (one per API). Each page deserializes into its wrapper, events are typed, and the corrected fields equal the JSON. It also covers a synthetic `copied_to` course event, an override-grade event (`course_override_grade`, `grade_current`), and an empty page.
- **Allowlist:** `UNDOCUMENTED_PAGINATED_OPERATIONS` drops the three authentication operations.
- **Live:** `test/custom/integration/test_paginated_models.py` lists one page of each API with the admin token and asserts typed events. Each test skips with a seed hint when its log is empty.

## Risks / Trade-offs

- [Other event fields mismatch in data the seed doesn't produce] → The serializers were read field by field, and any `ValidationError` in the integration run is fixed in the same docs commit.
- [`links`/`linked` stay untyped] → They hold URL templates and side-loaded records; the events, which are what callers want, are typed. Typing `linked` is a follow-up.
- [`object` as an inline type hides structure elsewhere if overused] → It's only used where keys vary, and the adapter spec pins the behavior.

## Migration Plan

1. Fork:
   1. seed and capture (uncommitted)
   2. adapter change with specs, then commit
   3. docs, regenerate (uncommitted), diff, then commit in upstream format
2. Client: regenerate, add tests and fixtures, run the suites, then commit.

Rollback: revert the commits.
