# QuizStatisticsResponse

Paginated `quiz_statistics` list response (from the Canvas example response).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quiz_statistics** | [**List[QuizStatistics]**](QuizStatistics.md) |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.quiz_statistics_response import QuizStatisticsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of QuizStatisticsResponse from a JSON string
quiz_statistics_response_instance = QuizStatisticsResponse.from_json(json)
# print the JSON string representation of the object
print(QuizStatisticsResponse.to_json())

# convert the object into a dict
quiz_statistics_response_dict = quiz_statistics_response_instance.to_dict()
# create an instance of QuizStatisticsResponse from a dict
quiz_statistics_response_from_dict = QuizStatisticsResponse.from_dict(quiz_statistics_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


