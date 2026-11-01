# UsersSetTextEditorPreferenceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text_editor_preference** | **str** | The identifier for the editor. | [optional] 

## Example

```python
from canvas_lms_python_client.models.users_set_text_editor_preference_request import UsersSetTextEditorPreferenceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UsersSetTextEditorPreferenceRequest from a JSON string
users_set_text_editor_preference_request_instance = UsersSetTextEditorPreferenceRequest.from_json(json)
# print the JSON string representation of the object
print(UsersSetTextEditorPreferenceRequest.to_json())

# convert the object into a dict
users_set_text_editor_preference_request_dict = users_set_text_editor_preference_request_instance.to_dict()
# create an instance of UsersSetTextEditorPreferenceRequest from a dict
users_set_text_editor_preference_request_from_dict = UsersSetTextEditorPreferenceRequest.from_dict(users_set_text_editor_preference_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


