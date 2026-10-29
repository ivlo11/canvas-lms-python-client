# UsageRightsSetUsageRightsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_ids** | **List[str]** | List of ids of files to set usage rights for. | 
**folder_ids** | **List[str]** | List of ids of folders to search for files to set usage rights for. Note that new files uploaded to these folders do not automatically inherit these rights. | [optional] 
**publish** | **bool** | Whether the file(s) or folder(s) should be published on save, provided that usage rights have been specified (set to &#x60;true&#x60; to publish on save). | [optional] 
**usage_rights** | [**UsageRightsSetUsageRightsRequestUsageRights**](UsageRightsSetUsageRightsRequestUsageRights.md) |  | 

## Example

```python
from canvas_lms_python_client.models.usage_rights_set_usage_rights_request import UsageRightsSetUsageRightsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UsageRightsSetUsageRightsRequest from a JSON string
usage_rights_set_usage_rights_request_instance = UsageRightsSetUsageRightsRequest.from_json(json)
# print the JSON string representation of the object
print(UsageRightsSetUsageRightsRequest.to_json())

# convert the object into a dict
usage_rights_set_usage_rights_request_dict = usage_rights_set_usage_rights_request_instance.to_dict()
# create an instance of UsageRightsSetUsageRightsRequest from a dict
usage_rights_set_usage_rights_request_from_dict = UsageRightsSetUsageRightsRequest.from_dict(usage_rights_set_usage_rights_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


