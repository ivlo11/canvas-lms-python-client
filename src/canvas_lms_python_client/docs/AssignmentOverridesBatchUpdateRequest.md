# AssignmentOverridesBatchUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assignment_overrides** | **List[str]** | Attributes for the updated overrides. | 

## Example

```python
from canvas_lms_python_client.models.assignment_overrides_batch_update_request import AssignmentOverridesBatchUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AssignmentOverridesBatchUpdateRequest from a JSON string
assignment_overrides_batch_update_request_instance = AssignmentOverridesBatchUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(AssignmentOverridesBatchUpdateRequest.to_json())

# convert the object into a dict
assignment_overrides_batch_update_request_dict = assignment_overrides_batch_update_request_instance.to_dict()
# create an instance of AssignmentOverridesBatchUpdateRequest from a dict
assignment_overrides_batch_update_request_from_dict = AssignmentOverridesBatchUpdateRequest.from_dict(assignment_overrides_batch_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


