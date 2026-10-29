# ContentExport



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | the unique identifier for the export | [optional] 
**created_at** | **datetime** | the date and time this export was requested | [optional] 
**export_type** | **str** | the type of content migration: &#39;common_cartridge&#39; or &#39;qti&#39; | [optional] 
**attachment** | [**File**](File.md) |  | [optional] 
**progress_url** | **str** | The api endpoint for polling the current progress | [optional] 
**user_id** | **int** | The ID of the user who started the export | [optional] 
**workflow_state** | **str** | Current state of the content migration: created exporting exported failed | [optional] 

## Example

```python
from canvas_lms_python_client.models.content_export import ContentExport

# TODO update the JSON string below
json = "{}"
# create an instance of ContentExport from a JSON string
content_export_instance = ContentExport.from_json(json)
# print the JSON string representation of the object
print(ContentExport.to_json())

# convert the object into a dict
content_export_dict = content_export_instance.to_dict()
# create an instance of ContentExport from a dict
content_export_from_dict = ContentExport.from_dict(content_export_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


