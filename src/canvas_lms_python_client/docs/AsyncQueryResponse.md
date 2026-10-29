# AsyncQueryResponse

Response returned when successfully initiating a page views query

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**poll_url** | **str** | URL endpoint to poll for query status updates | 

## Example

```python
from canvas_lms_python_client.models.async_query_response import AsyncQueryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AsyncQueryResponse from a JSON string
async_query_response_instance = AsyncQueryResponse.from_json(json)
# print the JSON string representation of the object
print(AsyncQueryResponse.to_json())

# convert the object into a dict
async_query_response_dict = async_query_response_instance.to_dict()
# create an instance of AsyncQueryResponse from a dict
async_query_response_from_dict = AsyncQueryResponse.from_dict(async_query_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


