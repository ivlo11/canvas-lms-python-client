# GradingPeriodsBatchUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**set_id** | **str** | The id of the grading period set. | 
**grading_periods_id** | **str** | The id of the grading period. If the id parameter does not exist, a new grading period will be created. | [optional] 
**grading_periods_title** | **str** | The title of the grading period. The title is required for creating a new grading period, but not for updating an existing grading period. | 
**grading_periods_start_date** | **str** | The date the grading period starts. The start_date is required for creating a new grading period, but not for updating an existing grading period. | 
**grading_periods_end_date** | **str** | The date the grading period ends. The end_date is required for creating a new grading period, but not for updating an existing grading period. | 
**grading_periods_close_date** | **str** | The date after which grades can no longer be changed for a grading period. The close_date is required for creating a new grading period, but not for updating an existing grading period. | 
**grading_periods_weight** | **float** | A weight value that contributes to the overall weight of a grading period set which is used to calculate how much assignments in this period contribute to the total grade | [optional] 

## Example

```python
from canvas_lms_python_client.models.grading_periods_batch_update_request import GradingPeriodsBatchUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GradingPeriodsBatchUpdateRequest from a JSON string
grading_periods_batch_update_request_instance = GradingPeriodsBatchUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(GradingPeriodsBatchUpdateRequest.to_json())

# convert the object into a dict
grading_periods_batch_update_request_dict = grading_periods_batch_update_request_instance.to_dict()
# create an instance of GradingPeriodsBatchUpdateRequest from a dict
grading_periods_batch_update_request_from_dict = GradingPeriodsBatchUpdateRequest.from_dict(grading_periods_batch_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


