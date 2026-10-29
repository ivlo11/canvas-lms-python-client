# CspSettingsSetCspSettingRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | If set to \&quot;enabled\&quot; for an account, CSP will be enabled for all its courses and sub-accounts (that have not explicitly enabled or disabled it), using the allowed domains set on this account. If set to \&quot;disabled\&quot;, CSP will be disabled for this account or course and for all sub-accounts that have not explicitly re-enabled it. If set to \&quot;inherited\&quot;, this account or course will reset to the default state where CSP settings are inherited from the first parent account to have them explicitly set. | 

## Example

```python
from canvas_lms_python_client.models.csp_settings_set_csp_setting_request import CspSettingsSetCspSettingRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CspSettingsSetCspSettingRequest from a JSON string
csp_settings_set_csp_setting_request_instance = CspSettingsSetCspSettingRequest.from_json(json)
# print the JSON string representation of the object
print(CspSettingsSetCspSettingRequest.to_json())

# convert the object into a dict
csp_settings_set_csp_setting_request_dict = csp_settings_set_csp_setting_request_instance.to_dict()
# create an instance of CspSettingsSetCspSettingRequest from a dict
csp_settings_set_csp_setting_request_from_dict = CspSettingsSetCspSettingRequest.from_dict(csp_settings_set_csp_setting_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


