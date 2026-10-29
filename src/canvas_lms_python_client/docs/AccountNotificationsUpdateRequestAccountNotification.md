# AccountNotificationsUpdateRequestAccountNotification


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subject** | **str** | [String] The subject of the notification. | [optional] 
**message** | **str** | [String] The message body of the notification. | [optional] 
**start_at** | **str** | [DateTime] The start date and time of the notification in ISO8601 format. e.g. 2014-01-01T01:00Z | [optional] 
**end_at** | **str** | [DateTime] The end date and time of the notification in ISO8601 format. e.g. 2014-01-01T01:00Z | [optional] 
**icon** | **str** | [\&quot;warning\&quot;|\&quot;information\&quot;|\&quot;question\&quot;|\&quot;error\&quot;|\&quot;calendar\&quot;] The icon to display with the notification. | [optional] 

## Example

```python
from canvas_lms_python_client.models.account_notifications_update_request_account_notification import AccountNotificationsUpdateRequestAccountNotification

# TODO update the JSON string below
json = "{}"
# create an instance of AccountNotificationsUpdateRequestAccountNotification from a JSON string
account_notifications_update_request_account_notification_instance = AccountNotificationsUpdateRequestAccountNotification.from_json(json)
# print the JSON string representation of the object
print(AccountNotificationsUpdateRequestAccountNotification.to_json())

# convert the object into a dict
account_notifications_update_request_account_notification_dict = account_notifications_update_request_account_notification_instance.to_dict()
# create an instance of AccountNotificationsUpdateRequestAccountNotification from a dict
account_notifications_update_request_account_notification_from_dict = AccountNotificationsUpdateRequestAccountNotification.from_dict(account_notifications_update_request_account_notification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


