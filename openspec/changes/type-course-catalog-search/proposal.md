# Proposal

## Why

`search_all_courses` (List all courses) is the last paginated operation with no response type: it returns `None`, and `search_all_courses_paginated` yields `Any`. The action has no `@returns`.

The obvious fix, `@returns [Course]`, would be wrong. The action renders `@courses.as_json`, which differs from every other course endpoint in two ways (read from `Course#as_json` in the seeded instance):
- **Each item is wrapped in a root key:** `[{"course": {...}}, ...]`. A `Course` model reading that item finds none of its fields, so every field would be silently unset, with no error.
- **The inner object is the raw database record, not `course_json`.** It has `conclude_at` where `Course` has `end_at`, `storage_quota` where `Course` has `storage_quota_mb`, and no `sis_course_id` or `uuid`.

## What Changes

- **Controller docs (canvas-lms fork), one upstreamable commit:** in `search_controller.rb`, add:
  - `@model CatalogCourse`: the public catalog fields of the raw record
  - `@model CatalogCourseEntry`: `{ "course": CatalogCourse }`
  - `@returns [CatalogCourseEntry]` on List all courses
- **Fields left undocumented on purpose:** the raw record also has internal columns such as `self_enrollment_code`, `sis_source_id`, `integration_id`, `lti_context_id`, `turnitin_id`, `sis_batch_id`, `settings`, `tab_configuration` and `stuck_sis_fields`. The docs don't advertise them, so the client drops them.
- **Seed script (fork, never committed):** a new `--course-catalog` option turns on `enable_course_catalog` for the default account and marks course 5 as indexed. Today the setting is off and no course is indexed, so the endpoint returns 401.
- **Client:**
  - Regenerate. `search_all_courses` returns `List[CatalogCourseEntry]`, and its `_paginated` and `_all` iterators are typed.
  - The operation leaves `UNDOCUMENTED_PAGINATED_OPERATIONS`.
  - An offline test uses a captured payload, and an integration test covers the catalog list and its `search` filter.
- **BREAKING (client):** this operation returns models instead of `None`. The client is unreleased, so this isn't documented.

## Capabilities

### New Capabilities
<!-- None. -->

### Modified Capabilities
- `paginated-list-responses`: course catalog search yields typed entries.

## Impact

- **canvas-lms (fork, `chore/fix-openapi-spec`):**
  - Docs: `app/controllers/search_controller.rb`.
  - Not committed: `spec/manual_seeding/large_gradebook_seeds.rb` and the regenerated `public/doc/openapi/canvas.openapi.yaml`.
- **canvas-lms-python-client (`fix/add-returns-for-paginated-models`):**
  - Regenerated `api/search_api.py`; new models `CatalogCourse` and `CatalogCourseEntry`.
  - `test/custom/unit/test_paginated_response_types.py`, a new `test/custom/unit/test_course_catalog.py` and its fixture, and `test/custom/integration/test_paginated_models.py`.
