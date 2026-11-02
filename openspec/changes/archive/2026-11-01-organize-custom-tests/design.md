# Design

## Context

- Motivation: see proposal.md, "Why". Requirements: `specs/test-organization/spec.md`.
- **Where the generator writes tests:** with `generateSourceCodeOnly: true`, the Python generator writes flat `test_<api>_api.py`, `test_<model>.py` and `__init__.py` files into `<package>/test` (`PythonClientCodegen#apiTestFileFolder`), with no option to change it. It never writes subdirectories and doesn't generate a `conftest.py`.
- **Today's test directory:**
  - 803 generated test files.
  - 8 custom test files: 6 unit; 2 integration, marked at module level with `pytestmark`.
  - A custom `conftest.py` with the `--integration` option, skip logic, the `integration` marker registration and Canvas fixtures.
  - `fixtures/lti/`.
- **How the files depend on each other:** custom tests don't import each other or the conftest module. Only the two integration files use conftest fixtures. `test_lti_model_payloads.py` finds its fixtures through `pathlib.Path(__file__).parent / "fixtures" / "lti"`.
- **Discovery:** `pyproject.toml` sets `testpaths = ["src/canvas_lms_python_client/test"]` and `pythonpath = ["src"]`. pytest registers command-line options only from conftest files it loads at startup, which are the ones in the `testpaths` directories and their parents.

## Goals / Non-Goals

**Goals:**
- A file's location tells you whether it's generated or custom, and whether it's unit or integration.
- No change to generator configuration, templates, or generated files.

**Non-Goals:**
- Moving generated tests or changing their names or content. The alternative of routing tests through API/Model template slots into `test/generated/` was explored and rejected as unnecessary re-plumbing.
- Dropping the generated model test stubs.
- The `[tool.setuptools.packages.find]` package-name bug and the README `--cov=canvas_python_client` name. Both are tracked separately.

## Decisions

### D1: `custom/` inside the generated test directory
Custom tests go under `src/canvas_lms_python_client/test/custom/{unit,integration}`.
- The generator only writes flat files to `test/`, so nothing in `custom/` can be overwritten. Orphan cleanup diffs `.openapi-generator/FILES`, which never lists `custom/`, so it can't delete custom files either.
- *Alternative: a top-level `tests/` or `src/test/` with the generated tests relocated.* That needs the generator's API/Model template slots to stand in for test slots, a full regeneration and renaming to `*_test.py`, which is more risk for the same outcome.

### D2: Move with `git mv`, dropping the `integration_` prefix
| From `test/` | To `test/custom/` |
|---|---|
| `conftest.py` | `conftest.py` |
| `test_pagination.py`, `test_paginated_response_types.py`, `test_inline_object_responses.py`, `test_lti_model_payloads.py`, `test_list_query_params.py`, `test_api_operation_coverage.py` | `unit/` (same names) |
| `fixtures/` | `unit/fixtures/` |
| `test_integration_observees.py` | `integration/test_observees.py` |
| `test_integration_paginated_models.py` | `integration/test_paginated_models.py` |

`fixtures/` moves next to its only user, so the `__file__`-relative path keeps working without edits.

### D3: `custom/` is listed first in `testpaths`
`testpaths = ["src/canvas_lms_python_client/test/custom", "src/canvas_lms_python_client/test"]`.
- That makes `custom/conftest.py` a startup conftest, so `--integration` is registered for plain `pdm run pytest` and for `pdm run pytest src/canvas_lms_python_client/test/custom`.
- pytest de-duplicates the overlapping paths, so custom tests aren't collected twice. Task 2.1 checks the collection count.
- *Alternative: keep `conftest.py` at the test root.* That works with no `testpaths` change, but it breaks "the root holds only generated files".

### D4: Integration marking by folder
`custom/conftest.py`'s `pytest_collection_modifyitems` first adds the `integration` marker to every item whose path is under `custom/integration`. Then it applies the existing skip-unless-`--integration` logic. pytest calls this hook for every collected item, generated ones included, which is harmless because generated tests are never under `custom/integration`. The two modules' `pytestmark = pytest.mark.integration` lines are kept: they're redundant but harmless, and they document the intent.
- *Alternative: rely on `pytestmark` only.* Then a new integration file that forgets the marker would run, and fail, in the default offline run.

### D5: Packages via `__init__.py`
Add empty `__init__.py` files to `custom/`, `custom/unit/` and `custom/integration/`. With the default `prepend` import mode, modules become `canvas_lms_python_client.test.custom.unit.test_pagination` and similar, so they can't collide with generated test modules or with each other.
- *Alternative: `--import-mode=importlib`.* That changes import behavior for all ~3,800 tests, which is a bigger change than this needs.

### D6: Ignore list and README
- Remove the `test/…` entries (the 8 files, `conftest.py` and `fixtures/`) from `src/.openapi-generator-ignore`. They protected files the generator never writes.
- In the README, "File Ownership" lists `src/canvas_lms_python_client/test/*.py` as generated and `src/canvas_lms_python_client/test/custom/` as custom.
- The Testing section shows the full, custom-only and integration commands. It fixes the stale `pytest test/test_pagination.py` path to `src/canvas_lms_python_client/test/custom/unit/test_pagination.py`.

## Risks / Trade-offs

- [Someone runs `rm -r test/` before regenerating] → That would delete `custom/`. The documented cleanup is a manifest diff, and the README says `custom/` is hand-written.
- [`pytest src/canvas_lms_python_client/test/test_polls_api.py --integration`] → `custom/conftest.py` isn't loaded when only a generated file is targeted, so `--integration` is unknown. That's acceptable: generated tests have no integration tests. Running from the repo root with `-k` still works, because `testpaths` applies when no path is given.
- [The in-flight `correct-grading-period-set-and-quiz-event-docs` change names the old paths] → Task 3.2 updates its tasks if it hasn't been applied yet. If it has been applied, its new tests move with this change.

## Migration Plan

Use `git mv` for all moves, then update the config and docs. Run the full offline suite and the integration suite, then commit.

Rollback: revert the commit.
