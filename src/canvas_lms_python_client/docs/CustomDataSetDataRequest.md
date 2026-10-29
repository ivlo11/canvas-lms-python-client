# CustomDataSetDataRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ns** | **str** | The namespace under which to store the data.  This should be something other Canvas API apps aren&#39;t likely to use, such as a reverse DNS for your organization. | 
**data** | **str** | The data you want to store for the user, at the specified scope.  If the data is composed of (possibly nested) JSON objects, scopes will be generated for the (nested) keys (see examples). | 

## Example

```python
from canvas_lms_python_client.models.custom_data_set_data_request import CustomDataSetDataRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CustomDataSetDataRequest from a JSON string
custom_data_set_data_request_instance = CustomDataSetDataRequest.from_json(json)
# print the JSON string representation of the object
print(CustomDataSetDataRequest.to_json())

# convert the object into a dict
custom_data_set_data_request_dict = custom_data_set_data_request_instance.to_dict()
# create an instance of CustomDataSetDataRequest from a dict
custom_data_set_data_request_from_dict = CustomDataSetDataRequest.from_dict(custom_data_set_data_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


