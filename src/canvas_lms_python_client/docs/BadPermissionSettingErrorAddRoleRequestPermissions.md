# BadPermissionSettingErrorAddRoleRequestPermissions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**x** | **str** | [applies_to_descendants] [Boolean] If the value is 1, permission &lt;X&gt; cascades down to sub accounts of the account this role is in. The default value is 1.  Must be true if applies_to_self is false.This value is only returned if enabled is true. | [optional] 

## Example

```python
from canvas_lms_python_client.models.bad_permission_setting_error_add_role_request_permissions import BadPermissionSettingErrorAddRoleRequestPermissions

# TODO update the JSON string below
json = "{}"
# create an instance of BadPermissionSettingErrorAddRoleRequestPermissions from a JSON string
bad_permission_setting_error_add_role_request_permissions_instance = BadPermissionSettingErrorAddRoleRequestPermissions.from_json(json)
# print the JSON string representation of the object
print(BadPermissionSettingErrorAddRoleRequestPermissions.to_json())

# convert the object into a dict
bad_permission_setting_error_add_role_request_permissions_dict = bad_permission_setting_error_add_role_request_permissions_instance.to_dict()
# create an instance of BadPermissionSettingErrorAddRoleRequestPermissions from a dict
bad_permission_setting_error_add_role_request_permissions_from_dict = BadPermissionSettingErrorAddRoleRequestPermissions.from_dict(bad_permission_setting_error_add_role_request_permissions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


