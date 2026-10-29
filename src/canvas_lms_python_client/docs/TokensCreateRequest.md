# TokensCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | [**TokensCreateRequestToken**](TokensCreateRequestToken.md) |  | 

## Example

```python
from canvas_lms_python_client.models.tokens_create_request import TokensCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TokensCreateRequest from a JSON string
tokens_create_request_instance = TokensCreateRequest.from_json(json)
# print the JSON string representation of the object
print(TokensCreateRequest.to_json())

# convert the object into a dict
tokens_create_request_dict = tokens_create_request_instance.to_dict()
# create an instance of TokensCreateRequest from a dict
tokens_create_request_from_dict = TokensCreateRequest.from_dict(tokens_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


