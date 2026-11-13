# GradingPeriodSetsIndexResponse

Object response with `grading_period_sets`, `meta` (from the Canvas `@returns`).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**grading_period_sets** | [**List[GradingPeriodSets]**](GradingPeriodSets.md) |  | [optional] 
**meta** | **object** |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.grading_period_sets_index_response import GradingPeriodSetsIndexResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GradingPeriodSetsIndexResponse from a JSON string
grading_period_sets_index_response_instance = GradingPeriodSetsIndexResponse.from_json(json)
# print the JSON string representation of the object
print(GradingPeriodSetsIndexResponse.to_json())

# convert the object into a dict
grading_period_sets_index_response_dict = grading_period_sets_index_response_instance.to_dict()
# create an instance of GradingPeriodSetsIndexResponse from a dict
grading_period_sets_index_response_from_dict = GradingPeriodSetsIndexResponse.from_dict(grading_period_sets_index_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


