# AuthorizationJWT

This is a JWT (https://tools.ietf.org/html/rfc7519), we highly recommend using a library to create these tokens. The token should be signed with the shared secret found in the Tool Proxy, which must be using the 'splitSecret' capability. If a tool proxy has not yet been created in Canvas a developer key may be used to sign the token. In this case the ‘sub’ claim of the token should be the developer key ID.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sub** | **str** | The Tool Proxy Guid OR Developer key ID. A developer key ID should only be used if a tool proxy has not been created in Canvas. In this case the token should be signed with the developer key rather than the tool proxy shared secret. | [optional] 
**aud** | **str** | The LTI 2 token authorization endpoint, can be found in the Tool Consumer Profile | [optional] 
**exp** | **int** | When this token expires, should be no more than 1 minute in the future | [optional] 
**iat** | **int** | The time this token was created | [optional] 
**jti** | **str** | A unique ID for this token. Should be a UUID | [optional] 

## Example

```python
from canvas_lms_python_client.models.authorization_jwt import AuthorizationJWT

# TODO update the JSON string below
json = "{}"
# create an instance of AuthorizationJWT from a JSON string
authorization_jwt_instance = AuthorizationJWT.from_json(json)
# print the JSON string representation of the object
print(AuthorizationJWT.to_json())

# convert the object into a dict
authorization_jwt_dict = authorization_jwt_instance.to_dict()
# create an instance of AuthorizationJWT from a dict
authorization_jwt_from_dict = AuthorizationJWT.from_dict(authorization_jwt_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


