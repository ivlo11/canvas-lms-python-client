# AccountsUpdateRequestAccount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | [String] Updates the account name | [optional] 
**sis_account_id** | **str** | [String] Updates the account sis_account_id Must have manage_sis permission and must not be a root_account. | [optional] 
**default_time_zone** | **str** | [String] The default time zone of the account. Allowed time zones are {http://www.iana.org/time-zones IANA time zones} or friendlier {http://api.rubyonrails.org/classes/ActiveSupport/TimeZone.html Ruby on Rails time zones}. | [optional] 
**default_storage_quota_mb** | **int** | [Integer] The default course storage quota to be used, if not otherwise specified. | [optional] 
**default_user_storage_quota_mb** | **int** | [Integer] The default user storage quota to be used, if not otherwise specified. | [optional] 
**default_group_storage_quota_mb** | **int** | [Integer] The default group storage quota to be used, if not otherwise specified. | [optional] 
**course_template_id** | **int** | [Integer] The ID of a course to be used as a template for all newly created courses. Empty means to inherit the setting from parent account, 0 means to not use a template even if a parent account has one set. The course must be marked as a template. | [optional] 
**parent_account_id** | **str** | [Integer|String] The ID of a parent account to move the account to. The new parent account must be in the same root account as the original. The hierarchy of sub-accounts will be preserved in the new parent account. The caller must be an administrator in both the original parent account and the new parent account. | [optional] 
**settings** | **str** | [lock_proficiency_calculation][value] [Boolean] [DEPRECATED] Restrict instructors from changing proficiency calculation method | 
**lock_outcome_proficiency** | **str** | [locked] [Boolean] [DEPRECATED] Lock this setting for sub-accounts and courses | [optional] 
**lock_proficiency_calculation** | **str** | [locked] [Boolean] [DEPRECATED] Lock this setting for sub-accounts and courses | [optional] 
**services** | **str** | [Hash] Give this a set of keys and boolean values to enable or disable services matching the keys | [optional] 

## Example

```python
from canvas_lms_python_client.models.accounts_update_request_account import AccountsUpdateRequestAccount

# TODO update the JSON string below
json = "{}"
# create an instance of AccountsUpdateRequestAccount from a JSON string
accounts_update_request_account_instance = AccountsUpdateRequestAccount.from_json(json)
# print the JSON string representation of the object
print(AccountsUpdateRequestAccount.to_json())

# convert the object into a dict
accounts_update_request_account_dict = accounts_update_request_account_instance.to_dict()
# create an instance of AccountsUpdateRequestAccount from a dict
accounts_update_request_account_from_dict = AccountsUpdateRequestAccount.from_dict(accounts_update_request_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


