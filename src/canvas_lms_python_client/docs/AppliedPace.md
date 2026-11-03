# AppliedPace

The course pace that applies to a pace context.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the context the pace belongs to. | [optional] 
**type** | **str** | The type of the pace: Course, Section or Enrollment. | [optional] 
**duration** | **int** | The pace&#39;s duration, in days. | [optional] 
**last_modified** | **datetime** | When the pace was last published. | [optional] 

## Example

```python
from canvas_lms_python_client.models.applied_pace import AppliedPace

# TODO update the JSON string below
json = "{}"
# create an instance of AppliedPace from a JSON string
applied_pace_instance = AppliedPace.from_json(json)
# print the JSON string representation of the object
print(AppliedPace.to_json())

# convert the object into a dict
applied_pace_dict = applied_pace_instance.to_dict()
# create an instance of AppliedPace from a dict
applied_pace_from_dict = AppliedPace.from_dict(applied_pace_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


