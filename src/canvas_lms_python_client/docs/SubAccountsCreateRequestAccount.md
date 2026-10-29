# SubAccountsCreateRequestAccount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | [Required, String] The name of the new sub-account. | 
**sis_account_id** | **str** | [String] The account&#39;s identifier in the Student Information System. | [optional] 
**default_storage_quota_mb** | **int** | [Integer] The default course storage quota to be used, if not otherwise specified. | [optional] 
**default_user_storage_quota_mb** | **int** | [Integer] The default user storage quota to be used, if not otherwise specified. | [optional] 
**default_group_storage_quota_mb** | **int** | [Integer] The default group storage quota to be used, if not otherwise specified. | [optional] 

## Example

```python
from canvas_lms_python_client.models.sub_accounts_create_request_account import SubAccountsCreateRequestAccount

# TODO update the JSON string below
json = "{}"
# create an instance of SubAccountsCreateRequestAccount from a JSON string
sub_accounts_create_request_account_instance = SubAccountsCreateRequestAccount.from_json(json)
# print the JSON string representation of the object
print(SubAccountsCreateRequestAccount.to_json())

# convert the object into a dict
sub_accounts_create_request_account_dict = sub_accounts_create_request_account_instance.to_dict()
# create an instance of SubAccountsCreateRequestAccount from a dict
sub_accounts_create_request_account_from_dict = SubAccountsCreateRequestAccount.from_dict(sub_accounts_create_request_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


