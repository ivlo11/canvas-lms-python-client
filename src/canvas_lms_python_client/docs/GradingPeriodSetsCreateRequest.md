# GradingPeriodSetsCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enrollment_term_ids** | **List[List[str]]** | A list of associated term ids for the grading period set | [optional] 
**grading_period_set** | [**GradingPeriodSetsCreateRequestGradingPeriodSet**](GradingPeriodSetsCreateRequestGradingPeriodSet.md) |  | 

## Example

```python
from canvas_lms_python_client.models.grading_period_sets_create_request import GradingPeriodSetsCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GradingPeriodSetsCreateRequest from a JSON string
grading_period_sets_create_request_instance = GradingPeriodSetsCreateRequest.from_json(json)
# print the JSON string representation of the object
print(GradingPeriodSetsCreateRequest.to_json())

# convert the object into a dict
grading_period_sets_create_request_dict = grading_period_sets_create_request_instance.to_dict()
# create an instance of GradingPeriodSetsCreateRequest from a dict
grading_period_sets_create_request_from_dict = GradingPeriodSetsCreateRequest.from_dict(grading_period_sets_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


