# PlannerOverridesUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**marked_complete** | **str** | determines whether the planner item is marked as completed | [optional] 
**dismissed** | **str** | determines whether the planner item shows in the opportunities list | [optional] 

## Example

```python
from canvas_lms_python_client.models.planner_overrides_update_request import PlannerOverridesUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PlannerOverridesUpdateRequest from a JSON string
planner_overrides_update_request_instance = PlannerOverridesUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(PlannerOverridesUpdateRequest.to_json())

# convert the object into a dict
planner_overrides_update_request_dict = planner_overrides_update_request_instance.to_dict()
# create an instance of PlannerOverridesUpdateRequest from a dict
planner_overrides_update_request_from_dict = PlannerOverridesUpdateRequest.from_dict(planner_overrides_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


