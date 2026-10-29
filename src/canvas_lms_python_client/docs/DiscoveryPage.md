# DiscoveryPage

Configuration for the login discovery page

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**primary** | [**List[DiscoveryPageEntry]**](DiscoveryPageEntry.md) | Primary authentication provider buttons displayed prominently | [optional] 
**secondary** | [**List[DiscoveryPageEntry]**](DiscoveryPageEntry.md) | Secondary authentication provider buttons displayed less prominently | [optional] 
**active** | **bool** | Whether the discovery page is enabled | [optional] 

## Example

```python
from canvas_lms_python_client.models.discovery_page import DiscoveryPage

# TODO update the JSON string below
json = "{}"
# create an instance of DiscoveryPage from a JSON string
discovery_page_instance = DiscoveryPage.from_json(json)
# print the JSON string representation of the object
print(DiscoveryPage.to_json())

# convert the object into a dict
discovery_page_dict = discovery_page_instance.to_dict()
# create an instance of DiscoveryPage from a dict
discovery_page_from_dict = DiscoveryPage.from_dict(discovery_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


