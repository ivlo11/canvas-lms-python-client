# Spec Delta

## ADDED Requirements

### Requirement: Creating a grading period set returns the created set
Creating a grading period set SHALL return a wrapper model whose `grading_period_set` attribute is the created set as a single grading period set model, not a list.

#### Scenario: Create a set
- **GIVEN** a root account the caller can manage
- **WHEN** a grading period set is created with a title
- **THEN** the result is a wrapper model whose `grading_period_set` is a grading period set model with the given title and the identifier Canvas assigned
