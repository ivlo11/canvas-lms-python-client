# GradingPeriodsUpdateResponse

Paginated `grading_periods` list response (from the Canvas example response).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**grading_periods** | [**List[GradingPeriod]**](GradingPeriod.md) |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.grading_periods_update_response import GradingPeriodsUpdateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GradingPeriodsUpdateResponse from a JSON string
grading_periods_update_response_instance = GradingPeriodsUpdateResponse.from_json(json)
# print the JSON string representation of the object
print(GradingPeriodsUpdateResponse.to_json())

# convert the object into a dict
grading_periods_update_response_dict = grading_periods_update_response_instance.to_dict()
# create an instance of GradingPeriodsUpdateResponse from a dict
grading_periods_update_response_from_dict = GradingPeriodsUpdateResponse.from_dict(grading_periods_update_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


