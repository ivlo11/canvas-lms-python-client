# ContextModulesApiUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**module** | [**ContextModulesApiUpdateRequestModule**](ContextModulesApiUpdateRequestModule.md) |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.context_modules_api_update_request import ContextModulesApiUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ContextModulesApiUpdateRequest from a JSON string
context_modules_api_update_request_instance = ContextModulesApiUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(ContextModulesApiUpdateRequest.to_json())

# convert the object into a dict
context_modules_api_update_request_dict = context_modules_api_update_request_instance.to_dict()
# create an instance of ContextModulesApiUpdateRequest from a dict
context_modules_api_update_request_from_dict = ContextModulesApiUpdateRequest.from_dict(context_modules_api_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


