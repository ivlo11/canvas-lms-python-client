# AssignmentOverridesCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assignment_override** | [**AssignmentOverridesCreateRequestAssignmentOverride**](AssignmentOverridesCreateRequestAssignmentOverride.md) |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.assignment_overrides_create_request import AssignmentOverridesCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AssignmentOverridesCreateRequest from a JSON string
assignment_overrides_create_request_instance = AssignmentOverridesCreateRequest.from_json(json)
# print the JSON string representation of the object
print(AssignmentOverridesCreateRequest.to_json())

# convert the object into a dict
assignment_overrides_create_request_dict = assignment_overrides_create_request_instance.to_dict()
# create an instance of AssignmentOverridesCreateRequest from a dict
assignment_overrides_create_request_from_dict = AssignmentOverridesCreateRequest.from_dict(assignment_overrides_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


