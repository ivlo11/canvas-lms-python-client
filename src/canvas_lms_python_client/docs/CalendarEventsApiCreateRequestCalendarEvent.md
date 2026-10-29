# CalendarEventsApiCreateRequestCalendarEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context_code** | **str** | [Required, String] Context code of the course, group, user, or account whose calendar this event should be added to. | 
**title** | **str** | [String] Short title for the calendar event. | [optional] 
**description** | **str** | [String] Longer HTML description of the event. | [optional] 
**start_at** | **str** | [DateTime] Start date/time of the event. | [optional] 
**end_at** | **str** | [DateTime] End date/time of the event. | [optional] 
**location_name** | **str** | [String] Location name of the event. | [optional] 
**location_address** | **str** | [String] Location address | [optional] 
**all_day** | **bool** | [Boolean] When true event is considered to span the whole day and times are ignored. | [optional] 
**child_event_data** | **str** | [X][context_code] [String] Context code(s) corresponding to the section-level start and end time(s). | [optional] 
**duplicate** | **str** | [append_iterator] [Boolean] Defaults to false.  If set to &#x60;true&#x60;, an increasing counter number will be appended to the event title when the event is duplicated.  (e.g. Event 1, Event 2, Event 3, etc) | [optional] 
**rrule** | **str** | [string] The recurrence rule to create a series of recurring events. Its value is the {https://icalendar.org/iCalendar-RFC-5545/3-8-5-3-recurrence-rule.html iCalendar RRULE} defining how the event repeats. Unending series not supported. | [optional] 
**blackout_date** | **bool** | [Boolean] If the blackout_date is true, this event represents a holiday or some other special day that does not count in course pacing. | [optional] 

## Example

```python
from canvas_lms_python_client.models.calendar_events_api_create_request_calendar_event import CalendarEventsApiCreateRequestCalendarEvent

# TODO update the JSON string below
json = "{}"
# create an instance of CalendarEventsApiCreateRequestCalendarEvent from a JSON string
calendar_events_api_create_request_calendar_event_instance = CalendarEventsApiCreateRequestCalendarEvent.from_json(json)
# print the JSON string representation of the object
print(CalendarEventsApiCreateRequestCalendarEvent.to_json())

# convert the object into a dict
calendar_events_api_create_request_calendar_event_dict = calendar_events_api_create_request_calendar_event_instance.to_dict()
# create an instance of CalendarEventsApiCreateRequestCalendarEvent from a dict
calendar_events_api_create_request_calendar_event_from_dict = CalendarEventsApiCreateRequestCalendarEvent.from_dict(calendar_events_api_create_request_calendar_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


