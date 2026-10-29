# CalendarEventsApiReserveForOtherRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comments** | **str** | Comments to associate with this reservation | [optional] 
**cancel_existing** | **bool** | Defaults to false. If true, cancel any previous reservation(s) for this participant and appointment group. | [optional] 

## Example

```python
from canvas_lms_python_client.models.calendar_events_api_reserve_for_other_request import CalendarEventsApiReserveForOtherRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CalendarEventsApiReserveForOtherRequest from a JSON string
calendar_events_api_reserve_for_other_request_instance = CalendarEventsApiReserveForOtherRequest.from_json(json)
# print the JSON string representation of the object
print(CalendarEventsApiReserveForOtherRequest.to_json())

# convert the object into a dict
calendar_events_api_reserve_for_other_request_dict = calendar_events_api_reserve_for_other_request_instance.to_dict()
# create an instance of CalendarEventsApiReserveForOtherRequest from a dict
calendar_events_api_reserve_for_other_request_from_dict = CalendarEventsApiReserveForOtherRequest.from_dict(calendar_events_api_reserve_for_other_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


