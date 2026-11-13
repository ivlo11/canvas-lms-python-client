# AccountCalendarsApiIndexResponse

Object response with `account_calendars`, `total_results` (from the Canvas `@returns`).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_calendars** | [**List[AccountCalendar]**](AccountCalendar.md) |  | [optional] 
**total_results** | **int** |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.account_calendars_api_index_response import AccountCalendarsApiIndexResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AccountCalendarsApiIndexResponse from a JSON string
account_calendars_api_index_response_instance = AccountCalendarsApiIndexResponse.from_json(json)
# print the JSON string representation of the object
print(AccountCalendarsApiIndexResponse.to_json())

# convert the object into a dict
account_calendars_api_index_response_dict = account_calendars_api_index_response_instance.to_dict()
# create an instance of AccountCalendarsApiIndexResponse from a dict
account_calendars_api_index_response_from_dict = AccountCalendarsApiIndexResponse.from_dict(account_calendars_api_index_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


