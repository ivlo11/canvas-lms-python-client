# OutcomeGroupsApiUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | The new outcome group title. | [optional] 
**description** | **str** | The new outcome group description. | [optional] 
**vendor_guid** | **str** | A custom GUID for the learning standard. | [optional] 
**parent_outcome_group_id** | **int** | The id of the new parent outcome group. | [optional] 

## Example

```python
from canvas_lms_python_client.models.outcome_groups_api_update_request import OutcomeGroupsApiUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OutcomeGroupsApiUpdateRequest from a JSON string
outcome_groups_api_update_request_instance = OutcomeGroupsApiUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(OutcomeGroupsApiUpdateRequest.to_json())

# convert the object into a dict
outcome_groups_api_update_request_dict = outcome_groups_api_update_request_instance.to_dict()
# create an instance of OutcomeGroupsApiUpdateRequest from a dict
outcome_groups_api_update_request_from_dict = OutcomeGroupsApiUpdateRequest.from_dict(outcome_groups_api_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


