# DiscoveryPagesApiUpsertRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**discovery_page** | [**DiscoveryPagesApiUpsertRequestDiscoveryPage**](DiscoveryPagesApiUpsertRequestDiscoveryPage.md) |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.discovery_pages_api_upsert_request import DiscoveryPagesApiUpsertRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DiscoveryPagesApiUpsertRequest from a JSON string
discovery_pages_api_upsert_request_instance = DiscoveryPagesApiUpsertRequest.from_json(json)
# print the JSON string representation of the object
print(DiscoveryPagesApiUpsertRequest.to_json())

# convert the object into a dict
discovery_pages_api_upsert_request_dict = discovery_pages_api_upsert_request_instance.to_dict()
# create an instance of DiscoveryPagesApiUpsertRequest from a dict
discovery_pages_api_upsert_request_from_dict = DiscoveryPagesApiUpsertRequest.from_dict(discovery_pages_api_upsert_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


