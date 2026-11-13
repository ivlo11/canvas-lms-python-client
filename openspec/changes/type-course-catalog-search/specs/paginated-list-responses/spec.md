# Spec Delta

## ADDED Requirements

### Requirement: Course catalog search yields typed entries
Listing all courses in the public course catalog SHALL yield catalog course entries from both the page iterator and the all-items iterator, across all result pages. Each entry's `course` SHALL be a typed catalog course that keeps the public fields Canvas sent.

#### Scenario: Catalog courses are typed
- **GIVEN** an account with the course catalog enabled and an indexed, available course
- **WHEN** the catalog is listed with the all-items iterator
- **THEN** each item is a catalog course entry whose `course` is a catalog course model
- **AND** that course's `id`, `name` and `workflow_state` equal what Canvas sent, and are not unset because of the `course` root key

#### Scenario: Search filter applies
- **GIVEN** a catalog with an indexed course
- **WHEN** the catalog is listed with a `search` term from that course's name, and again with a term that matches nothing
- **THEN** the first listing includes that course and the second yields no items

#### Scenario: Catalog disabled
- **GIVEN** an account with the course catalog disabled
- **WHEN** the catalog is listed
- **THEN** the client raises Canvas's unauthorized error rather than returning an empty or untyped result

### Requirement: Catalog models omit internal course columns
The catalog course model SHALL NOT expose internal columns that Canvas includes in the raw record, such as the self-enrollment code, SIS and integration identifiers, or course settings. A response that contains them SHALL still deserialize without a validation error.

#### Scenario: Internal columns are dropped
- **GIVEN** a captured catalog response whose records include internal columns
- **WHEN** it is deserialized
- **THEN** no validation error is raised, and the catalog course model has no `self_enrollment_code`, `sis_source_id` or `settings` attribute
