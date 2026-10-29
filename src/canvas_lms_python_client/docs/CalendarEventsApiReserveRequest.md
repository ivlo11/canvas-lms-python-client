# CalendarEventsApiReserveRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**participant_id** | **str** | User or group id for whom you are making the reservation (depends on the participant type). Defaults to the current user (or user&#39;s candidate group). | [optional] 
**comments** | **str** | Comments to associate with this reservation | [optional] 
**cancel_existing** | **bool** | Defaults to false. If true, cancel any previous reservation(s) for this participant and appointment group. | [optional] 

## Example

```python
from canvas_lms_python_client.models.calendar_events_api_reserve_request import CalendarEventsApiReserveRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CalendarEventsApiReserveRequest from a JSON string
calendar_events_api_reserve_request_instance = CalendarEventsApiReserveRequest.from_json(json)
# print the JSON string representation of the object
print(CalendarEventsApiReserveRequest.to_json())

# convert the object into a dict
calendar_events_api_reserve_request_dict = calendar_events_api_reserve_request_instance.to_dict()
# create an instance of CalendarEventsApiReserveRequest from a dict
calendar_events_api_reserve_request_from_dict = CalendarEventsApiReserveRequest.from_dict(calendar_events_api_reserve_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


