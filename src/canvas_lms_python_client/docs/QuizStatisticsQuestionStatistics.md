# QuizStatisticsQuestionStatistics

Statistics for submissions made to a specific quiz question.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**responses** | **int** | Number of students who have provided an answer to this question. Blank or empty responses are not counted. | [optional] 
**answers** | [**List[QuizStatisticsAnswerStatistics]**](QuizStatisticsAnswerStatistics.md) | Statistics related to each individual pre-defined answer. | [optional] 
**alpha** | **float** |  | [optional] 
**answered_student_count** | **int** |  | [optional] 
**bottom_student_count** | **int** |  | [optional] 
**correct_bottom_student_count** | **int** |  | [optional] 
**correct_middle_student_count** | **int** |  | [optional] 
**correct_student_count** | **int** |  | [optional] 
**correct_student_ratio** | **float** |  | [optional] 
**correct_top_student_count** | **int** |  | [optional] 
**difficulty_index** | **float** |  | [optional] 
**full_credit** | **int** |  | [optional] 
**graded** | **int** |  | [optional] 
**id** | **str** |  | [optional] 
**incorrect_student_count** | **int** |  | [optional] 
**incorrect_student_ratio** | **float** |  | [optional] 
**middle_student_count** | **int** |  | [optional] 
**point_biserials** | **List[object]** |  | [optional] 
**point_distribution** | **List[object]** |  | [optional] 
**position** | **int** |  | [optional] 
**question_text** | **str** |  | [optional] 
**question_type** | **str** |  | [optional] 
**stdev** | **float** |  | [optional] 
**top_student_count** | **int** |  | [optional] 
**variance** | **float** |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.quiz_statistics_question_statistics import QuizStatisticsQuestionStatistics

# TODO update the JSON string below
json = "{}"
# create an instance of QuizStatisticsQuestionStatistics from a JSON string
quiz_statistics_question_statistics_instance = QuizStatisticsQuestionStatistics.from_json(json)
# print the JSON string representation of the object
print(QuizStatisticsQuestionStatistics.to_json())

# convert the object into a dict
quiz_statistics_question_statistics_dict = quiz_statistics_question_statistics_instance.to_dict()
# create an instance of QuizStatisticsQuestionStatistics from a dict
quiz_statistics_question_statistics_from_dict = QuizStatisticsQuestionStatistics.from_dict(quiz_statistics_question_statistics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


