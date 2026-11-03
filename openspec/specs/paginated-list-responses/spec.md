# paginated-list-responses Specification

## Purpose

Defines the client contract for paginated Canvas list operations: every result page is deserialized into the documented item type and yielded to the caller, and an operation never ends silently with no items because its response type is undocumented.

## Requirements

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

### Requirement: Paginated operations whose documented model is undefined yield raw items
For each paginated operation whose response is documented as a list of a model that Canvas does not define, the client SHALL still yield each page's items as untyped objects instead of yielding nothing.

#### Scenario: LTI registration history yields raw items
- **GIVEN** an LTI registration with at least one history entry
- **WHEN** its history is listed with the all-items iterator
- **THEN** at least one item is yielded
- **AND** each item is a mapping, because `Lti::RegistrationHistoryEntry` has no documented model

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

### Requirement: Wrapped list responses yield per-action wrapper pages
For each paginated operation whose Canvas documentation describes the response as an object wrapping a list of an existing model, in its example response or inline in its documented response, the page iterator SHALL yield one wrapper model per page, named after the operation's controller and action, with the list deserialized as the item model, across all result pages. A wrapper key SHALL be required only if Canvas documents it as required.

#### Scenario: Polls are returned in typed wrapper pages
- **GIVEN** the caller can see at least one poll
- **WHEN** polls are listed with the page iterator
- **THEN** each yielded page is a `PollsIndexResponse` wrapper model whose `polls` attribute is a list of poll models

#### Scenario: Related operations have their own wrappers
- **WHEN** poll sessions are listed for a poll, as opened sessions, or as closed sessions with the page iterator
- **THEN** each operation yields its own wrapper model type (`PollSessionsIndexResponse`, `PollSessionsOpenedResponse`, `PollSessionsClosedResponse`), and each has a `poll_sessions` attribute that is a list of poll session models

#### Scenario: Account calendars are returned in typed wrapper pages
- **GIVEN** the caller can see at least one account calendar
- **WHEN** account calendars are listed with the page iterator
- **THEN** each yielded page is a wrapper model whose `account_calendars` attribute is a list of account calendar models and whose `total_results` is an integer
- **AND** no all-items iterator is provided for the operation

#### Scenario: Wrapper key absent from a page
- **GIVEN** a page response for a wrapped operation that omits the wrapper key
- **WHEN** the page is deserialized
- **THEN** the page is yielded as a wrapper model whose wrapper attribute is empty, and no validation error is raised

#### Scenario: Wrapped results span multiple pages
- **GIVEN** a wrapped operation whose results span more than one page
- **WHEN** it is listed with the page iterator and a page size smaller than the total
- **THEN** one wrapper is yielded per page, following the `Link` next relation until there is none

#### Scenario: Undocumentable wrappers stay untyped
- **GIVEN** a wrapped operation that documents no response of its own, and whose example names a model that does not exist or is not a single key mapped to a list of a model
- **WHEN** the client is generated
- **THEN** that operation has no response type and remains on the undocumented allowlist

### Requirement: All-items iterator exists only for list responses
The client SHALL provide the all-items iterator for a paginated operation only when that operation's response is a list. The single-call method and the page iterator SHALL be provided for every paginated operation.

#### Scenario: List response
- **GIVEN** a paginated operation whose response is a list of a model
- **WHEN** the client API class is inspected
- **THEN** it provides the single-call method, the page iterator, and the all-items iterator for that operation

#### Scenario: Wrapper or object response
- **GIVEN** a paginated operation whose response is a wrapper model or an untyped object, such as polls or enrollment terms
- **WHEN** the client API class is inspected
- **THEN** it provides the single-call method and the page iterator, and does not provide an all-items iterator

#### Scenario: Undocumented response
- **GIVEN** a paginated operation with no documented response type
- **WHEN** the client API class is inspected
- **THEN** it provides the single-call method and the page iterator, and does not provide an all-items iterator

### Requirement: Typed items deserialize live Canvas data
For each list or wrapper response whose item model the client types, the client SHALL deserialize every item Canvas actually returns into that model without a validation error. Item field types SHALL match the JSON types Canvas sends, including string identifiers and fractional numbers.

#### Scenario: Poll identifiers are strings
- **GIVEN** the caller owns at least one poll
- **WHEN** polls are listed with the page iterator
- **THEN** each yielded page's polls are poll models whose `id` and `user_id` are strings

#### Scenario: Poll choices without a poll link
- **GIVEN** a poll with at least one choice
- **WHEN** its choices are listed with the page iterator
- **THEN** each choice is a poll choice model with a string `id`, and a choice that omits its poll id raises no validation error

#### Scenario: Poll sessions carry a list of submissions
- **GIVEN** a published poll session with at least one submission that the caller can view
- **WHEN** the poll's sessions are listed with the page iterator
- **THEN** each session is a poll session model with string identifiers, and its `poll_submissions` is a list of poll submission models with string identifiers

#### Scenario: Quiz submission scores are fractional
- **GIVEN** a quiz with at least one graded submission
- **WHEN** its submissions are listed with the page iterator
- **THEN** each submission is a quiz submission model whose `score` and `kept_score` accept fractional values such as `0.0` or `7.5`

#### Scenario: Quiz points are fractional
- **GIVEN** a course with at least one quiz
- **WHEN** its quizzes are listed with the all-items iterator
- **THEN** each item is a quiz model whose `points_possible` accepts fractional values such as `10.0` or `2.5`

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
