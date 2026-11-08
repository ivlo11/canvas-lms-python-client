# CalendarEvent



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**CalendarEventId**](CalendarEventId.md) |  | [optional] 
**title** | **str** | The title of the calendar event | [optional] 
**start_at** | **datetime** | The start timestamp of the event | [optional] 
**end_at** | **datetime** | The end timestamp of the event | [optional] 
**description** | **str** | The HTML description of the event | [optional] 
**location_name** | **str** | The location name of the event | [optional] 
**location_address** | **str** | The address where the event is taking place | [optional] 
**context_code** | **str** | the context code of the calendar this event belongs to (course, group, user, or account) | [optional] 
**effective_context_code** | **str** | if specified, it indicates which calendar this event should be displayed on. for example, a section-level event would have the course&#39;s context code here, while the section&#39;s context code would be returned above) | [optional] 
**context_name** | **str** | the context name of the calendar this event belongs to (course, user or group) | [optional] 
**all_context_codes** | **str** | a comma-separated list of all calendar contexts this event is part of | [optional] 
**workflow_state** | **str** | Current state of the event (&#39;active&#39;, &#39;locked&#39; or &#39;deleted&#39;) &#39;locked&#39; indicates that start_at/end_at cannot be changed (though the event could be deleted). Normally only reservations or time slots with reservations are locked (see the Appointment Groups API) | [optional] 
**hidden** | **bool** | Whether this event should be displayed on the calendar. Only true for course-level events with section-level child events. | [optional] 
**parent_event_id** | **int** | Normally null. If this is a reservation (see the Appointment Groups API), the id will indicate the time slot it is for. If this is a section-level event, this will be the course-level parent event. | [optional] 
**child_events_count** | **int** | The number of child_events. See child_events (and parent_event_id) | [optional] 
**child_events** | [**List[AssignmentGroupAssignmentsInner]**](AssignmentGroupAssignmentsInner.md) | Included by default, but may be excluded (see include[] option). If this is a time slot (see the Appointment Groups API) this will be a list of any reservations. If this is a course-level event, this will be a list of section-level events (if any) | [optional] 
**url** | **str** | URL for this calendar event (to update, delete, etc.) | [optional] 
**html_url** | **str** | URL for a user to view this event | [optional] 
**all_day_date** | **datetime** | The date of this event | [optional] 
**all_day** | **bool** | Boolean indicating whether this is an all-day event (midnight to midnight) | [optional] 
**created_at** | **datetime** | When the calendar event was created | [optional] 
**updated_at** | **datetime** | When the calendar event was last updated | [optional] 
**appointment_group_id** | **int** | Various Appointment-Group-related fields.These fields are only pertinent to time slots (appointments) and reservations of those time slots. See the Appointment Groups API. The id of the appointment group | [optional] 
**appointment_group_url** | **str** | The API URL of the appointment group | [optional] 
**own_reservation** | **bool** | If the event is a reservation, this a boolean indicating whether it is the current user&#39;s reservation, or someone else&#39;s | [optional] 
**reserve_url** | **str** | If the event is a time slot, the API URL for reserving it | [optional] 
**reserved** | **bool** | If the event is a time slot, a boolean indicating whether the user has already made a reservation for it | [optional] 
**participant_type** | **str** | The type of participant to sign up for a slot: &#39;User&#39; or &#39;Group&#39; | [optional] 
**participants_per_appointment** | **int** | If the event is a time slot, this is the participant limit | [optional] 
**available_slots** | **int** | If the event is a time slot and it has a participant limit, an integer indicating how many slots are available | [optional] 
**user** | **str** | If the event is a user-level reservation, this will contain the user participant JSON (refer to the Users API). | [optional] 
**group** | **str** | If the event is a group-level reservation, this will contain the group participant JSON (refer to the Groups API). | [optional] 
**important_dates** | **bool** | Boolean indicating whether this has important dates. | [optional] 
**series_uuid** | **UUID** | Identifies the recurring event series this event may belong to. | [optional] 
**rrule** | **str** | An iCalendar RRULE for defining how events in a recurring event series repeat. | [optional] 
**series_head** | **bool** | Boolean indicating if is the first event in the series of recurring events. | [optional] 
**series_natural_language** | **str** | A natural language expression of how events occur in the series. | [optional] 
**blackout_date** | **bool** | Boolean indicating whether this has blackout date. | [optional] 
**can_manage_appointment_group** | **bool** |  | [optional] 
**comments** | **str** |  | [optional] 
**context_color** | **object** |  | [optional] 
**duplicates** | **List[object]** |  | [optional] 
**type** | **str** |  | [optional] 
**reserve_comments** | **str** |  | [optional] 
**assignment** | **object** |  | [optional] 
**assignment_overrides** | **List[object]** |  | [optional] 
**lock_info** | **object** |  | [optional] 
**sub_assignment** | **object** |  | [optional] 
**sub_assignment_overrides** | **List[object]** |  | [optional] 
**submission_types** | **str** |  | [optional] 
**web_conference** | **object** |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.calendar_event import CalendarEvent

# TODO update the JSON string below
json = "{}"
# create an instance of CalendarEvent from a JSON string
calendar_event_instance = CalendarEvent.from_json(json)
# print the JSON string representation of the object
print(CalendarEvent.to_json())

# convert the object into a dict
calendar_event_dict = calendar_event_instance.to_dict()
# create an instance of CalendarEvent from a dict
calendar_event_from_dict = CalendarEvent.from_dict(calendar_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


