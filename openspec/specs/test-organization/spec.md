# test-organization Specification

## Purpose
Defines where the client's generated and hand-written tests live, so that a test's origin (generated or custom) and kind (unit or integration) can be told from its location, and so that regenerating the client never touches custom tests.

## Requirements

### Requirement: Generated tests live only at the test root
The client's test directory root SHALL contain only files produced by the generator. Every hand-written test, fixture and pytest configuration file SHALL live under the `custom` subdirectory of the test directory.

#### Scenario: Inspecting the test root
- **WHEN** the files directly in the client's test directory are listed
- **THEN** every one of them is listed in the generator's file manifest, and the only directory there besides caches is `custom`

#### Scenario: Regeneration leaves custom tests untouched
- **GIVEN** the custom test directory with its unit tests, integration tests and fixtures
- **WHEN** the client is regenerated and orphaned generated files are removed
- **THEN** no file under the custom test directory is created, changed or deleted

### Requirement: Custom tests are grouped by kind
Hand-written tests SHALL live in `custom/unit` when they run offline, and in `custom/integration` when they need a live Canvas instance. A custom test file SHALL NOT mix the two kinds.

#### Scenario: Locating integration tests
- **WHEN** a developer looks for the tests that call a live Canvas instance
- **THEN** all of them, and only them, are in files under `custom/integration`

### Requirement: Integration tests are identified by location
Every test collected from `custom/integration` SHALL be treated as an integration test, so it runs only with the `--integration` option, whether or not the test or its module declares the integration marker itself.

#### Scenario: Unmarked test in the integration folder
- **GIVEN** a test under `custom/integration` without its own integration marker
- **WHEN** `pdm run pytest` runs without `--integration`
- **THEN** that test is reported as skipped with a reason mentioning `--integration`

#### Scenario: Integration run requested
- **WHEN** `pdm run pytest --integration` runs with Canvas credentials configured
- **THEN** the tests under `custom/integration` are executed

### Requirement: Custom tests run on their own
Running pytest on the custom test directory SHALL collect every custom test and no generated test, and the `--integration` option SHALL be accepted in that run.

#### Scenario: Custom-only offline run
- **WHEN** a developer runs `pdm run pytest src/canvas_lms_python_client/test/custom`
- **THEN** only the custom unit and integration tests are collected, the unit tests run, and the integration tests are skipped

#### Scenario: Full run
- **WHEN** a developer runs `pdm run pytest` with no path
- **THEN** both the generated tests and the custom tests are collected, and `--integration` is accepted
