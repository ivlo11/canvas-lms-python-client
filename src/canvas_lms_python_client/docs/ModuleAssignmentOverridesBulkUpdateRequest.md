# ModuleAssignmentOverridesBulkUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**overrides** | **List[List[str]]** | List of overrides to apply to the module. Overrides that already exist should include an ID and will be updated if needed. New overrides will be created for overrides in the list without an ID. Overrides not included in the list will be deleted. Providing an empty list will delete all of the module&#39;s overrides. Keys for each override object can include: &#39;id&#39;, &#39;title&#39;, &#39;student_ids&#39;, and &#39;course_section_id&#39;. &#39;group_id&#39; is accepted if the Differentiation Tags account setting is enabled. | 

## Example

```python
from canvas_lms_python_client.models.module_assignment_overrides_bulk_update_request import ModuleAssignmentOverridesBulkUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ModuleAssignmentOverridesBulkUpdateRequest from a JSON string
module_assignment_overrides_bulk_update_request_instance = ModuleAssignmentOverridesBulkUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(ModuleAssignmentOverridesBulkUpdateRequest.to_json())

# convert the object into a dict
module_assignment_overrides_bulk_update_request_dict = module_assignment_overrides_bulk_update_request_instance.to_dict()
# create an instance of ModuleAssignmentOverridesBulkUpdateRequest from a dict
module_assignment_overrides_bulk_update_request_from_dict = ModuleAssignmentOverridesBulkUpdateRequest.from_dict(module_assignment_overrides_bulk_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


