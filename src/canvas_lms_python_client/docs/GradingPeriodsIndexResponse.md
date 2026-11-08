# GradingPeriodsIndexResponse

Object response with `grading_periods`, `can_create_grading_periods`, `grading_periods_read_only`, `meta` (from the Canvas `@returns`).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**grading_periods** | [**List[GradingPeriod]**](GradingPeriod.md) |  | [optional] 
**can_create_grading_periods** | **bool** |  | [optional] 
**grading_periods_read_only** | **bool** |  | [optional] 
**meta** | **object** |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.grading_periods_index_response import GradingPeriodsIndexResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GradingPeriodsIndexResponse from a JSON string
grading_periods_index_response_instance = GradingPeriodsIndexResponse.from_json(json)
# print the JSON string representation of the object
print(GradingPeriodsIndexResponse.to_json())

# convert the object into a dict
grading_periods_index_response_dict = grading_periods_index_response_instance.to_dict()
# create an instance of GradingPeriodsIndexResponse from a dict
grading_periods_index_response_from_dict = GradingPeriodsIndexResponse.from_dict(grading_periods_index_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


