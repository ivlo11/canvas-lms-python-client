# Tasks

## 1. Check the shapes (read-only)

- [x] 1.1 Deserialize each `linked` list in `test/custom/unit/fixtures/audit/grade_change.json` and `authentication.json` with the current client models (`Assignment`, `Course`, `User`, `Login`, `Account`). Verify that none raises, and that `course.json`'s `linked` still fails on string ids. If a grade change or authentication item fails, update D1/D2 before editing docs.
  - Done: All 2 assignments, 1 course and 3 users in `grade_change.json`, and the 1 login, 1 account and 1 user in `authentication.json`, deserialize. In `course.json`, the course fails with `int_type` on `id`, `account_id`, `root_account_id` and `enrollment_term_id`, and the user on `id`.
- [x] 1.2 Compare `PageView` (`page_views_controller.rb`) with `page_view_json` (`lib/api/v1/page_view.rb`, including `API_PAGE_VIEW_JSON_OPTS`), field by field. Record each field's sent type next to its documented type in these notes. Verify there's no disagreement, or list each one to fix in 2.1.
  - Done: Sent types come from running `page_view_json` on an unsaved `PageView` in the web container. `as_json` sends every column, not only `EXPORTED_COLUMNS`.

    | Field | Sent | Documented |
    |---|---|---|
    | `id` | string, `SecureRandom.uuid` | string, uuid |
    | `app_name` | string or null | string |
    | `url`, `context_type`, `asset_type`, `controller`, `action`, `user_agent`, `http_method`, `remote_ip` | string | string |
    | `contributed`, `user_request`, `participated` | boolean | boolean |
    | `interaction_seconds`, `render_time` | float | number |
    | `created_at` | ISO 8601 string | datetime |
    | `developer_key_id`, `asset_user_access_id` | integer | number |
    | `links.user`, `.context`, `.asset`, `.real_user`, `.account` | integer | integer |
    | `session_id` | string, 32 hex characters (Rack session id) | **string, uuid** |
    | `updated_at`, `summarized` | timestamp, boolean | not documented; the model ignores them |

    One disagreement to fix in 2.1: `session_id` isn't a UUID. The client parses 32 hex characters into a `UUID`, so the value no longer equals what Canvas sent, and any other length fails the whole page. Fix: drop `format: uuid` and use a real example.

## 2. Doc corrections (canvas-lms fork)

- [x] 2.1 Apply D1–D3 (and any 1.2 `PageView` fixes) to the audit controllers. Verify that `git diff` shows comment lines only, and that both new models' JSON parses.
  - Done: Comment lines only across the four controllers, and both models' JSON parses. Also `PageView.session_id` per 1.2, in `page_views_controller.rb`.
- [x] 2.2 Regenerate (`bundle exec rake doc:openapi`, not committed) and diff against the current spec. Verify:
  - `GradeChangeLinkedRecords` and `AuthenticationLinkedRecords` exist, with array-of-`$ref` properties
  - the 8 grade change and authentication wrappers' `linked` is a `$ref` to them
  - the 2 course audit wrappers' `linked` is still `type: object`
  - no other schema or operation changed
  - Done: All of the above hold. The other differences are expected: `PageView.session_id` (1.2), and the `description` of the 2 course audit operations (D3).
- [x] 2.3 Commit only the controllers in upstream format: subject, why, `flag=none`, `Test Plan:`, every line under 60 characters. Verify that `git log -1 --stat` lists only them, and that `public/doc/` and the seed script stay uncommitted. Do not open a PR.
  - Done: `918a1649d21` on `chore/fix-openapi-spec`, listing only the four controllers. The commit hook's Ruby lint crashes on the host's Ruby 2.6 without blocking the commit, so rubocop ran in the web container: 2 `Naming/PredicateMethod` offenses, on method definitions this comment-only commit doesn't touch.

## 3. Client (canvas-lms-python-client)

- [x] 3.1 Copy `src/.openapi-generator/FILES`, regenerate, and delete orphans by manifest diff (keep existing `test_*.py` entries the manifest drops). Verify:
  - `GradeChangeAuditApiForCourseResponse.linked` is `Optional[GradeChangeLinkedRecords]`
  - `AuthenticationAuditApiForUserResponse.linked` is `Optional[AuthenticationLinkedRecords]`
  - `CourseAuditApiForCourseResponse.linked` is still `Optional[Dict[str, Any]]`
  - Done: All three hold, and `PageView.session_id` is `Optional[StrictStr]`. Used the `openapitools/openapi-generator-cli:latest` Docker image. No orphans. `FILES` is the `LC_ALL=C sort -u` union with the pre-change manifest, adding 6 lines.
- [x] 3.2 Update `test/custom/unit/test_audit_responses.py` per D4. Verify that it passes, and that the new assertions fail against the pre-change generated files: export them, confirm the failure, then discard the export.
  - Done: 61 passed. In an export with the 8 wrappers and `page_view.py` from `HEAD` and the new models kept, so the failures are assertions and not imports: 20 failed, including the page view test on `session_id`. Export discarded.
- [x] 3.3 Extend the grade change, authentication and course audit integration tests in `test/custom/integration/test_paginated_models.py` per D4. Run `pdm run pytest --integration -v -k audit` with the admin token. Verify that they pass, or skip with their seed hint (`--audit-events`).
  - Done: 123 passed, 0 skipped.
- [x] 3.4 Verify that `pdm run pytest` passes offline, that the full `--integration` run shows no new failures, and that `pdm run ruff check src/canvas_lms_python_client/test/custom` is clean. Then commit the client in the `fix(canvas_lms_python_client): ...` style.
  - Done: Offline: 3896 passed, 185 skipped. Full `--integration`: 3937 passed, 144 skipped, 0 failed. Ruff is clean. Committed as `8973fd8` on `fix/add-returns-for-paginated-models`.

## 4. Final checks

- [x] 4.1 Run `openspec validate type-audit-linked-records --strict` and verify that it passes. Its INFO note, that archive would refuse the MODIFIED delta, is expected until `fix-audit-compound-responses` is archived.
  - Done: Passes, with no INFO note, because `fix-audit-compound-responses` is already archived.

## Workflow follow-up

- Apply only after `type-discussion-entries-and-recipients` and `type-planner-and-todo-items` have landed, rebasing onto their tips.
- Archive `fix-audit-compound-responses` before this change. This change's delta modifies that change's requirement.
- Upstream: the user may cherry-pick the task 2.3 commit after signing the CLA.
- Archive with `/opsx:archive` after review.
