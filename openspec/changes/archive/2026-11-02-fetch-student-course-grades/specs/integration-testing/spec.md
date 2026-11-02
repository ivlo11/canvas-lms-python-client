# Spec Delta

## ADDED Requirements

### Requirement: Optional student credentials for student-scoped integration tests
Integration tests that must act as a student SHALL authenticate with a token read from `CANVAS_STUDENT_API_TOKEN`, using the same `CANVAS_BASE_URL`. When that variable is unset, only those tests SHALL be skipped. Tests that use the observer or admin tokens SHALL be unaffected.

#### Scenario: Student token missing
- **GIVEN** `--integration` is passed and `CANVAS_BASE_URL` is set
- **WHEN** `CANVAS_STUDENT_API_TOKEN` is unset
- **THEN** student-scoped integration tests are skipped with a reason naming `CANVAS_STUDENT_API_TOKEN`
- **AND** the other integration tests still run

#### Scenario: Student token present
- **WHEN** `CANVAS_BASE_URL` and `CANVAS_STUDENT_API_TOKEN` are set
- **THEN** student-scoped integration tests receive an open, authenticated client that sends `CANVAS_STUDENT_API_TOKEN` as a bearer token, and that client is closed after each test
