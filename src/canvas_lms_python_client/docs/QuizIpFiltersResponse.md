# QuizIpFiltersResponse

Paginated `quiz_ip_filters` list response (from the Canvas example response).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quiz_ip_filters** | [**List[QuizIPFilter]**](QuizIPFilter.md) |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.quiz_ip_filters_response import QuizIpFiltersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of QuizIpFiltersResponse from a JSON string
quiz_ip_filters_response_instance = QuizIpFiltersResponse.from_json(json)
# print the JSON string representation of the object
print(QuizIpFiltersResponse.to_json())

# convert the object into a dict
quiz_ip_filters_response_dict = quiz_ip_filters_response_instance.to_dict()
# create an instance of QuizIpFiltersResponse from a dict
quiz_ip_filters_response_from_dict = QuizIpFiltersResponse.from_dict(quiz_ip_filters_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


