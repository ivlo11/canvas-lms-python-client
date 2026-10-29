# GroupsUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the group | [optional] 
**description** | **str** | A description of the group | [optional] 
**is_public** | **bool** | Whether the group is public (applies only to community groups). Currently you cannot set a group back to private once it has been made public. | [optional] 
**join_level** | **str** |  | [optional] 
**avatar_id** | **int** | The id of the attachment previously uploaded to the group that you would like to use as the avatar image for this group. | [optional] 
**storage_quota_mb** | **int** | The allowed file storage for the group, in megabytes. This parameter is ignored if the caller does not have the manage_storage_quotas permission. | [optional] 
**members** | **List[str]** | An array of user ids for users you would like in the group. Users not in the group will be sent invitations. Existing group members who aren&#39;t in the list will be removed from the group. | [optional] 
**sis_group_id** | **str** | The sis ID of the group. Must have manage_sis permission to set. | [optional] 
**override_sis_stickiness** | **bool** | Default is true. If false, any fields containing “sticky” changes will not be updated. See SIS CSV Format documentation for information on which fields can have SIS stickiness | [optional] 

## Example

```python
from canvas_lms_python_client.models.groups_update_request import GroupsUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GroupsUpdateRequest from a JSON string
groups_update_request_instance = GroupsUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(GroupsUpdateRequest.to_json())

# convert the object into a dict
groups_update_request_dict = groups_update_request_instance.to_dict()
# create an instance of GroupsUpdateRequest from a dict
groups_update_request_from_dict = GroupsUpdateRequest.from_dict(groups_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


