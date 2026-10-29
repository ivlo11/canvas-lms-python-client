# AssignmentsApiUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assignment** | [**AssignmentsApiUpdateRequestAssignment**](AssignmentsApiUpdateRequestAssignment.md) |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.assignments_api_update_request import AssignmentsApiUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AssignmentsApiUpdateRequest from a JSON string
assignments_api_update_request_instance = AssignmentsApiUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(AssignmentsApiUpdateRequest.to_json())

# convert the object into a dict
assignments_api_update_request_dict = assignments_api_update_request_instance.to_dict()
# create an instance of AssignmentsApiUpdateRequest from a dict
assignments_api_update_request_from_dict = AssignmentsApiUpdateRequest.from_dict(assignments_api_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


