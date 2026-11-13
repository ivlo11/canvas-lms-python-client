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

### Requirement: Media, LTI history and rubric location lists yield typed items
The media object list operations (for the caller, a course, a group, and their media attachment variants), the LTI registration history operation, and the rubric used-locations operations SHALL yield typed item models from both the page iterator and the all-items iterator, across all result pages. The used-locations response SHALL be a list of courses, each carrying its id, name, concluded flag and the assignments that use the rubric.

#### Scenario: Course media objects are typed
- **GIVEN** a course with a media object that has a caption track
- **WHEN** the course's media objects are listed with the all-items iterator
- **THEN** at least one item is yielded
- **AND** each item is a media object model whose `media_id` and `media_type` are set, and whose media tracks are typed items with a `locale`

#### Scenario: LTI registration history is typed
- **GIVEN** an LTI registration with at least one history entry
- **WHEN** its history is listed with the all-items iterator
- **THEN** each yielded item is a registration history entry model whose `id`, `lti_registration_id` and `update_type` are set
- **AND** its `created_by` holds what Canvas sent, either a user object or the string `"Instructure"`, and no validation error is raised

#### Scenario: Rubric used locations are typed courses
- **GIVEN** a rubric associated with an assignment in a course
- **WHEN** the rubric's used locations are listed with the all-items iterator
- **THEN** each yielded item is a used-location model for one course, with that course's `id` and `name`, and a list of assignments each having an `id` and `title`

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

### Requirement: Logins, batches, progress, gradeable students and pace contexts yield typed items
These paginated operations SHALL yield typed items from the page iterator and, for list responses, from the all-items iterator, across all result pages:
- listing a user's logins
- listing the caller's running conversation batches
- getting bulk user progress for a course
- listing gradeable students for multiple assignments

Listing pace contexts SHALL yield page models whose `pace_contexts` are typed and whose `total_entries` is an integer.

#### Scenario: User logins are typed
- **GIVEN** a user with at least one login
- **WHEN** that user's logins are listed with the all-items iterator
- **THEN** each item is a login model whose `id`, `user_id`, `account_id`, `unique_id` and `workflow_state` equal what Canvas sent

#### Scenario: Bulk user progress is typed
- **GIVEN** a module-based course with an enrolled student
- **WHEN** bulk user progress is listed with the all-items iterator
- **THEN** each item is a user progress model with the user's `id` and `display_name`, and a course progress whose `requirement_count` is an integer

#### Scenario: Gradeable students carry their assignment ids
- **GIVEN** a course with assignments and students
- **WHEN** gradeable students are listed for two of its assignments
- **THEN** each item is a gradeable student model with an `id`, a `display_name`, and a list of integer `assignment_ids`

#### Scenario: Conversation batches are typed
- **GIVEN** the caller has a conversation batch in progress
- **WHEN** running batches are listed
- **THEN** each item is a conversation batch model whose `id`, `workflow_state` and `completion` equal what Canvas sent

#### Scenario: Pace contexts are typed
- **GIVEN** a course with course pacing enabled and a published course pace
- **WHEN** its course pace contexts are listed with the page iterator
- **THEN** each page's `pace_contexts` are pace context models with `name`, `type` and `item_id` set
- **AND** an applied pace, when present, is a typed model with `name` and `type`

### Requirement: Discussion entries and recipients yield typed items
Listing a topic's entries, an entry's replies, or entries by id SHALL yield discussion entry models from both the page iterator and the all-items iterator. This applies to course and group topics. A root entry's recent replies SHALL also be discussion entry models.

Finding recipients SHALL yield recipient models from both iterators. User and context recipients SHALL each keep their own `id` as Canvas sent it.

#### Scenario: Topic entries are typed
- **GIVEN** a course discussion topic with a root entry that has a reply and an attachment
- **WHEN** the topic's entries are listed with the all-items iterator
- **THEN** each item is a discussion entry model whose `id`, `user_id` and `message` are set
- **AND** the root entry's `recent_replies` are discussion entry models, and its `attachment` holds the file's `id` and `display_name`

#### Scenario: Deleted entries deserialize
- **GIVEN** a topic with a deleted entry
- **WHEN** the topic's entries are listed
- **THEN** that entry is a discussion entry model with `deleted` true and no `message`, and no validation error is raised

#### Scenario: Replies and entries by id are typed
- **GIVEN** a root entry with a reply
- **WHEN** its replies are listed, and when entries are listed by those ids
- **THEN** each yielded item is a discussion entry model whose `parent_id` or `id` matches

#### Scenario: User and context recipients are typed
- **GIVEN** a caller who can message users and courses
- **WHEN** recipients are searched with the all-items iterator
- **THEN** each item is a recipient model
- **AND** a user recipient keeps its integer `id` and `full_name`, a context recipient keeps its string `id` (such as `course_2`) and `user_count`, and no validation error is raised

### Requirement: Planner items yield typed envelopes
Listing planner items, for the caller or for an observed user, SHALL yield planner item models from both the page iterator and the all-items iterator. Each item's context, plannable id, type and date, planner override and HTML URL SHALL be typed. Its `plannable` and `submissions` SHALL keep whatever Canvas sent.

#### Scenario: Student planner items are typed
- **GIVEN** a student with an assignment due within the requested date range
- **WHEN** the student's planner items are listed with the all-items iterator for that range
- **THEN** at least one item is a planner item model with `plannable_type` `assignment`, an integer `plannable_id`, and a `plannable` mapping that contains that assignment's id
- **AND** no validation error is raised whether `submissions` is `false` or an object

#### Scenario: Planner notes are typed items
- **GIVEN** a student with a planner note in the requested range
- **WHEN** planner items are listed
- **THEN** the note's item is a planner item model with `plannable_type` `planner_note`

### Requirement: Todo items yield typed items
Listing the caller's or a course's todo items SHALL yield todo item models from both iterators, with `assignment` as an assignment model or `quiz` as a quiz model.

#### Scenario: Submitting todo items carry a typed assignment
- **GIVEN** a student with an unsubmitted assignment due soon
- **WHEN** the student's todo items are listed with the all-items iterator
- **THEN** an item has `type` `submitting` and an `assignment` that is an assignment model whose `id` equals the seeded assignment's

#### Scenario: Grading todo items carry a count
- **GIVEN** a captured grading todo item for a teacher
- **WHEN** it is deserialized
- **THEN** it is a todo item model with `type` `grading`, an integer `needs_grading_count`, and a typed `assignment`

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
