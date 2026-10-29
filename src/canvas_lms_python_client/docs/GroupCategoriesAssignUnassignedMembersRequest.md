# GroupCategoriesAssignUnassignedMembersRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sync** | **bool** | The assigning is done asynchronously by default. If you would like to override this and have the assigning done synchronously, set this value to true. | [optional] 

## Example

```python
from canvas_lms_python_client.models.group_categories_assign_unassigned_members_request import GroupCategoriesAssignUnassignedMembersRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GroupCategoriesAssignUnassignedMembersRequest from a JSON string
group_categories_assign_unassigned_members_request_instance = GroupCategoriesAssignUnassignedMembersRequest.from_json(json)
# print the JSON string representation of the object
print(GroupCategoriesAssignUnassignedMembersRequest.to_json())

# convert the object into a dict
group_categories_assign_unassigned_members_request_dict = group_categories_assign_unassigned_members_request_instance.to_dict()
# create an instance of GroupCategoriesAssignUnassignedMembersRequest from a dict
group_categories_assign_unassigned_members_request_from_dict = GroupCategoriesAssignUnassignedMembersRequest.from_dict(group_categories_assign_unassigned_members_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


