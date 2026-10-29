# CustomGradebookColumnDataApiUpdateRequestColumnData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **str** | [Required, String] Column content.  Setting this to blank will delete the datum object. | 

## Example

```python
from canvas_lms_python_client.models.custom_gradebook_column_data_api_update_request_column_data import CustomGradebookColumnDataApiUpdateRequestColumnData

# TODO update the JSON string below
json = "{}"
# create an instance of CustomGradebookColumnDataApiUpdateRequestColumnData from a JSON string
custom_gradebook_column_data_api_update_request_column_data_instance = CustomGradebookColumnDataApiUpdateRequestColumnData.from_json(json)
# print the JSON string representation of the object
print(CustomGradebookColumnDataApiUpdateRequestColumnData.to_json())

# convert the object into a dict
custom_gradebook_column_data_api_update_request_column_data_dict = custom_gradebook_column_data_api_update_request_column_data_instance.to_dict()
# create an instance of CustomGradebookColumnDataApiUpdateRequestColumnData from a dict
custom_gradebook_column_data_api_update_request_column_data_from_dict = CustomGradebookColumnDataApiUpdateRequestColumnData.from_dict(custom_gradebook_column_data_api_update_request_column_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


