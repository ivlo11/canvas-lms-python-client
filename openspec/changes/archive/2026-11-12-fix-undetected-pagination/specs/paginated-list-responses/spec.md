# Spec Delta

## ADDED Requirements

### Requirement: Operations that paginate through a helper are exposed as paginated
An operation whose action paginates its results SHALL offer page parameters and a page iterator, whether the action paginates directly, through a helper in its controller, through a shared API helper, or with JSON:API pagination. List responses SHALL also offer the all-items iterator.

#### Scenario: Pagination in a shared helper
- **GIVEN** a course whose gradebook history spans more than one page
- **WHEN** its history days are listed with the all-items iterator and a page size of 1
- **THEN** items from more than one page are yielded, and together they cover every date in the history

#### Scenario: JSON:API pagination
- **GIVEN** an account with more grading periods than one page holds
- **WHEN** they are listed with the page iterator and a page size of 1
- **THEN** more than one page is yielded, and each is a typed grading periods page

#### Scenario: Helper called without parentheses
- **GIVEN** an action that calls a paginating helper in its controller with no parentheses or arguments
- **WHEN** the spec is generated
- **THEN** that operation has page parameters and is marked as paginated

### Requirement: Operations that do not paginate are not marked as paginated
An operation SHALL NOT be marked as paginated only because its source mentions a word that matches a paginating method, whether in a string, as a local variable, or as a method called on another object. Every operation already marked as paginated SHALL remain so.

#### Scenario: Single-record reads stay unpaginated
- **WHEN** the client is regenerated
- **THEN** reads such as showing a course, a section, a group or a submission have no page iterator

#### Scenario: Matching word in a SQL string
- **GIVEN** an action whose SQL string mentions the name of a paginating action in its controller
- **WHEN** the spec is generated
- **THEN** that operation isn't marked as paginated

#### Scenario: Newly detected undocumented operations are tracked
- **GIVEN** a newly paginated operation with no documented response type
- **WHEN** the offline test suite runs
- **THEN** it passes only if that operation is on the allowlist of known-undocumented operations
