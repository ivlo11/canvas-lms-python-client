# NotificationPreferencesShowResponse

Object response with `notification_preferences` (from the Canvas `@returns`).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**notification_preferences** | [**List[NotificationPreference]**](NotificationPreference.md) |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.notification_preferences_show_response import NotificationPreferencesShowResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationPreferencesShowResponse from a JSON string
notification_preferences_show_response_instance = NotificationPreferencesShowResponse.from_json(json)
# print the JSON string representation of the object
print(NotificationPreferencesShowResponse.to_json())

# convert the object into a dict
notification_preferences_show_response_dict = notification_preferences_show_response_instance.to_dict()
# create an instance of NotificationPreferencesShowResponse from a dict
notification_preferences_show_response_from_dict = NotificationPreferencesShowResponse.from_dict(notification_preferences_show_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


