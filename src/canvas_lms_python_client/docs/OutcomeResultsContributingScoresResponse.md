# OutcomeResultsContributingScoresResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alignments** | **List[object]** |  | [optional] 
**outcome** | **object** |  | [optional] 
**scores** | **List[object]** |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.outcome_results_contributing_scores_response import OutcomeResultsContributingScoresResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OutcomeResultsContributingScoresResponse from a JSON string
outcome_results_contributing_scores_response_instance = OutcomeResultsContributingScoresResponse.from_json(json)
# print the JSON string representation of the object
print(OutcomeResultsContributingScoresResponse.to_json())

# convert the object into a dict
outcome_results_contributing_scores_response_dict = outcome_results_contributing_scores_response_instance.to_dict()
# create an instance of OutcomeResultsContributingScoresResponse from a dict
outcome_results_contributing_scores_response_from_dict = OutcomeResultsContributingScoresResponse.from_dict(outcome_results_contributing_scores_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


