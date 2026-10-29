# ContextModuleItemsApiUpdateRequestModuleItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | [String] The name of the module item | [optional] 
**position** | **int** | [Integer] The position of this item in the module (1-based) | [optional] 
**indent** | **int** | [Integer] 0-based indent level; module items may be indented to show a hierarchy | [optional] 
**external_url** | **str** | [String] External url that the item points to. Only applies to &#39;ExternalUrl&#39; type. | [optional] 
**new_tab** | **bool** | [Boolean] Whether the external tool opens in a new tab. Only applies to &#39;ExternalTool&#39; type. | [optional] 
**completion_requirement** | **str** | [min_score] [Integer] Minimum score required to complete, Required for completion_requirement type &#39;min_score&#39;. | [optional] 
**published** | **bool** | [Boolean] Whether the module item is published and visible to students. | [optional] 
**module_id** | **str** | [String] Move this item to another module by specifying the target module id here. The target module must be in the same course. | [optional] 

## Example

```python
from canvas_lms_python_client.models.context_module_items_api_update_request_module_item import ContextModuleItemsApiUpdateRequestModuleItem

# TODO update the JSON string below
json = "{}"
# create an instance of ContextModuleItemsApiUpdateRequestModuleItem from a JSON string
context_module_items_api_update_request_module_item_instance = ContextModuleItemsApiUpdateRequestModuleItem.from_json(json)
# print the JSON string representation of the object
print(ContextModuleItemsApiUpdateRequestModuleItem.to_json())

# convert the object into a dict
context_module_items_api_update_request_module_item_dict = context_module_items_api_update_request_module_item_instance.to_dict()
# create an instance of ContextModuleItemsApiUpdateRequestModuleItem from a dict
context_module_items_api_update_request_module_item_from_dict = ContextModuleItemsApiUpdateRequestModuleItem.from_dict(context_module_items_api_update_request_module_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


