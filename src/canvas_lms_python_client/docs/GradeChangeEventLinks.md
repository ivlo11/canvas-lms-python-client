# GradeChangeEventLinks



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assignment** | **int** | ID of the assignment associated with the event | [optional] 
**course** | **int** | ID of the course associated with the event. will match the context_id in the associated assignment if the context type for the assignment is a course | [optional] 
**student** | **int** | ID of the student associated with the event. will match the user_id in the associated submission. | [optional] 
**grader** | **int** | ID of the grader associated with the event. will match the grader_id in the associated submission. | [optional] 
**page_view** | **str** | ID of the page view during the event if it exists. | [optional] 

## Example

```python
from canvas_lms_python_client.models.grade_change_event_links import GradeChangeEventLinks

# TODO update the JSON string below
json = "{}"
# create an instance of GradeChangeEventLinks from a JSON string
grade_change_event_links_instance = GradeChangeEventLinks.from_json(json)
# print the JSON string representation of the object
print(GradeChangeEventLinks.to_json())

# convert the object into a dict
grade_change_event_links_dict = grade_change_event_links_instance.to_dict()
# create an instance of GradeChangeEventLinks from a dict
grade_change_event_links_from_dict = GradeChangeEventLinks.from_dict(grade_change_event_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


