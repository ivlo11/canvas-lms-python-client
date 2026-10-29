# AuthenticationProvider



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier_format** | **str** | Valid for SAML providers. | [optional] 
**auth_type** | **str** | Valid for all providers. | [optional] 
**id** | **int** | Valid for all providers. | [optional] 
**log_out_url** | **str** | Valid for SAML providers. | [optional] 
**log_in_url** | **str** | Valid for SAML and CAS providers. | [optional] 
**certificate_fingerprint** | **str** | Valid for SAML providers. | [optional] 
**requested_authn_context** | **str** | Valid for SAML providers. | [optional] 
**auth_host** | **str** | Valid for LDAP providers. | [optional] 
**auth_filter** | **str** | Valid for LDAP providers. | [optional] 
**auth_over_tls** | **int** | Valid for LDAP providers. | [optional] 
**auth_base** | **str** | Valid for LDAP and CAS providers. | [optional] 
**auth_username** | **str** | Valid for LDAP providers. | [optional] 
**auth_port** | **int** | Valid for LDAP providers. | [optional] 
**position** | **int** | Valid for all providers. | [optional] 
**idp_entity_id** | **str** | Valid for SAML providers. | [optional] 
**login_attribute** | **str** | Valid for SAML providers. | [optional] 
**sig_alg** | **str** | Valid for SAML providers. | [optional] 
**jit_provisioning** | **bool** | Just In Time provisioning. Valid for all providers except Canvas (which has the similar in concept self_registration setting). | [optional] 
**federated_attributes** | [**FederatedAttributesConfig**](FederatedAttributesConfig.md) |  | [optional] 
**mfa_required** | **bool** | If multi-factor authentication is required when logging in with this authentication provider. The account must not have MFA disabled. | [optional] 

## Example

```python
from canvas_lms_python_client.models.authentication_provider import AuthenticationProvider

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticationProvider from a JSON string
authentication_provider_instance = AuthenticationProvider.from_json(json)
# print the JSON string representation of the object
print(AuthenticationProvider.to_json())

# convert the object into a dict
authentication_provider_dict = authentication_provider_instance.to_dict()
# create an instance of AuthenticationProvider from a dict
authentication_provider_from_dict = AuthenticationProvider.from_dict(authentication_provider_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


