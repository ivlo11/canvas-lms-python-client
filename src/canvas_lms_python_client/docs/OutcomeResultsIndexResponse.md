# OutcomeResultsIndexResponse

Paginated `outcome_results` list response (from the Canvas example response).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**outcome_results** | [**List[OutcomeResult]**](OutcomeResult.md) |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.outcome_results_index_response import OutcomeResultsIndexResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OutcomeResultsIndexResponse from a JSON string
outcome_results_index_response_instance = OutcomeResultsIndexResponse.from_json(json)
# print the JSON string representation of the object
print(OutcomeResultsIndexResponse.to_json())

# convert the object into a dict
outcome_results_index_response_dict = outcome_results_index_response_instance.to_dict()
# create an instance of OutcomeResultsIndexResponse from a dict
outcome_results_index_response_from_dict = OutcomeResultsIndexResponse.from_dict(outcome_results_index_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


