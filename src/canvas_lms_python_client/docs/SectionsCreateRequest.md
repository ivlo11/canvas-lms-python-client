# SectionsCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable_sis_reactivation** | **bool** | When true, will first try to re-activate a deleted section with matching sis_section_id if possible. | [optional] 
**course_section** | [**SectionsCreateRequestCourseSection**](SectionsCreateRequestCourseSection.md) |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.sections_create_request import SectionsCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SectionsCreateRequest from a JSON string
sections_create_request_instance = SectionsCreateRequest.from_json(json)
# print the JSON string representation of the object
print(SectionsCreateRequest.to_json())

# convert the object into a dict
sections_create_request_dict = sections_create_request_instance.to_dict()
# create an instance of SectionsCreateRequest from a dict
sections_create_request_from_dict = SectionsCreateRequest.from_dict(sections_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


