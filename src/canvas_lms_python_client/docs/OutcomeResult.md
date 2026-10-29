# OutcomeResult

A student's result for an outcome

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | A unique identifier for this result | [optional] 
**score** | **int** | The student&#39;s score | [optional] 
**submitted_or_assessed_at** | **datetime** | The datetime the resulting OutcomeResult was submitted at, or absent that, when it was assessed. | [optional] 
**links** | **object** | Unique identifiers of objects associated with this result | [optional] 
**percent** | **float** | score&#39;s percent of maximum points possible for outcome, scaled to reflect any custom mastery levels that differ from the learning outcome | [optional] 

## Example

```python
from canvas_lms_python_client.models.outcome_result import OutcomeResult

# TODO update the JSON string below
json = "{}"
# create an instance of OutcomeResult from a JSON string
outcome_result_instance = OutcomeResult.from_json(json)
# print the JSON string representation of the object
print(OutcomeResult.to_json())

# convert the object into a dict
outcome_result_dict = outcome_result_instance.to_dict()
# create an instance of OutcomeResult from a dict
outcome_result_from_dict = OutcomeResult.from_dict(outcome_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


