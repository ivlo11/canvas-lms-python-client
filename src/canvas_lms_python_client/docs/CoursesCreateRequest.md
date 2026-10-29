# CoursesCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**course** | [**CoursesCreateRequestCourse**](CoursesCreateRequestCourse.md) |  | [optional] 
**offer** | **bool** | If this option is set to true, the course will be available to students immediately. | [optional] 
**enroll_me** | **bool** | Set to true to enroll the current user as the teacher. | [optional] 
**skip_course_template** | **bool** | If this option is set to true, the template of the account will not be applied to this course It means copy_from_course_template will not be executed. This option is thought for a course copy. | [optional] 
**enable_sis_reactivation** | **bool** | When true, will first try to re-activate a deleted course with matching sis_course_id if possible. | [optional] 

## Example

```python
from canvas_lms_python_client.models.courses_create_request import CoursesCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CoursesCreateRequest from a JSON string
courses_create_request_instance = CoursesCreateRequest.from_json(json)
# print the JSON string representation of the object
print(CoursesCreateRequest.to_json())

# convert the object into a dict
courses_create_request_dict = courses_create_request_instance.to_dict()
# create an instance of CoursesCreateRequest from a dict
courses_create_request_from_dict = CoursesCreateRequest.from_dict(courses_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


