# UserDisplay

This mini-object is used for secondary user responses, when we just want to provide enough information to display a user.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The ID of the user. | [optional] 
**short_name** | **str** | A short name the user has selected, for use in conversations or other less formal places through the site. | [optional] 
**avatar_image_url** | **str** | If avatars are enabled, this field will be included and contain a url to retrieve the user&#39;s avatar. | [optional] 
**html_url** | **str** | URL to access user, either nested to a context or directly. | [optional] 

## Example

```python
from canvas_lms_python_client.models.user_display import UserDisplay

# TODO update the JSON string below
json = "{}"
# create an instance of UserDisplay from a JSON string
user_display_instance = UserDisplay.from_json(json)
# print the JSON string representation of the object
print(UserDisplay.to_json())

# convert the object into a dict
user_display_dict = user_display_instance.to_dict()
# create an instance of UserDisplay from a dict
user_display_from_dict = UserDisplay.from_dict(user_display_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


