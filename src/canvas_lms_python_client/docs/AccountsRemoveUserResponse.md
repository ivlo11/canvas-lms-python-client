# AccountsRemoveUserResponse

Object response with `user` (from the Canvas `@returns`).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | [**User**](User.md) |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.accounts_remove_user_response import AccountsRemoveUserResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AccountsRemoveUserResponse from a JSON string
accounts_remove_user_response_instance = AccountsRemoveUserResponse.from_json(json)
# print the JSON string representation of the object
print(AccountsRemoveUserResponse.to_json())

# convert the object into a dict
accounts_remove_user_response_dict = accounts_remove_user_response_instance.to_dict()
# create an instance of AccountsRemoveUserResponse from a dict
accounts_remove_user_response_from_dict = AccountsRemoveUserResponse.from_dict(accounts_remove_user_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


