# QuizStatisticsLinks

Links to media related to QuizStatistics.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quiz** | **str** | HTTP/HTTPS API URL to the quiz this statistics describe. | [optional] 

## Example

```python
from canvas_lms_python_client.models.quiz_statistics_links import QuizStatisticsLinks

# TODO update the JSON string below
json = "{}"
# create an instance of QuizStatisticsLinks from a JSON string
quiz_statistics_links_instance = QuizStatisticsLinks.from_json(json)
# print the JSON string representation of the object
print(QuizStatisticsLinks.to_json())

# convert the object into a dict
quiz_statistics_links_dict = quiz_statistics_links_instance.to_dict()
# create an instance of QuizStatisticsLinks from a dict
quiz_statistics_links_from_dict = QuizStatisticsLinks.from_dict(quiz_statistics_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


