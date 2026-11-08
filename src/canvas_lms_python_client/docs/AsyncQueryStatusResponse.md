# AsyncQueryStatusResponse

Response containing the current status of a page views query

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query_id** | **UUID** | The UUID of the query being polled | 
**status** | **str** | Current processing status of the query | 
**format** | **str** | The format that results will be returned in | 
**results_url** | **str** | URL to retrieve query results. Only present when status is &#39;finished&#39; | [optional] 
**error_code** | **str** | Error code indicating the reason for query failure, if applicable | [optional] 
**warnings** | **List[object]** |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.async_query_status_response import AsyncQueryStatusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AsyncQueryStatusResponse from a JSON string
async_query_status_response_instance = AsyncQueryStatusResponse.from_json(json)
# print the JSON string representation of the object
print(AsyncQueryStatusResponse.to_json())

# convert the object into a dict
async_query_status_response_dict = async_query_status_response_instance.to_dict()
# create an instance of AsyncQueryStatusResponse from a dict
async_query_status_response_from_dict = AsyncQueryStatusResponse.from_dict(async_query_status_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


