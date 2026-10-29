# AssignmentExtensionsCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assignment_extensions_user_id** | **int** | The ID of the user we want to add assignment extensions for. | 
**assignment_extensions_extra_attempts** | **int** | Number of times the student is allowed to re-take the assignment over the limit. | 

## Example

```python
from canvas_lms_python_client.models.assignment_extensions_create_request import AssignmentExtensionsCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AssignmentExtensionsCreateRequest from a JSON string
assignment_extensions_create_request_instance = AssignmentExtensionsCreateRequest.from_json(json)
# print the JSON string representation of the object
print(AssignmentExtensionsCreateRequest.to_json())

# convert the object into a dict
assignment_extensions_create_request_dict = assignment_extensions_create_request_instance.to_dict()
# create an instance of AssignmentExtensionsCreateRequest from a dict
assignment_extensions_create_request_from_dict = AssignmentExtensionsCreateRequest.from_dict(assignment_extensions_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


