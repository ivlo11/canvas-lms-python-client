# ContextModulesApiUpdateRequestModule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | [String] The name of the module | [optional] 
**unlock_at** | **str** | [DateTime] The date the module will unlock | [optional] 
**position** | **int** | [Integer] The position of the module in the course (1-based) | [optional] 
**require_sequential_progress** | **bool** | [Boolean] Whether module items must be unlocked in order | [optional] 
**prerequisite_module_ids** | **str** | [] [String] IDs of Modules that must be completed before this one is unlocked Prerequisite modules must precede this module (i.e. have a lower position value), otherwise they will be ignored | [optional] 
**publish_final_grade** | **bool** | [Boolean] Whether to publish the student&#39;s final grade for the course upon completion of this module. | [optional] 
**published** | **bool** | [Boolean] Whether the module is published and visible to students | [optional] 

## Example

```python
from canvas_lms_python_client.models.context_modules_api_update_request_module import ContextModulesApiUpdateRequestModule

# TODO update the JSON string below
json = "{}"
# create an instance of ContextModulesApiUpdateRequestModule from a JSON string
context_modules_api_update_request_module_instance = ContextModulesApiUpdateRequestModule.from_json(json)
# print the JSON string representation of the object
print(ContextModulesApiUpdateRequestModule.to_json())

# convert the object into a dict
context_modules_api_update_request_module_dict = context_modules_api_update_request_module_instance.to_dict()
# create an instance of ContextModulesApiUpdateRequestModule from a dict
context_modules_api_update_request_module_from_dict = ContextModulesApiUpdateRequestModule.from_dict(context_modules_api_update_request_module_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


