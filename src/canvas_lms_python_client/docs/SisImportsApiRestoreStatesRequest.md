# SisImportsApiRestoreStatesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**batch_mode** | **bool** | If set, will only restore items that were deleted from batch_mode. | [optional] 
**undelete_only** | **bool** | If set, will only restore items that were deleted. This will ignore any items that were created or modified. | [optional] 
**unconclude_only** | **bool** | If set, will only restore enrollments that were concluded. This will ignore any items that were created or deleted. | [optional] 

## Example

```python
from canvas_lms_python_client.models.sis_imports_api_restore_states_request import SisImportsApiRestoreStatesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SisImportsApiRestoreStatesRequest from a JSON string
sis_imports_api_restore_states_request_instance = SisImportsApiRestoreStatesRequest.from_json(json)
# print the JSON string representation of the object
print(SisImportsApiRestoreStatesRequest.to_json())

# convert the object into a dict
sis_imports_api_restore_states_request_dict = sis_imports_api_restore_states_request_instance.to_dict()
# create an instance of SisImportsApiRestoreStatesRequest from a dict
sis_imports_api_restore_states_request_from_dict = SisImportsApiRestoreStatesRequest.from_dict(sis_imports_api_restore_states_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


