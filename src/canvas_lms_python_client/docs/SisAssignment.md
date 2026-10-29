# SisAssignment

Assignments that have post_to_sis enabled with other objects for convenience

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier for the assignment. | [optional] 
**course_id** | **int** | The unique identifier for the course. | [optional] 
**name** | **str** | the name of the assignment | [optional] 
**created_at** | **datetime** | The time at which this assignment was originally created | [optional] 
**due_at** | **datetime** | the due date for the assignment. returns null if not present. NOTE: If this assignment has assignment overrides, this field will be the due date as it applies to the user requesting information from the API. | [optional] 
**unlock_at** | **datetime** | (Optional) Time at which this was/will be unlocked. | [optional] 
**lock_at** | **datetime** | (Optional) Time at which this was/will be locked. | [optional] 
**points_possible** | **int** | The maximum points possible for the assignment | [optional] 
**submission_types** | **List[str]** | the types of submissions allowed for this assignment list containing one or more of the following: &#39;discussion_topic&#39;, &#39;online_quiz&#39;, &#39;on_paper&#39;, &#39;none&#39;, &#39;external_tool&#39;, &#39;online_text_entry&#39;, &#39;online_url&#39;, &#39;online_upload&#39;, &#39;media_recording&#39;, &#39;student_annotation&#39; | [optional] 
**integration_id** | **str** | Third Party integration id for assignment | [optional] 
**integration_data** | **str** | (optional, Third Party integration data for assignment) | [optional] 
**include_in_final_grade** | **bool** | If false, the assignment will be omitted from the student&#39;s final grade | [optional] 
**assignment_group** | [**List[AssignmentGroupAttributes]**](AssignmentGroupAttributes.md) | Includes attributes of a assignment_group for convenience. For more details see Assignments API. | [optional] 
**sections** | [**List[SectionAttributes]**](SectionAttributes.md) | Includes attributes of a section for convenience. For more details see Sections API. | [optional] 
**user_overrides** | [**List[UserAssignmentOverrideAttributes]**](UserAssignmentOverrideAttributes.md) | Includes attributes of a user assignment overrides. For more details see Assignments API. | [optional] 

## Example

```python
from canvas_lms_python_client.models.sis_assignment import SisAssignment

# TODO update the JSON string below
json = "{}"
# create an instance of SisAssignment from a JSON string
sis_assignment_instance = SisAssignment.from_json(json)
# print the JSON string representation of the object
print(SisAssignment.to_json())

# convert the object into a dict
sis_assignment_dict = sis_assignment_instance.to_dict()
# create an instance of SisAssignment from a dict
sis_assignment_from_dict = SisAssignment.from_dict(sis_assignment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


