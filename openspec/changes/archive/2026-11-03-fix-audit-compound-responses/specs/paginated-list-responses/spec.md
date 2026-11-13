# Spec Delta

## ADDED Requirements

### Requirement: Audit log queries yield compound pages with typed events
Every course audit, grade change audit and authentication audit query SHALL return, and its page iterator SHALL yield, a page model with three parts:
- `events`: a list of the matching event model
- `links`: an untyped mapping of link templates
- `linked`: an untyped mapping of the related records

A page SHALL deserialize without a validation error whatever ids, grades and link values Canvas sends.

#### Scenario: Grade change audit pages are typed
- **GIVEN** a course with at least one grade change
- **WHEN** its grade change log is listed with the page iterator
- **THEN** each page is a page model whose `events` are grade change event models
- **AND** each event's `version_number`, `points_possible_after` and link ids equal what Canvas sent, and no validation error is raised

#### Scenario: Course audit pages are typed
- **GIVEN** a course with at least one recorded course event
- **WHEN** its course audit log is listed with the page iterator
- **THEN** each page's `events` are course event models whose `event_type` is set and whose link values are strings

#### Scenario: Authentication audit pages are typed
- **GIVEN** a user who has logged in
- **WHEN** that user's authentication log is listed with the page iterator
- **THEN** each page's `events` are authentication event models with an `id`, `created_at`, `event_type` and `links` whose `login`, `account` and `user` are integers

#### Scenario: Empty audit page
- **GIVEN** a course with no recorded course events
- **WHEN** its course audit log is listed
- **THEN** one page is yielded whose `events` is an empty list, and no validation error is raised
