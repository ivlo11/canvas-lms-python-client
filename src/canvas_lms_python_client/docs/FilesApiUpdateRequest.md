# FilesApiUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The new display name of the file, with a limit of 255 characters. | [optional] 
**parent_folder_id** | **str** | The id of the folder to move this file into. The new folder must be in the same context as the original parent folder. If the file is in a context without folders this does not apply. | [optional] 
**on_duplicate** | **str** | If the file is moved to a folder containing a file with the same name, or renamed to a name matching an existing file, the API call will fail unless this parameter is supplied.  \&quot;overwrite\&quot;:: Replace the existing file with the same name \&quot;rename\&quot;:: Add a qualifier to make the new filename unique | [optional] 
**lock_at** | **str** | The datetime to lock the file at | [optional] 
**unlock_at** | **str** | The datetime to unlock the file at | [optional] 
**locked** | **bool** | Flag the file as locked | [optional] 
**hidden** | **bool** | Flag the file as hidden | [optional] 
**visibility_level** | **str** | Configure which roles can access this file | [optional] 

## Example

```python
from canvas_lms_python_client.models.files_api_update_request import FilesApiUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FilesApiUpdateRequest from a JSON string
files_api_update_request_instance = FilesApiUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(FilesApiUpdateRequest.to_json())

# convert the object into a dict
files_api_update_request_dict = files_api_update_request_instance.to_dict()
# create an instance of FilesApiUpdateRequest from a dict
files_api_update_request_from_dict = FilesApiUpdateRequest.from_dict(files_api_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


