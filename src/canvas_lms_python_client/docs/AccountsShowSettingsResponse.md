# AccountsShowSettingsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_assign_to_differentiation_tags** | **object** |  | [optional] 
**enable_as_k5_account** | **object** |  | [optional] 
**horizon_account** | **object** |  | [optional] 
**microsoft_sync_enabled** | **bool** |  | [optional] 
**microsoft_sync_tenant** | **str** |  | [optional] 
**password_policy** | **object** |  | [optional] 
**use_classic_font_in_k5** | **object** |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.accounts_show_settings_response import AccountsShowSettingsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AccountsShowSettingsResponse from a JSON string
accounts_show_settings_response_instance = AccountsShowSettingsResponse.from_json(json)
# print the JSON string representation of the object
print(AccountsShowSettingsResponse.to_json())

# convert the object into a dict
accounts_show_settings_response_dict = accounts_show_settings_response_instance.to_dict()
# create an instance of AccountsShowSettingsResponse from a dict
accounts_show_settings_response_from_dict = AccountsShowSettingsResponse.from_dict(accounts_show_settings_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


