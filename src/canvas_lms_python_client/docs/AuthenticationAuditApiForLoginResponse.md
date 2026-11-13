# AuthenticationAuditApiForLoginResponse

Object response with `links`, `events`, `linked` (from the Canvas `@returns`).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | **object** |  | [optional] 
**events** | [**List[AuthenticationEvent]**](AuthenticationEvent.md) |  | [optional] 
**linked** | [**AuthenticationLinkedRecords**](AuthenticationLinkedRecords.md) |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.authentication_audit_api_for_login_response import AuthenticationAuditApiForLoginResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticationAuditApiForLoginResponse from a JSON string
authentication_audit_api_for_login_response_instance = AuthenticationAuditApiForLoginResponse.from_json(json)
# print the JSON string representation of the object
print(AuthenticationAuditApiForLoginResponse.to_json())

# convert the object into a dict
authentication_audit_api_for_login_response_dict = authentication_audit_api_for_login_response_instance.to_dict()
# create an instance of AuthenticationAuditApiForLoginResponse from a dict
authentication_audit_api_for_login_response_from_dict = AuthenticationAuditApiForLoginResponse.from_dict(authentication_audit_api_for_login_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


