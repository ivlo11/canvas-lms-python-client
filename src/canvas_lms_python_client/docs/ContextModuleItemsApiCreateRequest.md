# ContextModuleItemsApiCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**module_item** | [**ContextModuleItemsApiCreateRequestModuleItem**](ContextModuleItemsApiCreateRequestModuleItem.md) |  | 

## Example

```python
from canvas_lms_python_client.models.context_module_items_api_create_request import ContextModuleItemsApiCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ContextModuleItemsApiCreateRequest from a JSON string
context_module_items_api_create_request_instance = ContextModuleItemsApiCreateRequest.from_json(json)
# print the JSON string representation of the object
print(ContextModuleItemsApiCreateRequest.to_json())

# convert the object into a dict
context_module_items_api_create_request_dict = context_module_items_api_create_request_instance.to_dict()
# create an instance of ContextModuleItemsApiCreateRequest from a dict
context_module_items_api_create_request_from_dict = ContextModuleItemsApiCreateRequest.from_dict(context_module_items_api_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


