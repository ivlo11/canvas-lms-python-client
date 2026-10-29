# ContextModuleItemsApiCreateRequestModuleItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | [String] The name of the module item and associated content | [optional] 
**type** | **str** | [Required, String, \&quot;File\&quot;|\&quot;Page\&quot;|\&quot;Discussion\&quot;|\&quot;Assignment\&quot;|\&quot;Quiz\&quot;|\&quot;SubHeader\&quot;|\&quot;ExternalUrl\&quot;|\&quot;ExternalTool\&quot;] The type of content linked to the item | 
**content_id** | **str** | [Required, String] The id of the content to link to the module item. Required, except for &#39;ExternalUrl&#39;, &#39;Page&#39;, and &#39;SubHeader&#39; types. | 
**position** | **int** | [Integer] The position of this item in the module (1-based). | [optional] 
**indent** | **int** | [Integer] 0-based indent level; module items may be indented to show a hierarchy | [optional] 
**page_url** | **str** | [String] Suffix for the linked wiki page (e.g. &#39;front-page&#39;). Required for &#39;Page&#39; type. | [optional] 
**external_url** | **str** | [String] External url that the item points to. [Required for &#39;ExternalUrl&#39; and &#39;ExternalTool&#39; types. | [optional] 
**new_tab** | **bool** | [Boolean] Whether the external tool opens in a new tab. Only applies to &#39;ExternalTool&#39; type. | [optional] 
**completion_requirement** | **str** | [min_score] [Integer] Minimum score required to complete. Required for completion_requirement type &#39;min_score&#39;. | [optional] 
**iframe** | **str** | [height] [Integer] Height of the ExternalTool on launch | [optional] 

## Example

```python
from canvas_lms_python_client.models.context_module_items_api_create_request_module_item import ContextModuleItemsApiCreateRequestModuleItem

# TODO update the JSON string below
json = "{}"
# create an instance of ContextModuleItemsApiCreateRequestModuleItem from a JSON string
context_module_items_api_create_request_module_item_instance = ContextModuleItemsApiCreateRequestModuleItem.from_json(json)
# print the JSON string representation of the object
print(ContextModuleItemsApiCreateRequestModuleItem.to_json())

# convert the object into a dict
context_module_items_api_create_request_module_item_dict = context_module_items_api_create_request_module_item_instance.to_dict()
# create an instance of ContextModuleItemsApiCreateRequestModuleItem from a dict
context_module_items_api_create_request_module_item_from_dict = ContextModuleItemsApiCreateRequestModuleItem.from_dict(context_module_items_api_create_request_module_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


