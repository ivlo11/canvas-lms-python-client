# CalendarEventsApiSetCourseTimetableRequestTimetables


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**course_section_id** | **str** | [][location_name] [Optional, String] A location name to set for each event | [optional] 

## Example

```python
from canvas_lms_python_client.models.calendar_events_api_set_course_timetable_request_timetables import CalendarEventsApiSetCourseTimetableRequestTimetables

# TODO update the JSON string below
json = "{}"
# create an instance of CalendarEventsApiSetCourseTimetableRequestTimetables from a JSON string
calendar_events_api_set_course_timetable_request_timetables_instance = CalendarEventsApiSetCourseTimetableRequestTimetables.from_json(json)
# print the JSON string representation of the object
print(CalendarEventsApiSetCourseTimetableRequestTimetables.to_json())

# convert the object into a dict
calendar_events_api_set_course_timetable_request_timetables_dict = calendar_events_api_set_course_timetable_request_timetables_instance.to_dict()
# create an instance of CalendarEventsApiSetCourseTimetableRequestTimetables from a dict
calendar_events_api_set_course_timetable_request_timetables_from_dict = CalendarEventsApiSetCourseTimetableRequestTimetables.from_dict(calendar_events_api_set_course_timetable_request_timetables_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


