# RolePermissions



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Whether the role has the permission | [optional] 
**locked** | **bool** | Whether the permission is locked by this role | [optional] 
**applies_to_self** | **bool** | Whether the permission applies to the account this role is in. Only present if enabled is true | [optional] 
**applies_to_descendants** | **bool** | Whether the permission cascades down to sub accounts of the account this role is in. Only present if enabled is true | [optional] 
**readonly** | **bool** | Whether the permission can be modified in this role (i.e. whether the permission is locked by an upstream role). | [optional] 
**explicit** | **bool** | Whether the value of enabled is specified explicitly by this role, or inherited from an upstream role. | [optional] 
**prior_default** | **bool** | The value that would have been inherited from upstream if the role had not explicitly set a value. Only present if explicit is true. | [optional] 

## Example

```python
from canvas_lms_python_client.models.role_permissions import RolePermissions

# TODO update the JSON string below
json = "{}"
# create an instance of RolePermissions from a JSON string
role_permissions_instance = RolePermissions.from_json(json)
# print the JSON string representation of the object
print(RolePermissions.to_json())

# convert the object into a dict
role_permissions_dict = role_permissions_instance.to_dict()
# create an instance of RolePermissions from a dict
role_permissions_from_dict = RolePermissions.from_dict(role_permissions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


