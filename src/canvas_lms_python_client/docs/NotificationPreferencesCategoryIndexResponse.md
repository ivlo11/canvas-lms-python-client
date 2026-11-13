# NotificationPreferencesCategoryIndexResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**categories** | **List[str]** |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.notification_preferences_category_index_response import NotificationPreferencesCategoryIndexResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationPreferencesCategoryIndexResponse from a JSON string
notification_preferences_category_index_response_instance = NotificationPreferencesCategoryIndexResponse.from_json(json)
# print the JSON string representation of the object
print(NotificationPreferencesCategoryIndexResponse.to_json())

# convert the object into a dict
notification_preferences_category_index_response_dict = notification_preferences_category_index_response_instance.to_dict()
# create an instance of NotificationPreferencesCategoryIndexResponse from a dict
notification_preferences_category_index_response_from_dict = NotificationPreferencesCategoryIndexResponse.from_dict(notification_preferences_category_index_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


