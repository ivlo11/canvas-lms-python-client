# CustomGradebookColumnDataApiBulkUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**column_data** | **List[List[str]]** | Column content. Setting this to an empty string will delete the data object. | 

## Example

```python
from canvas_lms_python_client.models.custom_gradebook_column_data_api_bulk_update_request import CustomGradebookColumnDataApiBulkUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CustomGradebookColumnDataApiBulkUpdateRequest from a JSON string
custom_gradebook_column_data_api_bulk_update_request_instance = CustomGradebookColumnDataApiBulkUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(CustomGradebookColumnDataApiBulkUpdateRequest.to_json())

# convert the object into a dict
custom_gradebook_column_data_api_bulk_update_request_dict = custom_gradebook_column_data_api_bulk_update_request_instance.to_dict()
# create an instance of CustomGradebookColumnDataApiBulkUpdateRequest from a dict
custom_gradebook_column_data_api_bulk_update_request_from_dict = CustomGradebookColumnDataApiBulkUpdateRequest.from_dict(custom_gradebook_column_data_api_bulk_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


