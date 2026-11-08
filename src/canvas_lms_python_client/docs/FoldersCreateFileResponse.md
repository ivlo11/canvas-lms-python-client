# FoldersCreateFileResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_param** | **str** |  | [optional] 
**upload_params** | **object** |  | [optional] 
**upload_url** | **str** |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.folders_create_file_response import FoldersCreateFileResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FoldersCreateFileResponse from a JSON string
folders_create_file_response_instance = FoldersCreateFileResponse.from_json(json)
# print the JSON string representation of the object
print(FoldersCreateFileResponse.to_json())

# convert the object into a dict
folders_create_file_response_dict = folders_create_file_response_instance.to_dict()
# create an instance of FoldersCreateFileResponse from a dict
folders_create_file_response_from_dict = FoldersCreateFileResponse.from_dict(folders_create_file_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


