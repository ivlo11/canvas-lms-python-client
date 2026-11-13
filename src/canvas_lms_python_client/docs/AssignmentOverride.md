# AssignmentOverride



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | the ID of the assignment override | [optional] 
**assignment_id** | **int** | the ID of the assignment the override applies to (present if the override applies to an assignment) | [optional] 
**quiz_id** | **int** | the ID of the quiz the override applies to (present if the override applies to a quiz) | [optional] 
**context_module_id** | **int** | the ID of the module the override applies to (present if the override applies to a module) | [optional] 
**discussion_topic_id** | **int** | the ID of the discussion the override applies to (present if the override applies to an ungraded discussion) | [optional] 
**wiki_page_id** | **int** | the ID of the page the override applies to (present if the override applies to a page) | [optional] 
**attachment_id** | **int** | the ID of the file the override applies to (present if the override applies to a file) | [optional] 
**student_ids** | **List[int]** | the IDs of the override&#39;s target students (present if the override targets an ad-hoc set of students) | [optional] 
**group_id** | **int** | the ID of the override&#39;s target group (present if the override targets a group and the assignment is a group assignment) | [optional] 
**course_section_id** | **int** | the ID of the overrides&#39;s target section (present if the override targets a section) | [optional] 
**title** | **str** | the title of the override | [optional] 
**due_at** | **datetime** | the overridden due at (present if due_at is overridden) | [optional] 
**all_day** | **bool** | the overridden all day flag (present if due_at is overridden) | [optional] 
**all_day_date** | **datetime** | the overridden all day date (present if due_at is overridden) | [optional] 
**unlock_at** | **datetime** | the overridden unlock at (present if unlock_at is overridden) | [optional] 
**lock_at** | **datetime** | the overridden lock at, if any (present if lock_at is overridden) | [optional] 
**unassign_item** | **bool** |  | [optional] 
**group_category_id** | **int** |  | [optional] 
**non_collaborative** | **bool** |  | [optional] 
**noop_id** | **object** |  | [optional] 
**course_id** | **int** |  | [optional] 
**parent_override_id** | **int** |  | [optional] 
**context_module_name** | **str** |  | [optional] 
**peer_review_dates** | **object** |  | [optional] 
**students** | **List[object]** |  | [optional] 
**sub_assignment_due_dates** | **List[object]** |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.assignment_override import AssignmentOverride

# TODO update the JSON string below
json = "{}"
# create an instance of AssignmentOverride from a JSON string
assignment_override_instance = AssignmentOverride.from_json(json)
# print the JSON string representation of the object
print(AssignmentOverride.to_json())

# convert the object into a dict
assignment_override_dict = assignment_override_instance.to_dict()
# create an instance of AssignmentOverride from a dict
assignment_override_from_dict = AssignmentOverride.from_dict(assignment_override_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


