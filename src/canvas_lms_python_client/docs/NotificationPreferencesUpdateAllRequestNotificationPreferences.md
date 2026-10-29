# NotificationPreferencesUpdateAllRequestNotificationPreferences


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**x** | **str** | [frequency] [Required] The desired frequency for &lt;X&gt; notification | [optional] 

## Example

```python
from canvas_lms_python_client.models.notification_preferences_update_all_request_notification_preferences import NotificationPreferencesUpdateAllRequestNotificationPreferences

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationPreferencesUpdateAllRequestNotificationPreferences from a JSON string
notification_preferences_update_all_request_notification_preferences_instance = NotificationPreferencesUpdateAllRequestNotificationPreferences.from_json(json)
# print the JSON string representation of the object
print(NotificationPreferencesUpdateAllRequestNotificationPreferences.to_json())

# convert the object into a dict
notification_preferences_update_all_request_notification_preferences_dict = notification_preferences_update_all_request_notification_preferences_instance.to_dict()
# create an instance of NotificationPreferencesUpdateAllRequestNotificationPreferences from a dict
notification_preferences_update_all_request_notification_preferences_from_dict = NotificationPreferencesUpdateAllRequestNotificationPreferences.from_dict(notification_preferences_update_all_request_notification_preferences_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


