# Token


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The internal database ID of the token. | [optional] 
**created_at** | **datetime** | The time the token was created. | [optional] 
**expires_at** | **datetime** | The time the token will permanently expire, or null if it does not permanently expire. | [optional] 
**workflow_state** | **str** | The current state of the token. One of &#39;active&#39;, &#39;pending&#39;, &#39;disabled&#39;, or &#39;deleted&#39;. | [optional] 
**remember_access** | **bool** | Whether the token should be remembered across sessions. Only applicable for OAuth tokens. | [optional] 
**scopes** | **List[str]** | The scopes associated with the token. If empty, there are no scope limitations. | [optional] 
**real_user_id** | **int** | If the token was created while masquerading, this is the ID of the real user. Otherwise, null. | [optional] 
**token** | **str** | The actual access token. Only included when the token is first created. | [optional] 
**token_hint** | **str** | A short, unique string that can be used to look up the token. | [optional] 
**user_id** | **int** | The ID of the user the token belongs to. | [optional] 
**purpose** | **str** | The purpose of the token. | [optional] 
**app_name** | **str** | If the token was created by an OAuth application, this is the name of that application. Otherwise, null. | [optional] 
**can_manually_regenerate** | **bool** | Whether the current user can manually regenerate this token. | [optional] 
**last_used_at** | **object** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**visible_token** | **str** |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.token import Token

# TODO update the JSON string below
json = "{}"
# create an instance of Token from a JSON string
token_instance = Token.from_json(json)
# print the JSON string representation of the object
print(Token.to_json())

# convert the object into a dict
token_dict = token_instance.to_dict()
# create an instance of Token from a dict
token_from_dict = Token.from_dict(token_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


