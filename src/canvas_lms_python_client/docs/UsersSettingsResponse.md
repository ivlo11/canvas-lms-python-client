# UsersSettingsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collapse_course_nav** | **bool** |  | [optional] 
**collapse_global_nav** | **bool** |  | [optional] 
**comment_library_suggestions_enabled** | **bool** |  | [optional] 
**default_to_block_editor** | **bool** |  | [optional] 
**elementary_dashboard_disabled** | **bool** |  | [optional] 
**hide_dashcard_color_overlays** | **bool** |  | [optional] 
**manual_mark_as_read** | **bool** |  | [optional] 
**release_notes_badge_disabled** | **bool** |  | [optional] 
**widget_dashboard_dark_mode** | **bool** |  | [optional] 
**widget_dashboard_user_preference** | **bool** |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.users_settings_response import UsersSettingsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UsersSettingsResponse from a JSON string
users_settings_response_instance = UsersSettingsResponse.from_json(json)
# print the JSON string representation of the object
print(UsersSettingsResponse.to_json())

# convert the object into a dict
users_settings_response_dict = users_settings_response_instance.to_dict()
# create an instance of UsersSettingsResponse from a dict
users_settings_response_from_dict = UsersSettingsResponse.from_dict(users_settings_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


