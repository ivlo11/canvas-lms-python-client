# GroupsCreateForGroupCategoriesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the group | [optional] 
**description** | **str** | A description of the group | [optional] 
**is_public** | **bool** | whether the group is public (applies only to community groups) | [optional] 
**join_level** | **str** |  | [optional] 
**storage_quota_mb** | **int** | The allowed file storage for the group, in megabytes. This parameter is ignored if the caller does not have the manage_storage_quotas permission. | [optional] 
**sis_group_id** | **str** | The sis ID of the group. Must have manage_sis permission to set. | [optional] 

## Example

```python
from canvas_lms_python_client.models.groups_create_for_group_categories_request import GroupsCreateForGroupCategoriesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GroupsCreateForGroupCategoriesRequest from a JSON string
groups_create_for_group_categories_request_instance = GroupsCreateForGroupCategoriesRequest.from_json(json)
# print the JSON string representation of the object
print(GroupsCreateForGroupCategoriesRequest.to_json())

# convert the object into a dict
groups_create_for_group_categories_request_dict = groups_create_for_group_categories_request_instance.to_dict()
# create an instance of GroupsCreateForGroupCategoriesRequest from a dict
groups_create_for_group_categories_request_from_dict = GroupsCreateForGroupCategoriesRequest.from_dict(groups_create_for_group_categories_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


