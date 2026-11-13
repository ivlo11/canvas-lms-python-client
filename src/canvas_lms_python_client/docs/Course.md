# Course



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | the unique identifier for the course | [optional] 
**sis_course_id** | **str** | the SIS identifier for the course, if defined. This field is only included if the user has permission to view SIS information. | [optional] 
**uuid** | **str** | the UUID of the course | [optional] 
**integration_id** | **str** | the integration identifier for the course, if defined. This field is only included if the user has permission to view SIS information. | [optional] 
**sis_import_id** | **int** | the unique identifier for the SIS import. This field is only included if the user has permission to manage SIS information. | [optional] 
**name** | **str** | the full name of the course. If the requesting user has set a nickname for the course, the nickname will be shown here. | [optional] 
**course_code** | **str** | the course code | [optional] 
**original_name** | **str** | the actual course name. This field is returned only if the requesting user has set a nickname for the course. | [optional] 
**workflow_state** | **str** | the current state of the course, also known as ‘status’.  The value will be one of the following values: &#39;unpublished&#39;, &#39;available&#39;, &#39;completed&#39;, or &#39;deleted&#39;.  NOTE: When fetching a singular course that has a &#39;deleted&#39; workflow state value, an error will be returned with a message of &#39;The specified resource does not exist.&#39; | [optional] 
**account_id** | **int** | the account associated with the course | [optional] 
**root_account_id** | **int** | the root account associated with the course | [optional] 
**enrollment_term_id** | **int** | the enrollment term associated with the course | [optional] 
**grading_periods** | [**List[CourseGradingPeriod]**](CourseGradingPeriod.md) | A list of grading periods associated with the course | [optional] 
**grading_standard_id** | **int** | the grading standard associated with the course | [optional] 
**grade_passback_setting** | **str** | the grade_passback_setting set on the course | [optional] 
**created_at** | **datetime** | the date the course was created. | [optional] 
**start_at** | **datetime** | the start date for the course, if applicable | [optional] 
**end_at** | **datetime** | the end date for the course, if applicable | [optional] 
**locale** | **str** | the course-set locale, if applicable | [optional] 
**enrollments** | [**List[Enrollment]**](Enrollment.md) | A list of enrollments linking the current user to the course. for student enrollments, grading information may be included if include[]&#x3D;total_scores | [optional] 
**total_students** | **int** | optional: the total number of active and invited students in the course | [optional] 
**calendar** | [**CalendarLink**](CalendarLink.md) |  | [optional] 
**default_view** | **str** | the type of page that users will see when they first visit the course - &#39;feed&#39;: Recent Activity Dashboard - &#39;wiki&#39;: Wiki Front Page - &#39;modules&#39;: Course Modules/Sections Page - &#39;assignments&#39;: Course Assignments List - &#39;syllabus&#39;: Course Syllabus Page other types may be added in the future | [optional] 
**syllabus_body** | **str** | optional: user-generated HTML for the course syllabus | [optional] 
**needs_grading_count** | **int** | optional: the number of submissions needing grading returned only if the current user has grading rights and include[]&#x3D;needs_grading_count | [optional] 
**term** | [**Term**](Term.md) |  | [optional] 
**course_progress** | [**CourseProgress**](CourseProgress.md) |  | [optional] 
**apply_assignment_group_weights** | **bool** | weight final grade based on assignment group percentages | [optional] 
**permissions** | **object** | optional: the permissions the user has for the course. returned only for a single course and include[]&#x3D;permissions | [optional] 
**is_public** | **bool** |  | [optional] 
**is_public_to_auth_users** | **bool** |  | [optional] 
**public_syllabus** | **bool** |  | [optional] 
**public_syllabus_to_auth** | **bool** |  | [optional] 
**public_description** | **str** | optional: the public description of the course | [optional] 
**storage_quota_mb** | **int** |  | [optional] 
**storage_quota_used_mb** | **float** |  | [optional] 
**hide_final_grades** | **bool** |  | [optional] 
**license** | **str** |  | [optional] 
**allow_student_assignment_edits** | **bool** |  | [optional] 
**allow_wiki_comments** | **bool** |  | [optional] 
**allow_student_forum_attachments** | **bool** |  | [optional] 
**open_enrollment** | **bool** |  | [optional] 
**self_enrollment** | **bool** |  | [optional] 
**restrict_enrollments_to_course_dates** | **bool** |  | [optional] 
**course_format** | **str** |  | [optional] 
**access_restricted_by_date** | **bool** | optional: this will be true if this user is currently prevented from viewing the course because of date restriction settings | [optional] 
**time_zone** | **str** | The course&#39;s IANA time zone name. | [optional] 
**blueprint** | **bool** | optional: whether the course is set as a Blueprint Course (blueprint fields require the Blueprint Courses feature) | [optional] 
**blueprint_restrictions** | **object** | optional: Set of restrictions applied to all locked course objects | [optional] 
**blueprint_restrictions_by_object_type** | **object** | optional: Sets of restrictions differentiated by object type applied to locked course objects | [optional] 
**template** | **bool** | optional: whether the course is set as a template (requires the Course Templates feature) | [optional] 

## Example

```python
from canvas_lms_python_client.models.course import Course

# TODO update the JSON string below
json = "{}"
# create an instance of Course from a JSON string
course_instance = Course.from_json(json)
# print the JSON string representation of the object
print(Course.to_json())

# convert the object into a dict
course_dict = course_instance.to_dict()
# create an instance of Course from a dict
course_from_dict = Course.from_dict(course_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


