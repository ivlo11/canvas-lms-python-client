# UsersCreateRequestPseudonym


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unique_id** | **str** | [Required, String] User&#39;s login ID. If this is a self-registration, it must be a valid email address. | 
**password** | **str** | [String] User&#39;s password. Cannot be set during self-registration. | [optional] 
**sis_user_id** | **str** | [String] SIS ID for the user&#39;s account. To set this parameter, the caller must be able to manage SIS permissions. | [optional] 
**integration_id** | **str** | [String] Integration ID for the login. To set this parameter, the caller must be able to manage SIS permissions. The Integration ID is a secondary identifier useful for more complex SIS integrations. | [optional] 
**send_confirmation** | **bool** | [Boolean] Send user notification of account creation if true. Automatically set to true during self-registration. | [optional] 
**force_self_registration** | **bool** | [Boolean] Send user a self-registration style email if true. Setting it means the users will get a notification asking them to \&quot;complete the registration process\&quot; by clicking it, setting a password, and letting them in.  Will only be executed on if the user does not need admin approval. Defaults to false unless explicitly provided. | [optional] 
**authentication_provider_id** | **str** | [String] The authentication provider this login is associated with. Logins associated with a specific provider can only be used with that provider. Legacy providers (LDAP, CAS, SAML) will search for logins associated with them, or unassociated logins. New providers will only search for logins explicitly associated with them. This can be the integer ID of the provider, or the type of the provider (in which case, it will find the first matching provider). | [optional] 

## Example

```python
from canvas_lms_python_client.models.users_create_request_pseudonym import UsersCreateRequestPseudonym

# TODO update the JSON string below
json = "{}"
# create an instance of UsersCreateRequestPseudonym from a JSON string
users_create_request_pseudonym_instance = UsersCreateRequestPseudonym.from_json(json)
# print the JSON string representation of the object
print(UsersCreateRequestPseudonym.to_json())

# convert the object into a dict
users_create_request_pseudonym_dict = users_create_request_pseudonym_instance.to_dict()
# create an instance of UsersCreateRequestPseudonym from a dict
users_create_request_pseudonym_from_dict = UsersCreateRequestPseudonym.from_dict(users_create_request_pseudonym_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


