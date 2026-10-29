# AccountNotificationsCreateRequestAccountNotification


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subject** | **str** | [Required, String] The subject of the notification. | 
**message** | **str** | [Required, String] The message body of the notification. | 
**start_at** | **str** | [Required, DateTime] The start date and time of the notification in ISO8601 format. e.g. 2014-01-01T01:00Z | 
**end_at** | **str** | [Required, DateTime] The end date and time of the notification in ISO8601 format. e.g. 2014-01-01T01:00Z | 
**icon** | **str** | [\&quot;warning\&quot;|\&quot;information\&quot;|\&quot;question\&quot;|\&quot;error\&quot;|\&quot;calendar\&quot;] The icon to display with the notification. Note: Defaults to warning. | [optional] 

## Example

```python
from canvas_lms_python_client.models.account_notifications_create_request_account_notification import AccountNotificationsCreateRequestAccountNotification

# TODO update the JSON string below
json = "{}"
# create an instance of AccountNotificationsCreateRequestAccountNotification from a JSON string
account_notifications_create_request_account_notification_instance = AccountNotificationsCreateRequestAccountNotification.from_json(json)
# print the JSON string representation of the object
print(AccountNotificationsCreateRequestAccountNotification.to_json())

# convert the object into a dict
account_notifications_create_request_account_notification_dict = account_notifications_create_request_account_notification_instance.to_dict()
# create an instance of AccountNotificationsCreateRequestAccountNotification from a dict
account_notifications_create_request_account_notification_from_dict = AccountNotificationsCreateRequestAccountNotification.from_dict(account_notifications_create_request_account_notification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


