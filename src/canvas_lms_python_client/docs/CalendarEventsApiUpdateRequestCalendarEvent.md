# CalendarEventsApiUpdateRequestCalendarEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context_code** | **str** | [Optional, String] Context code of the course, group, user, or account to move this event to. Scheduler appointments and events with section-specific times cannot be moved between calendars. | [optional] 
**title** | **str** | [String] Short title for the calendar event. | [optional] 
**description** | **str** | [String] Longer HTML description of the event. | [optional] 
**start_at** | **str** | [DateTime] Start date/time of the event. | [optional] 
**end_at** | **str** | [DateTime] End date/time of the event. | [optional] 
**location_name** | **str** | [String] Location name of the event. | [optional] 
**location_address** | **str** | [String] Location address | [optional] 
**all_day** | **bool** | [Boolean] When true event is considered to span the whole day and times are ignored. | [optional] 
**child_event_data** | **str** | [X][context_code] [String] Context code(s) corresponding to the section-level start and end time(s). | [optional] 
**rrule** | **str** | [Optional, String] Valid if the event whose ID is in the URL is part of a series. This defines the shape of the recurring event series after it&#39;s updated. Its value is the iCalendar RRULE. Unending series are not supported. | [optional] 
**blackout_date** | **bool** | [Boolean] If the blackout_date is true, this event represents a holiday or some other special day that does not count in course pacing. | [optional] 

## Example

```python
from canvas_lms_python_client.models.calendar_events_api_update_request_calendar_event import CalendarEventsApiUpdateRequestCalendarEvent

# TODO update the JSON string below
json = "{}"
# create an instance of CalendarEventsApiUpdateRequestCalendarEvent from a JSON string
calendar_events_api_update_request_calendar_event_instance = CalendarEventsApiUpdateRequestCalendarEvent.from_json(json)
# print the JSON string representation of the object
print(CalendarEventsApiUpdateRequestCalendarEvent.to_json())

# convert the object into a dict
calendar_events_api_update_request_calendar_event_dict = calendar_events_api_update_request_calendar_event_instance.to_dict()
# create an instance of CalendarEventsApiUpdateRequestCalendarEvent from a dict
calendar_events_api_update_request_calendar_event_from_dict = CalendarEventsApiUpdateRequestCalendarEvent.from_dict(calendar_events_api_update_request_calendar_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


