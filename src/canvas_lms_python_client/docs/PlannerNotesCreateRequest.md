# PlannerNotesCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | The title of the planner note. | [optional] 
**details** | **str** | Text of the planner note. | [optional] 
**todo_date** | **str** | The date where this planner note should appear in the planner. The value should be formatted as: yyyy-mm-dd. | [optional] 
**course_id** | **int** | The ID of the course to associate with the planner note. The caller must be able to view the course in order to associate it with a planner note. | [optional] 
**linked_object_type** | **str** | The type of a learning object to link to this planner note. Must be used in conjunction wtih linked_object_id and course_id. Valid linked_object_type values are: &#39;announcement&#39;, &#39;assignment&#39;, &#39;discussion_topic&#39;, &#39;wiki_page&#39;, &#39;quiz&#39; | [optional] 
**linked_object_id** | **int** | The id of a learning object to link to this planner note. Must be used in conjunction with linked_object_type and course_id. The object must be in the same course as specified by course_id. If the title argument is not provided, the planner note will use the learning object&#39;s title as its title. Only one planner note may be linked to a specific learning object. | [optional] 

## Example

```python
from canvas_lms_python_client.models.planner_notes_create_request import PlannerNotesCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PlannerNotesCreateRequest from a JSON string
planner_notes_create_request_instance = PlannerNotesCreateRequest.from_json(json)
# print the JSON string representation of the object
print(PlannerNotesCreateRequest.to_json())

# convert the object into a dict
planner_notes_create_request_dict = planner_notes_create_request_instance.to_dict()
# create an instance of PlannerNotesCreateRequest from a dict
planner_notes_create_request_from_dict = PlannerNotesCreateRequest.from_dict(planner_notes_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


