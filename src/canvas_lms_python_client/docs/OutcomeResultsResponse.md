# OutcomeResultsResponse

Paginated `outcome_results` list response (from the Canvas example response).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**outcome_results** | [**List[OutcomeResult]**](OutcomeResult.md) |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.outcome_results_response import OutcomeResultsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OutcomeResultsResponse from a JSON string
outcome_results_response_instance = OutcomeResultsResponse.from_json(json)
# print the JSON string representation of the object
print(OutcomeResultsResponse.to_json())

# convert the object into a dict
outcome_results_response_dict = outcome_results_response_instance.to_dict()
# create an instance of OutcomeResultsResponse from a dict
outcome_results_response_from_dict = OutcomeResultsResponse.from_dict(outcome_results_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


