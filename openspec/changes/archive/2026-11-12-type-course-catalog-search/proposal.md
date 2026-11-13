# Proposal

## Why

The API docs sweep gave `search_all_courses` (List all courses) a response type, `SearchAllCoursesResponse`, but only as `{ "course": object }`. The client yields entries whose `course` is an untyped dict, and the exceptions file lists the model as `needs_description`.

`@returns [Course]` would be wrong. The action renders `@courses.as_json`, which differs from every other course endpoint in two ways:
- **Each item is wrapped in a root key:** `[{"course": {...}}, ...]`. A `Course` model reading that item finds none of its fields, so every field would be silently unset, with no error.
- **The inner object is the raw database record, not `course_json`.** It has `conclude_at` where `Course` has `end_at`, `storage_quota` where `Course` has `storage_quota_mb`, and no `sis_course_id` or `uuid`.

## What Changes

- **Controller docs (canvas-lms fork), one commit on top of the sweep:** in `search_controller.rb`, replace `SearchAllCoursesResponse` with:
  - `@model CatalogCourse`: every column the catalog returns, 59 in the seeded instance, typed from the contract test's probes, or from the column type for columns seen only as null
  - `@model CatalogCourseEntry`: `{ "course": CatalogCourse }`
  - `@returns [CatalogCourseEntry]` on List all courses

  The model's `needs_description` entry leaves `lib/api_docs_audit/exceptions.yml`.
- **Columns that look internal are documented too**, such as `self_enrollment_code`, `sis_source_id`, `integration_id` and `settings`, per the sweep's rule that docs describe what the API returns.
- **Client:**
  - Regenerate. `search_all_courses` returns `List[CatalogCourseEntry]`, and its `_paginated` and `_all` iterators yield typed entries.
  - An offline test uses a captured payload, and an integration test covers the catalog list and its `search` filter.
- **BREAKING (client):** `SearchAllCoursesResponse` is replaced. The client is unreleased, so this isn't documented.

## Capabilities

### New Capabilities
<!-- None. -->

### Modified Capabilities
- `paginated-list-responses`: course catalog search yields typed entries.

## Impact

- **canvas-lms (fork, `chore/api-docs-enforcement`):**
  - `app/controllers/search_controller.rb` and `lib/api_docs_audit/exceptions.yml`.
  - Not committed: `spec/manual_seeding/large_gradebook_seeds.rb` (unchanged; `--contract-data` already seeds the catalog) and the regenerated `public/doc/openapi/canvas.openapi.yaml`.
- **canvas-lms-python-client (`fix/add-returns-for-paginated-models`):**
  - Regenerated `api/search_api.py`; new models `CatalogCourse` and `CatalogCourseEntry`, replacing `SearchAllCoursesResponse`.
  - A new `test/custom/unit/test_course_catalog.py` and its fixture, and `test/custom/integration/test_paginated_models.py`.
