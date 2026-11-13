# OutcomeResultsRollupsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**linked** | **object** |  | [optional] 
**meta** | **object** |  | [optional] 
**rollups** | [**List[OutcomeRollup]**](OutcomeRollup.md) |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.outcome_results_rollups_response import OutcomeResultsRollupsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OutcomeResultsRollupsResponse from a JSON string
outcome_results_rollups_response_instance = OutcomeResultsRollupsResponse.from_json(json)
# print the JSON string representation of the object
print(OutcomeResultsRollupsResponse.to_json())

# convert the object into a dict
outcome_results_rollups_response_dict = outcome_results_rollups_response_instance.to_dict()
# create an instance of OutcomeResultsRollupsResponse from a dict
outcome_results_rollups_response_from_dict = OutcomeResultsRollupsResponse.from_dict(outcome_results_rollups_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


