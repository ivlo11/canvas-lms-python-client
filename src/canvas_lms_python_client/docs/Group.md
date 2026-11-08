# Group



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The ID of the group. | [optional] 
**name** | **str** | The display name of the group. | [optional] 
**description** | **str** | A description of the group. This is plain text. | [optional] 
**is_public** | **bool** | Whether or not the group is public.  Currently only community groups can be made public.  Also, once a group has been set to public, it cannot be changed back to private. | [optional] 
**followed_by_user** | **bool** | Whether or not the current user is following this group. | [optional] 
**join_level** | **str** | How people are allowed to join the group.  For all groups except for community groups, the user must share the group&#39;s parent course or account.  For student organized or community groups, where a user can be a member of as many or few as they want, the applicable levels are &#39;parent_context_auto_join&#39;, &#39;parent_context_request&#39;, and &#39;invitation_only&#39;.  For class groups, where students are divided up and should only be part of one group of the category, this value will always be &#39;invitation_only&#39;, and is not relevant. * If &#39;parent_context_auto_join&#39;, anyone can join and will be automatically accepted. * If &#39;parent_context_request&#39;, anyone  can request to join, which must be approved by a group moderator. * If &#39;invitation_only&#39;, only those how have received an invitation my join the group, by accepting that invitation. | [optional] 
**members_count** | **int** | The number of members currently in the group | [optional] 
**avatar_url** | **str** | The url of the group&#39;s avatar | [optional] 
**context_type** | **str** | The course or account that the group belongs to. The pattern here is that whatever the context_type is, there will be an _id field named after that type. So if instead context_type was &#39;account&#39;, the course_id field would be replaced by an account_id field. | [optional] 
**context_name** | **str** | The course or account name that the group belongs to. | [optional] 
**course_id** | **int** |  | [optional] 
**role** | **str** | Certain types of groups have special role designations. Currently, these include: &#39;communities&#39;, &#39;student_organized&#39;, and &#39;imported&#39;. Regular course/account groups have a role of null. | [optional] 
**group_category_id** | **int** | The ID of the group&#39;s category. | [optional] 
**sis_group_id** | **str** | The SIS ID of the group. Only included if the user has permission to view SIS information. | [optional] 
**sis_import_id** | **int** | The id of the SIS import if created through SIS. Only included if the user has permission to manage SIS information. | [optional] 
**storage_quota_mb** | **int** | the storage quota for the group, in megabytes | [optional] 
**permissions** | **object** | optional: the permissions the user has for the group. returned only for a single group and include[]&#x3D;permissions | [optional] 
**users** | [**List[User]**](User.md) | optional: A list of users that are members in the group. Returned only if include[]&#x3D;users. WARNING: this collection&#39;s size is capped (if there are an extremely large number of users in the group (thousands) not all of them will be returned). If you need to capture all the users in a group with certainty or experiencing slow response consider using the paginated /api/v1/groups/&lt;group_id&gt;/users endpoint. | [optional] 
**non_collaborative** | **bool** | Indicates whether this group category is non-collaborative. A value of true means these group categories rely on the manage_tags permissions and do not have collaborative features | [optional] 
**concluded** | **bool** |  | [optional] 
**created_at** | **str** |  | [optional] 
**has_submission** | **bool** |  | [optional] 
**leader** | **object** |  | [optional] 
**max_membership** | **int** |  | [optional] 
**account_id** | **int** |  | [optional] 
**group_category** | **object** |  | [optional] 
**is_favorite** | **bool** |  | [optional] 
**tabs** | **List[object]** |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.group import Group

# TODO update the JSON string below
json = "{}"
# create an instance of Group from a JSON string
group_instance = Group.from_json(json)
# print the JSON string representation of the object
print(Group.to_json())

# convert the object into a dict
group_dict = group_instance.to_dict()
# create an instance of Group from a dict
group_from_dict = Group.from_dict(group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


