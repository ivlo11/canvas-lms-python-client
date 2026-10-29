# DiscoveryPagesApiTokenRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**discovery_page** | [**DiscoveryPagesApiTokenRequestDiscoveryPage**](DiscoveryPagesApiTokenRequestDiscoveryPage.md) |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.discovery_pages_api_token_request import DiscoveryPagesApiTokenRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DiscoveryPagesApiTokenRequest from a JSON string
discovery_pages_api_token_request_instance = DiscoveryPagesApiTokenRequest.from_json(json)
# print the JSON string representation of the object
print(DiscoveryPagesApiTokenRequest.to_json())

# convert the object into a dict
discovery_pages_api_token_request_dict = discovery_pages_api_token_request_instance.to_dict()
# create an instance of DiscoveryPagesApiTokenRequest from a dict
discovery_pages_api_token_request_from_dict = DiscoveryPagesApiTokenRequest.from_dict(discovery_pages_api_token_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


