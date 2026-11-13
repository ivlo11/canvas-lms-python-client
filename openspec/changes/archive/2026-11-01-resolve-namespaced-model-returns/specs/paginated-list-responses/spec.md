# Spec Delta

## MODIFIED Requirements

### Requirement: Paginated operations with a documented model yield typed items
For each paginated operation whose response is documented as a list of an existing Canvas model, the client SHALL yield one list of that model per page from the page iterator, and SHALL yield individual model instances from the all-items iterator, across all result pages.

#### Scenario: Appointment groups are typed
- **GIVEN** the client is authenticated against a Canvas instance where the caller can see at least one appointment group
- **WHEN** appointment groups are listed with the all-items iterator
- **THEN** each yielded item is an appointment group model with an integer `id`

#### Scenario: Appointment group participants are typed
- **GIVEN** an appointment group whose participant type is `User` (or `Group`)
- **WHEN** its user (or group) participants are listed with the all-items iterator
- **THEN** each yielded item is a user (or group) model with an integer `id`
- **AND** listing the participant type that does not match the group returns an empty result without error

#### Scenario: Rubrics are typed in both contexts
- **GIVEN** an account and a course that each have at least one active rubric
- **WHEN** rubrics are listed for the account and for the course with the all-items iterator
- **THEN** each yielded item is a rubric model with an integer `id`

#### Scenario: LTI launch definitions are typed
- **GIVEN** a course (or account) with at least one LTI tool installed for a requested placement
- **WHEN** launch definitions are listed for that course (or account) with the all-items iterator
- **THEN** at least one item is yielded
- **AND** each item is a launch definition model whose `definition_type` and `definition_id` are set

#### Scenario: LTI deployments, context controls and resource links are typed
- **GIVEN** an LTI registration with a deployment, a context control and a resource link visible to the caller
- **WHEN** deployments, a deployment's context controls, the account's context controls, and a course's resource links are listed with the all-items iterator
- **THEN** each yielded item is the corresponding LTI deployment, context control or resource link model

#### Scenario: Results span multiple pages
- **GIVEN** a typed paginated operation with more items than fit on one page
- **WHEN** it is listed with a page size smaller than the total
- **THEN** items from every page are yielded, with no duplicates

## ADDED Requirements

### Requirement: Paginated operations whose documented model is undefined yield raw items
For each paginated operation whose response is documented as a list of a model that Canvas does not define, the client SHALL still yield each page's items as untyped objects instead of yielding nothing.

#### Scenario: LTI registration history yields raw items
- **GIVEN** an LTI registration with at least one history entry
- **WHEN** its history is listed with the all-items iterator
- **THEN** at least one item is yielded
- **AND** each item is a mapping, because `Lti::RegistrationHistoryEntry` has no documented model

## REMOVED Requirements

### Requirement: Paginated operations with a documented but unresolved model yield raw items
**Reason**: Its only example, LTI launch definitions, was untyped because of a generator bug (namespaced model names were not resolved), not because the model was missing. That bug is now fixed, and launch definitions are covered by the typed-items requirement.
**Migration**: The remaining behavior (documented model is undefined, so items are untyped but still yielded) continues under "Paginated operations whose documented model is undefined yield raw items".
