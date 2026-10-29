# SectionsUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**override_sis_stickiness** | **bool** | Default is true. If false, any fields containing “sticky” changes will not be updated. See SIS CSV Format documentation for information on which fields can have SIS stickiness | [optional] 
**course_section** | [**SectionsUpdateRequestCourseSection**](SectionsUpdateRequestCourseSection.md) |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.sections_update_request import SectionsUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SectionsUpdateRequest from a JSON string
sections_update_request_instance = SectionsUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(SectionsUpdateRequest.to_json())

# convert the object into a dict
sections_update_request_dict = sections_update_request_instance.to_dict()
# create an instance of SectionsUpdateRequest from a dict
sections_update_request_from_dict = SectionsUpdateRequest.from_dict(sections_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


