# ModuleItemSequenceNode



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prev** | [**ModuleItem**](ModuleItem.md) |  | [optional] 
**current** | [**ModuleItem**](ModuleItem.md) |  | [optional] 
**next** | [**ModuleItem**](ModuleItem.md) |  | [optional] 
**mastery_path** | **object** | The conditional release rule for the module item, if applicable | [optional] 

## Example

```python
from canvas_lms_python_client.models.module_item_sequence_node import ModuleItemSequenceNode

# TODO update the JSON string below
json = "{}"
# create an instance of ModuleItemSequenceNode from a JSON string
module_item_sequence_node_instance = ModuleItemSequenceNode.from_json(json)
# print the JSON string representation of the object
print(ModuleItemSequenceNode.to_json())

# convert the object into a dict
module_item_sequence_node_dict = module_item_sequence_node_instance.to_dict()
# create an instance of ModuleItemSequenceNode from a dict
module_item_sequence_node_from_dict = ModuleItemSequenceNode.from_dict(module_item_sequence_node_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


