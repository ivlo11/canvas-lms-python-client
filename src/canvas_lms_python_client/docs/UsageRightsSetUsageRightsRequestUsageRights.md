# UsageRightsSetUsageRightsRequestUsageRights


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**use_justification** | **str** | [Required, String, \&quot;own_copyright\&quot;|\&quot;used_by_permission\&quot;|\&quot;fair_use\&quot;|\&quot;public_domain\&quot;|\&quot;creative_commons\&quot;] The intellectual property justification for using the files in Canvas | 
**legal_copyright** | **str** | [Optional, String] The legal copyright line for the files | [optional] 
**license** | **str** | [Optional, String] The license that applies to the files. See the {api:UsageRightsController#licenses List licenses endpoint} for the supported license types. | [optional] 

## Example

```python
from canvas_lms_python_client.models.usage_rights_set_usage_rights_request_usage_rights import UsageRightsSetUsageRightsRequestUsageRights

# TODO update the JSON string below
json = "{}"
# create an instance of UsageRightsSetUsageRightsRequestUsageRights from a JSON string
usage_rights_set_usage_rights_request_usage_rights_instance = UsageRightsSetUsageRightsRequestUsageRights.from_json(json)
# print the JSON string representation of the object
print(UsageRightsSetUsageRightsRequestUsageRights.to_json())

# convert the object into a dict
usage_rights_set_usage_rights_request_usage_rights_dict = usage_rights_set_usage_rights_request_usage_rights_instance.to_dict()
# create an instance of UsageRightsSetUsageRightsRequestUsageRights from a dict
usage_rights_set_usage_rights_request_usage_rights_from_dict = UsageRightsSetUsageRightsRequestUsageRights.from_dict(usage_rights_set_usage_rights_request_usage_rights_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


