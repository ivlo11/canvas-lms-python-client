# UserPermissions

Optional: This field is only returned in certain API calls, and will return a non-comprehensive list of permissions for the user.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**can_update_name** | **bool** | Whether the user can update their name. | [optional] 
**can_update_avatar** | **bool** | Whether the user can update their avatar. | [optional] 
**limit_parent_app_web_access** | **bool** | Whether the user can interact with Canvas web from the Canvas Parent app. | [optional] 

## Example

```python
from canvas_lms_python_client.models.user_permissions import UserPermissions

# TODO update the JSON string below
json = "{}"
# create an instance of UserPermissions from a JSON string
user_permissions_instance = UserPermissions.from_json(json)
# print the JSON string representation of the object
print(UserPermissions.to_json())

# convert the object into a dict
user_permissions_dict = user_permissions_instance.to_dict()
# create an instance of UserPermissions from a dict
user_permissions_from_dict = UserPermissions.from_dict(user_permissions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


