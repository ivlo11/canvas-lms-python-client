# SisImportsApiIndexResponse

Object response with `sis_imports` (from the Canvas `@returns`).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sis_imports** | [**List[SisImport]**](SisImport.md) |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.sis_imports_api_index_response import SisImportsApiIndexResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SisImportsApiIndexResponse from a JSON string
sis_imports_api_index_response_instance = SisImportsApiIndexResponse.from_json(json)
# print the JSON string representation of the object
print(SisImportsApiIndexResponse.to_json())

# convert the object into a dict
sis_imports_api_index_response_dict = sis_imports_api_index_response_instance.to_dict()
# create an instance of SisImportsApiIndexResponse from a dict
sis_imports_api_index_response_from_dict = SisImportsApiIndexResponse.from_dict(sis_imports_api_index_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


