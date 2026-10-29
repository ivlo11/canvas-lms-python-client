# BadPermissionSettingErrorUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** | The label for the role. Can only change the label of a custom role that belongs directly to the account. | [optional] 
**permissions** | [**BadPermissionSettingErrorAddRoleRequestPermissions**](BadPermissionSettingErrorAddRoleRequestPermissions.md) |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.bad_permission_setting_error_update_request import BadPermissionSettingErrorUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BadPermissionSettingErrorUpdateRequest from a JSON string
bad_permission_setting_error_update_request_instance = BadPermissionSettingErrorUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(BadPermissionSettingErrorUpdateRequest.to_json())

# convert the object into a dict
bad_permission_setting_error_update_request_dict = bad_permission_setting_error_update_request_instance.to_dict()
# create an instance of BadPermissionSettingErrorUpdateRequest from a dict
bad_permission_setting_error_update_request_from_dict = BadPermissionSettingErrorUpdateRequest.from_dict(bad_permission_setting_error_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


