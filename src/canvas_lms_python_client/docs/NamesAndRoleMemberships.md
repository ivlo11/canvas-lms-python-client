# NamesAndRoleMemberships



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Invocation URL | [optional] 
**context** | [**NamesAndRoleContext**](NamesAndRoleContext.md) |  | [optional] 
**members** | [**List[NamesAndRoleMembership]**](NamesAndRoleMembership.md) | A list of NamesAndRoleMembership | [optional] 

## Example

```python
from canvas_lms_python_client.models.names_and_role_memberships import NamesAndRoleMemberships

# TODO update the JSON string below
json = "{}"
# create an instance of NamesAndRoleMemberships from a JSON string
names_and_role_memberships_instance = NamesAndRoleMemberships.from_json(json)
# print the JSON string representation of the object
print(NamesAndRoleMemberships.to_json())

# convert the object into a dict
names_and_role_memberships_dict = names_and_role_memberships_instance.to_dict()
# create an instance of NamesAndRoleMemberships from a dict
names_and_role_memberships_from_dict = NamesAndRoleMemberships.from_dict(names_and_role_memberships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


