# AssignmentOverridesCreateRequestAssignmentOverride


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**student_ids** | **str** | [] [Integer] The IDs of the override&#39;s target students. If present, the IDs must each identify a user with an active student enrollment in the course that is not already targetted by a different adhoc override. | [optional] 
**title** | **str** | The title of the adhoc assignment override. Required if student_ids is present, ignored otherwise (the title is set to the name of the targetted group or section instead). | [optional] 
**group_id** | **int** | [Integer] The ID of the override&#39;s target group. If present, the following conditions must be met for the override to be successful:  1. the assignment MUST be a group assignment (a group_category_id is assigned to it) 2. the ID must identify an active group in the group set the assignment is in 3. the ID must not be targetted by a different override  See {Appendix: Group assignments} for more info. | [optional] 
**course_section_id** | **int** | [Integer] The ID of the override&#39;s target section. If present, must identify an active section of the assignment&#39;s course not already targetted by a different override. | [optional] 
**due_at** | **str** | [DateTime] The day/time the overridden assignment is due. Accepts times in ISO 8601 format, e.g. 2014-10-21T18:48:00Z. If absent, this override will not affect due date. May be present but null to indicate the override removes any previous due date. | [optional] 
**unlock_at** | **str** | [DateTime] The day/time the overridden assignment becomes unlocked. Accepts times in ISO 8601 format, e.g. 2014-10-21T18:48:00Z. If absent, this override will not affect the unlock date. May be present but null to indicate the override removes any previous unlock date. | [optional] 
**lock_at** | **str** | [DateTime] The day/time the overridden assignment becomes locked. Accepts times in ISO 8601 format, e.g. 2014-10-21T18:48:00Z. If absent, this override will not affect the lock date. May be present but null to indicate the override removes any previous lock date. | [optional] 

## Example

```python
from canvas_lms_python_client.models.assignment_overrides_create_request_assignment_override import AssignmentOverridesCreateRequestAssignmentOverride

# TODO update the JSON string below
json = "{}"
# create an instance of AssignmentOverridesCreateRequestAssignmentOverride from a JSON string
assignment_overrides_create_request_assignment_override_instance = AssignmentOverridesCreateRequestAssignmentOverride.from_json(json)
# print the JSON string representation of the object
print(AssignmentOverridesCreateRequestAssignmentOverride.to_json())

# convert the object into a dict
assignment_overrides_create_request_assignment_override_dict = assignment_overrides_create_request_assignment_override_instance.to_dict()
# create an instance of AssignmentOverridesCreateRequestAssignmentOverride from a dict
assignment_overrides_create_request_assignment_override_from_dict = AssignmentOverridesCreateRequestAssignmentOverride.from_dict(assignment_overrides_create_request_assignment_override_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


