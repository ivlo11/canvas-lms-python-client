# ContextModuleItemsApiUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**module_item** | [**ContextModuleItemsApiUpdateRequestModuleItem**](ContextModuleItemsApiUpdateRequestModuleItem.md) |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.context_module_items_api_update_request import ContextModuleItemsApiUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ContextModuleItemsApiUpdateRequest from a JSON string
context_module_items_api_update_request_instance = ContextModuleItemsApiUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(ContextModuleItemsApiUpdateRequest.to_json())

# convert the object into a dict
context_module_items_api_update_request_dict = context_module_items_api_update_request_instance.to_dict()
# create an instance of ContextModuleItemsApiUpdateRequest from a dict
context_module_items_api_update_request_from_dict = ContextModuleItemsApiUpdateRequest.from_dict(context_module_items_api_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


