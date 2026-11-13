# Tasks

## 1. Detector (canvas-lms fork)

- [x] 1.1 Save the current `public/doc/openapi/canvas.openapi.yaml` outside the repo as the baseline, or regenerate it first if it's stale. Do not commit it.
- [x] 1.2 Implement D1–D3 in `lib/swagger_yard/canvas_adapter.rb`, with the D5 examples in `spec/lib/swagger_yard/canvas_adapter_spec.rb`. Run the adapter spec in the web container and verify that it passes, and that the positive examples fail against the old detector.
- [x] 1.3 Regenerate (`bundle exec rake doc:openapi`, not committed) and apply D4. Verify that the `x-paginated` set gains exactly the 14 operations and loses none, and that nothing else in `paths` or `components` changed. Record the counts in these notes. Fix any extra hit in the detector before continuing.
- [x] 1.4 On `chore/fix-openapi-spec`, commit the adapter and spec in the fork's format (lines under 60 characters, the why, a test plan). Verify that `git log -1 --stat` lists only those two files. Do not open a PR.

Notes: tasks 1.1–1.4 were done during `automate-api-docs-accuracy`, and committed as `923e077f289` on `fix/api-docs-sweep` instead of `chore/fix-openapi-spec` (that change's design D9). The 1.3 counts weren't recorded then; the offline pin in 2.2 now checks the 14 operations directly. That sweep also typed the 8 operations this change would have allowlisted, so `UNDOCUMENTED_PAGINATED_OPERATIONS` stays empty.

## 2. Client (canvas-lms-python-client)

- [x] 2.1 Copy `src/.openapi-generator/FILES`, regenerate, and delete orphans by manifest diff (keep existing `test_*.py` entries the manifest drops). Verify:
  - each of the 14 operations has `_paginated`
  - `gradebook_history_api_days_all` yields `Day`
  - `grading_periods_index` has no `_all`
- [x] 2.2 Update `test_paginated_response_types.py` (D5). Verify that the tests pass, that `test_all_iterator_only_for_list_responses` still passes, and that the new tests fail against the pre-change generated files: check out the old files, confirm the failure, then restore them.
- [x] 2.3 Add the integration tests (D5) and run `pdm run pytest --integration -v -k "gradebook_history or grading_periods"` with the admin token. Verify that they pass and yield more than one page. If `GradeChangeEvent`-style type errors appear in `Day`, `Grader` or `SubmissionHistory`, record them as a follow-up naming the field.
- [x] 2.4 Verify that `pdm run pytest` passes offline, that the full `--integration` run shows no new failures, and that `pdm run ruff check src/canvas_lms_python_client/test/custom` is clean. Then commit the client on `fix/add-returns-for-paginated-models`.

## 3. Final checks

- [x] 3.1 Run `openspec validate fix-undetected-pagination --strict` and verify that it passes.

## Workflow follow-up

- Type the 8 newly allowlisted operations: activity streams, outcome rollups, SIS assignments, live assessments. Done by `automate-api-docs-accuracy`.
- Archive with `/opsx:archive` after review.
