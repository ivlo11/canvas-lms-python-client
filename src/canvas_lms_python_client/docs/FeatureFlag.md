# FeatureFlag

A canvas feature flag.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | **str** | The current state of the feature flag | [optional] 
**name** | **str** | The name of the feature flag | [optional] 
**context_id** | **int** |  | [optional] 
**context_type** | **str** |  | [optional] 
**feature** | **str** |  | [optional] 
**hidden** | **bool** |  | [optional] 
**locked** | **bool** |  | [optional] 
**locking_account_id** | **object** |  | [optional] 
**parent_state** | **str** |  | [optional] 
**transitions** | **object** |  | [optional] 
**applies_to** | **str** |  | [optional] 
**autoexpand** | **bool** |  | [optional] 
**beta** | **bool** |  | [optional] 
**description** | **object** |  | [optional] 
**display_name** | **object** |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.feature_flag import FeatureFlag

# TODO update the JSON string below
json = "{}"
# create an instance of FeatureFlag from a JSON string
feature_flag_instance = FeatureFlag.from_json(json)
# print the JSON string representation of the object
print(FeatureFlag.to_json())

# convert the object into a dict
feature_flag_dict = feature_flag_instance.to_dict()
# create an instance of FeatureFlag from a dict
feature_flag_from_dict = FeatureFlag.from_dict(feature_flag_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


