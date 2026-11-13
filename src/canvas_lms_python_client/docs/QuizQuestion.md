# QuizQuestion


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The ID of the quiz question. | 
**quiz_id** | **int** | The ID of the Quiz the question belongs to. | 
**assessment_question_bank_id** | **int** | The ID of the assessment question bank this question belongs to. If assessment_question_bank_id has been enabled by SiteAdmin. | [optional] 
**created_at** | **datetime** | The date and time when the quiz question was created. | [optional] 
**position** | **int** | The order in which the question will be retrieved and displayed. | [optional] 
**question_name** | **str** | The name of the question. | [optional] 
**question_type** | **str** | The type of the question. | [optional] 
**question_text** | **str** | The text of the question. | [optional] 
**points_possible** | **float** | The maximum amount of points possible received for getting this question correct. | [optional] 
**correct_comments** | **str** | The comments to display if the student answers the question correctly. | [optional] 
**incorrect_comments** | **str** | The comments to display if the student answers incorrectly. | [optional] 
**neutral_comments** | **str** | The comments to display regardless of how the student answered. | [optional] 
**answers** | [**List[Answer]**](Answer.md) | An array of available answers to display to the student. | [optional] 
**answer_tolerance** | **object** |  | [optional] 
**assessment_question_id** | **int** |  | [optional] 
**correct_comments_html** | **str** |  | [optional] 
**formula_decimal_places** | **object** |  | [optional] 
**formulas** | **object** |  | [optional] 
**incorrect_comments_html** | **str** |  | [optional] 
**matches** | **object** |  | [optional] 
**matching_answer_incorrect_matches** | **object** |  | [optional] 
**neutral_comments_html** | **str** |  | [optional] 
**quiz_group_id** | **int** |  | [optional] 
**variables** | **object** |  | [optional] 
**assessment_question** | **object** |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.quiz_question import QuizQuestion

# TODO update the JSON string below
json = "{}"
# create an instance of QuizQuestion from a JSON string
quiz_question_instance = QuizQuestion.from_json(json)
# print the JSON string representation of the object
print(QuizQuestion.to_json())

# convert the object into a dict
quiz_question_dict = quiz_question_instance.to_dict()
# create an instance of QuizQuestion from a dict
quiz_question_from_dict = QuizQuestion.from_dict(quiz_question_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


