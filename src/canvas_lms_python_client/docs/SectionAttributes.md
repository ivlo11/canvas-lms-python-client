# SectionAttributes

Some of the attributes of a section. For more details see Sections API.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier for the section. | [optional] 
**name** | **str** | The name of the section. | [optional] 
**sis_id** | **str** | The sis id of the section. | [optional] 
**integration_id** | **str** | Optional: The integration ID of the section. | [optional] 
**origin_course** | [**CourseAttributes**](CourseAttributes.md) |  | [optional] 
**xlist_course** | [**CourseAttributes**](CourseAttributes.md) |  | [optional] 
**override** | [**SectionAssignmentOverrideAttributes**](SectionAssignmentOverrideAttributes.md) |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.section_attributes import SectionAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of SectionAttributes from a JSON string
section_attributes_instance = SectionAttributes.from_json(json)
# print the JSON string representation of the object
print(SectionAttributes.to_json())

# convert the object into a dict
section_attributes_dict = section_attributes_instance.to_dict()
# create an instance of SectionAttributes from a dict
section_attributes_from_dict = SectionAttributes.from_dict(section_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


