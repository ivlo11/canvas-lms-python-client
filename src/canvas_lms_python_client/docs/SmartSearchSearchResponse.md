# SmartSearchSearchResponse

Object response with `indexing_progress`, `results`, `status` (from the Canvas `@returns`).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**indexing_progress** | **int** |  | [optional] 
**results** | [**List[SearchResult]**](SearchResult.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.smart_search_search_response import SmartSearchSearchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SmartSearchSearchResponse from a JSON string
smart_search_search_response_instance = SmartSearchSearchResponse.from_json(json)
# print the JSON string representation of the object
print(SmartSearchSearchResponse.to_json())

# convert the object into a dict
smart_search_search_response_dict = smart_search_search_response_instance.to_dict()
# create an instance of SmartSearchSearchResponse from a dict
smart_search_search_response_from_dict = SmartSearchSearchResponse.from_dict(smart_search_search_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


