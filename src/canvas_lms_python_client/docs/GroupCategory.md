# GroupCategory



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The ID of the group category. | [optional] 
**name** | **str** | The display name of the group category. | [optional] 
**role** | **str** | Certain types of group categories have special role designations. Currently, these include: &#39;communities&#39;, &#39;student_organized&#39;, and &#39;imported&#39;. Regular course/account group categories have a role of null. | [optional] 
**self_signup** | **str** | If the group category allows users to join a group themselves, thought they may only be a member of one group per group category at a time. Values include &#39;restricted&#39;, &#39;enabled&#39;, and null &#39;enabled&#39; allows students to assign themselves to a group &#39;restricted&#39; restricts them to only joining a group in their section null disallows students from joining groups | [optional] 
**auto_leader** | **str** | Gives instructors the ability to automatically have group leaders assigned.  Values include &#39;random&#39;, &#39;first&#39;, and null; &#39;random&#39; picks a student from the group at random as the leader, &#39;first&#39; sets the first student to be assigned to the group as the leader | [optional] 
**context_type** | **str** | The course or account that the category group belongs to. The pattern here is that whatever the context_type is, there will be an _id field named after that type. So if instead context_type was &#39;Course&#39;, the course_id field would be replaced by an course_id field. | [optional] 
**account_id** | **int** |  | [optional] 
**group_limit** | **int** | If self-signup is enabled, group_limit can be set to cap the number of users in each group. If null, there is no limit. | [optional] 
**sis_group_category_id** | **str** | The SIS identifier for the group category. This field is only included if the user has permission to manage or view SIS information. | [optional] 
**sis_import_id** | **int** | The unique identifier for the SIS import. This field is only included if the user has permission to manage SIS information. | [optional] 
**progress** | [**Progress**](Progress.md) |  | [optional] 
**non_collaborative** | **bool** | Indicates whether this group category is non-collaborative. A value of true means these group categories rely on the manage_tags permissions and do not have collaborative features | [optional] 

## Example

```python
from canvas_lms_python_client.models.group_category import GroupCategory

# TODO update the JSON string below
json = "{}"
# create an instance of GroupCategory from a JSON string
group_category_instance = GroupCategory.from_json(json)
# print the JSON string representation of the object
print(GroupCategory.to_json())

# convert the object into a dict
group_category_dict = group_category_instance.to_dict()
# create an instance of GroupCategory from a dict
group_category_from_dict = GroupCategory.from_dict(group_category_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


