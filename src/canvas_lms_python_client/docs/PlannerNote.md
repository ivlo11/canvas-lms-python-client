# PlannerNote

A planner note

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The ID of the planner note | [optional] 
**title** | **str** | The title for a planner note | [optional] 
**description** | **str** | The description of the planner note | [optional] 
**user_id** | **int** | The id of the associated user creating the planner note | [optional] 
**workflow_state** | **str** | The current published state of the planner note | [optional] 
**course_id** | **int** | The course that the note is in relation too, if applicable | [optional] 
**todo_date** | **datetime** | The datetime of when the planner note should show up on their planner | [optional] 
**linked_object_type** | **str** | the type of the linked learning object | [optional] 
**linked_object_id** | **int** | the id of the linked learning object | [optional] 
**linked_object_html_url** | **str** | the Canvas web URL of the linked learning object | [optional] 
**linked_object_url** | **str** | the API URL of the linked learning object | [optional] 

## Example

```python
from canvas_lms_python_client.models.planner_note import PlannerNote

# TODO update the JSON string below
json = "{}"
# create an instance of PlannerNote from a JSON string
planner_note_instance = PlannerNote.from_json(json)
# print the JSON string representation of the object
print(PlannerNote.to_json())

# convert the object into a dict
planner_note_dict = planner_note_instance.to_dict()
# create an instance of PlannerNote from a dict
planner_note_from_dict = PlannerNote.from_dict(planner_note_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


