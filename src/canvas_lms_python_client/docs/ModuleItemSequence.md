# ModuleItemSequence



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[ModuleItemSequenceNode]**](ModuleItemSequenceNode.md) | an array containing one ModuleItemSequenceNode for each appearence of the asset in the module sequence (up to 10 total) | [optional] 
**modules** | [**List[Module]**](Module.md) | an array containing each Module referenced above | [optional] 

## Example

```python
from canvas_lms_python_client.models.module_item_sequence import ModuleItemSequence

# TODO update the JSON string below
json = "{}"
# create an instance of ModuleItemSequence from a JSON string
module_item_sequence_instance = ModuleItemSequence.from_json(json)
# print the JSON string representation of the object
print(ModuleItemSequence.to_json())

# convert the object into a dict
module_item_sequence_dict = module_item_sequence_instance.to_dict()
# create an instance of ModuleItemSequence from a dict
module_item_sequence_from_dict = ModuleItemSequence.from_dict(module_item_sequence_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


