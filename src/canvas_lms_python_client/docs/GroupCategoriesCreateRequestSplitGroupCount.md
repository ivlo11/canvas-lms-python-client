# GroupCategoriesCreateRequestSplitGroupCount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deprecated** | **str** | Create this number of groups, and evenly distribute students among them. not allowed with \&quot;enable_self_signup\&quot;. because the group assignment happens synchronously, it&#39;s recommended that you instead use the assign_unassigned_members endpoint. (Course Only) | [optional] 

## Example

```python
from canvas_lms_python_client.models.group_categories_create_request_split_group_count import GroupCategoriesCreateRequestSplitGroupCount

# TODO update the JSON string below
json = "{}"
# create an instance of GroupCategoriesCreateRequestSplitGroupCount from a JSON string
group_categories_create_request_split_group_count_instance = GroupCategoriesCreateRequestSplitGroupCount.from_json(json)
# print the JSON string representation of the object
print(GroupCategoriesCreateRequestSplitGroupCount.to_json())

# convert the object into a dict
group_categories_create_request_split_group_count_dict = group_categories_create_request_split_group_count_instance.to_dict()
# create an instance of GroupCategoriesCreateRequestSplitGroupCount from a dict
group_categories_create_request_split_group_count_from_dict = GroupCategoriesCreateRequestSplitGroupCount.from_dict(group_categories_create_request_split_group_count_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


