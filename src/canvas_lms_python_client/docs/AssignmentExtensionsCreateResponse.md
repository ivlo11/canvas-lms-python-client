# AssignmentExtensionsCreateResponse

Paginated `assignment_extensions` list response (from the Canvas example response).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assignment_extensions** | [**List[AssignmentExtension]**](AssignmentExtension.md) |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.assignment_extensions_create_response import AssignmentExtensionsCreateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AssignmentExtensionsCreateResponse from a JSON string
assignment_extensions_create_response_instance = AssignmentExtensionsCreateResponse.from_json(json)
# print the JSON string representation of the object
print(AssignmentExtensionsCreateResponse.to_json())

# convert the object into a dict
assignment_extensions_create_response_dict = assignment_extensions_create_response_instance.to_dict()
# create an instance of AssignmentExtensionsCreateResponse from a dict
assignment_extensions_create_response_from_dict = AssignmentExtensionsCreateResponse.from_dict(assignment_extensions_create_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


