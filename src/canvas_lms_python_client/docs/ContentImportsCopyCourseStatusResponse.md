# ContentImportsCopyCourseStatusResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**progress** | **float** |  | [optional] 
**status_url** | **str** |  | [optional] 
**workflow_state** | **str** |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.content_imports_copy_course_status_response import ContentImportsCopyCourseStatusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ContentImportsCopyCourseStatusResponse from a JSON string
content_imports_copy_course_status_response_instance = ContentImportsCopyCourseStatusResponse.from_json(json)
# print the JSON string representation of the object
print(ContentImportsCopyCourseStatusResponse.to_json())

# convert the object into a dict
content_imports_copy_course_status_response_dict = content_imports_copy_course_status_response_instance.to_dict()
# create an instance of ContentImportsCopyCourseStatusResponse from a dict
content_imports_copy_course_status_response_from_dict = ContentImportsCopyCourseStatusResponse.from_dict(content_imports_copy_course_status_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


