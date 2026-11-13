# RoleOverridesAddRoleRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** | Label for the role. | 
**role** | **str** | Deprecated alias for label. | [optional] 
**base_role_type** | **str** | Specifies the role type that will be used as a base for the permissions granted to this role.  Defaults to &#39;AccountMembership&#39; if absent | [optional] 
**permissions** | [**RoleOverridesAddRoleRequestPermissions**](RoleOverridesAddRoleRequestPermissions.md) |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.role_overrides_add_role_request import RoleOverridesAddRoleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RoleOverridesAddRoleRequest from a JSON string
role_overrides_add_role_request_instance = RoleOverridesAddRoleRequest.from_json(json)
# print the JSON string representation of the object
print(RoleOverridesAddRoleRequest.to_json())

# convert the object into a dict
role_overrides_add_role_request_dict = role_overrides_add_role_request_instance.to_dict()
# create an instance of RoleOverridesAddRoleRequest from a dict
role_overrides_add_role_request_from_dict = RoleOverridesAddRoleRequest.from_dict(role_overrides_add_role_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


