# CustomDataSetDataResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**CustomDataSetDataResponseData**](CustomDataSetDataResponseData.md) |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.custom_data_set_data_response import CustomDataSetDataResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CustomDataSetDataResponse from a JSON string
custom_data_set_data_response_instance = CustomDataSetDataResponse.from_json(json)
# print the JSON string representation of the object
print(CustomDataSetDataResponse.to_json())

# convert the object into a dict
custom_data_set_data_response_dict = custom_data_set_data_response_instance.to_dict()
# create an instance of CustomDataSetDataResponse from a dict
custom_data_set_data_response_from_dict = CustomDataSetDataResponse.from_dict(custom_data_set_data_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


