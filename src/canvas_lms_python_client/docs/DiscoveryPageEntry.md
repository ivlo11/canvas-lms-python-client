# DiscoveryPageEntry

A single authentication provider entry on the discovery page

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authentication_provider_id** | **int** | The ID of the authentication provider | [optional] 
**label** | **str** | The display label for this provider button | [optional] 
**icon** | **str** | Icon key for this provider button | [optional] 

## Example

```python
from canvas_lms_python_client.models.discovery_page_entry import DiscoveryPageEntry

# TODO update the JSON string below
json = "{}"
# create an instance of DiscoveryPageEntry from a JSON string
discovery_page_entry_instance = DiscoveryPageEntry.from_json(json)
# print the JSON string representation of the object
print(DiscoveryPageEntry.to_json())

# convert the object into a dict
discovery_page_entry_dict = discovery_page_entry_instance.to_dict()
# create an instance of DiscoveryPageEntry from a dict
discovery_page_entry_from_dict = DiscoveryPageEntry.from_dict(discovery_page_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


