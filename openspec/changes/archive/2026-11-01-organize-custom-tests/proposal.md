# Proposal

## Why

The 8 hand-written test files sit among about 800 generated ones in one flat `src/canvas_lms_python_client/test/` directory, and their names look alike. The only record of which tests are custom is the `.openapi-generator-ignore` list and the README copy of it. You can't tell which files hold integration tests without opening them, and running only the custom tests means naming each file.

## What Changes

- Custom tests move to `src/canvas_lms_python_client/test/custom/`. Every file at the `test/` root is generated, as it is today:
  ```
  test/
  ├── __init__.py, test_*_api.py, test_<model>.py      generated (unchanged)
  └── custom/
      ├── conftest.py
      ├── unit/          test_pagination.py, test_paginated_response_types.py,
      │                  test_inline_object_responses.py, test_lti_model_payloads.py,
      │                  test_list_query_params.py, test_api_operation_coverage.py,
      │                  fixtures/lti/
      └── integration/   test_observees.py, test_paginated_models.py
  ```
- The integration files drop their `integration_` prefix: `test_integration_observees.py` → `integration/test_observees.py`, and `test_integration_paginated_models.py` → `integration/test_paginated_models.py`.
- **A test's folder decides whether it's an integration test.** Every test under `custom/integration/` is an integration test, so it runs only with `--integration`, with or without its own marker. The existing opt-in behavior and credentials handling are unchanged.
- **The custom tests run on their own:** `pdm run pytest src/canvas_lms_python_client/test/custom` runs the 217 custom tests without the about 3,600 generated ones.
- **Generator and config:**
  - No generator configuration or template changes, and no regeneration.
  - The `test/…` entries in `src/.openapi-generator-ignore` are removed, because the generator never writes into `custom/`.
  - `pyproject.toml` `testpaths` lists `custom/` first, so `--integration` stays registered.
- **README:**
  - "File Ownership" becomes "everything at the `test/` root is generated; `test/custom/` is custom".
  - The test commands are updated, including the stale `pytest test/test_pagination.py` path.

## Capabilities

### New Capabilities
- `test-organization`: where generated and custom tests live, how integration tests are identified by location, and that custom tests can be run apart from generated ones.

### Modified Capabilities
<!-- None. integration-testing requirements (opt-in, credentials, shared clients, seeded-data skips) are unchanged; folder-based identification is added under test-organization. -->

## Impact

- **canvas-lms-python-client only:**
  - Files moved with `git mv`, so history is kept.
  - `pyproject.toml` (`testpaths`, import mode).
  - `src/.openapi-generator-ignore`.
  - `README.md`.
  - A new `custom/conftest.py` that holds today's `test/conftest.py` content plus the folder-based integration marking.
- **No canvas-lms changes.** No generated code or test content changes, other than the moved files' paths.
- **In-flight change:** `correct-grading-period-set-and-quiz-event-docs` tasks 3.2 and 3.3 name `test/test_paginated_response_types.py` and `test/test_integration_paginated_models.py`. If this change lands first, those tasks are updated to the new paths, as this change's tasks say.
