# DiscoveryPagesApiUpsertResponse

Object response with `discovery_page` (from the Canvas `@returns`).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**discovery_page** | [**DiscoveryPage**](DiscoveryPage.md) |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.discovery_pages_api_upsert_response import DiscoveryPagesApiUpsertResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DiscoveryPagesApiUpsertResponse from a JSON string
discovery_pages_api_upsert_response_instance = DiscoveryPagesApiUpsertResponse.from_json(json)
# print the JSON string representation of the object
print(DiscoveryPagesApiUpsertResponse.to_json())

# convert the object into a dict
discovery_pages_api_upsert_response_dict = discovery_pages_api_upsert_response_instance.to_dict()
# create an instance of DiscoveryPagesApiUpsertResponse from a dict
discovery_pages_api_upsert_response_from_dict = DiscoveryPagesApiUpsertResponse.from_dict(discovery_pages_api_upsert_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


