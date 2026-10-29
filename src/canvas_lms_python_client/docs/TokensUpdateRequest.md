# TokensUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | [**TokensUpdateRequestToken**](TokensUpdateRequestToken.md) |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.tokens_update_request import TokensUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TokensUpdateRequest from a JSON string
tokens_update_request_instance = TokensUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(TokensUpdateRequest.to_json())

# convert the object into a dict
tokens_update_request_dict = tokens_update_request_instance.to_dict()
# create an instance of TokensUpdateRequest from a dict
tokens_update_request_from_dict = TokensUpdateRequest.from_dict(tokens_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


