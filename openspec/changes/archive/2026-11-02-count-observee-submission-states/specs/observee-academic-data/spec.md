# Spec Delta

## ADDED Requirements

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
