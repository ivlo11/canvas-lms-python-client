# TokensUpdateRequestToken


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**purpose** | **str** | [String] The purpose of the token. | [optional] 
**expires_at** | **str** | [DateTime] The time at which the token will expire. | [optional] 
**scopes** | **str** | [] [Array] The scopes to associate with the token. | [optional] 
**regenerate** | **bool** | [Boolean] Regenerate the actual token. | [optional] 

## Example

```python
from canvas_lms_python_client.models.tokens_update_request_token import TokensUpdateRequestToken

# TODO update the JSON string below
json = "{}"
# create an instance of TokensUpdateRequestToken from a JSON string
tokens_update_request_token_instance = TokensUpdateRequestToken.from_json(json)
# print the JSON string representation of the object
print(TokensUpdateRequestToken.to_json())

# convert the object into a dict
tokens_update_request_token_dict = tokens_update_request_token_instance.to_dict()
# create an instance of TokensUpdateRequestToken from a dict
tokens_update_request_token_from_dict = TokensUpdateRequestToken.from_dict(tokens_update_request_token_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


