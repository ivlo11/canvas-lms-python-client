# PseudonymsUpdateRequestLogin


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unique_id** | **str** | [String] The new unique ID for the login. | [optional] 
**password** | **str** | [String] The new password for the login. Admins can only set a password for another user if the \&quot;Password setting by admins\&quot; account setting is enabled. | [optional] 
**old_password** | **str** | [String] The prior password for the login. Required if the caller is changing their own password. | [optional] 
**sis_user_id** | **str** | [String] SIS ID for the login. To set this parameter, the caller must be able to manage SIS permissions on the account. | [optional] 
**integration_id** | **str** | [String] Integration ID for the login. To set this parameter, the caller must be able to manage SIS permissions on the account. The Integration ID is a secondary identifier useful for more complex SIS integrations. | [optional] 
**authentication_provider_id** | **str** | [String] The authentication provider this login is associated with. Logins associated with a specific provider can only be used with that provider. Legacy providers (LDAP, CAS, SAML) will search for logins associated with them, or unassociated logins. New providers will only search for logins explicitly associated with them. This can be the integer ID of the provider, or the type of the provider (in which case, it will find the first matching provider). To unassociate from a known provider, specify null or an empty string. | [optional] 
**workflow_state** | **str** | [String, \&quot;active\&quot;|\&quot;suspended\&quot;] Used to suspend or re-activate a login. | [optional] 
**declared_user_type** | **str** | [String] The declared intention of the user type. This can be set, but does not change any Canvas functionality with respect to their access. A user can still be a teacher, admin, student, etc. in any particular context without regard to this setting. This can be used for administrative purposes for integrations to be able to more easily identify why the user was created. Valid values are:   * administrative   * observer   * staff   * student   * student_other   * teacher | [optional] 

## Example

```python
from canvas_lms_python_client.models.pseudonyms_update_request_login import PseudonymsUpdateRequestLogin

# TODO update the JSON string below
json = "{}"
# create an instance of PseudonymsUpdateRequestLogin from a JSON string
pseudonyms_update_request_login_instance = PseudonymsUpdateRequestLogin.from_json(json)
# print the JSON string representation of the object
print(PseudonymsUpdateRequestLogin.to_json())

# convert the object into a dict
pseudonyms_update_request_login_dict = pseudonyms_update_request_login_instance.to_dict()
# create an instance of PseudonymsUpdateRequestLogin from a dict
pseudonyms_update_request_login_from_dict = PseudonymsUpdateRequestLogin.from_dict(pseudonyms_update_request_login_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


