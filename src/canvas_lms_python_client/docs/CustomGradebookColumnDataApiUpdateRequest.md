# CustomGradebookColumnDataApiUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**column_data** | [**CustomGradebookColumnDataApiUpdateRequestColumnData**](CustomGradebookColumnDataApiUpdateRequestColumnData.md) |  | 

## Example

```python
from canvas_lms_python_client.models.custom_gradebook_column_data_api_update_request import CustomGradebookColumnDataApiUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CustomGradebookColumnDataApiUpdateRequest from a JSON string
custom_gradebook_column_data_api_update_request_instance = CustomGradebookColumnDataApiUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(CustomGradebookColumnDataApiUpdateRequest.to_json())

# convert the object into a dict
custom_gradebook_column_data_api_update_request_dict = custom_gradebook_column_data_api_update_request_instance.to_dict()
# create an instance of CustomGradebookColumnDataApiUpdateRequest from a dict
custom_gradebook_column_data_api_update_request_from_dict = CustomGradebookColumnDataApiUpdateRequest.from_dict(custom_gradebook_column_data_api_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


