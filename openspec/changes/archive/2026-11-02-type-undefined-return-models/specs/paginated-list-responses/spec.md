# Spec Delta

## ADDED Requirements

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

## REMOVED Requirements

### Requirement: Paginated operations whose documented model is undefined yield raw items
**Reason**: Its only member, LTI registration history, now has a documented model and is covered by "Media, LTI history and rubric location lists yield typed items". No paginated list operation is left whose documented model is undefined.
**Migration**: The general fallback for a documented model that is undefined, an untyped response rather than an error, continues under the `typed-operation-responses` requirement "Unresolvable documented models stay untyped". The client is unreleased, so there are no consumers to migrate.
