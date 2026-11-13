# PaceContextsApiIndexResponse

Object response with `pace_contexts`, `total_entries` (from the Canvas `@returns`).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pace_contexts** | [**List[PaceContext]**](PaceContext.md) |  | [optional] 
**total_entries** | **int** |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.pace_contexts_api_index_response import PaceContextsApiIndexResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PaceContextsApiIndexResponse from a JSON string
pace_contexts_api_index_response_instance = PaceContextsApiIndexResponse.from_json(json)
# print the JSON string representation of the object
print(PaceContextsApiIndexResponse.to_json())

# convert the object into a dict
pace_contexts_api_index_response_dict = pace_contexts_api_index_response_instance.to_dict()
# create an instance of PaceContextsApiIndexResponse from a dict
pace_contexts_api_index_response_from_dict = PaceContextsApiIndexResponse.from_dict(pace_contexts_api_index_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


