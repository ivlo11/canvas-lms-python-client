# AssignmentOverridesBatchCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assignment_overrides** | **List[str]** | Attributes for the new assignment overrides. See {api:AssignmentOverridesController#create Create an assignment override} for available attributes | 

## Example

```python
from canvas_lms_python_client.models.assignment_overrides_batch_create_request import AssignmentOverridesBatchCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AssignmentOverridesBatchCreateRequest from a JSON string
assignment_overrides_batch_create_request_instance = AssignmentOverridesBatchCreateRequest.from_json(json)
# print the JSON string representation of the object
print(AssignmentOverridesBatchCreateRequest.to_json())

# convert the object into a dict
assignment_overrides_batch_create_request_dict = assignment_overrides_batch_create_request_instance.to_dict()
# create an instance of AssignmentOverridesBatchCreateRequest from a dict
assignment_overrides_batch_create_request_from_dict = AssignmentOverridesBatchCreateRequest.from_dict(assignment_overrides_batch_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


