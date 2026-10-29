# SisImportError



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sis_import_id** | **int** | The unique identifier for the SIS import. | [optional] 
**file** | **str** | The file where the error message occurred. | [optional] 
**message** | **str** | The error message that from the record. | [optional] 
**row_info** | **str** | The contents of the line that had the error. | [optional] 
**row** | **int** | The line number where the error occurred. Some Importers do not yet support this. This is a 1 based index starting with the header row. | [optional] 

## Example

```python
from canvas_lms_python_client.models.sis_import_error import SisImportError

# TODO update the JSON string below
json = "{}"
# create an instance of SisImportError from a JSON string
sis_import_error_instance = SisImportError.from_json(json)
# print the JSON string representation of the object
print(SisImportError.to_json())

# convert the object into a dict
sis_import_error_dict = sis_import_error_instance.to_dict()
# create an instance of SisImportError from a dict
sis_import_error_from_dict = SisImportError.from_dict(sis_import_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


