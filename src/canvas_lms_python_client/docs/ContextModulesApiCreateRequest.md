# ContextModulesApiCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**module** | [**ContextModulesApiCreateRequestModule**](ContextModulesApiCreateRequestModule.md) |  | 

## Example

```python
from canvas_lms_python_client.models.context_modules_api_create_request import ContextModulesApiCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ContextModulesApiCreateRequest from a JSON string
context_modules_api_create_request_instance = ContextModulesApiCreateRequest.from_json(json)
# print the JSON string representation of the object
print(ContextModulesApiCreateRequest.to_json())

# convert the object into a dict
context_modules_api_create_request_dict = context_modules_api_create_request_instance.to_dict()
# create an instance of ContextModulesApiCreateRequest from a dict
context_modules_api_create_request_from_dict = ContextModulesApiCreateRequest.from_dict(context_modules_api_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


