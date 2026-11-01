# integration-testing Specification

## Purpose

Provides an opt-in way to run the client's tests against a live Canvas instance (for example, the seeded dockerized canvas-lms) without affecting the default offline test run.

## Requirements

### Requirement: Integration tests are opt-in
Tests marked as integration tests SHALL run only when the test run is started with the `--integration` option. Without that option they SHALL be reported as skipped, and the rest of the suite SHALL run unchanged.

#### Scenario: Default test run
- **WHEN** a developer runs `pdm run pytest` without `--integration`
- **THEN** every integration-marked test is reported as skipped with a reason that mentions `--integration`
- **AND** no network request is made to a Canvas instance

#### Scenario: Integration run requested
- **WHEN** a developer runs `pdm run pytest --integration` with valid Canvas credentials configured
- **THEN** integration-marked tests are collected and executed

### Requirement: Integration credentials come from the environment
The integration harness SHALL read the Canvas base URL from `CANVAS_BASE_URL` and the API token from `CANVAS_API_TOKEN`. Credentials SHALL NOT be hard-coded in test sources.

#### Scenario: Credentials missing
- **WHEN** `--integration` is passed but `CANVAS_BASE_URL` or `CANVAS_API_TOKEN` is unset
- **THEN** integration tests are skipped with a reason naming the missing variables

#### Scenario: Credentials present
- **WHEN** both variables are set
- **THEN** the client used by integration tests targets `CANVAS_BASE_URL` and sends `CANVAS_API_TOKEN` as a bearer token

### Requirement: Shared authenticated client for integration tests
The harness SHALL give each integration test an authenticated async API client and SHALL close that client when the test finishes, whether the test passes or fails.

#### Scenario: Client lifecycle
- **WHEN** an integration test requests the shared client
- **THEN** it receives an open, authenticated client
- **AND** the client's HTTP session is closed after the test completes

### Requirement: Optional admin credentials for admin-scoped integration tests
Integration tests that require account-administrator permissions SHALL authenticate with a token read from `CANVAS_ADMIN_API_TOKEN`, using the same `CANVAS_BASE_URL`. When that variable is unset, only those tests SHALL be skipped. Tests that use `CANVAS_API_TOKEN` SHALL be unaffected.

#### Scenario: Admin token missing
- **GIVEN** `--integration` is passed and `CANVAS_BASE_URL` and `CANVAS_API_TOKEN` are set
- **WHEN** `CANVAS_ADMIN_API_TOKEN` is unset
- **THEN** admin-scoped integration tests are skipped with a reason naming `CANVAS_ADMIN_API_TOKEN`
- **AND** the other integration tests still run

#### Scenario: Admin token present
- **WHEN** `CANVAS_BASE_URL` and `CANVAS_ADMIN_API_TOKEN` are set
- **THEN** admin-scoped integration tests receive an open, authenticated client that sends `CANVAS_ADMIN_API_TOKEN` as a bearer token, and that client is closed after each test

### Requirement: Integration tests skip when seeded data is absent
An integration test whose precondition depends on seeded data SHALL be skipped, with a reason naming the missing data, when that data is not present. It SHALL NOT fail or pass vacuously.

#### Scenario: No seeded rubric
- **WHEN** an integration test needs an active rubric and the seeded instance has none in the target context
- **THEN** the test is reported as skipped with a reason that says no rubric was found
