# FoldersUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The new name of the folder | [optional] 
**parent_folder_id** | **str** | The id of the folder to move this folder into. The new folder must be in the same context as the original parent folder. | [optional] 
**lock_at** | **str** | The datetime to lock the folder at | [optional] 
**unlock_at** | **str** | The datetime to unlock the folder at | [optional] 
**locked** | **bool** | Flag the folder as locked | [optional] 
**hidden** | **bool** | Flag the folder as hidden | [optional] 
**position** | **int** | Set an explicit sort position for the folder | [optional] 

## Example

```python
from canvas_lms_python_client.models.folders_update_request import FoldersUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FoldersUpdateRequest from a JSON string
folders_update_request_instance = FoldersUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(FoldersUpdateRequest.to_json())

# convert the object into a dict
folders_update_request_dict = folders_update_request_instance.to_dict()
# create an instance of FoldersUpdateRequest from a dict
folders_update_request_from_dict = FoldersUpdateRequest.from_dict(folders_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


