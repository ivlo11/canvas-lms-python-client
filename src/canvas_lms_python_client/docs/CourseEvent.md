# CourseEvent



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of the event. | [optional] 
**created_at** | **datetime** | timestamp of the event | [optional] 
**event_type** | **str** | Course event type The event type defines the type and schema of the event_data object. | [optional] 
**event_data** | **object** | Course event data depending on the event type.  This will return an object containing the relevant event data.  An updated event type will return an UpdatedEventData object. | [optional] 
**event_source** | **str** | Course event source depending on the event type.  This will return a string containing the source of the event. | [optional] 
**links** | [**CourseEventLink**](CourseEventLink.md) |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.course_event import CourseEvent

# TODO update the JSON string below
json = "{}"
# create an instance of CourseEvent from a JSON string
course_event_instance = CourseEvent.from_json(json)
# print the JSON string representation of the object
print(CourseEvent.to_json())

# convert the object into a dict
course_event_dict = course_event_instance.to_dict()
# create an instance of CourseEvent from a dict
course_event_from_dict = CourseEvent.from_dict(course_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


