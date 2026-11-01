# RoleOverridesUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** | The label for the role. Can only change the label of a custom role that belongs directly to the account. | [optional] 
**permissions** | [**RoleOverridesAddRoleRequestPermissions**](RoleOverridesAddRoleRequestPermissions.md) |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.role_overrides_update_request import RoleOverridesUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RoleOverridesUpdateRequest from a JSON string
role_overrides_update_request_instance = RoleOverridesUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(RoleOverridesUpdateRequest.to_json())

# convert the object into a dict
role_overrides_update_request_dict = role_overrides_update_request_instance.to_dict()
# create an instance of RoleOverridesUpdateRequest from a dict
role_overrides_update_request_from_dict = RoleOverridesUpdateRequest.from_dict(role_overrides_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


