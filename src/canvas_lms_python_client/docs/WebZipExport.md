# WebZipExport



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | the unique identifier for the export | [optional] 
**created_at** | **datetime** | the date and time this export was requested | [optional] 
**updated_at** | **datetime** | the date and time this export was last updated | [optional] 
**zip_attachment** | [**File**](File.md) |  | [optional] 
**progress_id** | **int** | the unique identifier for the progress object | [optional] 
**progress_url** | **str** | The api endpoint for polling the current progress | [optional] 
**user_id** | **int** | The ID of the user who started the export | [optional] 
**course_id** | **int** | The ID of the course the export is for | [optional] 
**content_export_id** | **int** | The ID of the content export used in the offline export | [optional] 
**workflow_state** | **str** | Current state of the web zip export: created exporting exported generating generated failed | [optional] 

## Example

```python
from canvas_lms_python_client.models.web_zip_export import WebZipExport

# TODO update the JSON string below
json = "{}"
# create an instance of WebZipExport from a JSON string
web_zip_export_instance = WebZipExport.from_json(json)
# print the JSON string representation of the object
print(WebZipExport.to_json())

# convert the object into a dict
web_zip_export_dict = web_zip_export_instance.to_dict()
# create an instance of WebZipExport from a dict
web_zip_export_from_dict = WebZipExport.from_dict(web_zip_export_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


