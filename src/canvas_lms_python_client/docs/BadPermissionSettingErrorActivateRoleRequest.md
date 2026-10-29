# BadPermissionSettingErrorActivateRoleRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role_id** | **int** | The unique identifier for the role | 
**role** | [**BadPermissionSettingErrorActivateRoleRequestRole**](BadPermissionSettingErrorActivateRoleRequestRole.md) |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.bad_permission_setting_error_activate_role_request import BadPermissionSettingErrorActivateRoleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BadPermissionSettingErrorActivateRoleRequest from a JSON string
bad_permission_setting_error_activate_role_request_instance = BadPermissionSettingErrorActivateRoleRequest.from_json(json)
# print the JSON string representation of the object
print(BadPermissionSettingErrorActivateRoleRequest.to_json())

# convert the object into a dict
bad_permission_setting_error_activate_role_request_dict = bad_permission_setting_error_activate_role_request_instance.to_dict()
# create an instance of BadPermissionSettingErrorActivateRoleRequest from a dict
bad_permission_setting_error_activate_role_request_from_dict = BadPermissionSettingErrorActivateRoleRequest.from_dict(bad_permission_setting_error_activate_role_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


