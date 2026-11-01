# ResultsCreateResponse

Paginated `results` list response (from the Canvas example response).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[Result]**](Result.md) |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.results_create_response import ResultsCreateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ResultsCreateResponse from a JSON string
results_create_response_instance = ResultsCreateResponse.from_json(json)
# print the JSON string representation of the object
print(ResultsCreateResponse.to_json())

# convert the object into a dict
results_create_response_dict = results_create_response_instance.to_dict()
# create an instance of ResultsCreateResponse from a dict
results_create_response_from_dict = ResultsCreateResponse.from_dict(results_create_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


