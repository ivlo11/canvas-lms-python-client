# Spec Delta

## ADDED Requirements

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
