# AssessmentQuestion


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The ID of the assessment question. | 
**position** | **int** | The order of the question. | [optional] 
**assessment_question_bank_id** | **int** | The ID of the question bank this question belongs to. | [optional] 
**created_at** | **datetime** | The date and time when the assessment question was created. | [optional] 
**question_name** | **str** | The name of the question. | [optional] 
**question_type** | **str** | The type of the question. | [optional] 
**question_text** | **str** | The text of the question. | [optional] 
**points_possible** | **float** | The maximum amount of points possible received for getting this question correct. | [optional] 
**correct_comments** | **str** | The comments to display if the student answers the question correctly. | [optional] 
**incorrect_comments** | **str** | The comments to display if the student answers incorrectly. | [optional] 
**neutral_comments** | **str** | The comments to display regardless of how the student answered. | [optional] 
**correct_comments_html** | **str** | The HTML version of the comments to display if the student answers the question correctly. | [optional] 
**incorrect_comments_html** | **str** | The HTML version of the comments to display if the student answers incorrectly. | [optional] 
**neutral_comments_html** | **str** | The HTML version of the comments to display regardless of how the student answered. | [optional] 
**answers** | [**List[AssessmentQuestionAnswersInner]**](AssessmentQuestionAnswersInner.md) | An array of available answers. Each answer contains id, text, html, comments, comments_html, and weight properties. | [optional] 
**variables** | **List[object]** | Variables for calculated questions. Null for other question types. | [optional] 
**formulas** | **List[object]** | Formulas for calculated questions. Null for other question types. | [optional] 
**answer_tolerance** | **str** | The tolerance for numerical answers. Null for non-numerical question types. | [optional] 
**formula_decimal_places** | **int** | The number of decimal places for formula results. Null for non-calculated question types. | [optional] 
**matches** | **List[object]** | Matching pairs for matching questions. Null for other question types. | [optional] 
**matching_answer_incorrect_matches** | **List[object]** | Incorrect match options for matching questions. Null for other question types. | [optional] 

## Example

```python
from canvas_lms_python_client.models.assessment_question import AssessmentQuestion

# TODO update the JSON string below
json = "{}"
# create an instance of AssessmentQuestion from a JSON string
assessment_question_instance = AssessmentQuestion.from_json(json)
# print the JSON string representation of the object
print(AssessmentQuestion.to_json())

# convert the object into a dict
assessment_question_dict = assessment_question_instance.to_dict()
# create an instance of AssessmentQuestion from a dict
assessment_question_from_dict = AssessmentQuestion.from_dict(assessment_question_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


