# ContentImportsCopyCourseContentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_course** | **str** | ID or SIS-ID of the course to copy the content from | [optional] 
**var_except** | **List[str]** | A list of the course content types to exclude, all areas not listed will be copied. | [optional] 
**only** | **List[str]** | A list of the course content types to copy, all areas not listed will not be copied. | [optional] 

## Example

```python
from canvas_lms_python_client.models.content_imports_copy_course_content_request import ContentImportsCopyCourseContentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ContentImportsCopyCourseContentRequest from a JSON string
content_imports_copy_course_content_request_instance = ContentImportsCopyCourseContentRequest.from_json(json)
# print the JSON string representation of the object
print(ContentImportsCopyCourseContentRequest.to_json())

# convert the object into a dict
content_imports_copy_course_content_request_dict = content_imports_copy_course_content_request_instance.to_dict()
# create an instance of ContentImportsCopyCourseContentRequest from a dict
content_imports_copy_course_content_request_from_dict = ContentImportsCopyCourseContentRequest.from_dict(content_imports_copy_course_content_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


