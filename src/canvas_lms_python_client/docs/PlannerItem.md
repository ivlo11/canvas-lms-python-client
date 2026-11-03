# PlannerItem

An object to be shown on the planner, with the planner override that controls its visibility for the user

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context_type** | **str** | The type of the item&#39;s context: Course, Group or User. Absent for a planner note without a course. | [optional] 
**course_id** | **int** | The id of the item&#39;s course, when the context is a course | [optional] 
**group_id** | **int** | The id of the item&#39;s group, when the context is a group | [optional] 
**user_id** | **int** | The id of the item&#39;s user, when the context is a user | [optional] 
**context_name** | **str** | The name of the item&#39;s context | [optional] 
**context_image** | **str** | The image URL of the item&#39;s course, if it has one | [optional] 
**plannable_id** | **int** | The id of the plannable object | 
**plannable_type** | **str** | The type of the plannable object: discussion_topic, announcement, quiz, assignment, wiki_page, planner_note, calendar_event, assessment_request, sub_assignment or peer_review_sub_assignment | 
**plannable_date** | **datetime** | The date the item is shown on the planner | [optional] 
**plannable** | **object** | The plannable object&#39;s attributes. Its fields depend on plannable_type. | [optional] 
**planner_override** | [**PlannerOverride**](PlannerOverride.md) |  | [optional] 
**new_activity** | **bool** | Whether the item has new or unread activity for the user | [optional] 
**submissions** | **object** | false if the item has no associated assignment; otherwise the status of the user&#39;s submission, with submitted, excused, graded, posted_at, late, missing, needs_grading, has_feedback and redo_request | [optional] 
**html_url** | **str** | The URL of the item in Canvas | [optional] 

## Example

```python
from canvas_lms_python_client.models.planner_item import PlannerItem

# TODO update the JSON string below
json = "{}"
# create an instance of PlannerItem from a JSON string
planner_item_instance = PlannerItem.from_json(json)
# print the JSON string representation of the object
print(PlannerItem.to_json())

# convert the object into a dict
planner_item_dict = planner_item_instance.to_dict()
# create an instance of PlannerItem from a dict
planner_item_from_dict = PlannerItem.from_dict(planner_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


