# Spec Delta

## Purpose

Defines how the client handles model fields that Canvas documents as holding one of several types, so that every documented shape deserializes and undocumented shapes are still rejected.

## ADDED Requirements

### Requirement: Fields accept every documented type
When a model field is documented with several types, the client SHALL accept a value of any of those types and keep it as Canvas sent it.

#### Scenario: Primitive or model
- **GIVEN** a field documented as a string or a user
- **WHEN** Canvas sends either the string `"Instructure"` or a user object
- **THEN** the field holds that string, or a user model, and no validation error is raised

#### Scenario: Two primitives
- **GIVEN** a field documented as an integer or a string
- **WHEN** Canvas sends `5` or `"5"`
- **THEN** the field holds the value with the type Canvas sent

#### Scenario: Nullable model
- **GIVEN** a field documented as a model or null
- **WHEN** Canvas sends `null`
- **THEN** the field is `None` and no validation error is raised

### Requirement: Fields reject undocumented types
A field documented with several types SHALL still reject a value whose type matches none of them.

#### Scenario: Undocumented shape
- **GIVEN** a field documented as a string or a user
- **WHEN** a payload holds a number in that field
- **THEN** deserializing raises a validation error

### Requirement: Indistinguishable unions stay usable
When a field is documented as one of several models, which the client can't tell apart, the client SHALL type it as the first documented model instead of failing on every value.

#### Scenario: Two models
- **GIVEN** a field documented as one of two models
- **WHEN** Canvas sends an object for it
- **THEN** the object deserializes as the first documented model, and no "multiple matches" error is raised

### Requirement: Existing fields are unchanged
Fields documented with a single type, or with a single type plus null, SHALL keep their current client types.

#### Scenario: Regeneration without union changes
- **WHEN** the client is regenerated with this behavior
- **THEN** no model field type changes, and the `string|User` fields still accept a user or `"Instructure"`
