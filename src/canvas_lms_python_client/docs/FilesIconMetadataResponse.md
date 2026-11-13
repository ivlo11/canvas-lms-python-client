# FilesIconMetadataResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alt** | **str** |  | [optional] 
**color** | **str** |  | [optional] 
**encoded_image** | **str** |  | [optional] 
**encoded_image_name** | **str** |  | [optional] 
**encoded_image_type** | **str** |  | [optional] 
**height** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**outline_color** | **str** |  | [optional] 
**outline_size** | **str** |  | [optional] 
**shape** | **str** |  | [optional] 
**size** | **str** |  | [optional] 
**text** | **str** |  | [optional] 
**text_background_color** | **str** |  | [optional] 
**text_color** | **str** |  | [optional] 
**text_position** | **str** |  | [optional] 
**text_size** | **str** |  | [optional] 
**transform** | **str** |  | [optional] 
**translate_x** | **int** |  | [optional] 
**translate_y** | **int** |  | [optional] 
**type** | **str** |  | [optional] 
**width** | **int** |  | [optional] 
**x** | **str** |  | [optional] 
**y** | **str** |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.files_icon_metadata_response import FilesIconMetadataResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FilesIconMetadataResponse from a JSON string
files_icon_metadata_response_instance = FilesIconMetadataResponse.from_json(json)
# print the JSON string representation of the object
print(FilesIconMetadataResponse.to_json())

# convert the object into a dict
files_icon_metadata_response_dict = files_icon_metadata_response_instance.to_dict()
# create an instance of FilesIconMetadataResponse from a dict
files_icon_metadata_response_from_dict = FilesIconMetadataResponse.from_dict(files_icon_metadata_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


