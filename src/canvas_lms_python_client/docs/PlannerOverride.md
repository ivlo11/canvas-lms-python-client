# PlannerOverride

User-controlled setting for whether an item should be displayed on the planner or not

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The ID of the planner override | [optional] 
**plannable_type** | **str** | The type of the associated object for the planner override | [optional] 
**plannable_id** | **int** | The id of the associated object for the planner override | [optional] 
**user_id** | **int** | The id of the associated user for the planner override | [optional] 
**assignment_id** | **int** | The id of the plannable&#39;s associated assignment, if it has one | [optional] 
**workflow_state** | **str** | The current published state of the item, synced with the associated object | [optional] 
**marked_complete** | **bool** | Controls whether or not the associated plannable item is marked complete on the planner | [optional] 
**dismissed** | **bool** | Controls whether or not the associated plannable item shows up in the opportunities list | [optional] 
**created_at** | **datetime** | The datetime of when the planner override was created | [optional] 
**updated_at** | **datetime** | The datetime of when the planner override was updated | [optional] 
**deleted_at** | **datetime** | The datetime of when the planner override was deleted, if applicable | [optional] 

## Example

```python
from canvas_lms_python_client.models.planner_override import PlannerOverride

# TODO update the JSON string below
json = "{}"
# create an instance of PlannerOverride from a JSON string
planner_override_instance = PlannerOverride.from_json(json)
# print the JSON string representation of the object
print(PlannerOverride.to_json())

# convert the object into a dict
planner_override_dict = planner_override_instance.to_dict()
# create an instance of PlannerOverride from a dict
planner_override_from_dict = PlannerOverride.from_dict(planner_override_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


