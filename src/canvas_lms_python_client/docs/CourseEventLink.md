# CourseEventLink

IDs related to the event. course, user, page_view and sis_batch are strings, and an empty string means none.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**course** | **str** | ID of the course for the event. | [optional] 
**user** | **str** | ID of the user for the event (who made the change). | [optional] 
**page_view** | **str** | ID of the page view during the event if it exists. | [optional] 
**copied_from** | **int** | ID of the course that this course was copied from. This is only included if the event_type is copied_from. | [optional] 
**copied_to** | **int** | ID of the course that this course was copied to. This is only included if the event_type is copied_to. | [optional] 
**reset_from** | **int** | ID of the course that this course was reset from. This is only included if the event_type is reset_from. | [optional] 
**reset_to** | **int** | ID of the course that this course was reset to. This is only included if the event_type is reset_to. | [optional] 
**sis_batch** | **str** | ID of the SIS batch that triggered the event. | [optional] 

## Example

```python
from canvas_lms_python_client.models.course_event_link import CourseEventLink

# TODO update the JSON string below
json = "{}"
# create an instance of CourseEventLink from a JSON string
course_event_link_instance = CourseEventLink.from_json(json)
# print the JSON string representation of the object
print(CourseEventLink.to_json())

# convert the object into a dict
course_event_link_dict = course_event_link_instance.to_dict()
# create an instance of CourseEventLink from a dict
course_event_link_from_dict = CourseEventLink.from_dict(course_event_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


