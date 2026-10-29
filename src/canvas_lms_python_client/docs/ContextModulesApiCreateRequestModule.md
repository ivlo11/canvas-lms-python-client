# ContextModulesApiCreateRequestModule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | [Required, String] The name of the module | 
**unlock_at** | **str** | [DateTime] The date the module will unlock | [optional] 
**position** | **int** | [Integer] The position of this module in the course (1-based) | [optional] 
**require_sequential_progress** | **bool** | [Boolean] Whether module items must be unlocked in order | [optional] 
**prerequisite_module_ids** | **str** | [] [String] IDs of Modules that must be completed before this one is unlocked. Prerequisite modules must precede this module (i.e. have a lower position value), otherwise they will be ignored | [optional] 
**publish_final_grade** | **bool** | [Boolean] Whether to publish the student&#39;s final grade for the course upon completion of this module. | [optional] 

## Example

```python
from canvas_lms_python_client.models.context_modules_api_create_request_module import ContextModulesApiCreateRequestModule

# TODO update the JSON string below
json = "{}"
# create an instance of ContextModulesApiCreateRequestModule from a JSON string
context_modules_api_create_request_module_instance = ContextModulesApiCreateRequestModule.from_json(json)
# print the JSON string representation of the object
print(ContextModulesApiCreateRequestModule.to_json())

# convert the object into a dict
context_modules_api_create_request_module_dict = context_modules_api_create_request_module_instance.to_dict()
# create an instance of ContextModulesApiCreateRequestModule from a dict
context_modules_api_create_request_module_from_dict = ContextModulesApiCreateRequestModule.from_dict(context_modules_api_create_request_module_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


