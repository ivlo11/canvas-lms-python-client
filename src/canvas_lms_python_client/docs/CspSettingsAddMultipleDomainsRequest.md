# CspSettingsAddMultipleDomainsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domains** | **List[str]** |  | 

## Example

```python
from canvas_lms_python_client.models.csp_settings_add_multiple_domains_request import CspSettingsAddMultipleDomainsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CspSettingsAddMultipleDomainsRequest from a JSON string
csp_settings_add_multiple_domains_request_instance = CspSettingsAddMultipleDomainsRequest.from_json(json)
# print the JSON string representation of the object
print(CspSettingsAddMultipleDomainsRequest.to_json())

# convert the object into a dict
csp_settings_add_multiple_domains_request_dict = csp_settings_add_multiple_domains_request_instance.to_dict()
# create an instance of CspSettingsAddMultipleDomainsRequest from a dict
csp_settings_add_multiple_domains_request_from_dict = CspSettingsAddMultipleDomainsRequest.from_dict(csp_settings_add_multiple_domains_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


