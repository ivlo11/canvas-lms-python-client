# Spec Delta

## ADDED Requirements

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
