# AuthenticationAuditApiForAccountResponse

Object response with `links`, `events`, `linked` (from the Canvas `@returns`).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | **object** |  | [optional] 
**events** | [**List[AuthenticationEvent]**](AuthenticationEvent.md) |  | [optional] 
**linked** | **object** |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.authentication_audit_api_for_account_response import AuthenticationAuditApiForAccountResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticationAuditApiForAccountResponse from a JSON string
authentication_audit_api_for_account_response_instance = AuthenticationAuditApiForAccountResponse.from_json(json)
# print the JSON string representation of the object
print(AuthenticationAuditApiForAccountResponse.to_json())

# convert the object into a dict
authentication_audit_api_for_account_response_dict = authentication_audit_api_for_account_response_instance.to_dict()
# create an instance of AuthenticationAuditApiForAccountResponse from a dict
authentication_audit_api_for_account_response_from_dict = AuthenticationAuditApiForAccountResponse.from_dict(authentication_audit_api_for_account_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


