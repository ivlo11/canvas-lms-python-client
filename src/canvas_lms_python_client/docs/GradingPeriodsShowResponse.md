# GradingPeriodsShowResponse

Object response with `grading_periods`, `meta` (from the Canvas `@returns`).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**grading_periods** | [**List[GradingPeriod]**](GradingPeriod.md) |  | [optional] 
**meta** | **object** |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.grading_periods_show_response import GradingPeriodsShowResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GradingPeriodsShowResponse from a JSON string
grading_periods_show_response_instance = GradingPeriodsShowResponse.from_json(json)
# print the JSON string representation of the object
print(GradingPeriodsShowResponse.to_json())

# convert the object into a dict
grading_periods_show_response_dict = grading_periods_show_response_instance.to_dict()
# create an instance of GradingPeriodsShowResponse from a dict
grading_periods_show_response_from_dict = GradingPeriodsShowResponse.from_dict(grading_periods_show_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


