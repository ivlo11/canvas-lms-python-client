# Tasks

## 1. Generator (canvas-lms fork)

- [x] 1.1 Add D2's `.convert_single_property` examples to `spec/lib/swagger_yard/canvas_adapter_spec.rb`. Verify with `bin/rspec spec/lib/swagger_yard/canvas_adapter_spec.rb` in the web container that only the new nested-properties examples fail, and that the "without `properties`" example passes.

  Notes: done in a git worktree (`.claude/worktrees/type-nested-object-properties`, branch `wt/type-nested-object-properties`), with rspec run from the main checkout's web container. 165 examples, 3 failures: the nested, `required` and two-level examples. The "without `properties`" example passes. The two-level example first used `"bool"`, which the adapter never maps to `boolean` at any level, so it uses `"datetime"` instead.
- [x] 1.2 Implement D1 in `convert_single_property`. Verify that the 1.1 examples pass, that `bin/rspec spec/lib/swagger_yard/` passes as a whole, and that `bin/rubocop lib/swagger_yard/canvas_adapter.rb spec/lib/swagger_yard/canvas_adapter_spec.rb` reports no new offenses.

  Notes: `handle_nested_properties`, called at the end of `convert_single_property`. 165 examples, 0 failures. Rubocop offenses are the same before and after (`Rails/Output` 1; `RSpec/BeforeAfterAll` 1, `RSpec/RepeatedDescription` 12).
- [x] 1.3 Regenerate the spec in the web container (`bundle exec rake doc:openapi`, not committed) and diff it with the previous spec. Verify:
  - `User.permissions` has its 3 boolean properties.
  - `LearningObjectDates.peer_review_sub_assignment` has its 7 properties: dates as `string` / `date-time`, and `overrides` as an array of `$ref: AssignmentOverride`.
  - No other schema and no operation changed.

  Notes: generated from the worktree adapter with `bin/rails runner` (`OpenApiGenerator.generate`, `canvas_root: /usr/src/app`). Only `User` and `LearningObjectDates` changed; `paths` are identical. `peer_review_sub_assignment` has its 7 properties (dates `string`/`date-time`, `overrides` items `$ref: AssignmentOverride`), and `permissions` has its 3 booleans. A falsy `example` (for example `can_update_avatar: false`) is dropped by the existing `copy_basic_property_fields`, which copies only truthy values. That's pre-existing.
- [x] 1.4 Commit the adapter and its spec (D5). Verify that `git log -1 --stat` lists only those two files, and that the seed script and `public/doc/` stay uncommitted. Do not open a PR.

  Notes: committed in the worktree, then cherry-picked onto `chore/fix-openapi-spec` as `fix(swagger_yard): keep nested object properties`. The worktree commit used `--no-verify` because the host `script/rlint` hook errors without blocking. After landing, `rake doc:openapi` in the main checkout produced a spec byte-identical to the worktree's (uncommitted).

## 2. Live evidence (canvas-lms fork, uncommitted)

- [x] 2.1 Follow D3: try to give one seeded assignment a peer review sub-assignment, then capture `GET /api/v1/courses/:course_id/assignments/:assignment_id/date_details` with the admin token into `test/custom/unit/fixtures/learning_object_dates/date_details.json`. Record the course and assignment ids. If Canvas can't produce one, record why, use the controller's documented example as the fixture, and mark the field unverified.

  Notes: **replaced at the user's request**. No seeding or live capture. `fixtures/learning_object_dates/date_details.json` is built by hand from the `LearningObjectDates` and `AssignmentOverride` `@model` docs, with a populated `peer_review_sub_assignment` (dates set, one override). `peer_review_sub_assignment` is **unverified against live Canvas**.

## 3. Client (canvas-lms-python-client)

- [x] 3.1 Copy `src/.openapi-generator/FILES`, regenerate, and delete orphans by manifest diff (keeping existing `test_*.py` entries the generator drops). Verify:
  - `models/user_permissions.py` and `models/learning_object_dates_peer_review_sub_assignment.py` exist.
  - `User.permissions` and `LearningObjectDates.peer_review_sub_assignment` reference them.
  - Record the actual names if they differ.

  Notes: done in a client worktree (scratchpad `wt-client`). The generated names match the design: `UserPermissions` (`models/user_permissions.py`) and `LearningObjectDatesPeerReviewSubAssignment` (`models/learning_object_dates_peer_review_sub_assignment.py`), plus their docs and generated test stubs. `docs/LtiRegistrationCreatedBy.md` also changes, because it lists the `User` fields. No orphans. The existing `test_user.py`/`test_learning_object_dates.py` stubs still pass (`{}` validates into the new model), so they weren't regenerated.
- [x] 3.2 Update `test_user_model.py` and add `test_learning_object_dates_model.py` and the annotation check (D4). Verify that they pass, and that they fail against the pre-change `models/user.py` and `models/learning_object_dates.py`: check out the old files, confirm the failure, then restore them.

  Notes: 8 passed. Against the HEAD `models/user.py` and `models/learning_object_dates.py`, 7 failed (all except the fixture-shape check).
- [x] 3.3 Verify that `pdm run pytest` passes offline, that the full `--integration` run (all three tokens set) shows no new failures, and that `pdm run ruff check src/canvas_lms_python_client/test/custom` is clean. Record any `ValidationError` as a follow-up naming the field. Then commit the client, staging only this change's files.

  Notes: per the user, the `--integration` suites weren't run. Offline: 3727 passed, 161 skipped, in the worktree (imports confirmed to resolve to the worktree's `src`) and again in the main checkout after landing. ruff clean. Committed in the worktree and cherry-picked onto `fix/add-returns-for-paginated-models` as `fix(canvas_lms_python_client): type nested object properties`. Regenerating the main checkout from the new spec leaves no diff.

## 4. Final checks

- [x] 4.1 Run `openspec validate type-nested-object-properties --strict` and verify that it passes.

## Workflow follow-up

- Convert array items with `properties` through `convert_single_property` once it handles a raw `enum`.
- Verify `peer_review_sub_assignment` against a live `date_details` response once a seeded assignment has a peer review sub-assignment.
- Keep falsy `example` values in `copy_basic_property_fields`.
- Archive with `/opsx:archive` after review.
