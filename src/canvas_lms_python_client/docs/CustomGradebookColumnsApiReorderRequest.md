# CustomGradebookColumnsApiReorderRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order** | **List[int]** |  | 

## Example

```python
from canvas_lms_python_client.models.custom_gradebook_columns_api_reorder_request import CustomGradebookColumnsApiReorderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CustomGradebookColumnsApiReorderRequest from a JSON string
custom_gradebook_columns_api_reorder_request_instance = CustomGradebookColumnsApiReorderRequest.from_json(json)
# print the JSON string representation of the object
print(CustomGradebookColumnsApiReorderRequest.to_json())

# convert the object into a dict
custom_gradebook_columns_api_reorder_request_dict = custom_gradebook_columns_api_reorder_request_instance.to_dict()
# create an instance of CustomGradebookColumnsApiReorderRequest from a dict
custom_gradebook_columns_api_reorder_request_from_dict = CustomGradebookColumnsApiReorderRequest.from_dict(custom_gradebook_columns_api_reorder_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


