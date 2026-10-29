# GroupMembershipsUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workflow_state** | **str** | Currently, the only allowed value is \&quot;accepted\&quot; | [optional] 
**moderator** | **str** |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.group_memberships_update_request import GroupMembershipsUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GroupMembershipsUpdateRequest from a JSON string
group_memberships_update_request_instance = GroupMembershipsUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(GroupMembershipsUpdateRequest.to_json())

# convert the object into a dict
group_memberships_update_request_dict = group_memberships_update_request_instance.to_dict()
# create an instance of GroupMembershipsUpdateRequest from a dict
group_memberships_update_request_from_dict = GroupMembershipsUpdateRequest.from_dict(group_memberships_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


