# AsyncQueryResultsResponse

File download response containing page views query results

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **bytes** | The query results data in the requested format (CSV or JSON) | [optional] 
**filename** | **str** | Suggested filename for the downloaded results | [optional] 
**content_type** | **str** | MIME type of the response content | [optional] 
**content_encoding** | **str** | Content encoding if the response is compressed | [optional] 

## Example

```python
from canvas_lms_python_client.models.async_query_results_response import AsyncQueryResultsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AsyncQueryResultsResponse from a JSON string
async_query_results_response_instance = AsyncQueryResultsResponse.from_json(json)
# print the JSON string representation of the object
print(AsyncQueryResultsResponse.to_json())

# convert the object into a dict
async_query_results_response_dict = async_query_results_response_instance.to_dict()
# create an instance of AsyncQueryResultsResponse from a dict
async_query_results_response_from_dict = AsyncQueryResultsResponse.from_dict(async_query_results_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


