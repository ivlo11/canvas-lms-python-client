# Design

## Context

- Motivation: see proposal.md, "Why". Requirements: `specs/paginated-list-responses/spec.md`.
- **The action** (`search_controller#all_courses`):
  - renders unauthorized unless `@domain_root_account.enable_course_catalog?`: 401 without a user, 403 with one
  - lists `Course.where(root_account_id:, indexed: true, workflow_state: "available")`, optionally filtered by `search`, `public_only` and `open_enrollment_only`
  - renders `@courses.as_json` for JSON requests and HTML otherwise
  - is reachable without a user (`skip_before_action :require_user, only: [:all_courses]`)
- **After the API docs sweep** (`automate-api-docs-accuracy`, archived):
  - On `chore/api-docs-enforcement`, `search_controller.rb` has `@model SearchAllCoursesResponse { "course": { "type": "object" } }` and `@returns [SearchAllCoursesResponse]` on List all courses.
  - `lib/api_docs_audit/exceptions.yml` lists `model: SearchAllCoursesResponse, reason: needs_description`, a to-do entry that covers no finding.
  - The client yields `SearchAllCoursesResponse` from `search_all_courses`, and its `course` is `Optional[Dict[str, Any]]`. Callers get the record as an untyped dict.
  - `UNDOCUMENTED_PAGINATED_OPERATIONS` is empty.
  - The sweep isn't in `chore/fix-openapi-spec`, which still has no `@returns` on this action.
  - The sweep's rule: every field a response shows goes in the docs and the client, sensitive-looking or not. Only fields no response has shown are left out, as `unverifiable` exceptions.
- **Seed:** `--contract-data` already turns on `enable_course_catalog` for the default account ("course catalog setting") and indexes the seeded course ("course catalog"). The live instance has the catalog on, with 2 indexed courses.
- **Evidence:** the contract test's probes (`build/contract/probes-<role>.jsonl`, all 4 roles) record `GET /api/v1/search/all_courses` as status 200, a list of `{ "course": object }`, and the course's 59 columns by name and JSON type. They hold no values. `uuid` is the only column not returned. The contract outcome is `parsed`.

## Goals / Non-Goals

**Goals:**
- `search_all_courses` yields models that type every column the catalog returns.
- The fork commit passes the sweep's checks: the cop, the lint and the full audit.

**Non-Goals:**
- Changing what the endpoint returns. It's a docs-only change.
- Deciding whether Canvas should expose the raw record (see Risks).
- The HTML form of the page.

## Decisions

### D1: Two named models, keeping the root key
Replace `SearchAllCoursesResponse` with:
- `CatalogCourseEntry`, with one property, `course` (`$ref CatalogCourse`)
- `CatalogCourse`, the record (D2)

`@returns [CatalogCourseEntry]` describes the array exactly, so callers read `entry.course.name`. The `needs_description` entry for `SearchAllCoursesResponse` leaves `exceptions.yml`.
- *Alternative: keep `SearchAllCoursesResponse` and type its `course` inline.* Rejected: an inline object generates an anonymous model name, and the record deserves a name of its own.
- *Alternative: `@returns [Course]`.* Rejected: the root key leaves every field unset with no error, which is worse than `None`.
- *Alternative: `{ "course": Course }` entries.* Rejected: the raw record isn't `course_json`. `Course.end_at` and `storage_quota_mb` would always be unset, and the model would promise many fields the catalog never sends.
- *Alternative: unwrap the root key in a client hook.* Rejected: generated models should describe the wire format, and no other operation needs a hook.

### D2: `CatalogCourse` documents every returned column
All 59 columns the probes show, typed from the observed JSON. A column seen only as null is typed from its database column and is nullable. `id` and `name` are required; the rest are optional.

Seen with a value:
- `integer`: `id`, `account_id`, `root_account_id`, `enrollment_term_id`, `wiki_id`, `storage_quota`; `grading_standard_id` (seen as integer and null, so nullable)
- `string`: `name`, `course_code`, `workflow_state`, `default_view`, `time_zone`
- `datetime`: `created_at`, `updated_at`
- `boolean`: `indexed`, `allow_student_wiki_edits`, `allow_student_forum_attachments`, `allow_student_organized_groups`, `template`, `homeroom_course`, `sync_enrollments_from_homeroom`, `horizon_course`, `content_library`, `career_learning_library_only`
- `object`: `settings` (seen with `enable_course_paces`, a boolean)
- `array`: `stuck_sis_fields` of strings; `tab_configuration`, whose items no probe has shown; the generator gives it its default object items, which is what `Course#tab_configuration` holds

Seen only as null, typed from the column:
- `datetime`: `start_at`, `conclude_at`, `deleted_at`, `archived_at`
- `boolean`: `is_public`, `open_enrollment`, `self_enrollment`, `restrict_enrollments_to_course_dates`, `show_public_context_messages`, `allow_wiki_comments`, `show_announcements_on_home_page`
- `string`: `syllabus_body`, `public_description`, `license`, `locale`, `group_weighting_scheme`, `default_wiki_editing_roles`, `sis_source_id`, `integration_id`, `lti_context_id`, `self_enrollment_code`, `turnitin_comments`, `grade_passback_setting`
- `integer`: `abstract_course_id`, `sis_batch_id`, `template_course_id`, `replacement_course_id`, `homeroom_course_id`, `latest_outcome_import_id`, `self_enrollment_limit`, `home_page_announcement_limit`, `turnitin_id`

Each field gets a short description; the model description says it's the raw course record, not the Courses API's `Course`.
- *Alternative: public fields only.* Rejected by the sweep's rule. Leaving a column out doesn't hide it; it only leaves the client unable to model it.
- *Alternative: leave null-only columns out.* Rejected: the responses show them, so they aren't `unverifiable`. The column type is the best evidence of what a value would be.

### D3: Seed
No seed change. `--contract-data` already enables the catalog and indexes the seeded course (Context), and the probes came from that state. The script stays uncommitted.

### D4: Tests and checks
- **Fork:**
  - `bin/rubocop --only Lint/ApiDocs app/controllers/search_controller.rb` passes.
  - `script/api_docs_lint` shows nothing new.
  - The full audit, run as in `doc/api_docs_audit/enforcement.md` with the client's probes as evidence, has no unlisted finding for this action and no stale exceptions entry.
- **Offline:** `test/custom/unit/test_course_catalog.py`, with a fixture `test/custom/unit/fixtures/catalog/all_courses.json` captured in task 1.1. It checks that:
  - the captured list deserializes as `List[CatalogCourseEntry]`
  - `entry.course.id`, `name` and `workflow_state` equal the JSON
  - every key of the captured record is a `CatalogCourse` field, so a column the docs miss fails the test
- **Live:** `test_paginated_models.py` lists the catalog with the admin token and checks the search filter with a term from the course name. On a 401 or 403 it skips with the `--contract-data` hint, because the catalog setting belongs to the seed data.
- The contract test still reports `parsed` for the operation.

The disabled-catalog scenario is checked by hand in task 3.3, not by an automated test, because the seed leaves the setting on. The web process caches the account, so a setting change shows only after clearing `MultiCache` for the account lookup and waiting out the 60-second special-account cache.

## Risks / Trade-offs

- [The endpoint serves raw records, including columns such as `self_enrollment_code`, and doesn't require a user] → Existing Canvas behaviour on accounts with the catalog on; this change doesn't alter it. The docs describe it, per the sweep's rule. If a captured value turns out sensitive, the fixture uses a placeholder, and the behaviour belongs in a private report to Instructure, not a public commit message.
- [Raw columns change between Canvas versions] → All but two fields are optional, and the audit and lint flag new columns.
- [Null-only columns typed from the schema, not a response] → A wrong type fails deserialization. The column types are exact, and the offline test captures what the seed returns.
- [The HTML branch] → The client sends `Accept: application/json`. Task 1.1 confirms a JSON response through the client's headers.
- [The fork commit depends on the sweep] → It goes on `chore/api-docs-enforcement`, which has the sweep and the checks. It can't apply to `chore/fix-openapi-spec` until the sweep does.

## Migration Plan

1. Fork, on `chore/api-docs-enforcement`: capture the fixture; edit the docs and `exceptions.yml`; regenerate (uncommitted), diff and run the checks; commit in upstream format.
2. Client, on `fix/add-returns-for-paginated-models`: regenerate, add tests and the fixture, run the suites, then commit.

Rollback: revert the commits.
