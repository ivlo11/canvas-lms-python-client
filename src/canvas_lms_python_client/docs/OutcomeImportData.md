# OutcomeImportData



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**import_type** | **str** | The type of outcome import | [optional] 

## Example

```python
from canvas_lms_python_client.models.outcome_import_data import OutcomeImportData

# TODO update the JSON string below
json = "{}"
# create an instance of OutcomeImportData from a JSON string
outcome_import_data_instance = OutcomeImportData.from_json(json)
# print the JSON string representation of the object
print(OutcomeImportData.to_json())

# convert the object into a dict
outcome_import_data_dict = outcome_import_data_instance.to_dict()
# create an instance of OutcomeImportData from a dict
outcome_import_data_from_dict = OutcomeImportData.from_dict(outcome_import_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


