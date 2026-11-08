# AccountsEnvironmentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**calendar_contexts_limit** | **int** |  | [optional] 
**enable_inbox_auto_response** | **bool** |  | [optional] 
**enable_inbox_signature_block** | **bool** |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.accounts_environment_response import AccountsEnvironmentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AccountsEnvironmentResponse from a JSON string
accounts_environment_response_instance = AccountsEnvironmentResponse.from_json(json)
# print the JSON string representation of the object
print(AccountsEnvironmentResponse.to_json())

# convert the object into a dict
accounts_environment_response_dict = accounts_environment_response_instance.to_dict()
# create an instance of AccountsEnvironmentResponse from a dict
accounts_environment_response_from_dict = AccountsEnvironmentResponse.from_dict(accounts_environment_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


