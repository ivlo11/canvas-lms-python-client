# FileAttachment

A file attachment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content_type** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**filename** | **str** |  | [optional] 
**display_name** | **str** |  | [optional] 
**category** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**folder_id** | **int** |  | [optional] 
**hidden** | **bool** |  | [optional] 
**hidden_for_user** | **bool** |  | [optional] 
**id** | **int** |  | [optional] 
**lock_at** | **object** |  | [optional] 
**locked** | **bool** |  | [optional] 
**locked_for_user** | **bool** |  | [optional] 
**media_entry_id** | **object** |  | [optional] 
**mime_class** | **str** |  | [optional] 
**modified_at** | **str** |  | [optional] 
**size** | **int** |  | [optional] 
**thumbnail_url** | **object** |  | [optional] 
**unlock_at** | **object** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**upload_status** | **str** |  | [optional] 
**uuid** | **str** |  | [optional] 
**visibility_level** | **str** |  | [optional] 
**usage_rights** | **object** |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.file_attachment import FileAttachment

# TODO update the JSON string below
json = "{}"
# create an instance of FileAttachment from a JSON string
file_attachment_instance = FileAttachment.from_json(json)
# print the JSON string representation of the object
print(FileAttachment.to_json())

# convert the object into a dict
file_attachment_dict = file_attachment_instance.to_dict()
# create an instance of FileAttachment from a dict
file_attachment_from_dict = FileAttachment.from_dict(file_attachment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


