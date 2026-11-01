# UsersSettingsForUsersRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**manual_mark_as_read** | **bool** | If true, require user to manually mark discussion posts as read (don&#39;t auto-mark as read). | [optional] 
**release_notes_badge_disabled** | **bool** | If true, hide the badge for new release notes. | [optional] 
**collapse_global_nav** | **bool** | If true, the user&#39;s page loads with the global navigation collapsed | [optional] 
**collapse_course_nav** | **bool** | If true, the user&#39;s course pages will load with the course navigation collapsed. | [optional] 
**hide_dashcard_color_overlays** | **bool** | If true, images on course cards will be presented without being tinted to match the course color. | [optional] 
**comment_library_suggestions_enabled** | **bool** | If true, suggestions within the comment library will be shown. | [optional] 
**elementary_dashboard_disabled** | **bool** | If true, will display the user&#39;s preferred class Canvas dashboard view instead of the canvas for elementary view. | [optional] 
**widget_dashboard_user_preference** | **bool** | If true, enables the widget dashboard for the user. Only applies when the widget_dashboard feature is enabled at the account level. Defaults to true when the feature becomes available. | [optional] 
**widget_dashboard_dark_mode** | **bool** | If true, enables the dark color theme for the widget dashboard. | [optional] 

## Example

```python
from canvas_lms_python_client.models.users_settings_for_users_request import UsersSettingsForUsersRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UsersSettingsForUsersRequest from a JSON string
users_settings_for_users_request_instance = UsersSettingsForUsersRequest.from_json(json)
# print the JSON string representation of the object
print(UsersSettingsForUsersRequest.to_json())

# convert the object into a dict
users_settings_for_users_request_dict = users_settings_for_users_request_instance.to_dict()
# create an instance of UsersSettingsForUsersRequest from a dict
users_settings_for_users_request_from_dict = UsersSettingsForUsersRequest.from_dict(users_settings_for_users_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


