# SectionAssignmentOverrideAttributes

Attributes of an assignment override that apply to the section object.  See Assignments API for more details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**override_title** | **str** | The title for the assignment override | [optional] 
**due_at** | **datetime** | the due date for the assignment. returns null if not present. NOTE: If this assignment has assignment overrides, this field will be the due date as it applies to the user requesting information from the API. | [optional] 
**unlock_at** | **datetime** | (Optional) Time at which this was/will be unlocked. | [optional] 
**lock_at** | **datetime** | (Optional) Time at which this was/will be locked. | [optional] 
**id** | **int** |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.section_assignment_override_attributes import SectionAssignmentOverrideAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of SectionAssignmentOverrideAttributes from a JSON string
section_assignment_override_attributes_instance = SectionAssignmentOverrideAttributes.from_json(json)
# print the JSON string representation of the object
print(SectionAssignmentOverrideAttributes.to_json())

# convert the object into a dict
section_assignment_override_attributes_dict = section_assignment_override_attributes_instance.to_dict()
# create an instance of SectionAssignmentOverrideAttributes from a dict
section_assignment_override_attributes_from_dict = SectionAssignmentOverrideAttributes.from_dict(section_assignment_override_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


