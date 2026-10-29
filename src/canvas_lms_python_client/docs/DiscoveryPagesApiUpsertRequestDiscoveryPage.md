# DiscoveryPagesApiUpsertRequestDiscoveryPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**primary** | **str** | [][icon] [String] Icon key for this authentication provider button. | [optional] 
**secondary** | **str** | [][icon] [String] Icon key for this authentication provider button. | [optional] 
**active** | **bool** | [Boolean] Whether the discovery page is enabled. Defaults to false if not provided. | [optional] 

## Example

```python
from canvas_lms_python_client.models.discovery_pages_api_upsert_request_discovery_page import DiscoveryPagesApiUpsertRequestDiscoveryPage

# TODO update the JSON string below
json = "{}"
# create an instance of DiscoveryPagesApiUpsertRequestDiscoveryPage from a JSON string
discovery_pages_api_upsert_request_discovery_page_instance = DiscoveryPagesApiUpsertRequestDiscoveryPage.from_json(json)
# print the JSON string representation of the object
print(DiscoveryPagesApiUpsertRequestDiscoveryPage.to_json())

# convert the object into a dict
discovery_pages_api_upsert_request_discovery_page_dict = discovery_pages_api_upsert_request_discovery_page_instance.to_dict()
# create an instance of DiscoveryPagesApiUpsertRequestDiscoveryPage from a dict
discovery_pages_api_upsert_request_discovery_page_from_dict = DiscoveryPagesApiUpsertRequestDiscoveryPage.from_dict(discovery_pages_api_upsert_request_discovery_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


