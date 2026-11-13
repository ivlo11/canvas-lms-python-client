# api-docs-enforcement Specification

## Purpose

Defines the checks that keep Canvas's `@API` documentation matching what the API returns as code changes, failing only on findings the exceptions file doesn't list.

## Requirements

### Requirement: Missing or malformed documentation is flagged in the changed file
A custom cop SHALL flag an `@API` action with no `@returns`, and malformed `@model` JSON, when a controller is linted.

#### Scenario: New action without a return type
- **GIVEN** a controller change adding an `@API` action with no `@returns`
- **WHEN** `script/rlint` runs on it
- **THEN** the cop reports an offense on that action

### Requirement: Documentation is checked against code
`script/api_docs_lint` SHALL report documented responses that contradict the traced code, without needing a database.

#### Scenario: Controller adds a wrapper
- **GIVEN** an action documented as a list, whose `render json:` is changed to a hash wrapper
- **WHEN** the lint runs on the change
- **THEN** it reports the contradiction and exits non-zero

#### Scenario: Shared helper changes
- **GIVEN** a change that adds a key to a helper in `lib/api/v1`
- **WHEN** the lint runs on the change
- **THEN** every documented action reaching that helper is checked, and each one whose model lacks the key is reported

### Requirement: Documentation is checked against spec responses
When enabled, the API spec suite SHALL compare responses from `raw_api_call` with the documented model and report contradictions.

#### Scenario: Spec returns an undocumented field
- **GIVEN** the response check is enabled
- **WHEN** an API spec receives a successful response with a field its model doesn't document
- **THEN** the example fails and names the action and field

#### Scenario: Check disabled
- **GIVEN** the response check is not enabled
- **WHEN** an API spec runs
- **THEN** behavior and results are unchanged

### Requirement: Checks fail only on new findings
Each check SHALL pass on any finding listed in the exceptions file, and every entry SHALL state a reason.

#### Scenario: Listed finding
- **GIVEN** a finding listed in the exceptions file with a reason
- **WHEN** a check encounters it
- **THEN** the check doesn't fail

#### Scenario: Entry without a reason
- **GIVEN** an exceptions entry with no reason
- **WHEN** a check loads the file
- **THEN** the check fails and names the entry

#### Scenario: Stale entry
- **GIVEN** an exceptions entry that no longer matches any finding
- **WHEN** the full audit runs
- **THEN** the entry is reported for removal
