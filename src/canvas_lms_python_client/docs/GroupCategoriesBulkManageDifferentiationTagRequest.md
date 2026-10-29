# GroupCategoriesBulkManageDifferentiationTagRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operations** | **str** | A hash containing arrays of create/update/delete operations: {   \&quot;create\&quot;: [     { \&quot;name\&quot;: \&quot;New Group A\&quot; },     { \&quot;name\&quot;: \&quot;New Group B\&quot; }   ],   \&quot;update\&quot;: [     { \&quot;id\&quot;: 123, \&quot;name\&quot;: \&quot;Updated Group Name A\&quot; },     { \&quot;id\&quot;: 456, \&quot;name\&quot;: \&quot;Updated Group Name B\&quot; }   ],   \&quot;delete\&quot;: [     { \&quot;id\&quot;: 789 },     { \&quot;id\&quot;: 101 }   ] } | 
**group_category** | **str** | Attributes for the GroupCategory. May include:   - id [Optional, Integer]: The ID of an existing GroupCategory.   - name [Optional, String]: A new name for the GroupCategory. If provided with an ID, the category name will be updated. | 

## Example

```python
from canvas_lms_python_client.models.group_categories_bulk_manage_differentiation_tag_request import GroupCategoriesBulkManageDifferentiationTagRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GroupCategoriesBulkManageDifferentiationTagRequest from a JSON string
group_categories_bulk_manage_differentiation_tag_request_instance = GroupCategoriesBulkManageDifferentiationTagRequest.from_json(json)
# print the JSON string representation of the object
print(GroupCategoriesBulkManageDifferentiationTagRequest.to_json())

# convert the object into a dict
group_categories_bulk_manage_differentiation_tag_request_dict = group_categories_bulk_manage_differentiation_tag_request_instance.to_dict()
# create an instance of GroupCategoriesBulkManageDifferentiationTagRequest from a dict
group_categories_bulk_manage_differentiation_tag_request_from_dict = GroupCategoriesBulkManageDifferentiationTagRequest.from_dict(group_categories_bulk_manage_differentiation_tag_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


