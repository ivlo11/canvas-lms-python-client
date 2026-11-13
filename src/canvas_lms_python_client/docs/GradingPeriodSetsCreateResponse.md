# GradingPeriodSetsCreateResponse

Object response with `grading_period_set` (from the Canvas `@returns`).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**grading_period_set** | [**GradingPeriodSets**](GradingPeriodSets.md) |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.grading_period_sets_create_response import GradingPeriodSetsCreateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GradingPeriodSetsCreateResponse from a JSON string
grading_period_sets_create_response_instance = GradingPeriodSetsCreateResponse.from_json(json)
# print the JSON string representation of the object
print(GradingPeriodSetsCreateResponse.to_json())

# convert the object into a dict
grading_period_sets_create_response_dict = grading_period_sets_create_response_instance.to_dict()
# create an instance of GradingPeriodSetsCreateResponse from a dict
grading_period_sets_create_response_from_dict = GradingPeriodSetsCreateResponse.from_dict(grading_period_sets_create_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


