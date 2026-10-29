# FoldersCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the folder | 
**parent_folder_id** | **str** | The id of the folder to store the new folder in. An error will be returned if this does not correspond to an existing folder. If this and parent_folder_path are sent an error will be returned. If neither is given, a default folder will be used. | [optional] 
**parent_folder_path** | **str** | The path of the folder to store the new folder in. The path separator is the forward slash &#x60;/&#x60;, never a back slash. The parent folder will be created if it does not already exist. This parameter only applies to new folders in a context that has folders, such as a user, a course, or a group. If this and parent_folder_id are sent an error will be returned. If neither is given, a default folder will be used. | [optional] 
**lock_at** | **str** | The datetime to lock the folder at | [optional] 
**unlock_at** | **str** | The datetime to unlock the folder at | [optional] 
**locked** | **bool** | Flag the folder as locked | [optional] 
**hidden** | **bool** | Flag the folder as hidden | [optional] 
**position** | **int** | Set an explicit sort position for the folder | [optional] 

## Example

```python
from canvas_lms_python_client.models.folders_create_request import FoldersCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FoldersCreateRequest from a JSON string
folders_create_request_instance = FoldersCreateRequest.from_json(json)
# print the JSON string representation of the object
print(FoldersCreateRequest.to_json())

# convert the object into a dict
folders_create_request_dict = folders_create_request_instance.to_dict()
# create an instance of FoldersCreateRequest from a dict
folders_create_request_from_dict = FoldersCreateRequest.from_dict(folders_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


