# GradingPeriodsUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**grading_periods_start_date** | **str** | The date the grading period starts. | 
**grading_periods_end_date** | **str** |  | 
**grading_periods_weight** | **float** | A weight value that contributes to the overall weight of a grading period set which is used to calculate how much assignments in this period contribute to the total grade | [optional] 

## Example

```python
from canvas_lms_python_client.models.grading_periods_update_request import GradingPeriodsUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GradingPeriodsUpdateRequest from a JSON string
grading_periods_update_request_instance = GradingPeriodsUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(GradingPeriodsUpdateRequest.to_json())

# convert the object into a dict
grading_periods_update_request_dict = grading_periods_update_request_instance.to_dict()
# create an instance of GradingPeriodsUpdateRequest from a dict
grading_periods_update_request_from_dict = GradingPeriodsUpdateRequest.from_dict(grading_periods_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


