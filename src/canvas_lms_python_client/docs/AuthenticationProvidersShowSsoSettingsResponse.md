# AuthenticationProvidersShowSsoSettingsResponse

Object response with `sso_settings` (from the Canvas `@returns`).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sso_settings** | [**SSOSettings**](SSOSettings.md) |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.authentication_providers_show_sso_settings_response import AuthenticationProvidersShowSsoSettingsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticationProvidersShowSsoSettingsResponse from a JSON string
authentication_providers_show_sso_settings_response_instance = AuthenticationProvidersShowSsoSettingsResponse.from_json(json)
# print the JSON string representation of the object
print(AuthenticationProvidersShowSsoSettingsResponse.to_json())

# convert the object into a dict
authentication_providers_show_sso_settings_response_dict = authentication_providers_show_sso_settings_response_instance.to_dict()
# create an instance of AuthenticationProvidersShowSsoSettingsResponse from a dict
authentication_providers_show_sso_settings_response_from_dict = AuthenticationProvidersShowSsoSettingsResponse.from_dict(authentication_providers_show_sso_settings_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


