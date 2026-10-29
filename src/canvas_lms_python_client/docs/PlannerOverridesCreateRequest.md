# PlannerOverridesCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plannable_type** | **str** | Type of the item that you are overriding in the planner | 
**plannable_id** | **int** | ID of the item that you are overriding in the planner | 
**marked_complete** | **bool** | If this is true, the item will show in the planner as completed | [optional] 
**dismissed** | **bool** | If this is true, the item will not show in the opportunities list | [optional] 

## Example

```python
from canvas_lms_python_client.models.planner_overrides_create_request import PlannerOverridesCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PlannerOverridesCreateRequest from a JSON string
planner_overrides_create_request_instance = PlannerOverridesCreateRequest.from_json(json)
# print the JSON string representation of the object
print(PlannerOverridesCreateRequest.to_json())

# convert the object into a dict
planner_overrides_create_request_dict = planner_overrides_create_request_instance.to_dict()
# create an instance of PlannerOverridesCreateRequest from a dict
planner_overrides_create_request_from_dict = PlannerOverridesCreateRequest.from_dict(planner_overrides_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


