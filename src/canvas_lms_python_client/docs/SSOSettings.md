# SSOSettings

Settings that are applicable across an account's authentication configuration, even if there are multiple individual providers

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**login_handle_name** | **str** | The label used for unique login identifiers. | [optional] 
**change_password_url** | **str** | The url to redirect users to for password resets. Leave blank for default Canvas behavior | [optional] 
**auth_discovery_url** | **str** | If a discovery url is set, canvas will forward all users to that URL when they need to be authenticated. That page will need to then help the user figure out where they need to go to log in. If no discovery url is configured, the first configuration will be used to attempt to authenticate the user. | [optional] 
**unknown_user_url** | **str** | If an unknown user url is set, Canvas will forward to that url when a service authenticates a user, but that user does not exist in Canvas. The default behavior is to present an error. | [optional] 
**login_help_url** | **str** | A login help URL shown as a &#39;Trouble logging in?&#39; link on the login page and in failed login messages. Falls back to the global setting if not set. | [optional] 

## Example

```python
from canvas_lms_python_client.models.sso_settings import SSOSettings

# TODO update the JSON string below
json = "{}"
# create an instance of SSOSettings from a JSON string
sso_settings_instance = SSOSettings.from_json(json)
# print the JSON string representation of the object
print(SSOSettings.to_json())

# convert the object into a dict
sso_settings_dict = sso_settings_instance.to_dict()
# create an instance of SSOSettings from a dict
sso_settings_from_dict = SSOSettings.from_dict(sso_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


