# CoursesUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**course** | [**CoursesUpdateRequestCourse**](CoursesUpdateRequestCourse.md) |  | [optional] 
**offer** | **bool** | If this option is set to true, the course will be available to students immediately. | [optional] 
**override_sis_stickiness** | **bool** | Default is true. If false, any fields containing “sticky” changes will not be updated. See SIS CSV Format documentation for information on which fields can have SIS stickiness | [optional] 

## Example

```python
from canvas_lms_python_client.models.courses_update_request import CoursesUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CoursesUpdateRequest from a JSON string
courses_update_request_instance = CoursesUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(CoursesUpdateRequest.to_json())

# convert the object into a dict
courses_update_request_dict = courses_update_request_instance.to_dict()
# create an instance of CoursesUpdateRequest from a dict
courses_update_request_from_dict = CoursesUpdateRequest.from_dict(courses_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


