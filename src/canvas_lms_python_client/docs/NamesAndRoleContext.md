# NamesAndRoleContext

An abbreviated representation of an LTI Context

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | LTI Context unique identifier | [optional] 
**label** | **str** | LTI Context short name or code | [optional] 
**title** | **str** | LTI Context full name | [optional] 

## Example

```python
from canvas_lms_python_client.models.names_and_role_context import NamesAndRoleContext

# TODO update the JSON string below
json = "{}"
# create an instance of NamesAndRoleContext from a JSON string
names_and_role_context_instance = NamesAndRoleContext.from_json(json)
# print the JSON string representation of the object
print(NamesAndRoleContext.to_json())

# convert the object into a dict
names_and_role_context_dict = names_and_role_context_instance.to_dict()
# create an instance of NamesAndRoleContext from a dict
names_and_role_context_from_dict = NamesAndRoleContext.from_dict(names_and_role_context_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


