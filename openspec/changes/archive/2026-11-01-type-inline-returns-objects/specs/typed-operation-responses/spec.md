# Spec Delta

## ADDED Requirements

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
