# Spec Delta

## ADDED Requirements

### Requirement: Grading period set pages are typed
The page iterator for an account's grading period sets SHALL yield one wrapper model per page whose `grading_period_sets` attribute is a list of grading period set models, each holding the set's identifiers and its grading periods as Canvas sends them. No all-items iterator SHALL be provided.

#### Scenario: Listing an account's grading period sets
- **GIVEN** an account with a grading period set that has at least one grading period
- **WHEN** the account's grading period sets are listed with the page iterator
- **THEN** each yielded page is a wrapper model whose `grading_period_sets` is a list of grading period set models
- **AND** each set's `id`, `title` and `grading_periods` hold what Canvas sent, and each grading period is a grading period model

#### Scenario: Pagination metadata is not required
- **GIVEN** a grading period sets page that also carries Canvas's `meta` object
- **WHEN** the page is deserialized
- **THEN** no validation error is raised, and the next page is found from the `Link` header

#### Scenario: Grading periods keep Canvas's types
- **GIVEN** an account with a grading period set whose grading periods have fractional weights
- **WHEN** the account's grading periods, or a set's nested grading periods, are deserialized
- **THEN** no validation error is raised, and each grading period's `id` and `grading_period_group_id` are the strings and its `weight` the number Canvas sent

#### Scenario: A course's included grading periods deserialize
- **GIVEN** a course whose term has a grading period set
- **WHEN** the course is fetched with `include[]=grading_periods`
- **THEN** no validation error is raised, and each included grading period is a course grading period model with the integer `id`, `title`, dates and `workflow_state` Canvas sent

### Requirement: Quiz submission event pages are typed
The page iterator for a quiz submission's events SHALL yield one wrapper model per page whose `quiz_submission_events` attribute is a list of quiz submission event models with their identifiers. No all-items iterator SHALL be provided.

#### Scenario: Listing a submission's events
- **GIVEN** a quiz submission in a course with quiz log auditing enabled, with recorded events
- **WHEN** the submission's events are listed with the page iterator
- **THEN** each yielded page is a wrapper model whose `quiz_submission_events` is a list of quiz submission event models, each with a string `id`, an `event_type` and a `created_at`

### Requirement: Quiz submission event data accepts every shape Canvas sends
A quiz submission event model SHALL hold its `event_data` exactly as Canvas sends it, whether a list, an object or null, without a validation error.

#### Scenario: Answered, flagged and focus events
- **GIVEN** a quiz submission with a `question_answered` event (list data), a `question_flagged` event (object data) and a `page_blurred` event (null data)
- **WHEN** its events are listed with the page iterator
- **THEN** every event deserializes, and each `event_data` equals the JSON Canvas sent for it
