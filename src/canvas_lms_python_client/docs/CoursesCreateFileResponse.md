# CoursesCreateFileResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_param** | **str** |  | [optional] 
**progress** | **object** |  | [optional] 
**upload_params** | **object** |  | [optional] 
**upload_url** | **str** |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.courses_create_file_response import CoursesCreateFileResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CoursesCreateFileResponse from a JSON string
courses_create_file_response_instance = CoursesCreateFileResponse.from_json(json)
# print the JSON string representation of the object
print(CoursesCreateFileResponse.to_json())

# convert the object into a dict
courses_create_file_response_dict = courses_create_file_response_instance.to_dict()
# create an instance of CoursesCreateFileResponse from a dict
courses_create_file_response_from_dict = CoursesCreateFileResponse.from_dict(courses_create_file_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


