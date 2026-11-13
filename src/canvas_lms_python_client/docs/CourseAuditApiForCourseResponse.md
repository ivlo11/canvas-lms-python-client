# CourseAuditApiForCourseResponse

Object response with `links`, `events`, `linked` (from the Canvas `@returns`).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | **object** |  | [optional] 
**events** | [**List[CourseEvent]**](CourseEvent.md) |  | [optional] 
**linked** | **object** |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.course_audit_api_for_course_response import CourseAuditApiForCourseResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CourseAuditApiForCourseResponse from a JSON string
course_audit_api_for_course_response_instance = CourseAuditApiForCourseResponse.from_json(json)
# print the JSON string representation of the object
print(CourseAuditApiForCourseResponse.to_json())

# convert the object into a dict
course_audit_api_for_course_response_dict = course_audit_api_for_course_response_instance.to_dict()
# create an instance of CourseAuditApiForCourseResponse from a dict
course_audit_api_for_course_response_from_dict = CourseAuditApiForCourseResponse.from_dict(course_audit_api_for_course_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


