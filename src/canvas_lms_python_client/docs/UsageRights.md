# UsageRights

Describes the copyright and license information for a File

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**legal_copyright** | **str** | Copyright line for the file | [optional] 
**use_justification** | **str** | Justification for using the file in a Canvas course. Valid values are &#39;own_copyright&#39;, &#39;public_domain&#39;, &#39;used_by_permission&#39;, &#39;fair_use&#39;, &#39;creative_commons&#39; | [optional] 
**license** | **str** | License identifier for the file. | [optional] 
**license_name** | **str** | Readable license name | [optional] 
**message** | **str** | Explanation of the action performed | [optional] 
**file_ids** | **List[int]** | List of ids of files that were updated | [optional] 

## Example

```python
from canvas_lms_python_client.models.usage_rights import UsageRights

# TODO update the JSON string below
json = "{}"
# create an instance of UsageRights from a JSON string
usage_rights_instance = UsageRights.from_json(json)
# print the JSON string representation of the object
print(UsageRights.to_json())

# convert the object into a dict
usage_rights_dict = usage_rights_instance.to_dict()
# create an instance of UsageRights from a dict
usage_rights_from_dict = UsageRights.from_dict(usage_rights_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


