# QuizStatisticsAnswerPointBiserial

A point-biserial construct for a single pre-defined answer in a Multiple-Choice or True/False question.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**answer_id** | **int** | ID of the answer the point biserial is for. | [optional] 
**point_biserial** | **float** | The point biserial value for this answer. Value ranges between -1 and 1. | [optional] 
**correct** | **bool** | Convenience attribute that denotes whether this is the correct answer as opposed to being a distractor. This is mutually exclusive with the &#x60;distractor&#x60; value | [optional] 
**distractor** | **bool** | Convenience attribute that denotes whether this is a distractor answer and not the correct one. This is mutually exclusive with the &#x60;correct&#x60; value | [optional] 

## Example

```python
from canvas_lms_python_client.models.quiz_statistics_answer_point_biserial import QuizStatisticsAnswerPointBiserial

# TODO update the JSON string below
json = "{}"
# create an instance of QuizStatisticsAnswerPointBiserial from a JSON string
quiz_statistics_answer_point_biserial_instance = QuizStatisticsAnswerPointBiserial.from_json(json)
# print the JSON string representation of the object
print(QuizStatisticsAnswerPointBiserial.to_json())

# convert the object into a dict
quiz_statistics_answer_point_biserial_dict = quiz_statistics_answer_point_biserial_instance.to_dict()
# create an instance of QuizStatisticsAnswerPointBiserial from a dict
quiz_statistics_answer_point_biserial_from_dict = QuizStatisticsAnswerPointBiserial.from_dict(quiz_statistics_answer_point_biserial_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


