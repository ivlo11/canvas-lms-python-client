# AccountsUpdateUsersRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_ids** | **List[str]** | The IDs of the users to update. | [optional] 
**user** | **str** | The attributes to update for each user. | [optional] 

## Example

```python
from canvas_lms_python_client.models.accounts_update_users_request import AccountsUpdateUsersRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AccountsUpdateUsersRequest from a JSON string
accounts_update_users_request_instance = AccountsUpdateUsersRequest.from_json(json)
# print the JSON string representation of the object
print(AccountsUpdateUsersRequest.to_json())

# convert the object into a dict
accounts_update_users_request_dict = accounts_update_users_request_instance.to_dict()
# create an instance of AccountsUpdateUsersRequest from a dict
accounts_update_users_request_from_dict = AccountsUpdateUsersRequest.from_dict(accounts_update_users_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


