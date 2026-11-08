# Folder



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context_type** | **str** |  | [optional] 
**context_id** | **int** |  | [optional] 
**files_count** | **int** |  | [optional] 
**position** | **int** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**folders_url** | **str** |  | [optional] 
**files_url** | **str** |  | [optional] 
**full_name** | **str** |  | [optional] 
**lock_at** | **datetime** |  | [optional] 
**id** | **int** |  | [optional] 
**folders_count** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**parent_folder_id** | **int** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**unlock_at** | **datetime** |  | [optional] 
**hidden** | **bool** |  | [optional] 
**hidden_for_user** | **bool** |  | [optional] 
**locked** | **bool** |  | [optional] 
**locked_for_user** | **bool** |  | [optional] 
**for_submissions** | **bool** | If true, indicates this is a read-only folder containing files submitted to assignments | [optional] 
**data** | **object** |  | [optional] 
**url** | **str** |  | [optional] 
**all_url** | **str** |  | [optional] 
**can_upload** | **bool** |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.folder import Folder

# TODO update the JSON string below
json = "{}"
# create an instance of Folder from a JSON string
folder_instance = Folder.from_json(json)
# print the JSON string representation of the object
print(Folder.to_json())

# convert the object into a dict
folder_dict = folder_instance.to_dict()
# create an instance of Folder from a dict
folder_from_dict = Folder.from_dict(folder_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


