# Spec Delta

## ADDED Requirements

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
