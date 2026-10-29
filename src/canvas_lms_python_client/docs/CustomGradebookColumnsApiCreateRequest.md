# CustomGradebookColumnsApiCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**column** | [**CustomGradebookColumnsApiCreateRequestColumn**](CustomGradebookColumnsApiCreateRequestColumn.md) |  | 

## Example

```python
from canvas_lms_python_client.models.custom_gradebook_columns_api_create_request import CustomGradebookColumnsApiCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CustomGradebookColumnsApiCreateRequest from a JSON string
custom_gradebook_columns_api_create_request_instance = CustomGradebookColumnsApiCreateRequest.from_json(json)
# print the JSON string representation of the object
print(CustomGradebookColumnsApiCreateRequest.to_json())

# convert the object into a dict
custom_gradebook_columns_api_create_request_dict = custom_gradebook_columns_api_create_request_instance.to_dict()
# create an instance of CustomGradebookColumnsApiCreateRequest from a dict
custom_gradebook_columns_api_create_request_from_dict = CustomGradebookColumnsApiCreateRequest.from_dict(custom_gradebook_columns_api_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


