# CalendarEventsApiSetCourseTimetableRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timetables** | [**CalendarEventsApiSetCourseTimetableRequestTimetables**](CalendarEventsApiSetCourseTimetableRequestTimetables.md) |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.calendar_events_api_set_course_timetable_request import CalendarEventsApiSetCourseTimetableRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CalendarEventsApiSetCourseTimetableRequest from a JSON string
calendar_events_api_set_course_timetable_request_instance = CalendarEventsApiSetCourseTimetableRequest.from_json(json)
# print the JSON string representation of the object
print(CalendarEventsApiSetCourseTimetableRequest.to_json())

# convert the object into a dict
calendar_events_api_set_course_timetable_request_dict = calendar_events_api_set_course_timetable_request_instance.to_dict()
# create an instance of CalendarEventsApiSetCourseTimetableRequest from a dict
calendar_events_api_set_course_timetable_request_from_dict = CalendarEventsApiSetCourseTimetableRequest.from_dict(calendar_events_api_set_course_timetable_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


