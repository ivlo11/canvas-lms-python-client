# AccountCalendar


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | the ID of the account associated with this calendar | [optional] 
**name** | **str** | the name of the account associated with this calendar | [optional] 
**parent_account_id** | **int** | the account&#39;s parent ID, or null if this is the root account | [optional] 
**root_account_id** | **int** | the ID of the root account, or null if this is the root account | [optional] 
**visible** | **bool** | whether this calendar is visible to users | [optional] 
**auto_subscribe** | **bool** | whether users see this calendar&#39;s events without needing to manually add it | [optional] 
**sub_account_count** | **int** | number of this account&#39;s direct sub-accounts | [optional] 
**asset_string** | **str** | Asset string of the account | [optional] 
**type** | **str** | Object type | [optional] 
**calendar_event_url** | **str** | url to get full detailed events | [optional] 
**can_create_calendar_events** | **bool** | whether the user can create calendar events | [optional] 
**create_calendar_event_url** | **str** | API path to create events for the account | [optional] 
**new_calendar_event_url** | **str** | url to open the more options event editor | [optional] 

## Example

```python
from canvas_lms_python_client.models.account_calendar import AccountCalendar

# TODO update the JSON string below
json = "{}"
# create an instance of AccountCalendar from a JSON string
account_calendar_instance = AccountCalendar.from_json(json)
# print the JSON string representation of the object
print(AccountCalendar.to_json())

# convert the object into a dict
account_calendar_dict = account_calendar_instance.to_dict()
# create an instance of AccountCalendar from a dict
account_calendar_from_dict = AccountCalendar.from_dict(account_calendar_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


