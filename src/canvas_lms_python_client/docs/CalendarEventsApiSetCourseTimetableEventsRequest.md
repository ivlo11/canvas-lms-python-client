# CalendarEventsApiSetCourseTimetableEventsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**course_section_id** | **str** | Events will be created for the course section specified by course_section_id. If not present, events will be created for the entire course. | [optional] 
**events** | **List[List[str]]** | An array of event objects to use. | [optional] 
**events_start_at** | **str** | Start time for the event | [optional] 
**events_end_at** | **str** | End time for the event | [optional] 
**events_location_name** | **str** | Location name for the event | [optional] 
**events_code** | **str** | A unique identifier that can be used to update the event at a later time If one is not specified, an identifier will be generated based on the start and end times | [optional] 
**events_title** | **str** | Title for the meeting. If not present, will default to the associated course&#39;s name | [optional] 

## Example

```python
from canvas_lms_python_client.models.calendar_events_api_set_course_timetable_events_request import CalendarEventsApiSetCourseTimetableEventsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CalendarEventsApiSetCourseTimetableEventsRequest from a JSON string
calendar_events_api_set_course_timetable_events_request_instance = CalendarEventsApiSetCourseTimetableEventsRequest.from_json(json)
# print the JSON string representation of the object
print(CalendarEventsApiSetCourseTimetableEventsRequest.to_json())

# convert the object into a dict
calendar_events_api_set_course_timetable_events_request_dict = calendar_events_api_set_course_timetable_events_request_instance.to_dict()
# create an instance of CalendarEventsApiSetCourseTimetableEventsRequest from a dict
calendar_events_api_set_course_timetable_events_request_from_dict = CalendarEventsApiSetCourseTimetableEventsRequest.from_dict(calendar_events_api_set_course_timetable_events_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


