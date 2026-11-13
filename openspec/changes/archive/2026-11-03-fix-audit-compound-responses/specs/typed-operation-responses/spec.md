# Spec Delta

## ADDED Requirements

### Requirement: Inline object entries documented as object are untyped mappings
When an inline object response documents an entry's value as `object`, that entry SHALL be an untyped mapping. It SHALL NOT prevent the other entries from being typed or the response from being a wrapper model.

#### Scenario: Mixed typed and mapping entries
- **GIVEN** an operation documented to return an inline object with a list of a defined model and two entries documented as `object`
- **WHEN** a response with arbitrary keys in the two `object` entries is deserialized
- **THEN** the result is a wrapper model whose list entry holds typed models, and whose two other entries are mappings equal to what Canvas sent
