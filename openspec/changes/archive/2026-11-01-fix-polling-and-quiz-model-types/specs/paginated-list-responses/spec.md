# Spec Delta

## ADDED Requirements

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
