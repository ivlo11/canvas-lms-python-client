# GradingPeriodsBatchUpdateResponse

Object response with `grading_periods`, `meta` (from the Canvas `@returns`).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**grading_periods** | [**List[GradingPeriod]**](GradingPeriod.md) |  | [optional] 
**meta** | **object** |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.grading_periods_batch_update_response import GradingPeriodsBatchUpdateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GradingPeriodsBatchUpdateResponse from a JSON string
grading_periods_batch_update_response_instance = GradingPeriodsBatchUpdateResponse.from_json(json)
# print the JSON string representation of the object
print(GradingPeriodsBatchUpdateResponse.to_json())

# convert the object into a dict
grading_periods_batch_update_response_dict = grading_periods_batch_update_response_instance.to_dict()
# create an instance of GradingPeriodsBatchUpdateResponse from a dict
grading_periods_batch_update_response_from_dict = GradingPeriodsBatchUpdateResponse.from_dict(grading_periods_batch_update_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


