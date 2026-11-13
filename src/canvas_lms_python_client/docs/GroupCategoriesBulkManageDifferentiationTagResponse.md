# GroupCategoriesBulkManageDifferentiationTagResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **List[object]** |  | [optional] 
**deleted** | **List[object]** |  | [optional] 
**group_category** | [**GroupCategory**](GroupCategory.md) |  | [optional] 
**updated** | **List[object]** |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.group_categories_bulk_manage_differentiation_tag_response import GroupCategoriesBulkManageDifferentiationTagResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GroupCategoriesBulkManageDifferentiationTagResponse from a JSON string
group_categories_bulk_manage_differentiation_tag_response_instance = GroupCategoriesBulkManageDifferentiationTagResponse.from_json(json)
# print the JSON string representation of the object
print(GroupCategoriesBulkManageDifferentiationTagResponse.to_json())

# convert the object into a dict
group_categories_bulk_manage_differentiation_tag_response_dict = group_categories_bulk_manage_differentiation_tag_response_instance.to_dict()
# create an instance of GroupCategoriesBulkManageDifferentiationTagResponse from a dict
group_categories_bulk_manage_differentiation_tag_response_from_dict = GroupCategoriesBulkManageDifferentiationTagResponse.from_dict(group_categories_bulk_manage_differentiation_tag_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


