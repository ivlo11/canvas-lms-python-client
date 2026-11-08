# File



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**size** | **int** |  | [optional] 
**content_type** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**display_name** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**category** | **str** |  | [optional] 
**filename** | **str** |  | [optional] 
**folder_id** | **int** |  | [optional] 
**hidden** | **bool** |  | [optional] 
**hidden_for_user** | **bool** |  | [optional] 
**lock_at** | **str** |  | [optional] 
**locked** | **bool** |  | [optional] 
**locked_for_user** | **bool** |  | [optional] 
**media_entry_id** | **str** |  | [optional] 
**mime_class** | **str** |  | [optional] 
**modified_at** | **str** |  | [optional] 
**thumbnail_url** | **str** |  | [optional] 
**unlock_at** | **str** |  | [optional] 
**upload_status** | **str** |  | [optional] 
**instfs_uuid** | **object** |  | [optional] 
**usage_rights** | **object** |  | [optional] 
**user** | **object** |  | [optional] 
**uuid** | **str** |  | [optional] 
**visibility_level** | **str** |  | [optional] 
**canvadoc_session_url** | **str** |  | [optional] 
**is_master_course_child_content** | **bool** |  | [optional] 
**lock_explanation** | **str** |  | [optional] 
**lock_info** | **object** |  | [optional] 
**master_course_restrictions** | **object** |  | [optional] 
**preview_url** | **str** |  | [optional] 
**restricted_by_master_course** | **bool** |  | [optional] 
**view** | **bool** |  | [optional] 
**attachment** | **object** |  | [optional] 
**ok** | **bool** |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.file import File

# TODO update the JSON string below
json = "{}"
# create an instance of File from a JSON string
file_instance = File.from_json(json)
# print the JSON string representation of the object
print(File.to_json())

# convert the object into a dict
file_dict = file_instance.to_dict()
# create an instance of File from a dict
file_from_dict = File.from_dict(file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


