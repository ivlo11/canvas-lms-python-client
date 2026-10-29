# GradingPeriod


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier for the grading period. | 
**title** | **str** | The title for the grading period. | [optional] 
**start_date** | **datetime** | The start date of the grading period. | 
**end_date** | **datetime** | The end date of the grading period. | 
**close_date** | **datetime** | Grades can only be changed before the close date of the grading period. | [optional] 
**weight** | **int** | A weight value that contributes to the overall weight of a grading period set which is used to calculate how much assignments in this period contribute to the total grade | [optional] 
**is_closed** | **bool** | If true, the grading period&#39;s close_date has passed. | [optional] 

## Example

```python
from canvas_lms_python_client.models.grading_period import GradingPeriod

# TODO update the JSON string below
json = "{}"
# create an instance of GradingPeriod from a JSON string
grading_period_instance = GradingPeriod.from_json(json)
# print the JSON string representation of the object
print(GradingPeriod.to_json())

# convert the object into a dict
grading_period_dict = grading_period_instance.to_dict()
# create an instance of GradingPeriod from a dict
grading_period_from_dict = GradingPeriod.from_dict(grading_period_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


