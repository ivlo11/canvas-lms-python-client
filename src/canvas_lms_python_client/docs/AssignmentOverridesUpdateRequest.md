# AssignmentOverridesUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assignment_override** | [**AssignmentOverridesUpdateRequestAssignmentOverride**](AssignmentOverridesUpdateRequestAssignmentOverride.md) |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.assignment_overrides_update_request import AssignmentOverridesUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AssignmentOverridesUpdateRequest from a JSON string
assignment_overrides_update_request_instance = AssignmentOverridesUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(AssignmentOverridesUpdateRequest.to_json())

# convert the object into a dict
assignment_overrides_update_request_dict = assignment_overrides_update_request_instance.to_dict()
# create an instance of AssignmentOverridesUpdateRequest from a dict
assignment_overrides_update_request_from_dict = AssignmentOverridesUpdateRequest.from_dict(assignment_overrides_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


