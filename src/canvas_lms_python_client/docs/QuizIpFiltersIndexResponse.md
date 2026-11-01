# QuizIpFiltersIndexResponse

Paginated `quiz_ip_filters` list response (from the Canvas example response).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quiz_ip_filters** | [**List[QuizIPFilter]**](QuizIPFilter.md) |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.quiz_ip_filters_index_response import QuizIpFiltersIndexResponse

# TODO update the JSON string below
json = "{}"
# create an instance of QuizIpFiltersIndexResponse from a JSON string
quiz_ip_filters_index_response_instance = QuizIpFiltersIndexResponse.from_json(json)
# print the JSON string representation of the object
print(QuizIpFiltersIndexResponse.to_json())

# convert the object into a dict
quiz_ip_filters_index_response_dict = quiz_ip_filters_index_response_instance.to_dict()
# create an instance of QuizIpFiltersIndexResponse from a dict
quiz_ip_filters_index_response_from_dict = QuizIpFiltersIndexResponse.from_dict(quiz_ip_filters_index_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


