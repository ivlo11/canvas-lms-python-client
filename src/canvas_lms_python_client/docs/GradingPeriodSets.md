# GradingPeriodSets


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | The title of the grading period set. | 
**weighted** | **bool** | If true, the grading periods in the set are weighted. | [optional] 
**display_totals_for_all_grading_periods** | **bool** | If true, the totals for all grading periods in the set are displayed. | [optional] 
**id** | **str** | The unique identifier for the grading period set. | [optional] 
**account_id** | **str** | The id of the account the set belongs to, or null if it belongs to a course. | [optional] 
**course_id** | **str** | The id of the course the set belongs to, or null if it belongs to an account. | [optional] 
**grading_periods** | [**List[GradingPeriod]**](GradingPeriod.md) | The active grading periods in the set. | [optional] 
**permissions** | **object** | The current user&#39;s permissions on the set (read, create, update, delete). | [optional] 
**created_at** | **datetime** | When the set was created. | [optional] 

## Example

```python
from canvas_lms_python_client.models.grading_period_sets import GradingPeriodSets

# TODO update the JSON string below
json = "{}"
# create an instance of GradingPeriodSets from a JSON string
grading_period_sets_instance = GradingPeriodSets.from_json(json)
# print the JSON string representation of the object
print(GradingPeriodSets.to_json())

# convert the object into a dict
grading_period_sets_dict = grading_period_sets_instance.to_dict()
# create an instance of GradingPeriodSets from a dict
grading_period_sets_from_dict = GradingPeriodSets.from_dict(grading_period_sets_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


