# NotificationPreferencesUpdateAllRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**notification_preferences** | [**NotificationPreferencesUpdateAllRequestNotificationPreferences**](NotificationPreferencesUpdateAllRequestNotificationPreferences.md) |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.notification_preferences_update_all_request import NotificationPreferencesUpdateAllRequest

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationPreferencesUpdateAllRequest from a JSON string
notification_preferences_update_all_request_instance = NotificationPreferencesUpdateAllRequest.from_json(json)
# print the JSON string representation of the object
print(NotificationPreferencesUpdateAllRequest.to_json())

# convert the object into a dict
notification_preferences_update_all_request_dict = notification_preferences_update_all_request_instance.to_dict()
# create an instance of NotificationPreferencesUpdateAllRequest from a dict
notification_preferences_update_all_request_from_dict = NotificationPreferencesUpdateAllRequest.from_dict(notification_preferences_update_all_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


