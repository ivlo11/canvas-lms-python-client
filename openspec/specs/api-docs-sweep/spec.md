# api-docs-sweep Specification

## Purpose

Defines how the audit's findings are fixed: in the controller documentation the client is generated from, so that every finding ends resolved or listed with a reason and the generated client parses every successful read.

## Requirements

### Requirement: Fixes are made in controller documentation
Every documentation fix SHALL be written to the `@model` or `@returns` documentation in the controllers. No correction layer SHALL be applied between the documentation and the generated spec.

#### Scenario: Wrapped list
- **GIVEN** an action documented as a list whose response and trace agree it is `{"sis_imports": [...]}`
- **WHEN** the sweep runs
- **THEN** the action's `@returns` documents the wrapper, and the generated client parses the response

#### Scenario: Float returned for a documented integer
- **GIVEN** a field documented as an integer with an observed float, such as `group_weight`
- **WHEN** the sweep runs
- **THEN** every definition of that field in that model is documented as a number

### Requirement: Types only widen
The sweep SHALL NOT narrow a documented type based on observed responses.

#### Scenario: Only whole numbers observed
- **GIVEN** a field documented as a number with only whole numbers observed
- **WHEN** the sweep runs
- **THEN** the field stays documented as a number

### Requirement: Absence does not remove documentation
The sweep SHALL NOT remove a documented field because no response contained it.

#### Scenario: Documented field never seen
- **GIVEN** a documented field that appears in no recorded response
- **WHEN** the sweep runs
- **THEN** the field stays documented and is reported for review

### Requirement: New fields require review
A field not already documented SHALL be added only after it is accepted in review. A rejected field SHALL be recorded as an exception with a reason.

#### Scenario: Field rejected in review
- **GIVEN** an undocumented field found in responses and rejected in review
- **WHEN** the sweep runs
- **THEN** the field isn't added to the documentation, and the exceptions file lists it

#### Scenario: Field accepted in review
- **GIVEN** an undocumented field accepted in review
- **WHEN** the sweep runs
- **THEN** the field is documented without an invented description, and listed as still needing one

### Requirement: Public status is not changed automatically
The sweep SHALL NOT add `@API` documentation to an action that lacks it.

#### Scenario: Undocumented action seen in traffic
- **GIVEN** an action without an `@API` tag that returned a response during a spec run
- **WHEN** the sweep runs
- **THEN** no documentation is added for it

### Requirement: Every API ends fixed or listed with a reason
After the sweep, every finding SHALL be either resolved in the documentation or listed in the exceptions file with a reason.

#### Scenario: Second audit
- **GIVEN** a completed sweep
- **WHEN** the audit runs again
- **THEN** no finding remains that is unresolved and missing from the exceptions file

### Requirement: The generated client parses every successful read
Every GET that returns a successful response on the seeded instance SHALL parse through the generated client without a validation error, for each configured role.

#### Scenario: Contract check
- **GIVEN** the client regenerated after the sweep
- **WHEN** the contract test calls every reachable GET as each role
- **THEN** no call raises a validation error
- **AND** the operations it couldn't reach are reported with a reason
