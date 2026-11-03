# Spec Delta

## ADDED Requirements

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
