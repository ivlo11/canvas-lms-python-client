# Spec Delta

## ADDED Requirements

### Requirement: Media object and media track operations return typed models
Listing and updating a media object's tracks SHALL return a list of media track models. Updating a media object SHALL return a media object model. These apply to both the media object and media attachment routes. Each model SHALL keep the fields Canvas sends.

#### Scenario: Media tracks are typed
- **GIVEN** a media object with a caption track
- **WHEN** its tracks are listed
- **THEN** the result is a list of media track models, each with `id`, `locale`, `kind` and `media_object_id` equal to what Canvas sent

#### Scenario: Updated media object is typed
- **GIVEN** a media object owned by the caller
- **WHEN** its title is updated
- **THEN** the result is a media object model whose `title` is the new title

### Requirement: Generation reports unresolved documented models
When an operation's documented response names a model that Canvas does not define, spec generation SHALL report a warning naming the operation and the model, and SHALL still complete with that response untyped. Responses documented as a primitive, an inline object or prose SHALL NOT be reported.

#### Scenario: Undefined model is reported
- **GIVEN** an operation whose documented response is a list of a model name that no model definition provides
- **WHEN** the spec is generated
- **THEN** the output includes a warning naming that operation and model
- **AND** generation succeeds, and the operation's response is an untyped list

#### Scenario: Defined models are not reported
- **GIVEN** an operation whose documented response names a defined model, a namespaced model, or a schema class
- **WHEN** the spec is generated
- **THEN** no unresolved-model warning names that operation
