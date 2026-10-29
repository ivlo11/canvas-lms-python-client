# ModuleAssignmentOverride


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | the ID of the assignment override | [optional] 
**context_module_id** | **int** | the ID of the module the override applies to | [optional] 
**title** | **str** | the title of the override | [optional] 
**students** | [**OverrideTarget**](OverrideTarget.md) |  | [optional] 
**course_section** | [**OverrideTarget**](OverrideTarget.md) |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.module_assignment_override import ModuleAssignmentOverride

# TODO update the JSON string below
json = "{}"
# create an instance of ModuleAssignmentOverride from a JSON string
module_assignment_override_instance = ModuleAssignmentOverride.from_json(json)
# print the JSON string representation of the object
print(ModuleAssignmentOverride.to_json())

# convert the object into a dict
module_assignment_override_dict = module_assignment_override_instance.to_dict()
# create an instance of ModuleAssignmentOverride from a dict
module_assignment_override_from_dict = ModuleAssignmentOverride.from_dict(module_assignment_override_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


