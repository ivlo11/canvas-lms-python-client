# QuizStatisticsAnswerStatistics

Statistics for a specific pre-defined answer in a Multiple-Choice or True/False quiz question.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**QuizStatisticsAnswerStatisticsId**](QuizStatisticsAnswerStatisticsId.md) |  | [optional] 
**text** | **str** | The text attached to the answer. | [optional] 
**weight** | **int** | An integer to determine correctness of the answer. Incorrect answers should be 0, correct answers should 100 | [optional] 
**responses** | **int** | Number of students who have chosen this answer. | [optional] 
**correct** | **bool** |  | [optional] 
**full_credit** | **bool** |  | [optional] 
**score** | **float** |  | [optional] 
**user_ids** | **List[int]** |  | [optional] 
**user_names** | **List[str]** |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.quiz_statistics_answer_statistics import QuizStatisticsAnswerStatistics

# TODO update the JSON string below
json = "{}"
# create an instance of QuizStatisticsAnswerStatistics from a JSON string
quiz_statistics_answer_statistics_instance = QuizStatisticsAnswerStatistics.from_json(json)
# print the JSON string representation of the object
print(QuizStatisticsAnswerStatistics.to_json())

# convert the object into a dict
quiz_statistics_answer_statistics_dict = quiz_statistics_answer_statistics_instance.to_dict()
# create an instance of QuizStatisticsAnswerStatistics from a dict
quiz_statistics_answer_statistics_from_dict = QuizStatisticsAnswerStatistics.from_dict(quiz_statistics_answer_statistics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


