# Spec Delta

## Purpose

Defines the client contract for paginated Canvas list operations: every result page is deserialized into the documented item type and yielded to the caller, and an operation never ends silently with no items because its response type is undocumented.

## ADDED Requirements

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

#### Scenario: Results span multiple pages
- **GIVEN** a typed paginated operation with more items than fit on one page
- **WHEN** it is listed with a page size smaller than the total
- **THEN** items from every page are yielded, with no duplicates

### Requirement: Paginated operations with a documented but unresolved model yield raw items
For each paginated operation whose response is documented as a list but whose item model the spec does not resolve, the client SHALL still yield each page's items as untyped objects instead of yielding nothing.

#### Scenario: LTI launch definitions yield items
- **GIVEN** a course (or account) with at least one LTI tool installed for a requested placement
- **WHEN** launch definitions are listed for that course (or account) with the all-items iterator
- **THEN** at least one item is yielded
- **AND** each item is a mapping that contains `definition_type` and `definition_id`

### Requirement: Undocumented paginated responses are tracked
Every paginated operation in the generated client SHALL have a response type for its successful response, except operations named on an explicit allowlist of known-undocumented operations. The allowlist SHALL NOT contain any operation that has a response type.

#### Scenario: New undocumented paginated operation
- **GIVEN** a regenerated client in which a paginated operation not on the allowlist has no response type
- **WHEN** the offline test suite runs
- **THEN** a test fails and names that operation

#### Scenario: Allowlisted operation becomes documented
- **GIVEN** an allowlisted operation that now has a response type after regeneration
- **WHEN** the offline test suite runs
- **THEN** a test fails, naming the operation that should be removed from the allowlist

#### Scenario: Operations fixed by this change are not allowlisted
- **WHEN** the offline test suite runs against the regenerated client
- **THEN** none of the appointment group, rubric, or LTI launch definition list operations is on the allowlist, and the suite passes
