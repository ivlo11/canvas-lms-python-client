# RoleOverridesActivateRoleRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role_id** | **int** | The unique identifier for the role | 
**role** | [**RoleOverridesActivateRoleRequestRole**](RoleOverridesActivateRoleRequestRole.md) |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.role_overrides_activate_role_request import RoleOverridesActivateRoleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RoleOverridesActivateRoleRequest from a JSON string
role_overrides_activate_role_request_instance = RoleOverridesActivateRoleRequest.from_json(json)
# print the JSON string representation of the object
print(RoleOverridesActivateRoleRequest.to_json())

# convert the object into a dict
role_overrides_activate_role_request_dict = role_overrides_activate_role_request_instance.to_dict()
# create an instance of RoleOverridesActivateRoleRequest from a dict
role_overrides_activate_role_request_from_dict = RoleOverridesActivateRoleRequest.from_dict(role_overrides_activate_role_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


