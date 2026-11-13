# SisImportErrorsApiIndexResponse

Object response with `sis_import_errors` (from the Canvas `@returns`).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sis_import_errors** | [**List[SisImportError]**](SisImportError.md) |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.sis_import_errors_api_index_response import SisImportErrorsApiIndexResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SisImportErrorsApiIndexResponse from a JSON string
sis_import_errors_api_index_response_instance = SisImportErrorsApiIndexResponse.from_json(json)
# print the JSON string representation of the object
print(SisImportErrorsApiIndexResponse.to_json())

# convert the object into a dict
sis_import_errors_api_index_response_dict = sis_import_errors_api_index_response_instance.to_dict()
# create an instance of SisImportErrorsApiIndexResponse from a dict
sis_import_errors_api_index_response_from_dict = SisImportErrorsApiIndexResponse.from_dict(sis_import_errors_api_index_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


