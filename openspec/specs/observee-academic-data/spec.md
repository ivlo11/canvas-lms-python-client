# observee-academic-data Specification

## Purpose

Defines the client contract an observer (for example, a parent) relies on to read the students they observe, those students' courses, and those students' assignments, all returned as typed models across every result page.

## Requirements

### Requirement: Observer can list their observees
When authenticated as an observer, the client SHALL return every user the observer is linked to, using `self` as the user id, as typed user models with integer ids, across all result pages.

#### Scenario: Observer with linked students
- **GIVEN** the client is authenticated with a token belonging to an observer linked to at least one student
- **WHEN** the observer's observees are listed for user `self`
- **THEN** a non-empty list of user models is returned
- **AND** every user has an integer `id` and a non-empty `name`

#### Scenario: Results span multiple pages
- **GIVEN** the observer has more observees than fit on one page
- **WHEN** observees are listed with a page size smaller than the total
- **THEN** observees from every page are returned, with no duplicates

### Requirement: Observer can list each observee's courses
For each observee, the client SHALL return that observee's courses as typed course models, across all result pages, when called with the observer's credentials.

#### Scenario: Courses per observee
- **GIVEN** an observee returned by the observee listing
- **WHEN** courses are listed for that observee's id
- **THEN** a list of course models is returned, each with an integer `id`
- **AND** the request succeeds with the observer's token (no authorization error)

#### Scenario: Seeded observee has courses
- **GIVEN** the seeded test environment
- **WHEN** courses are listed for all observees
- **THEN** at least one observee has at least one course

### Requirement: Observer can list an observee's assignments in a course
For each observee course, the client SHALL return that observee's assignments for the course as typed assignment models, across all result pages. It SHALL NOT return an untyped or empty result.

#### Scenario: Assignments per observee course
- **GIVEN** an observee and one of that observee's courses
- **WHEN** assignments are listed for that user and course
- **THEN** a list of assignment models is returned
- **AND** every assignment has an integer `id` and a `course_id` equal to the requested course

#### Scenario: Seeded observee has assignments
- **GIVEN** the seeded test environment
- **WHEN** assignments are listed for every course of every observee
- **THEN** at least one assignment is returned overall

#### Scenario: Endpoint is typed in the generated client
- **WHEN** the generated client exposes the "list assignments for user" operation
- **THEN** its single-page, all-pages, and paginated variants are declared to return assignment models rather than no value or untyped data

### Requirement: Observer can list an observee's submissions in a course
For each observee course, the client SHALL return that observee's submissions for the course as typed submission models across all result pages, when called with the observer's credentials. Each submission SHALL carry its `workflow_state` and the other submission fields Canvas sends.

#### Scenario: Submissions per observee course
- **GIVEN** an observee and one of that observee's courses
- **WHEN** submissions are listed for that course with the observee as the only student
- **THEN** a list of submission models is returned, each with an integer `id`, a `user_id` equal to the observee's id, and a `workflow_state`
- **AND** the request succeeds with the observer's token (no authorization error)

#### Scenario: Submissions span multiple pages
- **GIVEN** an observee with more submissions in a course than fit on one page
- **WHEN** the submissions are listed with a page size smaller than the total
- **THEN** submissions from every page are returned, with no duplicate ids

#### Scenario: Submission fields are not dropped
- **GIVEN** a submissions response captured from Canvas
- **WHEN** it is deserialized
- **THEN** every submission keeps the `workflow_state`, `assignment_id`, `user_id`, `submitted_at` and `grade` values Canvas sent

### Requirement: Observee submissions can be counted by workflow state
For each observee, counting the observee's submissions across all of their courses by `workflow_state` SHALL produce counts that add up to the number of submissions listed. Every state SHALL be one of `graded`, `submitted`, `unsubmitted` or `pending_review`.

#### Scenario: Counts per observee
- **GIVEN** the seeded test environment, where an observee has submissions in more than one state
- **WHEN** each observee's submissions are listed for every course and counted by `workflow_state`
- **THEN** each observee's counts add up to that observee's number of submissions, and every counted state is a documented value
- **AND** at least one observee has counts for two or more states

#### Scenario: Seeded data lacks varied states
- **GIVEN** a test environment in which no observee has submissions in more than one state
- **WHEN** the counting test runs
- **THEN** it is skipped with a reason saying that no observee has submissions in more than one state
