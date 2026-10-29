# QuizStatisticsSubmissionStatistics

Generic statistics for all submissions for a quiz.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unique_count** | **int** | The number of students who have taken the quiz. | [optional] 
**score_average** | **float** | The mean of the student submission scores. | [optional] 
**score_high** | **float** | The highest submission score. | [optional] 
**score_low** | **float** | The lowest submission score. | [optional] 
**score_stdev** | **float** | Standard deviation of the submission scores. | [optional] 
**scores** | **object** | A percentile distribution of the student scores, each key is the percentile (ranges between 0 and 100%) while the value is the number of students who received that score. | [optional] 
**correct_count_average** | **float** | The mean of the number of questions answered correctly by each student. | [optional] 
**incorrect_count_average** | **float** | The mean of the number of questions answered incorrectly by each student. | [optional] 
**duration_average** | **float** | The average time spent by students while taking the quiz. | [optional] 

## Example

```python
from canvas_lms_python_client.models.quiz_statistics_submission_statistics import QuizStatisticsSubmissionStatistics

# TODO update the JSON string below
json = "{}"
# create an instance of QuizStatisticsSubmissionStatistics from a JSON string
quiz_statistics_submission_statistics_instance = QuizStatisticsSubmissionStatistics.from_json(json)
# print the JSON string representation of the object
print(QuizStatisticsSubmissionStatistics.to_json())

# convert the object into a dict
quiz_statistics_submission_statistics_dict = quiz_statistics_submission_statistics_instance.to_dict()
# create an instance of QuizStatisticsSubmissionStatistics from a dict
quiz_statistics_submission_statistics_from_dict = QuizStatisticsSubmissionStatistics.from_dict(quiz_statistics_submission_statistics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


