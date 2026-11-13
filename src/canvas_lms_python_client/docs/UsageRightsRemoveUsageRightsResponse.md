# UsageRightsRemoveUsageRightsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_ids** | **List[int]** |  | [optional] 
**message** | **str** |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.usage_rights_remove_usage_rights_response import UsageRightsRemoveUsageRightsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UsageRightsRemoveUsageRightsResponse from a JSON string
usage_rights_remove_usage_rights_response_instance = UsageRightsRemoveUsageRightsResponse.from_json(json)
# print the JSON string representation of the object
print(UsageRightsRemoveUsageRightsResponse.to_json())

# convert the object into a dict
usage_rights_remove_usage_rights_response_dict = usage_rights_remove_usage_rights_response_instance.to_dict()
# create an instance of UsageRightsRemoveUsageRightsResponse from a dict
usage_rights_remove_usage_rights_response_from_dict = UsageRightsRemoveUsageRightsResponse.from_dict(usage_rights_remove_usage_rights_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


