# PlannerNotesUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | The title of the planner note. | [optional] 
**details** | **str** | Text of the planner note. | [optional] 
**todo_date** | **str** | The date where this planner note should appear in the planner. The value should be formatted as: yyyy-mm-dd. | [optional] 
**course_id** | **int** | The ID of the course to associate with the planner note. The caller must be able to view the course in order to associate it with a planner note. Use a null or empty value to remove a planner note from a course. Note that if the planner note is linked to a learning object, its course_id cannot be changed. | [optional] 

## Example

```python
from canvas_lms_python_client.models.planner_notes_update_request import PlannerNotesUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PlannerNotesUpdateRequest from a JSON string
planner_notes_update_request_instance = PlannerNotesUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(PlannerNotesUpdateRequest.to_json())

# convert the object into a dict
planner_notes_update_request_dict = planner_notes_update_request_instance.to_dict()
# create an instance of PlannerNotesUpdateRequest from a dict
planner_notes_update_request_from_dict = PlannerNotesUpdateRequest.from_dict(planner_notes_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


