# DiscoveryPagesApiTokenResponse

Object response with `token` (from the Canvas `@returns`).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.discovery_pages_api_token_response import DiscoveryPagesApiTokenResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DiscoveryPagesApiTokenResponse from a JSON string
discovery_pages_api_token_response_instance = DiscoveryPagesApiTokenResponse.from_json(json)
# print the JSON string representation of the object
print(DiscoveryPagesApiTokenResponse.to_json())

# convert the object into a dict
discovery_pages_api_token_response_dict = discovery_pages_api_token_response_instance.to_dict()
# create an instance of DiscoveryPagesApiTokenResponse from a dict
discovery_pages_api_token_response_from_dict = DiscoveryPagesApiTokenResponse.from_dict(discovery_pages_api_token_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


