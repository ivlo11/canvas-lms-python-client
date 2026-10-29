# CalendarEventsApiUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**calendar_event** | [**CalendarEventsApiUpdateRequestCalendarEvent**](CalendarEventsApiUpdateRequestCalendarEvent.md) |  | [optional] 
**which** | **str** | Valid if the event whose ID is in the URL is part of a series. Update just the event whose ID is in in the URL, all events in the series, or the given event and all those following. Some updates may create a new series. For example, changing the start time of this and all following events from the middle of a series. | [optional] 

## Example

```python
from canvas_lms_python_client.models.calendar_events_api_update_request import CalendarEventsApiUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CalendarEventsApiUpdateRequest from a JSON string
calendar_events_api_update_request_instance = CalendarEventsApiUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(CalendarEventsApiUpdateRequest.to_json())

# convert the object into a dict
calendar_events_api_update_request_dict = calendar_events_api_update_request_instance.to_dict()
# create an instance of CalendarEventsApiUpdateRequest from a dict
calendar_events_api_update_request_from_dict = CalendarEventsApiUpdateRequest.from_dict(calendar_events_api_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


