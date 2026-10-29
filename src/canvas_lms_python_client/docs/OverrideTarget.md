# OverrideTarget


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | the ID of the user or section that the override is targeting | [optional] 
**name** | **str** | the name of the user or section that the override is targeting | [optional] 

## Example

```python
from canvas_lms_python_client.models.override_target import OverrideTarget

# TODO update the JSON string below
json = "{}"
# create an instance of OverrideTarget from a JSON string
override_target_instance = OverrideTarget.from_json(json)
# print the JSON string representation of the object
print(OverrideTarget.to_json())

# convert the object into a dict
override_target_dict = override_target_instance.to_dict()
# create an instance of OverrideTarget from a dict
override_target_from_dict = OverrideTarget.from_dict(override_target_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


