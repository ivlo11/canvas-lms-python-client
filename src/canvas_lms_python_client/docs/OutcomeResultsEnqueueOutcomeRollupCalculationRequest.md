# OutcomeResultsEnqueueOutcomeRollupCalculationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**course_id** | **str** | The course ID for the rollup job | [optional] 
**student_uuid** | **str** | The student UUID for the rollup job. If provided, calculates for specific student. | [optional] 

## Example

```python
from canvas_lms_python_client.models.outcome_results_enqueue_outcome_rollup_calculation_request import OutcomeResultsEnqueueOutcomeRollupCalculationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OutcomeResultsEnqueueOutcomeRollupCalculationRequest from a JSON string
outcome_results_enqueue_outcome_rollup_calculation_request_instance = OutcomeResultsEnqueueOutcomeRollupCalculationRequest.from_json(json)
# print the JSON string representation of the object
print(OutcomeResultsEnqueueOutcomeRollupCalculationRequest.to_json())

# convert the object into a dict
outcome_results_enqueue_outcome_rollup_calculation_request_dict = outcome_results_enqueue_outcome_rollup_calculation_request_instance.to_dict()
# create an instance of OutcomeResultsEnqueueOutcomeRollupCalculationRequest from a dict
outcome_results_enqueue_outcome_rollup_calculation_request_from_dict = OutcomeResultsEnqueueOutcomeRollupCalculationRequest.from_dict(outcome_results_enqueue_outcome_rollup_calculation_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


