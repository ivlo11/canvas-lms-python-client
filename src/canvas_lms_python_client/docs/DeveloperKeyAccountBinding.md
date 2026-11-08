# DeveloperKeyAccountBinding



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **float** | The Canvas ID of the binding | [optional] 
**account_id** | **float** | The global Canvas ID of the account in the binding | [optional] 
**developer_key_id** | **float** | The global Canvas ID of the developer key in the binding | [optional] 
**workflow_state** | [**DeveloperKeyAccountBindingWorkflowState**](DeveloperKeyAccountBindingWorkflowState.md) |  | [optional] 
**account_owns_binding** | **bool** | True if the requested context owns the binding | [optional] 

## Example

```python
from canvas_lms_python_client.models.developer_key_account_binding import DeveloperKeyAccountBinding

# TODO update the JSON string below
json = "{}"
# create an instance of DeveloperKeyAccountBinding from a JSON string
developer_key_account_binding_instance = DeveloperKeyAccountBinding.from_json(json)
# print the JSON string representation of the object
print(DeveloperKeyAccountBinding.to_json())

# convert the object into a dict
developer_key_account_binding_dict = developer_key_account_binding_instance.to_dict()
# create an instance of DeveloperKeyAccountBinding from a dict
developer_key_account_binding_from_dict = DeveloperKeyAccountBinding.from_dict(developer_key_account_binding_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


