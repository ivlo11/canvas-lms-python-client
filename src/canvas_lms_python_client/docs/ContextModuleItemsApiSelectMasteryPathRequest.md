# ContextModuleItemsApiSelectMasteryPathRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assignment_set_id** | **str** | Assignment set chosen, as specified in the mastery_paths portion of the context module item response | [optional] 
**student_id** | **str** | Which student the selection applies to.  If not specified, current user is implied. | [optional] 

## Example

```python
from canvas_lms_python_client.models.context_module_items_api_select_mastery_path_request import ContextModuleItemsApiSelectMasteryPathRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ContextModuleItemsApiSelectMasteryPathRequest from a JSON string
context_module_items_api_select_mastery_path_request_instance = ContextModuleItemsApiSelectMasteryPathRequest.from_json(json)
# print the JSON string representation of the object
print(ContextModuleItemsApiSelectMasteryPathRequest.to_json())

# convert the object into a dict
context_module_items_api_select_mastery_path_request_dict = context_module_items_api_select_mastery_path_request_instance.to_dict()
# create an instance of ContextModuleItemsApiSelectMasteryPathRequest from a dict
context_module_items_api_select_mastery_path_request_from_dict = ContextModuleItemsApiSelectMasteryPathRequest.from_dict(context_module_items_api_select_mastery_path_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


