# CalendarEventsApiSaveEnabledAccountCalendarsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mark_feature_as_seen** | **bool** | Flag to mark account calendars feature as seen | [optional] 
**enabled_account_calendars** | **List[List[str]]** | An array of account Ids to remember in the calendars list of the user | [optional] 

## Example

```python
from canvas_lms_python_client.models.calendar_events_api_save_enabled_account_calendars_request import CalendarEventsApiSaveEnabledAccountCalendarsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CalendarEventsApiSaveEnabledAccountCalendarsRequest from a JSON string
calendar_events_api_save_enabled_account_calendars_request_instance = CalendarEventsApiSaveEnabledAccountCalendarsRequest.from_json(json)
# print the JSON string representation of the object
print(CalendarEventsApiSaveEnabledAccountCalendarsRequest.to_json())

# convert the object into a dict
calendar_events_api_save_enabled_account_calendars_request_dict = calendar_events_api_save_enabled_account_calendars_request_instance.to_dict()
# create an instance of CalendarEventsApiSaveEnabledAccountCalendarsRequest from a dict
calendar_events_api_save_enabled_account_calendars_request_from_dict = CalendarEventsApiSaveEnabledAccountCalendarsRequest.from_dict(calendar_events_api_save_enabled_account_calendars_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


