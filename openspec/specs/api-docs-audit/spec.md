# api-docs-audit Specification

## Purpose

Defines how Canvas's `@API` documentation is audited against what the API returns: every documented action gets a findings record built from recorded responses, GET probes and a trace of its code, with no response values or credentials kept.

## Requirements

### Requirement: Every documented action has a findings record
The audit SHALL produce one record for every action tagged `@API`, with an evidence status of verified, static or none.

#### Scenario: Action with a recorded response
- **GIVEN** a documented action that returned a successful response during a spec run or a GET probe
- **WHEN** the audit runs
- **THEN** its status is verified

#### Scenario: Action with only a code trace
- **GIVEN** a documented action with no recorded successful response and a usable trace of its code
- **WHEN** the audit runs
- **THEN** its status is static

#### Scenario: Action with no evidence
- **GIVEN** a documented action with no recorded response and no usable trace
- **WHEN** the audit runs
- **THEN** it still appears in the findings with status none

### Requirement: Evidence never contains response values or credentials
Recorded evidence and findings SHALL contain only key names, JSON type names, status codes, roles and action names.

#### Scenario: Response containing a token
- **GIVEN** a response whose body contains a token value
- **WHEN** the response is recorded
- **THEN** the record holds the key name and its type, and not the value

### Requirement: Reads are probed as each role and writes come only from specs
The audit SHALL probe GET operations as each configured role against the seeded instance, and SHALL NOT send POST, PUT, PATCH or DELETE requests to it.

#### Scenario: Evidence for a write
- **GIVEN** a documented POST action
- **WHEN** the audit gathers evidence
- **THEN** any response evidence comes from the spec suite

#### Scenario: Findings by role
- **GIVEN** responses recorded as a student and as an observer
- **WHEN** the findings are filtered by a role
- **THEN** only actions with a successful response for that role are listed as verified for it

### Requirement: The audit finds the known bugs
The audit SHALL find every benchmark bug in the design when run against the documentation from before the fixes.

#### Scenario: Benchmark run
- **GIVEN** the documentation at `upstream/master`
- **WHEN** the audit runs without manual input
- **THEN** each benchmark bug appears in the findings, or is reported as a named miss

### Requirement: String-ID responses don't produce type conflicts
Responses to requests that ask for string IDs SHALL NOT be used to compare field types.

#### Scenario: Spec requesting string IDs
- **GIVEN** a spec that requests `application/json+canvas-string-ids`
- **WHEN** its response is compared with an `id` documented as an integer
- **THEN** no type conflict is reported
