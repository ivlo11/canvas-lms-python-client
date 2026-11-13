# Design

## Context

- Motivation: see proposal.md, "Why". Requirements: `specs/paginated-list-responses/spec.md`.
- **The action** (`search_controller#all_courses`):
  - returns 401 unless `@domain_root_account.enable_course_catalog?`
  - lists `Course.where(root_account_id:, indexed: true, workflow_state: "available")`, optionally filtered by `search`, `public_only` and `open_enrollment_only`
  - renders `@courses.as_json` for JSON requests and HTML otherwise
  - is reachable without a user (`skip_before_action :require_user, only: [:all_courses]`)
- **What `as_json` emits**, from a read-only `Course.where(id: 5).as_json` in the web container: top-level key `course`, wrapping every column of the record, including `id`, `name`, `course_code`, `workflow_state`, `account_id`, `root_account_id`, `enrollment_term_id`, `start_at`, `conclude_at`, `created_at`, `updated_at`, `is_public`, `indexed`, `open_enrollment`, `self_enrollment`, `public_description`, `syllabus_body`, `default_view`, `license`, `locale`, `time_zone`, `restrict_enrollments_to_course_dates` and `storage_quota`, plus internal columns. This hasn't been seen through the endpoint yet, because the catalog is off. Task 1.2 confirms it over HTTP.
- **Live state:** `enable_course_catalog` is off, and no course is indexed.

## Goals / Non-Goals

**Goals:**
- `search_all_courses` yields models that really hold the catalog's values.

**Non-Goals:**
- Changing what the endpoint returns. It's a docs-only change.
- Deciding whether Canvas should expose the raw record (see Risks).
- The HTML form of the page.

## Decisions

### D1: Two models, keeping the root key
`CatalogCourseEntry` has one property, `course` (`$ref CatalogCourse`). `@returns [CatalogCourseEntry]` describes the array exactly, so callers read `entry.course.name`.
- *Alternative: `@returns [Course]`.* Rejected: the root key leaves every field unset with no error, which is worse than `None`.
- *Alternative: `{ "course": Course }` entries.* Rejected: the raw record isn't `course_json`. `Course.end_at` and `storage_quota_mb` would always be unset, and the model would promise many fields the catalog never sends.
- *Alternative: unwrap the root key in a client hook.* Rejected: generated models should describe the wire format, and no other operation needs a hook.

### D2: `CatalogCourse` documents public fields only
- `integer`: `id`, `account_id`, `root_account_id`, `enrollment_term_id`
- `string`: `name`, `course_code`, `workflow_state`, `public_description`, `syllabus_body`, `default_view`, `license`, `locale`, `time_zone`
- `datetime`: `start_at`, `conclude_at`, `created_at`, `updated_at`
- `boolean`: `is_public`, `indexed`, `open_enrollment`, `self_enrollment`, `restrict_enrollments_to_course_dates`

All are optional except `id` and `name`. Task 1.2 checks each type over HTTP, `time_zone` in particular.

The other columns stay undocumented: `self_enrollment_code`, `sis_source_id`, `sis_batch_id`, `integration_id`, `lti_context_id`, `turnitin_id`, `turnitin_comments`, `settings`, `tab_configuration`, `stuck_sis_fields`, `storage_quota` and the remaining internal ids and flags. A catalog reader doesn't need them, and a docs commit meant for upstream shouldn't advertise them as API.
- *Alternative: document every column.* Rejected for the reason above, and most would be noise.

### D3: Seed `--course-catalog`
Standalone and idempotent:
- set `settings[:enable_course_catalog] = true` on `Account.default` if it isn't set
- `course.update!(indexed: true)` on course 5 if it isn't indexed
- print the setting, the course id, and the count of indexed courses

Reverting by hand means clearing the setting. It's never committed.

### D4: Tests
- **Offline:** `test/custom/unit/test_course_catalog.py`, with `test/custom/unit/fixtures/catalog/all_courses.json` captured in task 1.2. It checks that:
  - the captured list deserializes as `List[CatalogCourseEntry]`
  - `entry.course.id`, `name` and `workflow_state` equal the JSON
  - `CatalogCourse` has no `self_enrollment_code`, `sis_source_id` or `settings` field
- **Allowlist:** `search_all_courses` leaves `UNDOCUMENTED_PAGINATED_OPERATIONS`. The guard test stays, so any new undocumented operation still fails. If `fix-undetected-pagination` landed first, the list still holds its 8 operations.
- **Live:** `test_paginated_models.py` lists the catalog with the admin token and checks the search filter with a term from the course name. On a 401 it skips with the `--course-catalog` hint, because the catalog setting belongs to the seed data.

The disabled-catalog scenario is checked by hand in task 3.3, not by an automated test, because the seed leaves the setting on.

## Risks / Trade-offs

- [The endpoint serves raw records, including columns such as `self_enrollment_code`, and doesn't require a user] → This is existing Canvas behaviour on accounts with the catalog on, and this change doesn't alter it. Task 1.2 records over HTTP which columns are really returned. If a sensitive value does come back, raise it with the user before committing; it would belong in a private report to Instructure, not in a public commit message.
- [Raw columns can change between Canvas versions] → Only stable, public columns are documented, and all but two are optional.
- [The HTML branch] → The client sends `Accept: application/json`. Task 1.2 confirms a JSON response through the client's headers.

## Migration Plan

1. Fork, on `chore/fix-openapi-spec`: seed and capture (uncommitted); edit the docs, regenerate (uncommitted), diff, then commit in upstream format.
2. Client, on `fix/add-returns-for-paginated-models`: regenerate, add tests and the fixture, run the suites, then commit.

Rollback: revert the commits and clear the account setting.
