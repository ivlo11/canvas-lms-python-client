# CspSettingsAddDomainRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** |  | 

## Example

```python
from canvas_lms_python_client.models.csp_settings_add_domain_request import CspSettingsAddDomainRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CspSettingsAddDomainRequest from a JSON string
csp_settings_add_domain_request_instance = CspSettingsAddDomainRequest.from_json(json)
# print the JSON string representation of the object
print(CspSettingsAddDomainRequest.to_json())

# convert the object into a dict
csp_settings_add_domain_request_dict = csp_settings_add_domain_request_instance.to_dict()
# create an instance of CspSettingsAddDomainRequest from a dict
csp_settings_add_domain_request_from_dict = CspSettingsAddDomainRequest.from_dict(csp_settings_add_domain_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


