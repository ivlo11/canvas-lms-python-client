# Spec Delta

## ADDED Requirements

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
