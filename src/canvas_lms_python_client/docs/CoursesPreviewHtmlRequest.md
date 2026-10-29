# CoursesPreviewHtmlRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**html** | **str** | The html content to process | [optional] 

## Example

```python
from canvas_lms_python_client.models.courses_preview_html_request import CoursesPreviewHtmlRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CoursesPreviewHtmlRequest from a JSON string
courses_preview_html_request_instance = CoursesPreviewHtmlRequest.from_json(json)
# print the JSON string representation of the object
print(CoursesPreviewHtmlRequest.to_json())

# convert the object into a dict
courses_preview_html_request_dict = courses_preview_html_request_instance.to_dict()
# create an instance of CoursesPreviewHtmlRequest from a dict
courses_preview_html_request_from_dict = CoursesPreviewHtmlRequest.from_dict(courses_preview_html_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


