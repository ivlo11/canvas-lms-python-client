# DeveloperKeyAccountBindingsCreateOrUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workflow_state** | **str** | The workflow state for the binding. Must be one of \&quot;on\&quot;, \&quot;off\&quot;, or \&quot;allow\&quot;. Defaults to \&quot;off\&quot;. | [optional] 

## Example

```python
from canvas_lms_python_client.models.developer_key_account_bindings_create_or_update_request import DeveloperKeyAccountBindingsCreateOrUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeveloperKeyAccountBindingsCreateOrUpdateRequest from a JSON string
developer_key_account_bindings_create_or_update_request_instance = DeveloperKeyAccountBindingsCreateOrUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(DeveloperKeyAccountBindingsCreateOrUpdateRequest.to_json())

# convert the object into a dict
developer_key_account_bindings_create_or_update_request_dict = developer_key_account_bindings_create_or_update_request_instance.to_dict()
# create an instance of DeveloperKeyAccountBindingsCreateOrUpdateRequest from a dict
developer_key_account_bindings_create_or_update_request_from_dict = DeveloperKeyAccountBindingsCreateOrUpdateRequest.from_dict(developer_key_account_bindings_create_or_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


