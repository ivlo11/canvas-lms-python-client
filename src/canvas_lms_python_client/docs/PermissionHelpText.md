# PermissionHelpText

Information about a permission, including its purpose and considerations for use.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**details** | **List[object]** | Detailed explanations about what the permission does. | [optional] 
**considerations** | **List[object]** | A list of considerations or warnings about using the permission. | [optional] 

## Example

```python
from canvas_lms_python_client.models.permission_help_text import PermissionHelpText

# TODO update the JSON string below
json = "{}"
# create an instance of PermissionHelpText from a JSON string
permission_help_text_instance = PermissionHelpText.from_json(json)
# print the JSON string representation of the object
print(PermissionHelpText.to_json())

# convert the object into a dict
permission_help_text_dict = permission_help_text_instance.to_dict()
# create an instance of PermissionHelpText from a dict
permission_help_text_from_dict = PermissionHelpText.from_dict(permission_help_text_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


