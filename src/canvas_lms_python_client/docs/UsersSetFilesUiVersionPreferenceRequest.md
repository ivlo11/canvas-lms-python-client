# UsersSetFilesUiVersionPreferenceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**files_ui_version** | **str** | The identifier for the files UI version. | [optional] 

## Example

```python
from canvas_lms_python_client.models.users_set_files_ui_version_preference_request import UsersSetFilesUiVersionPreferenceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UsersSetFilesUiVersionPreferenceRequest from a JSON string
users_set_files_ui_version_preference_request_instance = UsersSetFilesUiVersionPreferenceRequest.from_json(json)
# print the JSON string representation of the object
print(UsersSetFilesUiVersionPreferenceRequest.to_json())

# convert the object into a dict
users_set_files_ui_version_preference_request_dict = users_set_files_ui_version_preference_request_instance.to_dict()
# create an instance of UsersSetFilesUiVersionPreferenceRequest from a dict
users_set_files_ui_version_preference_request_from_dict = UsersSetFilesUiVersionPreferenceRequest.from_dict(users_set_files_ui_version_preference_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


