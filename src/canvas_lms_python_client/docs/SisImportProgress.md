# SisImportProgress

The progress of the SIS import. The progress will reset when using batch_mode and have a different progress for the cleanup stage

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from canvas_lms_python_client.models.sis_import_progress import SisImportProgress

# TODO update the JSON string below
json = "{}"
# create an instance of SisImportProgress from a JSON string
sis_import_progress_instance = SisImportProgress.from_json(json)
# print the JSON string representation of the object
print(SisImportProgress.to_json())

# convert the object into a dict
sis_import_progress_dict = sis_import_progress_instance.to_dict()
# create an instance of SisImportProgress from a dict
sis_import_progress_from_dict = SisImportProgress.from_dict(sis_import_progress_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


