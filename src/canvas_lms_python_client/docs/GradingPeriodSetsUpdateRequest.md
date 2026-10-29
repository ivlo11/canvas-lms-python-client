# GradingPeriodSetsUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enrollment_term_ids** | **List[List[str]]** | A list of associated term ids for the grading period set | [optional] 
**grading_period_set_title** | **str** | The title of the grading period set | 
**grading_period_set_weighted** | **bool** | A boolean to determine whether the grading periods in the set are weighted | [optional] 
**grading_period_set_display_totals_for_all_grading_periods** | **bool** | A boolean to determine whether the totals for all grading periods in the set are displayed | [optional] 

## Example

```python
from canvas_lms_python_client.models.grading_period_sets_update_request import GradingPeriodSetsUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GradingPeriodSetsUpdateRequest from a JSON string
grading_period_sets_update_request_instance = GradingPeriodSetsUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(GradingPeriodSetsUpdateRequest.to_json())

# convert the object into a dict
grading_period_sets_update_request_dict = grading_period_sets_update_request_instance.to_dict()
# create an instance of GradingPeriodSetsUpdateRequest from a dict
grading_period_sets_update_request_from_dict = GradingPeriodSetsUpdateRequest.from_dict(grading_period_sets_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


