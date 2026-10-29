# NotificationPreferencesUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**notification_preferences** | [**NotificationPreferencesUpdateRequestNotificationPreferences**](NotificationPreferencesUpdateRequestNotificationPreferences.md) |  | 

## Example

```python
from canvas_lms_python_client.models.notification_preferences_update_request import NotificationPreferencesUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationPreferencesUpdateRequest from a JSON string
notification_preferences_update_request_instance = NotificationPreferencesUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(NotificationPreferencesUpdateRequest.to_json())

# convert the object into a dict
notification_preferences_update_request_dict = notification_preferences_update_request_instance.to_dict()
# create an instance of NotificationPreferencesUpdateRequest from a dict
notification_preferences_update_request_from_dict = NotificationPreferencesUpdateRequest.from_dict(notification_preferences_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


