# Role



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The id of the role | [optional] 
**label** | **str** | The label of the role. | [optional] 
**role** | **str** | The label of the role. (Deprecated alias for &#39;label&#39;) | [optional] 
**base_role_type** | **str** | The role type that is being used as a base for this role. For account-level roles, this is &#39;AccountMembership&#39;. For course-level roles, it is an enrollment type. | [optional] 
**is_account_role** | **bool** | Whether this role applies to account memberships (i.e., not linked to an enrollment in a course). | [optional] 
**account** | [**Account**](Account.md) |  | [optional] 
**workflow_state** | **str** | The state of the role: &#39;active&#39;, &#39;inactive&#39;, or &#39;built_in&#39; | [optional] 
**created_at** | **datetime** | The date and time the role was created. | [optional] 
**last_updated_at** | **datetime** | The date and time the role was last updated. | [optional] 
**permissions** | **object** | A dictionary of permissions keyed by name (see &#39;List assignable permissions&#39; API). | [optional] 
**base_role_type_label** | **str** |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.role import Role

# TODO update the JSON string below
json = "{}"
# create an instance of Role from a JSON string
role_instance = Role.from_json(json)
# print the JSON string representation of the object
print(Role.to_json())

# convert the object into a dict
role_dict = role_instance.to_dict()
# create an instance of Role from a dict
role_from_dict = Role.from_dict(role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


