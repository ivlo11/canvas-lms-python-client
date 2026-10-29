# BadPermissionSettingErrorAddRoleRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** | Label for the role. | 
**role** | **str** | Deprecated alias for label. | [optional] 
**base_role_type** | **str** | Specifies the role type that will be used as a base for the permissions granted to this role.  Defaults to &#39;AccountMembership&#39; if absent | [optional] 
**permissions** | [**BadPermissionSettingErrorAddRoleRequestPermissions**](BadPermissionSettingErrorAddRoleRequestPermissions.md) |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.bad_permission_setting_error_add_role_request import BadPermissionSettingErrorAddRoleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BadPermissionSettingErrorAddRoleRequest from a JSON string
bad_permission_setting_error_add_role_request_instance = BadPermissionSettingErrorAddRoleRequest.from_json(json)
# print the JSON string representation of the object
print(BadPermissionSettingErrorAddRoleRequest.to_json())

# convert the object into a dict
bad_permission_setting_error_add_role_request_dict = bad_permission_setting_error_add_role_request_instance.to_dict()
# create an instance of BadPermissionSettingErrorAddRoleRequest from a dict
bad_permission_setting_error_add_role_request_from_dict = BadPermissionSettingErrorAddRoleRequest.from_dict(bad_permission_setting_error_add_role_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


