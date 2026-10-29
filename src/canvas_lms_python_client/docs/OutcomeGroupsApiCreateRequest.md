# OutcomeGroupsApiCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | The title of the new outcome group. | 
**description** | **str** | The description of the new outcome group. | [optional] 
**vendor_guid** | **str** | A custom GUID for the learning standard | [optional] 

## Example

```python
from canvas_lms_python_client.models.outcome_groups_api_create_request import OutcomeGroupsApiCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OutcomeGroupsApiCreateRequest from a JSON string
outcome_groups_api_create_request_instance = OutcomeGroupsApiCreateRequest.from_json(json)
# print the JSON string representation of the object
print(OutcomeGroupsApiCreateRequest.to_json())

# convert the object into a dict
outcome_groups_api_create_request_dict = outcome_groups_api_create_request_instance.to_dict()
# create an instance of OutcomeGroupsApiCreateRequest from a dict
outcome_groups_api_create_request_from_dict = OutcomeGroupsApiCreateRequest.from_dict(outcome_groups_api_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


