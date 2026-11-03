# AuthenticationAuditApiForUserResponse

Object response with `links`, `events`, `linked` (from the Canvas `@returns`).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | **object** |  | [optional] 
**events** | [**List[AuthenticationEvent]**](AuthenticationEvent.md) |  | [optional] 
**linked** | **object** |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.authentication_audit_api_for_user_response import AuthenticationAuditApiForUserResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticationAuditApiForUserResponse from a JSON string
authentication_audit_api_for_user_response_instance = AuthenticationAuditApiForUserResponse.from_json(json)
# print the JSON string representation of the object
print(AuthenticationAuditApiForUserResponse.to_json())

# convert the object into a dict
authentication_audit_api_for_user_response_dict = authentication_audit_api_for_user_response_instance.to_dict()
# create an instance of AuthenticationAuditApiForUserResponse from a dict
authentication_audit_api_for_user_response_from_dict = AuthenticationAuditApiForUserResponse.from_dict(authentication_audit_api_for_user_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


