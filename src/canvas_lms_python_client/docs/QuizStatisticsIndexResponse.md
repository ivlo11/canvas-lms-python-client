# QuizStatisticsIndexResponse

Paginated `quiz_statistics` list response (from the Canvas example response).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quiz_statistics** | [**List[QuizStatistics]**](QuizStatistics.md) |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.quiz_statistics_index_response import QuizStatisticsIndexResponse

# TODO update the JSON string below
json = "{}"
# create an instance of QuizStatisticsIndexResponse from a JSON string
quiz_statistics_index_response_instance = QuizStatisticsIndexResponse.from_json(json)
# print the JSON string representation of the object
print(QuizStatisticsIndexResponse.to_json())

# convert the object into a dict
quiz_statistics_index_response_dict = quiz_statistics_index_response_instance.to_dict()
# create an instance of QuizStatisticsIndexResponse from a dict
quiz_statistics_index_response_from_dict = QuizStatisticsIndexResponse.from_dict(quiz_statistics_index_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


