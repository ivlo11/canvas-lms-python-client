# AccountNotification



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subject** | **str** | The subject of the notifications | [optional] 
**message** | **str** | The message to be sent in the notification. | [optional] 
**start_at** | **datetime** | When to send out the notification. | [optional] 
**end_at** | **datetime** | When to expire the notification. | [optional] 
**icon** | **str** | The icon to display with the message.  Defaults to warning. | [optional] 
**roles** | **List[str]** | (Deprecated) The roles to send the notification to.  If roles is not passed it defaults to all roles | [optional] 
**role_ids** | **List[int]** | The roles to send the notification to.  If roles is not passed it defaults to all roles | [optional] 
**author** | **object** | The author of the notification. Available only to admins using include_all. | [optional] 

## Example

```python
from canvas_lms_python_client.models.account_notification import AccountNotification

# TODO update the JSON string below
json = "{}"
# create an instance of AccountNotification from a JSON string
account_notification_instance = AccountNotification.from_json(json)
# print the JSON string representation of the object
print(AccountNotification.to_json())

# convert the object into a dict
account_notification_dict = account_notification_instance.to_dict()
# create an instance of AccountNotification from a dict
account_notification_from_dict = AccountNotification.from_dict(account_notification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


