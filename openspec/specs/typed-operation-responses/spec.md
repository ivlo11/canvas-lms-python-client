# typed-operation-responses Specification

## Purpose

Defines the client contract for any Canvas operation whose documentation names a response model: the operation returns that model (or a list of it), regardless of how the model name is namespaced, and it stays untyped rather than failing when the named model does not exist.

## Requirements

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

### Requirement: Inline object responses are returned as objects
When an operation's Canvas documentation describes its response inline as an object (`{ ... }`), the client SHALL return that response as an object, either a model or a mapping, and never as a list. Every key and value Canvas sends for a mapping SHALL be preserved.

#### Scenario: Untypeable inline object keeps its data
- **GIVEN** an operation documented as `{Object}` with a prose description, such as fetching an AI conversation
- **WHEN** the operation is called and Canvas returns a JSON object
- **THEN** the result is a mapping holding every key and value Canvas sent, not a list of its key names

#### Scenario: Union and nested inline objects stay mappings
- **GIVEN** an operation whose inline object documents alternative shapes (`{ ... } | { ... }`) or an object nested inside a list, such as LTI configuration validation or the domain duplicate check
- **WHEN** the operation is called
- **THEN** the result is a mapping of the JSON object Canvas returned and no validation error is raised

#### Scenario: Inline object naming a missing model
- **GIVEN** an inline object whose entry names a model Canvas does not define
- **WHEN** the client is generated
- **THEN** the operation returns a mapping, not a list and not a partially typed model

### Requirement: Inline object responses with typed entries return a wrapper model
When every entry of an inline object response maps a key to an existing model, a list of an existing model, or a primitive type (integer, string, boolean or number, in any case, quoted or not), the client SHALL return a wrapper model with one attribute per key, typed accordingly. No attribute SHALL be required.

#### Scenario: List of models alongside a scalar
- **GIVEN** an account calendars response documented as `{ "account_calendars": [AccountCalendar], "total_results": "integer" }`
- **WHEN** the response is deserialized
- **THEN** the result is a wrapper model whose `account_calendars` is a list of account calendar models and whose `total_results` is an integer

#### Scenario: Model and list of models
- **GIVEN** a what-if grades update response documented as `{"grades": [Grades], "submission": Submission}`
- **WHEN** the response is deserialized
- **THEN** the result is a wrapper model whose `grades` is a list of grades models and whose `submission` is a submission model

#### Scenario: Scalar-only object
- **GIVEN** a content shares unread count response documented as `{ "unread_count": "integer" }`
- **WHEN** the response is deserialized
- **THEN** the result is a wrapper model whose `unread_count` is an integer

#### Scenario: Capitalized primitive with trailing description
- **GIVEN** a career experience switch response documented as `{experience: String} The newly set experience`
- **WHEN** the response is deserialized
- **THEN** the result is a wrapper model whose `experience` is a string

#### Scenario: Documented key missing from the response
- **GIVEN** a typed inline object response from which Canvas omits a documented key
- **WHEN** the response is deserialized
- **THEN** the wrapper model is returned with that attribute unset and no validation error is raised

### Requirement: Primitive literals in an inline object are typed by their value
When an inline object response documents a literal value instead of a type for an entry, the client SHALL type that attribute from the literal: `true` or `false` as boolean, a quoted value as string, and a whole number as integer. The entry SHALL otherwise be treated like a typed entry.

#### Scenario: Boolean literal
- **GIVEN** the push token deletion response documented as `{success: true}`
- **WHEN** the response is deserialized
- **THEN** the result is a wrapper model whose `success` is a boolean

#### Scenario: String literal
- **GIVEN** the discovery page token response documented as `{ "token": "eyJ..." }`
- **WHEN** the response is deserialized
- **THEN** the result is a wrapper model whose `token` is a string holding the token Canvas sent

### Requirement: Wrapper models are named after their controller and action
Each wrapper model the client generates SHALL be named after the Canvas controller and action that return it, in the form `<Controller><Action>Response`. Routes of the same action SHALL share one wrapper model. A wrapper's name SHALL NOT depend on any other operation or wrapper.

#### Scenario: Wrapper names for inline objects
- **WHEN** the client is generated
- **THEN** the account calendars list returns `AccountCalendarsApiIndexResponse` and the visible calendars count returns `AccountCalendarsApiVisibleCalendarsCountResponse`

#### Scenario: Identical shapes on different actions
- **GIVEN** two actions of one controller whose documented responses have the same shape, such as creating a poll and showing a poll
- **WHEN** the client is generated
- **THEN** each action returns its own wrapper model (`PollsCreateResponse`, `PollsShowResponse`) with the same attributes

#### Scenario: Adding an operation does not rename a wrapper
- **GIVEN** a generated client and a new Canvas action that returns a wrapper in the same controller
- **WHEN** the client is regenerated
- **THEN** every wrapper model that existed before keeps its name and attributes

### Requirement: Operations documented with a schema class return its model
When an operation's Canvas documentation names its response as a Ruby schema class (`Schemas::Docs::<Model>`), the client SHALL return the model that class defines, as it does for a model documented with `@model`. The operation SHALL NOT be returned untyped.

#### Scenario: Show user details is typed
- **GIVEN** the client is authenticated as any seeded user
- **WHEN** the caller's own details are fetched with the show user operation (`id="self"`)
- **THEN** the result is a user model, not a dict
- **AND** its `id` and `name` are the caller's

#### Scenario: Show user details keeps the documented fields
- **GIVEN** a user details response captured from Canvas that carries `permissions`, `effective_locale` and `uuid`
- **WHEN** it is deserialized into the user model
- **THEN** no validation error is raised and those fields hold the values Canvas sent

#### Scenario: Other user responses are unaffected
- **WHEN** the client is regenerated with this behavior
- **THEN** every other operation that returned a user model before still returns it, and no other operation's response type changes

### Requirement: Nested object properties are typed models
When a Canvas model documents a property as an object with its own fields, the client SHALL type that property as a nested model that keeps each documented field. The fields SHALL follow the same type rules as top-level properties. The property SHALL NOT be an untyped mapping.

#### Scenario: User permissions are typed
- **GIVEN** a show user details response captured from Canvas whose `permissions` object carries `can_update_name`, `can_update_avatar` and `limit_parent_app_web_access`
- **WHEN** it is deserialized into the user model
- **THEN** `permissions` is a nested model, not a dict
- **AND** each of the three fields is a boolean equal to the value Canvas sent

#### Scenario: Nested fields keep their types
- **GIVEN** a learning object dates response whose `peer_review_sub_assignment` carries dates and a list of overrides
- **WHEN** it is deserialized
- **THEN** `peer_review_sub_assignment` is a nested model whose dates are datetimes and whose overrides are assignment override models

#### Scenario: Objects without documented fields stay untyped
- **GIVEN** a model property documented as an object with no fields of its own
- **WHEN** the client is regenerated with this behavior
- **THEN** that property is still an untyped mapping, and no other model's fields change

### Requirement: Creating a grading period set returns the created set
Creating a grading period set SHALL return a wrapper model whose `grading_period_set` attribute is the created set as a single grading period set model, not a list.

#### Scenario: Create a set
- **GIVEN** a root account the caller can manage
- **WHEN** a grading period set is created with a title
- **THEN** the result is a wrapper model whose `grading_period_set` is a grading period set model with the given title and the identifier Canvas assigned
