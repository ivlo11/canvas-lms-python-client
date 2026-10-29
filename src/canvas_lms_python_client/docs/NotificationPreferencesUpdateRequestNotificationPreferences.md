# NotificationPreferencesUpdateRequestNotificationPreferences


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**frequency** | **str** | [Required] The desired frequency for this notification | 

## Example

```python
from canvas_lms_python_client.models.notification_preferences_update_request_notification_preferences import NotificationPreferencesUpdateRequestNotificationPreferences

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationPreferencesUpdateRequestNotificationPreferences from a JSON string
notification_preferences_update_request_notification_preferences_instance = NotificationPreferencesUpdateRequestNotificationPreferences.from_json(json)
# print the JSON string representation of the object
print(NotificationPreferencesUpdateRequestNotificationPreferences.to_json())

# convert the object into a dict
notification_preferences_update_request_notification_preferences_dict = notification_preferences_update_request_notification_preferences_instance.to_dict()
# create an instance of NotificationPreferencesUpdateRequestNotificationPreferences from a dict
notification_preferences_update_request_notification_preferences_from_dict = NotificationPreferencesUpdateRequestNotificationPreferences.from_dict(notification_preferences_update_request_notification_preferences_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


