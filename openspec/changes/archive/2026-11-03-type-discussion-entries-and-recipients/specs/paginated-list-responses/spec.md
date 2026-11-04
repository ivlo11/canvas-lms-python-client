# Spec Delta

## ADDED Requirements

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
