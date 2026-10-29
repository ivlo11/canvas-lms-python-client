# GroupMembershipsCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** | - The ID of the user for individual membership creation. | [optional] 
**members** | **List[int]** | - Bulk add multiple users to a differentiation tag. | [optional] 
**all_in_group_course** | **bool** | - If true, add all enrolled students from the course. | [optional] 
**exclude_user_ids** | **List[int]** | - An array of user IDs to exclude when using all_in_group_course. | [optional] 

## Example

```python
from canvas_lms_python_client.models.group_memberships_create_request import GroupMembershipsCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GroupMembershipsCreateRequest from a JSON string
group_memberships_create_request_instance = GroupMembershipsCreateRequest.from_json(json)
# print the JSON string representation of the object
print(GroupMembershipsCreateRequest.to_json())

# convert the object into a dict
group_memberships_create_request_dict = group_memberships_create_request_instance.to_dict()
# create an instance of GroupMembershipsCreateRequest from a dict
group_memberships_create_request_from_dict = GroupMembershipsCreateRequest.from_dict(group_memberships_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


