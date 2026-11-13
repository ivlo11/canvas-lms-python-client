# Spec Delta

## ADDED Requirements

### Requirement: Course catalog search yields typed entries
Listing all courses in the public course catalog SHALL yield catalog course entries from both the page iterator and the all-items iterator, across all result pages. Each entry's `course` SHALL be a typed catalog course that keeps the fields Canvas sent.

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
- **THEN** the client raises Canvas's unauthorized (401) or forbidden (403) error rather than returning an empty or untyped result

### Requirement: Catalog models type every returned column
The catalog course model SHALL type every column Canvas returns in the catalog record, including ones that look internal, such as the self-enrollment code, SIS and integration identifiers, and course settings. A column Canvas has only sent as null SHALL be nullable.

#### Scenario: Every column is typed
- **GIVEN** a captured catalog response
- **WHEN** it is deserialized
- **THEN** no validation error is raised, and every key of each record is a typed attribute of the catalog course model, including `self_enrollment_code`, `sis_source_id` and `settings`

#### Scenario: Null-only columns stay nullable
- **GIVEN** a catalog record whose `start_at`, `public_description` or `self_enrollment_code` is null
- **WHEN** it is deserialized
- **THEN** no validation error is raised, and the attribute is `None`
