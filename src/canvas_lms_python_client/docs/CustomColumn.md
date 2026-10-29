# CustomColumn



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The ID of the custom gradebook column | [optional] 
**teacher_notes** | **bool** | When true, this column&#39;s visibility will be toggled in the Gradebook when a user selects to show or hide notes | [optional] 
**title** | **str** | header text | [optional] 
**position** | **int** | column order | [optional] 
**hidden** | **bool** | won&#39;t be displayed if hidden is true | [optional] 
**read_only** | **bool** | won&#39;t be editable in the gradebook UI | [optional] 

## Example

```python
from canvas_lms_python_client.models.custom_column import CustomColumn

# TODO update the JSON string below
json = "{}"
# create an instance of CustomColumn from a JSON string
custom_column_instance = CustomColumn.from_json(json)
# print the JSON string representation of the object
print(CustomColumn.to_json())

# convert the object into a dict
custom_column_dict = custom_column_instance.to_dict()
# create an instance of CustomColumn from a dict
custom_column_from_dict = CustomColumn.from_dict(custom_column_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


