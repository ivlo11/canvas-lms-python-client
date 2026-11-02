# Enrollment



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The ID of the enrollment. | [optional] 
**course_id** | **int** | The unique id of the course. | [optional] 
**sis_course_id** | **str** | The SIS Course ID in which the enrollment is associated. Only displayed if present. This field is only included if the user has permission to view SIS information. | [optional] 
**course_integration_id** | **str** | The Course Integration ID in which the enrollment is associated. This field is only included if the user has permission to view SIS information. | [optional] 
**course_section_id** | **int** | The unique id of the user&#39;s section. | [optional] 
**section_integration_id** | **str** | The Section Integration ID in which the enrollment is associated. This field is only included if the user has permission to view SIS information. | [optional] 
**sis_account_id** | **str** | The SIS Account ID in which the enrollment is associated. Only displayed if present. This field is only included if the user has permission to view SIS information. | [optional] 
**sis_section_id** | **str** | The SIS Section ID in which the enrollment is associated. Only displayed if present. This field is only included if the user has permission to view SIS information. | [optional] 
**sis_user_id** | **str** | The SIS User ID in which the enrollment is associated. Only displayed if present. This field is only included if the user has permission to view SIS information. | [optional] 
**enrollment_state** | **str** | The state of the user&#39;s enrollment in the course. | [optional] 
**limit_privileges_to_course_section** | **bool** | User can only access his or her own course section. | [optional] 
**sis_import_id** | **int** | The unique identifier for the SIS import. This field is only included if the user has permission to manage SIS information. | [optional] 
**root_account_id** | **int** | The unique id of the user&#39;s account. | [optional] 
**type** | **str** | The enrollment type. One of &#39;StudentEnrollment&#39;, &#39;TeacherEnrollment&#39;, &#39;TaEnrollment&#39;, &#39;DesignerEnrollment&#39;, &#39;ObserverEnrollment&#39;. | [optional] 
**user_id** | **int** | The unique id of the user. | [optional] 
**associated_user_id** | **int** | The unique id of the associated user. Will be null unless type is ObserverEnrollment. | [optional] 
**role** | **str** | The enrollment role, for course-level permissions. This field will match &#x60;type&#x60; if the enrollment role has not been customized. | [optional] 
**role_id** | **int** | The id of the enrollment role. | [optional] 
**created_at** | **datetime** | The created time of the enrollment, in ISO8601 format. | [optional] 
**updated_at** | **datetime** | The updated time of the enrollment, in ISO8601 format. | [optional] 
**start_at** | **datetime** | The start time of the enrollment, in ISO8601 format. | [optional] 
**end_at** | **datetime** | The end time of the enrollment, in ISO8601 format. | [optional] 
**last_activity_at** | **datetime** | The last activity time of the user for the enrollment, in ISO8601 format. | [optional] 
**last_attended_at** | **datetime** | The last attended date of the user for the enrollment in a course, in ISO8601 format. | [optional] 
**total_activity_time** | **int** | The total activity time of the user for the enrollment, in seconds. | [optional] 
**html_url** | **str** | The URL to the Canvas web UI page for this course enrollment. | [optional] 
**grades** | [**Grade**](Grade.md) |  | [optional] 
**user** | [**User**](User.md) |  | [optional] 
**override_grade** | **str** | The user&#39;s override grade for the course. | [optional] 
**override_score** | **float** | The user&#39;s override score for the course. | [optional] 
**unposted_current_grade** | **str** | The user&#39;s current grade in the class including muted/unposted assignments. Only included if user has permissions to view this grade, typically teachers, TAs, and admins. | [optional] 
**unposted_final_grade** | **str** | The user&#39;s final grade for the class including muted/unposted assignments. Only included if user has permissions to view this grade, typically teachers, TAs, and admins.. | [optional] 
**unposted_current_score** | **float** | The user&#39;s current score in the class including muted/unposted assignments. Only included if user has permissions to view this score, typically teachers, TAs, and admins.. | [optional] 
**unposted_final_score** | **float** | The user&#39;s final score for the class including muted/unposted assignments. Only included if user has permissions to view this score, typically teachers, TAs, and admins.. | [optional] 
**has_grading_periods** | **bool** | optional: Indicates whether the course the enrollment belongs to has grading periods set up. (applies only to student enrollments, and only available in course endpoints) | [optional] 
**totals_for_all_grading_periods_option** | **bool** | optional: Indicates whether the course the enrollment belongs to has the Display Totals for &#39;All Grading Periods&#39; feature enabled. (applies only to student enrollments, and only available in course endpoints) | [optional] 
**current_grading_period_title** | **str** | optional: The name of the currently active grading period, if one exists. If the course the enrollment belongs to does not have grading periods, or if no currently active grading period exists, the value will be null. (applies only to student enrollments, and only available in course endpoints) | [optional] 
**current_grading_period_id** | **int** | optional: The id of the currently active grading period, if one exists. If the course the enrollment belongs to does not have grading periods, or if no currently active grading period exists, the value will be null. (applies only to student enrollments, and only available in course endpoints) | [optional] 
**current_period_override_grade** | **str** | The user&#39;s override grade for the current grading period. | [optional] 
**current_period_override_score** | **float** | The user&#39;s override score for the current grading period. | [optional] 
**computed_current_score** | **float** | optional: The student&#39;s score in the course, ignoring ungraded assignments. (applies only to student enrollments, and only available in course endpoints with include[]&#x3D;total_scores) | [optional] 
**computed_final_score** | **float** | optional: The student&#39;s score in the course including ungraded assignments with a score of 0. (applies only to student enrollments, and only available in course endpoints with include[]&#x3D;total_scores) | [optional] 
**computed_current_grade** | **str** | optional: The letter grade equivalent of computed_current_score, if the course uses a grading scheme. (applies only to student enrollments, and only available in course endpoints with include[]&#x3D;total_scores) | [optional] 
**computed_final_grade** | **str** | optional: The letter grade equivalent of computed_final_score, if the course uses a grading scheme. (applies only to student enrollments, and only available in course endpoints with include[]&#x3D;total_scores) | [optional] 
**current_period_computed_current_score** | **float** | optional: The student&#39;s score in the course for the current grading period, ignoring ungraded assignments. If the course the enrollment belongs to does not have grading periods, or if no currently active grading period exists, the value will be null. (applies only to student enrollments, and only available in course endpoints with include[]&#x3D;current_grading_period_scores) | [optional] 
**current_period_computed_final_score** | **float** | optional: The student&#39;s score in the course for the current grading period, including ungraded assignments with a score of 0. If the course the enrollment belongs to does not have grading periods, or if no currently active grading period exists, the value will be null. (applies only to student enrollments, and only available in course endpoints with include[]&#x3D;current_grading_period_scores) | [optional] 
**current_period_computed_current_grade** | **str** | optional: The letter grade equivalent of current_period_computed_current_score, if available. If the course the enrollment belongs to does not have grading periods, or if no currently active grading period exists, the value will be null. (applies only to student enrollments, and only available in course endpoints with include[]&#x3D;current_grading_period_scores) | [optional] 
**current_period_computed_final_grade** | **str** | optional: The letter grade equivalent of current_period_computed_final_score, if available. If the course the enrollment belongs to does not have grading periods, or if no currently active grading period exists, the value will be null. (applies only to student enrollments, and only available in course endpoints with include[]&#x3D;current_grading_period_scores) | [optional] 
**current_period_unposted_current_score** | **float** | optional: The student&#39;s score in the course for the current grading period, including muted/unposted assignments. Only included if user has permission to view this score, typically teachers, TAs, and admins. If the course the enrollment belongs to does not have grading periods, or if no currently active grading period exists, the value will be null. (applies only to student enrollments, and only available in course endpoints) | [optional] 
**current_period_unposted_final_score** | **float** | optional: The student&#39;s score in the course for the current grading period, including muted/unposted assignments and including ungraded assignments with a score of 0. Only included if user has permission to view this score, typically teachers, TAs, and admins. If the course the enrollment belongs to does not have grading periods, or if no currently active grading period exists, the value will be null. (applies only to student enrollments, and only available in course endpoints) | [optional] 
**current_period_unposted_current_grade** | **str** | optional: The letter grade equivalent of current_period_unposted_current_score, if available. Only included if user has permission to view this grade, typically teachers, TAs, and admins. If the course the enrollment belongs to does not have grading periods, or if no currently active grading period exists, the value will be null. (applies only to student enrollments, and only available in course endpoints) | [optional] 
**current_period_unposted_final_grade** | **str** | optional: The letter grade equivalent of current_period_unposted_final_score, if available. Only included if user has permission to view this grade, typically teachers, TAs, and admins. If the course the enrollment belongs to does not have grading periods, or if no currently active grading period exists, the value will be null. (applies only to student enrollments, and only available in course endpoints) | [optional] 

## Example

```python
from canvas_lms_python_client.models.enrollment import Enrollment

# TODO update the JSON string below
json = "{}"
# create an instance of Enrollment from a JSON string
enrollment_instance = Enrollment.from_json(json)
# print the JSON string representation of the object
print(Enrollment.to_json())

# convert the object into a dict
enrollment_dict = enrollment_instance.to_dict()
# create an instance of Enrollment from a dict
enrollment_from_dict = Enrollment.from_dict(enrollment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


