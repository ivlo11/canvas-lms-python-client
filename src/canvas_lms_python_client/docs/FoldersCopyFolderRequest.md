# FoldersCopyFolderRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_folder_id** | **str** | The id of the source folder | 

## Example

```python
from canvas_lms_python_client.models.folders_copy_folder_request import FoldersCopyFolderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FoldersCopyFolderRequest from a JSON string
folders_copy_folder_request_instance = FoldersCopyFolderRequest.from_json(json)
# print the JSON string representation of the object
print(FoldersCopyFolderRequest.to_json())

# convert the object into a dict
folders_copy_folder_request_dict = folders_copy_folder_request_instance.to_dict()
# create an instance of FoldersCopyFolderRequest from a dict
folders_copy_folder_request_from_dict = FoldersCopyFolderRequest.from_dict(folders_copy_folder_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


