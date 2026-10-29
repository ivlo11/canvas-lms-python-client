# AssessmentQuestionAnswersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The ID of the answer. | [optional] 
**text** | **str** | The text of the answer. | [optional] 
**html** | **str** | The HTML version of the answer text. | [optional] 
**comments** | **str** | Comments for this specific answer. | [optional] 
**comments_html** | **str** | The HTML version of the comments for this answer. | [optional] 
**weight** | **float** | The weight of the answer. 100 indicates a correct answer, 0 indicates incorrect. | [optional] 

## Example

```python
from canvas_lms_python_client.models.assessment_question_answers_inner import AssessmentQuestionAnswersInner

# TODO update the JSON string below
json = "{}"
# create an instance of AssessmentQuestionAnswersInner from a JSON string
assessment_question_answers_inner_instance = AssessmentQuestionAnswersInner.from_json(json)
# print the JSON string representation of the object
print(AssessmentQuestionAnswersInner.to_json())

# convert the object into a dict
assessment_question_answers_inner_dict = assessment_question_answers_inner_instance.to_dict()
# create an instance of AssessmentQuestionAnswersInner from a dict
assessment_question_answers_inner_from_dict = AssessmentQuestionAnswersInner.from_dict(assessment_question_answers_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


