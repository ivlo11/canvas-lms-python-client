# AuthenticationProvidersUpdateSsoSettingsResponse

Object response with `sso_settings` (from the Canvas `@returns`).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sso_settings** | [**SSOSettings**](SSOSettings.md) |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.authentication_providers_update_sso_settings_response import AuthenticationProvidersUpdateSsoSettingsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticationProvidersUpdateSsoSettingsResponse from a JSON string
authentication_providers_update_sso_settings_response_instance = AuthenticationProvidersUpdateSsoSettingsResponse.from_json(json)
# print the JSON string representation of the object
print(AuthenticationProvidersUpdateSsoSettingsResponse.to_json())

# convert the object into a dict
authentication_providers_update_sso_settings_response_dict = authentication_providers_update_sso_settings_response_instance.to_dict()
# create an instance of AuthenticationProvidersUpdateSsoSettingsResponse from a dict
authentication_providers_update_sso_settings_response_from_dict = AuthenticationProvidersUpdateSsoSettingsResponse.from_dict(authentication_providers_update_sso_settings_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


