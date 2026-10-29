# AccountCalendarsApiUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**visible** | **bool** | Allow administrators with &#x60;manage_account_calendar_events&#x60; permission to create events on this calendar, and allow users to view this calendar and its events. | [optional] 
**auto_subscribe** | **bool** | When true, users will automatically see events from this account in their calendar, even if they haven&#39;t manually added that calendar. | [optional] 

## Example

```python
from canvas_lms_python_client.models.account_calendars_api_update_request import AccountCalendarsApiUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AccountCalendarsApiUpdateRequest from a JSON string
account_calendars_api_update_request_instance = AccountCalendarsApiUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(AccountCalendarsApiUpdateRequest.to_json())

# convert the object into a dict
account_calendars_api_update_request_dict = account_calendars_api_update_request_instance.to_dict()
# create an instance of AccountCalendarsApiUpdateRequest from a dict
account_calendars_api_update_request_from_dict = AccountCalendarsApiUpdateRequest.from_dict(account_calendars_api_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


