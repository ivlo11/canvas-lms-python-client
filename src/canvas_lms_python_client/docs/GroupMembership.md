# GroupMembership



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The id of the membership object | [optional] 
**group_id** | **int** | The id of the group object to which the membership belongs | [optional] 
**user_id** | **int** | The id of the user object to which the membership belongs | [optional] 
**workflow_state** | **str** | The current state of the membership. Current possible values are &#39;accepted&#39;, &#39;invited&#39;, and &#39;requested&#39; | [optional] 
**moderator** | **bool** | Whether or not the user is a moderator of the group (the must also be an active member of the group to moderate) | [optional] 
**just_created** | **bool** | optional: whether or not the record was just created on a create call (POST), i.e. was the user just added to the group, or was the user already a member | [optional] 
**sis_import_id** | **int** | The id of the SIS import if created through SIS. Only included if the user has permission to manage SIS information. | [optional] 
**created_at** | **str** |  | [optional] 
**sis_group_id** | **object** |  | [optional] 
**invalid_user_ids** | **List[int]** |  | [optional] 
**membership_errors** | **List[object]** |  | [optional] 
**message** | **str** |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.group_membership import GroupMembership

# TODO update the JSON string below
json = "{}"
# create an instance of GroupMembership from a JSON string
group_membership_instance = GroupMembership.from_json(json)
# print the JSON string representation of the object
print(GroupMembership.to_json())

# convert the object into a dict
group_membership_dict = group_membership_instance.to_dict()
# create an instance of GroupMembership from a dict
group_membership_from_dict = GroupMembership.from_dict(group_membership_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


