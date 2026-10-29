# AsyncApiErrorResponse

Error response structure returned by the API when validation or processing failures occur

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | **List[str]** | Array of error messages describing what went wrong with the request | [optional] 

## Example

```python
from canvas_lms_python_client.models.async_api_error_response import AsyncApiErrorResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AsyncApiErrorResponse from a JSON string
async_api_error_response_instance = AsyncApiErrorResponse.from_json(json)
# print the JSON string representation of the object
print(AsyncApiErrorResponse.to_json())

# convert the object into a dict
async_api_error_response_dict = async_api_error_response_instance.to_dict()
# create an instance of AsyncApiErrorResponse from a dict
async_api_error_response_from_dict = AsyncApiErrorResponse.from_dict(async_api_error_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


