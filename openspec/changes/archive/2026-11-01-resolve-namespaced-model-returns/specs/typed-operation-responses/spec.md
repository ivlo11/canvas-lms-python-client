# Spec Delta

## Purpose

Defines the client contract for any Canvas operation whose documentation names a response model: the operation returns that model (or a list of it), regardless of how the model name is namespaced, and it stays untyped rather than failing when the named model does not exist.

## ADDED Requirements

### Requirement: Operations return the documented model
For each operation whose Canvas documentation names an existing model as its response, the client SHALL return an instance of that model, or a list of instances when the documentation describes a list. This SHALL hold whether the model name is namespaced (for example `Lti::Deployment`) or not.

#### Scenario: Namespaced single-object response
- **GIVEN** an LTI deployment that the caller can read
- **WHEN** the deployment is fetched with the show operation
- **THEN** the result is an LTI deployment model, not a dict

#### Scenario: Namespaced list response
- **GIVEN** an LTI registration with at least one deployment in the caller's account
- **WHEN** its deployments are listed
- **THEN** the result is a list of LTI deployment models

#### Scenario: Non-namespaced responses are unaffected
- **WHEN** the client is regenerated with this behavior
- **THEN** every operation that returned a non-namespaced model before still returns the same model type

### Requirement: Documented list shape matches the response
When an operation's response is a JSON array, its documented response type SHALL be a list, so that the client deserializes the array rather than failing on it.

#### Scenario: Bulk creation returns a list
- **GIVEN** a valid request to create several context controls (or resource links) at once
- **WHEN** the bulk-create operation is called
- **THEN** the result is a list of context control (or resource link) models, one per created record, and no validation error is raised

### Requirement: Unresolvable documented models stay untyped
When an operation's documentation names a model that is not defined, the client SHALL return the response untyped instead of raising an error or returning nothing.

#### Scenario: Registration update request without a model
- **GIVEN** an LTI registration with a pending update request
- **WHEN** the latest update request is fetched
- **THEN** the result is the raw response mapping and no validation error is raised

### Requirement: Typed LTI models deserialize live Canvas data
For each LTI model the client types, the client SHALL deserialize every response Canvas actually returns into that model without a validation error. Field types SHALL match the JSON types Canvas sends.

#### Scenario: Launch definition ids are integers
- **GIVEN** a course with an installed LTI tool that has a launch placement
- **WHEN** launch definitions are listed for that course and placement
- **THEN** each item is a launch definition model whose `definition_id` holds the integer tool id Canvas sent

#### Scenario: Records created by Instructure
- **GIVEN** an LTI registration, account binding or overlay version whose creator can read Site Admin
- **WHEN** it is fetched
- **THEN** `created_by` (and `updated_by`, where present) holds the string `"Instructure"` and no validation error is raised
- **AND** a record created by any other user holds a user model in the same field

#### Scenario: Live-shaped payloads are accepted
- **GIVEN** JSON payloads captured from a seeded Canvas for deployments, context controls, launch definitions, registrations, registration account bindings, overlay versions and resource links
- **WHEN** each payload is deserialized into its model
- **THEN** no validation error is raised and every documented field Canvas sent holds the value Canvas sent
