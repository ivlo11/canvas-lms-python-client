# AccountsUpdateUsersRequestUserIds


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**array_integer** | **str** | The IDs of the users to update. | [optional] 

## Example

```python
from canvas_lms_python_client.models.accounts_update_users_request_user_ids import AccountsUpdateUsersRequestUserIds

# TODO update the JSON string below
json = "{}"
# create an instance of AccountsUpdateUsersRequestUserIds from a JSON string
accounts_update_users_request_user_ids_instance = AccountsUpdateUsersRequestUserIds.from_json(json)
# print the JSON string representation of the object
print(AccountsUpdateUsersRequestUserIds.to_json())

# convert the object into a dict
accounts_update_users_request_user_ids_dict = accounts_update_users_request_user_ids_instance.to_dict()
# create an instance of AccountsUpdateUsersRequestUserIds from a dict
accounts_update_users_request_user_ids_from_dict = AccountsUpdateUsersRequestUserIds.from_dict(accounts_update_users_request_user_ids_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


