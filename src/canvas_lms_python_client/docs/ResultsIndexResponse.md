# ResultsIndexResponse

Object response with `results`, `meta` (from the Canvas `@returns`).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[Result]**](Result.md) |  | [optional] 
**meta** | **object** |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.results_index_response import ResultsIndexResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ResultsIndexResponse from a JSON string
results_index_response_instance = ResultsIndexResponse.from_json(json)
# print the JSON string representation of the object
print(ResultsIndexResponse.to_json())

# convert the object into a dict
results_index_response_dict = results_index_response_instance.to_dict()
# create an instance of ResultsIndexResponse from a dict
results_index_response_from_dict = ResultsIndexResponse.from_dict(results_index_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


