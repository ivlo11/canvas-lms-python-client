# TodoItem

An assignment or quiz that the user needs to grade or submit

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context_type** | **str** | The type of the item&#39;s context: course or group | [optional] 
**course_id** | **int** | The id of the item&#39;s course, when the context is a course | [optional] 
**group_id** | **int** | The id of the item&#39;s group, when the context is a group | [optional] 
**context_name** | **str** | The name of the item&#39;s context | [optional] 
**context_short_name** | **str** | The short name of the item&#39;s context | [optional] 
**type** | **str** | grading for an assignment that needs grading, or submitting for an assignment or quiz that needs submitting soon | 
**assignment** | [**Assignment**](Assignment.md) |  | [optional] 
**quiz** | [**Quiz**](Quiz.md) |  | [optional] 
**ignore** | **str** | A URL that hides this item from future requests until it changes, with a DELETE request | [optional] 
**ignore_permanently** | **str** | A URL that hides this item forever, with a DELETE request | [optional] 
**html_url** | **str** | The URL of the item in Canvas: SpeedGrader for grading items, the submission page otherwise | [optional] 
**needs_grading_count** | **int** | The number of submissions that need grading, for grading items | [optional] 
**checkpoint_label** | **str** | The checkpoint&#39;s tag, for checkpoint (sub-assignment) items | [optional] 
**parent_assignment_id** | **int** | The id of the parent assignment, for checkpoint (sub-assignment) items | [optional] 
**on_time_needs_grading_count** | **int** | Optional: on-time submissions that need grading, for grading items with include[]&#x3D;grading_counts | [optional] 
**late_needs_grading_count** | **int** | Optional: late submissions that need grading, for grading items with include[]&#x3D;grading_counts | [optional] 
**resubmitted_needs_grading_count** | **int** | Optional: resubmissions that need grading, for grading items with include[]&#x3D;grading_counts | [optional] 
**submitted_submissions_count** | **int** | Optional: submitted submissions, for grading items with include[]&#x3D;grading_counts | [optional] 
**total_submissions_count** | **int** | Optional: all submissions, for grading items with include[]&#x3D;grading_counts | [optional] 

## Example

```python
from canvas_lms_python_client.models.todo_item import TodoItem

# TODO update the JSON string below
json = "{}"
# create an instance of TodoItem from a JSON string
todo_item_instance = TodoItem.from_json(json)
# print the JSON string representation of the object
print(TodoItem.to_json())

# convert the object into a dict
todo_item_dict = todo_item_instance.to_dict()
# create an instance of TodoItem from a dict
todo_item_from_dict = TodoItem.from_dict(todo_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


