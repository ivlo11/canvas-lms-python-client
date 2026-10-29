# CalendarEventsApiCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**calendar_event** | [**CalendarEventsApiCreateRequestCalendarEvent**](CalendarEventsApiCreateRequestCalendarEvent.md) |  | 

## Example

```python
from canvas_lms_python_client.models.calendar_events_api_create_request import CalendarEventsApiCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CalendarEventsApiCreateRequest from a JSON string
calendar_events_api_create_request_instance = CalendarEventsApiCreateRequest.from_json(json)
# print the JSON string representation of the object
print(CalendarEventsApiCreateRequest.to_json())

# convert the object into a dict
calendar_events_api_create_request_dict = calendar_events_api_create_request_instance.to_dict()
# create an instance of CalendarEventsApiCreateRequest from a dict
calendar_events_api_create_request_from_dict = CalendarEventsApiCreateRequest.from_dict(calendar_events_api_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


