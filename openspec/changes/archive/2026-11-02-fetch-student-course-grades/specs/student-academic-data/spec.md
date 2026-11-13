# Spec Delta

## Purpose

Defines the client contract a student relies on to read their own courses and the grades Canvas computes for them, returned as typed models without losing grade fields.

## ADDED Requirements

### Requirement: Student can list their courses with computed grades
When authenticated as a student and listing their courses with total scores included, the client SHALL return typed course models across all result pages. Each course's student enrollment for the caller SHALL carry Canvas's computed current and final scores and grades.

#### Scenario: Courses with a letter grade
- **GIVEN** a student enrolled in a course that uses a letter grading scheme and has at least one graded submission
- **WHEN** the student lists their courses with total scores included
- **THEN** each result is a course model, and that course's student enrollment has a non-empty `computed_current_grade` from the course's grading scheme and a numeric `computed_current_score`

#### Scenario: Course without a grading scheme
- **GIVEN** a student enrolled in a course without a grading scheme
- **WHEN** the student lists their courses with total scores included
- **THEN** that course's student enrollment has a null `computed_current_grade` and still carries its numeric `computed_current_score`, and no validation error is raised

### Requirement: Course enrollment grade fields deserialize as Canvas sends them
A course list that includes total scores SHALL deserialize without a validation error for any caller. Each enrollment SHALL keep the `computed_*`, `current_period_computed_*` and `unposted_*` values Canvas sent, with scores as numbers and grades as strings or null.

#### Scenario: Unposted scores are numbers
- **GIVEN** a course list response captured from Canvas in which an enrollment has `unposted_current_score` and `unposted_final_score` as numbers
- **WHEN** it is deserialized
- **THEN** no validation error is raised and both values equal the numbers Canvas sent

### Requirement: Enrollment grades use the enrollment grade model
An enrollment's `grades` SHALL be the enrollment grade model, with `html_url`, `current_grade`, `final_grade`, `current_score` and `final_score`. It SHALL NOT be the what-if grade calculation model.

#### Scenario: Enrollment grades keep their scores
- **GIVEN** an enrollment response whose `grades` object has `current_score` and `current_grade`
- **WHEN** it is deserialized
- **THEN** the enrollment's `grades` holds those values
