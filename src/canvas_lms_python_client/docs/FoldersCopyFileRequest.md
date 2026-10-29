# FoldersCopyFileRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_file_id** | **str** | The id of the source file | 
**on_duplicate** | **str** | What to do if a file with the same name already exists at the destination. If such a file exists and this parameter is not given, the call will fail.  \&quot;overwrite\&quot;:: Replace an existing file with the same name \&quot;rename\&quot;:: Add a qualifier to make the new filename unique | [optional] 

## Example

```python
from canvas_lms_python_client.models.folders_copy_file_request import FoldersCopyFileRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FoldersCopyFileRequest from a JSON string
folders_copy_file_request_instance = FoldersCopyFileRequest.from_json(json)
# print the JSON string representation of the object
print(FoldersCopyFileRequest.to_json())

# convert the object into a dict
folders_copy_file_request_dict = folders_copy_file_request_instance.to_dict()
# create an instance of FoldersCopyFileRequest from a dict
folders_copy_file_request_from_dict = FoldersCopyFileRequest.from_dict(folders_copy_file_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


