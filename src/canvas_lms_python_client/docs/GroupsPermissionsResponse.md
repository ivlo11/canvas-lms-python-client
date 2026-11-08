# GroupsPermissionsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_course_admin_actions** | **bool** |  | [optional] 
**create** | **bool** |  | [optional] 
**create_collaborations** | **bool** |  | [optional] 
**create_conferences** | **bool** |  | [optional] 
**create_forum** | **bool** |  | [optional] 
**delete** | **bool** |  | [optional] 
**join** | **bool** |  | [optional] 
**leave** | **bool** |  | [optional] 
**manage** | **bool** |  | [optional] 
**manage_blarghs** | **bool** |  | [optional] 
**manage_calendar** | **bool** |  | [optional] 
**manage_course_content_add** | **bool** |  | [optional] 
**manage_course_content_delete** | **bool** |  | [optional] 
**manage_course_content_edit** | **bool** |  | [optional] 
**manage_files_add** | **bool** |  | [optional] 
**manage_files_delete** | **bool** |  | [optional] 
**manage_files_edit** | **bool** |  | [optional] 
**manage_students** | **bool** |  | [optional] 
**manage_wiki_create** | **bool** |  | [optional] 
**manage_wiki_delete** | **bool** |  | [optional] 
**manage_wiki_update** | **bool** |  | [optional] 
**moderate_forum** | **bool** |  | [optional] 
**participate** | **bool** |  | [optional] 
**participate_as_student** | **bool** |  | [optional] 
**post_to_forum** | **bool** |  | [optional] 
**read** | **bool** |  | [optional] 
**read_announcements** | **bool** |  | [optional] 
**read_as_admin** | **bool** |  | [optional] 
**read_email_addresses** | **bool** |  | [optional] 
**read_files** | **bool** |  | [optional] 
**read_forum** | **bool** |  | [optional] 
**read_roster** | **bool** |  | [optional] 
**read_sis** | **bool** |  | [optional] 
**send_messages** | **bool** |  | [optional] 
**send_messages_all** | **bool** |  | [optional] 
**update** | **bool** |  | [optional] 
**view_unpublished_items** | **bool** |  | [optional] 
**view_user_logins** | **bool** |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.groups_permissions_response import GroupsPermissionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GroupsPermissionsResponse from a JSON string
groups_permissions_response_instance = GroupsPermissionsResponse.from_json(json)
# print the JSON string representation of the object
print(GroupsPermissionsResponse.to_json())

# convert the object into a dict
groups_permissions_response_dict = groups_permissions_response_instance.to_dict()
# create an instance of GroupsPermissionsResponse from a dict
groups_permissions_response_from_dict = GroupsPermissionsResponse.from_dict(groups_permissions_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


