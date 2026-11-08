# CspSettingsGetCspSettingsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_account_whitelist** | **List[object]** |  | [optional] 
**enabled** | **bool** |  | [optional] 
**inherited** | **bool** |  | [optional] 
**settings_locked** | **bool** |  | [optional] 
**tools_whitelist** | **object** |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.csp_settings_get_csp_settings_response import CspSettingsGetCspSettingsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CspSettingsGetCspSettingsResponse from a JSON string
csp_settings_get_csp_settings_response_instance = CspSettingsGetCspSettingsResponse.from_json(json)
# print the JSON string representation of the object
print(CspSettingsGetCspSettingsResponse.to_json())

# convert the object into a dict
csp_settings_get_csp_settings_response_dict = csp_settings_get_csp_settings_response_instance.to_dict()
# create an instance of CspSettingsGetCspSettingsResponse from a dict
csp_settings_get_csp_settings_response_from_dict = CspSettingsGetCspSettingsResponse.from_dict(csp_settings_get_csp_settings_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


