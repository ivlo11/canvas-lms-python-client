# QuizStatistics


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The ID of the quiz statistics report. | 
**quiz_id** | **int** | The ID of the Quiz the statistics report is for.  NOTE: AVAILABLE ONLY IN NON-JSON-API REQUESTS. | 
**multiple_attempts_exist** | **bool** | Whether there are any students that have made mutliple submissions for this quiz. | [optional] 
**includes_all_versions** | **bool** | In the presence of multiple attempts, this field describes whether the statistics describe all the submission attempts and not only the latest ones. | [optional] 
**generated_at** | **datetime** | The time at which the statistics were generated, which is usually after the occurrence of a quiz event, like a student submitting it. | [optional] 
**url** | **str** | The API HTTP/HTTPS URL to this quiz statistics. | [optional] 
**html_url** | **str** | The HTTP/HTTPS URL to the page where the statistics can be seen visually. | [optional] 
**question_statistics** | [**QuizStatisticsQuestionStatistics**](QuizStatisticsQuestionStatistics.md) |  | [optional] 
**submission_statistics** | [**QuizStatisticsSubmissionStatistics**](QuizStatisticsSubmissionStatistics.md) |  | [optional] 
**links** | [**QuizStatisticsLinks**](QuizStatisticsLinks.md) |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.quiz_statistics import QuizStatistics

# TODO update the JSON string below
json = "{}"
# create an instance of QuizStatistics from a JSON string
quiz_statistics_instance = QuizStatistics.from_json(json)
# print the JSON string representation of the object
print(QuizStatistics.to_json())

# convert the object into a dict
quiz_statistics_dict = quiz_statistics_instance.to_dict()
# create an instance of QuizStatistics from a dict
quiz_statistics_from_dict = QuizStatistics.from_dict(quiz_statistics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


