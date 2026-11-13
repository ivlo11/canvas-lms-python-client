# Tasks

## 1. Seed and capture (canvas-lms fork, uncommitted)

- [ ] 1.1 Re-read `spec/manual_seeding/large_gradebook_seeds.rb` and add `--course-catalog` (D3) as an additive edit. Run it twice in the web container. Verify that the first run enables the setting and indexes course 5, and the second changes nothing. Do not commit the script.
- [ ] 1.2 Capture `GET /search/all_courses` with the admin token and `Accept: application/json`. Verify:
  - the response is JSON, and each item has the single key `course`
  - each D2 field's JSON type matches D2, recorded in these notes (`time_zone` in particular); update D2 if one disagrees
  - which internal columns come back, recorded by name only

  If `self_enrollment_code` or another sensitive column holds a real value, stop and raise it with the user (Risks). Save the payload as the D4 fixture, and verify that it contains no tokens or personal data.

## 2. Doc corrections (canvas-lms fork)

- [ ] 2.1 Apply D1 and D2 to `search_controller.rb`. Verify that `git diff` shows comment lines only, and that both models' JSON parses.
- [ ] 2.2 Regenerate (`bundle exec rake doc:openapi`, not committed) and diff. Verify:
  - `CatalogCourse` and `CatalogCourseEntry` exist, and `CatalogCourse` has only the D2 properties
  - `search_all_courses` returns an array of `CatalogCourseEntry`
  - no other operation changed
  - no unresolved `@returns` warning names `search_all_courses`
- [ ] 2.3 On `chore/fix-openapi-spec`, commit only `search_controller.rb` in upstream format: subject, why, `flag=none`, `Test Plan:`, every line under 60 characters. Verify that `git log -1 --stat` lists only that file, and that the seed script and `public/doc/` stay uncommitted. Do not open a PR.

## 3. Client (canvas-lms-python-client)

- [ ] 3.1 Copy `src/.openapi-generator/FILES`, regenerate, and delete orphans by manifest diff (keep existing `test_*.py` entries the manifest drops). Verify that `search_all_courses_all` yields `CatalogCourseEntry`, and that `CatalogCourseEntry.course` is `CatalogCourse`.
- [ ] 3.2 Add the 1.2 fixture and `test/custom/unit/test_course_catalog.py` (D4), and remove `search_all_courses` from `UNDOCUMENTED_PAGINATED_OPERATIONS`. Verify that the tests pass, and that they fail against the pre-change generated files: check out the old files, confirm the failure, then restore them.
- [ ] 3.3 Add the integration test (D4) and run `pdm run pytest --integration -v -k catalog` with the admin token. Verify that it passes. Confirm by hand that clearing the setting makes the client raise the unauthorized error and the test skip with the `--course-catalog` hint, then turn the setting back on.
- [ ] 3.4 Verify that `pdm run pytest` passes offline, that the full `--integration` run shows no new failures, and that `pdm run ruff check src/canvas_lms_python_client/test/custom` is clean. Then commit the client on `fix/add-returns-for-paginated-models`.

## 4. Final checks

- [ ] 4.1 Run `openspec validate type-course-catalog-search --strict` and verify that it passes.

## Workflow follow-up

- Upstream: the user may cherry-pick the task 2.3 commit after signing the CLA.
- Archive with `/opsx:archive` after review.
