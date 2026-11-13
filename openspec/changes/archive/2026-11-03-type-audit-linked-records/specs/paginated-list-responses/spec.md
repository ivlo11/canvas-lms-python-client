# Spec Delta

## MODIFIED Requirements

### Requirement: Audit log queries yield compound pages with typed events
Every course audit, grade change audit and authentication audit query SHALL return, and its page iterator SHALL yield, a page model with three parts:
- `events`: a list of the matching event model
- `links`: an untyped mapping of link templates
- `linked`: the related records

For grade change and authentication queries, `linked` SHALL be a model whose lists hold typed records:
- grade change: `assignments`, `courses`, `users` and `page_views`
- authentication: `logins`, `accounts`, `users` and `page_views`

For course audit queries, `linked` SHALL stay an untyped mapping, because Canvas sends its record ids as strings.

A page SHALL deserialize without a validation error whatever ids, grades and link values Canvas sends.

#### Scenario: Grade change audit pages are typed
- **GIVEN** a course with at least one grade change
- **WHEN** its grade change log is listed with the page iterator
- **THEN** each page is a page model whose `events` are grade change event models
- **AND** each event's `version_number`, `points_possible_after` and link ids equal what Canvas sent, and no validation error is raised

#### Scenario: Grade change linked records are typed
- **GIVEN** a course with at least one grade change
- **WHEN** its grade change log is listed with the page iterator
- **THEN** each page's `linked` holds assignment, course and user models whose `id` values are integers equal to what Canvas sent
- **AND** every event's `links.assignment` and `links.course` id appears in `linked.assignments` and `linked.courses`

#### Scenario: Course audit pages are typed
- **GIVEN** a course with at least one recorded course event
- **WHEN** its course audit log is listed with the page iterator
- **THEN** each page's `events` are course event models whose `event_type` is set and whose link values are strings
- **AND** `linked` is a mapping equal to what Canvas sent

#### Scenario: Authentication audit pages are typed
- **GIVEN** a user who has logged in
- **WHEN** that user's authentication log is listed with the page iterator
- **THEN** each page's `events` are authentication event models with an `id`, `created_at`, `event_type` and `links` whose `login`, `account` and `user` are integers

#### Scenario: Authentication linked records are typed
- **GIVEN** a user who has logged in
- **WHEN** that user's authentication log is listed with the page iterator
- **THEN** each page's `linked` holds login, account and user models
- **AND** every event's `links.login`, `links.account` and `links.user` id appears in the matching `linked` list

#### Scenario: Linked page views are typed
- **GIVEN** a grade change or authentication page whose `linked.page_views` holds a page view
- **WHEN** the page is deserialized
- **THEN** each page view is a page view model with its `id`, `url` and `links` set

#### Scenario: Empty audit page
- **GIVEN** a course with no recorded course events
- **WHEN** its course audit log is listed
- **THEN** one page is yielded whose `events` is an empty list, and no validation error is raised
