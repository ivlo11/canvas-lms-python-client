# CourseReportsCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parameters** | **List[str]** | The parameters will vary for each report. A few example parameters have been provided below. Note: the example parameters provided below may not be valid for every report. | [optional] 
**parameters_section_ids** | **int** | [Integer] The sections of the course to report on. Note: this parameter has been listed to serve as an example and may not be valid for every report. | [optional] 

## Example

```python
from canvas_lms_python_client.models.course_reports_create_request import CourseReportsCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CourseReportsCreateRequest from a JSON string
course_reports_create_request_instance = CourseReportsCreateRequest.from_json(json)
# print the JSON string representation of the object
print(CourseReportsCreateRequest.to_json())

# convert the object into a dict
course_reports_create_request_dict = course_reports_create_request_instance.to_dict()
# create an instance of CourseReportsCreateRequest from a dict
course_reports_create_request_from_dict = CourseReportsCreateRequest.from_dict(course_reports_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


