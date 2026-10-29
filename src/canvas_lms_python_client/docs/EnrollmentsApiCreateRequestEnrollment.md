# EnrollmentsApiCreateRequestEnrollment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_at** | **str** | [DateTime] The start time of the enrollment, in ISO8601 format. e.g. 2012-04-18T23:08:51Z | [optional] 
**end_at** | **str** | [DateTime] The end time of the enrollment, in ISO8601 format. e.g. 2012-04-18T23:08:51Z | [optional] 
**user_id** | **str** | [Required, String] The ID of the user to be enrolled in the course. | 
**type** | **str** | [Required, String, \&quot;StudentEnrollment\&quot;|\&quot;TeacherEnrollment\&quot;|\&quot;TaEnrollment\&quot;|\&quot;ObserverEnrollment\&quot;|\&quot;DesignerEnrollment\&quot;] Enroll the user as a student, teacher, TA, observer, or designer. If no value is given, the type will be inferred by +enrollment[role]+ if supplied, otherwise &#39;StudentEnrollment&#39; will be used. | 
**role** | **str** | [Deprecated, String] Assigns a custom course-level role to the user. | [optional] 
**role_id** | **int** | [Integer] Assigns a custom course-level role to the user. | [optional] 
**enrollment_state** | **str** | [String, \&quot;active\&quot;|\&quot;invited\&quot;|\&quot;inactive\&quot;] If set to &#39;active,&#39; student will be immediately enrolled in the course. Otherwise they will be required to accept a course invitation. Default is &#39;invited.&#39;.  If set to &#39;inactive&#39;, student will be listed in the course roster for teachers, but will not be able to participate in the course until their enrollment is activated. | [optional] 
**course_section_id** | **int** | [Integer] The ID of the course section to enroll the student in. If the section-specific URL is used, this argument is redundant and will be ignored. | [optional] 
**limit_privileges_to_course_section** | **bool** | [Boolean] If set, the enrollment will only allow the user to see and interact with users enrolled in the section given by course_section_id. * For teachers and TAs, this includes grading privileges. * Section-limited students will not see any users (including teachers   and TAs) not enrolled in their sections. * Users may have other enrollments that grant privileges to   multiple sections in the same course. | [optional] 
**notify** | **bool** | [Boolean] If true, a notification will be sent to the enrolled user. Notifications are not sent by default. | [optional] 
**self_enrollment_code** | **str** | [String] If the current user is not allowed to manage enrollments in this course, but the course allows self-enrollment, the user can self- enroll as a student in the default section by passing in a valid code. When self-enrolling, the user_id must be &#39;self&#39;. The enrollment_state will be set to &#39;active&#39; and all other arguments will be ignored. | [optional] 
**self_enrolled** | **bool** | [Boolean] If true, marks the enrollment as a self-enrollment, which gives students the ability to drop the course if desired. Defaults to false. | [optional] 
**associated_user_id** | **int** | [Integer] For an observer enrollment, the ID of a student to observe. This is a one-off operation; to automatically observe all a student&#39;s enrollments (for example, as a parent), please use the {api:UserObserveesController#create User Observees API}. | [optional] 
**sis_user_id** | **str** | [String] Required if the user is being enrolled from another trusted account. The unique identifier for the user (sis_user_id) must also be accompanied by the root_account parameter. The user_id will be ignored. | [optional] 
**integration_id** | **str** | [String] Required if the user is being enrolled from another trusted account. The unique identifier for the user (integration_id) must also be accompanied by the root_account parameter. The user_id will be ignored. | [optional] 

## Example

```python
from canvas_lms_python_client.models.enrollments_api_create_request_enrollment import EnrollmentsApiCreateRequestEnrollment

# TODO update the JSON string below
json = "{}"
# create an instance of EnrollmentsApiCreateRequestEnrollment from a JSON string
enrollments_api_create_request_enrollment_instance = EnrollmentsApiCreateRequestEnrollment.from_json(json)
# print the JSON string representation of the object
print(EnrollmentsApiCreateRequestEnrollment.to_json())

# convert the object into a dict
enrollments_api_create_request_enrollment_dict = enrollments_api_create_request_enrollment_instance.to_dict()
# create an instance of EnrollmentsApiCreateRequestEnrollment from a dict
enrollments_api_create_request_enrollment_from_dict = EnrollmentsApiCreateRequestEnrollment.from_dict(enrollments_api_create_request_enrollment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


