# Tasks

## 1. Capture (canvas-lms fork, uncommitted)

- [x] 1.1 Confirm that the probes in `build/contract/probes-admin.jsonl` still match D2 (59 columns, same types). Then capture `GET /search/all_courses` with the admin token through the client's headers, and verify that:
  - the response is JSON, and each item has the single key `course`
  - the record's keys are the D2 columns; update D2 if one differs

  Save the payload as the D4 fixture. Replace tokens, personal data and any real `self_enrollment_code`, `sis_source_id` or `integration_id` value with a placeholder of the same type, and verify that none remains.

## 2. Doc corrections (canvas-lms fork)

- [x] 2.1 Apply D1 and D2 to `search_controller.rb`, and remove the `SearchAllCoursesResponse` entry from `lib/api_docs_audit/exceptions.yml`. Verify that `git diff` shows comment lines in the controller and that one removal in `exceptions.yml`, and that both models' JSON parses.
- [x] 2.2 Regenerate (`bundle exec rake doc:openapi`, not committed) and diff. Verify:
  - `CatalogCourse` and `CatalogCourseEntry` exist, `SearchAllCoursesResponse` doesn't, and `CatalogCourse` has exactly the D2 properties, nullable where D2 says
  - `search_all_courses` returns an array of `CatalogCourseEntry`
  - no other operation changed
  - no unresolved `@returns` warning names `search_all_courses`
- [x] 2.3 Run the D4 fork checks: the cop, `script/api_docs_lint`, and the full audit with the client's probes as evidence. Verify that each passes, and that the audit lists no stale entry.
- [x] 2.4 On `chore/api-docs-enforcement`, commit only `search_controller.rb` and `exceptions.yml` in upstream format: subject, why, `flag=none`, `Test Plan:`, every line under 60 characters. Verify that `git log -1 --stat` lists only those files, and that the seed script and `public/doc/` stay uncommitted. Do not open a PR.

## 3. Client (canvas-lms-python-client)

- [x] 3.1 Copy `src/.openapi-generator/FILES`, regenerate, and delete orphans by manifest diff (keep existing `test_*.py` entries the manifest drops). Verify that `SearchAllCoursesResponse` is gone, that `search_all_courses_all` yields `CatalogCourseEntry`, and that `CatalogCourseEntry.course` is `CatalogCourse`.
- [x] 3.2 Add the 1.1 fixture and `test/custom/unit/test_course_catalog.py` (D4). Verify that the tests pass, and that they fail against the pre-change generated files: check out the old files, confirm the failure, then restore them.
- [x] 3.3 Add the integration test (D4) and run `pdm run pytest --integration -v -k catalog` with the admin token. Verify that it passes. Confirm by hand that clearing the setting makes the client raise `ForbiddenException` (403) for the admin token and the tests skip with the `--contract-data` hint, then turn the setting back on.
- [x] 3.4 Verify that `pdm run pytest` passes offline, that the full `--integration` run shows no new failures, that the contract test still reports `parsed` for `search_all_courses`, and that `pdm run ruff check src/canvas_lms_python_client/test/custom` is clean. Then commit the client on `fix/add-returns-for-paginated-models`.

## 4. Final checks

- [x] 4.1 Run `openspec validate type-course-catalog-search --strict` and verify that it passes.

## Workflow follow-up

- Upstream: the task 2.4 commit depends on the sweep, so it goes upstream after it.
- Archive with `/opsx:archive` after review.
