# GroupsInviteRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invitees** | **List[str]** | An array of email addresses to be sent invitations. | 

## Example

```python
from canvas_lms_python_client.models.groups_invite_request import GroupsInviteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GroupsInviteRequest from a JSON string
groups_invite_request_instance = GroupsInviteRequest.from_json(json)
# print the JSON string representation of the object
print(GroupsInviteRequest.to_json())

# convert the object into a dict
groups_invite_request_dict = groups_invite_request_instance.to_dict()
# create an instance of GroupsInviteRequest from a dict
groups_invite_request_from_dict = GroupsInviteRequest.from_dict(groups_invite_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


