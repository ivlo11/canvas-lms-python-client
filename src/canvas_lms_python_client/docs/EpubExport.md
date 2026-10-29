# EpubExport



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | the unique identifier for the export | [optional] 
**created_at** | **datetime** | the date and time this export was requested | [optional] 
**attachment** | [**File**](File.md) |  | [optional] 
**progress_url** | **str** | The api endpoint for polling the current progress | [optional] 
**user_id** | **int** | The ID of the user who started the export | [optional] 
**workflow_state** | **str** | Current state of the ePub export: created exporting exported generating generated failed | [optional] 

## Example

```python
from canvas_lms_python_client.models.epub_export import EpubExport

# TODO update the JSON string below
json = "{}"
# create an instance of EpubExport from a JSON string
epub_export_instance = EpubExport.from_json(json)
# print the JSON string representation of the object
print(EpubExport.to_json())

# convert the object into a dict
epub_export_dict = epub_export_instance.to_dict()
# create an instance of EpubExport from a dict
epub_export_from_dict = EpubExport.from_dict(epub_export_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


