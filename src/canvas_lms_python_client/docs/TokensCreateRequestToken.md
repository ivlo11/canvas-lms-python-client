# TokensCreateRequestToken


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**purpose** | **str** | [Required, String] The purpose of the token. | 
**expires_at** | **str** | [DateTime] The time at which the token will expire. | [optional] 
**scopes** | **str** | [] [Array] The scopes to associate with the token. Ignored if the default developer key does not have the \&quot;enable scopes\&quot; option enabled. In such cases, the token will inherit the user&#39;s permissions instead. | [optional] 

## Example

```python
from canvas_lms_python_client.models.tokens_create_request_token import TokensCreateRequestToken

# TODO update the JSON string below
json = "{}"
# create an instance of TokensCreateRequestToken from a JSON string
tokens_create_request_token_instance = TokensCreateRequestToken.from_json(json)
# print the JSON string representation of the object
print(TokensCreateRequestToken.to_json())

# convert the object into a dict
tokens_create_request_token_dict = tokens_create_request_token_instance.to_dict()
# create an instance of TokensCreateRequestToken from a dict
tokens_create_request_token_from_dict = TokensCreateRequestToken.from_dict(tokens_create_request_token_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


