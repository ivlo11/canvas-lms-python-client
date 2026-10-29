# AssignmentsApiCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assignment** | [**AssignmentsApiCreateRequestAssignment**](AssignmentsApiCreateRequestAssignment.md) |  | 

## Example

```python
from canvas_lms_python_client.models.assignments_api_create_request import AssignmentsApiCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AssignmentsApiCreateRequest from a JSON string
assignments_api_create_request_instance = AssignmentsApiCreateRequest.from_json(json)
# print the JSON string representation of the object
print(AssignmentsApiCreateRequest.to_json())

# convert the object into a dict
assignments_api_create_request_dict = assignments_api_create_request_instance.to_dict()
# create an instance of AssignmentsApiCreateRequest from a dict
assignments_api_create_request_from_dict = AssignmentsApiCreateRequest.from_dict(assignments_api_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


