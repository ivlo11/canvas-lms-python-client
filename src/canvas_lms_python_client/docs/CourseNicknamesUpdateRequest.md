# CourseNicknamesUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nickname** | **str** | The nickname to set.  It must be non-empty and shorter than 60 characters. | 

## Example

```python
from canvas_lms_python_client.models.course_nicknames_update_request import CourseNicknamesUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CourseNicknamesUpdateRequest from a JSON string
course_nicknames_update_request_instance = CourseNicknamesUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(CourseNicknamesUpdateRequest.to_json())

# convert the object into a dict
course_nicknames_update_request_dict = course_nicknames_update_request_instance.to_dict()
# create an instance of CourseNicknamesUpdateRequest from a dict
course_nicknames_update_request_from_dict = CourseNicknamesUpdateRequest.from_dict(course_nicknames_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


