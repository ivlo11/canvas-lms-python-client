# SisImportData



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**import_type** | **str** | The type of SIS import | [optional] 
**supplied_batches** | **List[str]** | Which files were included in the SIS import | [optional] 
**counts** | [**SisImportCounts**](SisImportCounts.md) |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.sis_import_data import SisImportData

# TODO update the JSON string below
json = "{}"
# create an instance of SisImportData from a JSON string
sis_import_data_instance = SisImportData.from_json(json)
# print the JSON string representation of the object
print(SisImportData.to_json())

# convert the object into a dict
sis_import_data_dict = sis_import_data_instance.to_dict()
# create an instance of SisImportData from a dict
sis_import_data_from_dict = SisImportData.from_dict(sis_import_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


