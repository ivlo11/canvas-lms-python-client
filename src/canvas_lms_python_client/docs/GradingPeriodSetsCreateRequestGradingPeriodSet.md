# GradingPeriodSetsCreateRequestGradingPeriodSet


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | [Required, String] The title of the grading period set | 
**weighted** | **bool** | [Boolean] A boolean to determine whether the grading periods in the set are weighted | [optional] 
**display_totals_for_all_grading_periods** | **bool** | [Boolean] A boolean to determine whether the totals for all grading periods in the set are displayed | [optional] 

## Example

```python
from canvas_lms_python_client.models.grading_period_sets_create_request_grading_period_set import GradingPeriodSetsCreateRequestGradingPeriodSet

# TODO update the JSON string below
json = "{}"
# create an instance of GradingPeriodSetsCreateRequestGradingPeriodSet from a JSON string
grading_period_sets_create_request_grading_period_set_instance = GradingPeriodSetsCreateRequestGradingPeriodSet.from_json(json)
# print the JSON string representation of the object
print(GradingPeriodSetsCreateRequestGradingPeriodSet.to_json())

# convert the object into a dict
grading_period_sets_create_request_grading_period_set_dict = grading_period_sets_create_request_grading_period_set_instance.to_dict()
# create an instance of GradingPeriodSetsCreateRequestGradingPeriodSet from a dict
grading_period_sets_create_request_grading_period_set_from_dict = GradingPeriodSetsCreateRequestGradingPeriodSet.from_dict(grading_period_sets_create_request_grading_period_set_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


