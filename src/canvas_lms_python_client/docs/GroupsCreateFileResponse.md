# GroupsCreateFileResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_param** | **str** |  | [optional] 
**progress** | **object** |  | [optional] 
**upload_params** | **object** |  | [optional] 
**upload_url** | **str** |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.groups_create_file_response import GroupsCreateFileResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GroupsCreateFileResponse from a JSON string
groups_create_file_response_instance = GroupsCreateFileResponse.from_json(json)
# print the JSON string representation of the object
print(GroupsCreateFileResponse.to_json())

# convert the object into a dict
groups_create_file_response_dict = groups_create_file_response_instance.to_dict()
# create an instance of GroupsCreateFileResponse from a dict
groups_create_file_response_from_dict = GroupsCreateFileResponse.from_dict(groups_create_file_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


