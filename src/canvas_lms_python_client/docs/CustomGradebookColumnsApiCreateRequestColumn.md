# CustomGradebookColumnsApiCreateRequestColumn


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | [Required, String] | 
**position** | **int** | [Integer] The position of the column relative to other custom columns | [optional] 
**hidden** | **bool** | [Boolean] Hidden columns are not displayed in the gradebook | [optional] 
**teacher_notes** | **bool** | [Boolean] Set this if the column is created by a teacher.  The gradebook only supports one teacher_notes column. | [optional] 
**read_only** | **bool** | [Boolean] Set this to prevent the column from being editable in the gradebook ui | [optional] 

## Example

```python
from canvas_lms_python_client.models.custom_gradebook_columns_api_create_request_column import CustomGradebookColumnsApiCreateRequestColumn

# TODO update the JSON string below
json = "{}"
# create an instance of CustomGradebookColumnsApiCreateRequestColumn from a JSON string
custom_gradebook_columns_api_create_request_column_instance = CustomGradebookColumnsApiCreateRequestColumn.from_json(json)
# print the JSON string representation of the object
print(CustomGradebookColumnsApiCreateRequestColumn.to_json())

# convert the object into a dict
custom_gradebook_columns_api_create_request_column_dict = custom_gradebook_columns_api_create_request_column_instance.to_dict()
# create an instance of CustomGradebookColumnsApiCreateRequestColumn from a dict
custom_gradebook_columns_api_create_request_column_from_dict = CustomGradebookColumnsApiCreateRequestColumn.from_dict(custom_gradebook_columns_api_create_request_column_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


