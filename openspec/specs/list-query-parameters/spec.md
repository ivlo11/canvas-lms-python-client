# list-query-parameters Specification

## Purpose

Defines how the client sends list-valued query parameters to Canvas so that Canvas applies every value, instead of ignoring the filter or failing the request.

## Requirements

### Requirement: List query parameters use Canvas's bracket form
For every operation whose Canvas documentation describes a query parameter as a list, the client SHALL send each value as a separate `name[]=value` pair, so that Canvas receives the whole list.

#### Scenario: Launch definitions filtered by placements
- **GIVEN** a course with an installed LTI tool that has a `course_navigation` placement
- **WHEN** launch definitions are listed for that course with placements `course_navigation` and `account_navigation`
- **THEN** the request sends `placements[]=course_navigation&placements[]=account_navigation`
- **AND** at least one launch definition is returned, and no error is raised

#### Scenario: A single-value list
- **WHEN** a list query parameter is given a list with one value
- **THEN** the request sends that value as `name[]=value`

#### Scenario: Scalar query parameters are unaffected
- **WHEN** an operation is called with a query parameter that is not a list (for example `per_page`)
- **THEN** the request sends it as `name=value`, as before

### Requirement: Calling code does not change
The client SHALL keep the same method signatures and argument names for operations with list query parameters. Only the parameter name sent on the wire changes.

#### Scenario: Existing call keeps working
- **GIVEN** code that calls a list operation with `include=["term"]`
- **WHEN** the client is regenerated with this behavior
- **THEN** the same call works without changes and sends `include[]=term`
