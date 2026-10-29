# NotificationPreference



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | [optional] 
**notification** | **str** | The notification this preference belongs to | [optional] 
**category** | **str** | The category of that notification | [optional] 
**frequency** | **str** | How often to send notifications to this communication channel for the given notification. Possible values are &#39;immediately&#39;, &#39;daily&#39;, &#39;weekly&#39;, and &#39;never&#39; | [optional] 

## Example

```python
from canvas_lms_python_client.models.notification_preference import NotificationPreference

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationPreference from a JSON string
notification_preference_instance = NotificationPreference.from_json(json)
# print the JSON string representation of the object
print(NotificationPreference.to_json())

# convert the object into a dict
notification_preference_dict = notification_preference_instance.to_dict()
# create an instance of NotificationPreference from a dict
notification_preference_from_dict = NotificationPreference.from_dict(notification_preference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


