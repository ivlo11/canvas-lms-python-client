# UserAssignmentOverrideAttributes

Attributes of assignment overrides that apply to users.  See Assignments API for more details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique Canvas identifier for the assignment override | [optional] 
**title** | **str** | The title of the assignment override. | [optional] 
**due_at** | **datetime** | The time at which this assignment is due | [optional] 
**unlock_at** | **datetime** | (Optional) Time at which this was/will be unlocked. | [optional] 
**lock_at** | **datetime** | (Optional) Time at which this was/will be locked. | [optional] 
**students** | [**List[StudentAttributes]**](StudentAttributes.md) | Includes attributes of a student for convenience. For more details see Users API. | [optional] 

## Example

```python
from canvas_lms_python_client.models.user_assignment_override_attributes import UserAssignmentOverrideAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of UserAssignmentOverrideAttributes from a JSON string
user_assignment_override_attributes_instance = UserAssignmentOverrideAttributes.from_json(json)
# print the JSON string representation of the object
print(UserAssignmentOverrideAttributes.to_json())

# convert the object into a dict
user_assignment_override_attributes_dict = user_assignment_override_attributes_instance.to_dict()
# create an instance of UserAssignmentOverrideAttributes from a dict
user_assignment_override_attributes_from_dict = UserAssignmentOverrideAttributes.from_dict(user_assignment_override_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


