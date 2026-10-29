# GroupCategoriesUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the group category | [optional] 
**self_signup** | **str** | Allow students to sign up for a group themselves (Course Only). Valid values are: \&quot;enabled\&quot;:: allows students to self sign up for any group in course \&quot;restricted\&quot;:: allows students to self sign up only for groups in the                same section null disallows self sign up | [optional] 
**auto_leader** | **str** | Assigns group leaders automatically when generating and allocating students to groups Valid values are: \&quot;first\&quot;:: the first student to be allocated to a group is the leader \&quot;random\&quot;:: a random student from all members is chosen as the leader | [optional] 
**group_limit** | **int** | Limit the maximum number of users in each group (Course Only). Requires self signup. | [optional] 
**sis_group_category_id** | **str** | The unique SIS identifier. | [optional] 
**create_group_count** | **int** | Create this number of groups (Course Only). | [optional] 
**split_group_count** | [**GroupCategoriesCreateRequestSplitGroupCount**](GroupCategoriesCreateRequestSplitGroupCount.md) |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.group_categories_update_request import GroupCategoriesUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GroupCategoriesUpdateRequest from a JSON string
group_categories_update_request_instance = GroupCategoriesUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(GroupCategoriesUpdateRequest.to_json())

# convert the object into a dict
group_categories_update_request_dict = group_categories_update_request_instance.to_dict()
# create an instance of GroupCategoriesUpdateRequest from a dict
group_categories_update_request_from_dict = GroupCategoriesUpdateRequest.from_dict(group_categories_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


