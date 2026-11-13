# Scope



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource** | **str** | The resource the scope is associated with | [optional] 
**resource_name** | **str** | The localized resource name | [optional] 
**controller** | **str** | The controller the scope is associated to | [optional] 
**action** | **str** | The controller action the scope is associated to | [optional] 
**verb** | **str** | The HTTP verb for the scope | [optional] 
**scope** | **str** | The identifier for the scope | [optional] 
**path** | **str** |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.scope import Scope

# TODO update the JSON string below
json = "{}"
# create an instance of Scope from a JSON string
scope_instance = Scope.from_json(json)
# print the JSON string representation of the object
print(Scope.to_json())

# convert the object into a dict
scope_dict = scope_instance.to_dict()
# create an instance of Scope from a dict
scope_from_dict = Scope.from_dict(scope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


