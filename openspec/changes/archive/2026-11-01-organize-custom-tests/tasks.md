# Tasks

## 1. Move custom tests (canvas-lms-python-client)

- [x] 1.1 Record the baseline:
  - `pdm run pytest --co -q | tail -1` (currently 3816 tests collected)
  - `pdm run pytest -q`, offline pass and skip counts
  - the node ids collected from the 8 custom files

  Save these to the scratchpad. **Notes:** 3816 collected; offline 3658 passed, 158 skipped; 217 custom node ids; integration run 16 passed, 6 skipped.
- [x] 1.2 Create `src/canvas_lms_python_client/test/custom/{unit,integration}/` with empty `__init__.py` files in `custom/`, `unit/` and `integration/` (D5). Move the files with `git mv` as in the D2 table: `conftest.py`, the 6 unit files, `fixtures/` → `unit/fixtures/`, and the 2 integration files without their `integration_` prefix. Verify that `git status` shows renames, not deletions plus additions, and that `ls src/canvas_lms_python_client/test` lists only generated files, `__init__.py` and `custom/`.
- [x] 1.3 In `custom/conftest.py`, make `pytest_collection_modifyitems` add the `integration` marker to every item under `custom/integration` before the existing skip logic (D4). Keep the modules' `pytestmark` lines. Verify with a throwaway, unmarked `custom/integration/test_tmp_probe.py`: it's skipped without `--integration` and collected with it. Then delete the probe.

## 2. Configuration and checks (canvas-lms-python-client)

- [x] 2.1 Set `testpaths = ["src/canvas_lms_python_client/test/custom", "src/canvas_lms_python_client/test"]` in `pyproject.toml` (D3). Verify:
  - `pdm run pytest --co -q` reports the 1.1 count, so nothing is collected twice or lost.
  - The custom node ids match 1.1 apart from the new module paths.
  - `pdm run pytest -q` gives the 1.1 pass and skip counts.
  - `pdm run pytest src/canvas_lms_python_client/test/custom -q` collects only the custom tests (217 at baseline) and accepts `--integration`.
- [x] 2.2 Remove the `test/…` entries from `src/.openapi-generator-ignore`. Verify that regeneration leaves `custom/` untouched: copy `src/.openapi-generator/FILES`, regenerate with the usual command, check that `git status -- src/canvas_lms_python_client/test/custom` is clean, and check that no path under `custom/` appears in `FILES`. Discard any unrelated regeneration diff. **Notes:** `openapi-generator-cli` isn't on PATH, so regeneration used the `openapitools/openapi-generator-cli:latest` Docker image with the same `-c`, `-t mustache-templates` and `-o src` arguments. The only regeneration diff was 23 `test_*_api.py` lines dropped from `FILES` (the generator lists a test stub only in the run that creates it), which was discarded.
- [x] 2.3 Run `pdm run pytest --integration -m integration -v` against the seeded instance and verify that the same tests pass and skip as before the move.
- [x] 2.4 Run `pdm run ruff check src/canvas_lms_python_client/test/custom` and verify that it reports no new findings compared with the moved files at HEAD.

## 3. Docs and in-flight references

- [x] 3.1 Update the README (D6):
  - In "File Ownership", generated `src/canvas_lms_python_client/test/*.py` and custom `src/canvas_lms_python_client/test/custom/`, replacing the per-file list.
  - In Testing, the full-run, custom-only, single-file and integration commands, with the stale `test/test_pagination.py` path fixed.

  Verify that each documented command runs as written.
- [x] 3.2 If `correct-grading-period-set-and-quiz-event-docs` is not yet applied, update its tasks 3.2 and 3.3 to `custom/unit/test_paginated_response_types.py` and `custom/integration/test_paginated_models.py`. Search `openspec/changes` (excluding the archive) for `test/test_` and verify that no non-archived change names an old custom test path. **Notes:** not yet applied, so its tasks 3.2 and 3.3 were updated, and the same two paths in its proposal's Impact list too.

## 4. Final checks

- [x] 4.1 Run `openspec validate organize-custom-tests --strict` and verify that it passes. Then commit the client with the moves, config and README. Verify with `git log -1 --stat` that the moved files appear as renames.

## Workflow follow-up

- Archive with `/opsx:archive` after review.
- Separate follow-ups:
  - the `packages.find` package-name bug
  - the README `--cov=canvas_python_client` name
  - whether to keep generating model test stubs
