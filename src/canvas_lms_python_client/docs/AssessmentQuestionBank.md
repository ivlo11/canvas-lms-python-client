# AssessmentQuestionBank


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The ID of the assessment question bank. | 
**context_id** | **int** | The ID of the context (course or account) the question bank belongs to. | 
**context_type** | **str** | The type of context (Course or Account). | 
**title** | **str** | The title of the question bank. | 
**workflow_state** | **str** | The workflow state of the question bank. | [optional] 
**assessment_question_count** | **int** | The number of questions in the bank. | [optional] 
**context_code** | **str** | The combined context type and ID. | [optional] 
**created_at** | **datetime** | The date and time the question bank was created. | [optional] 
**updated_at** | **datetime** | The date and time the question bank was last updated. | [optional] 

## Example

```python
from canvas_lms_python_client.models.assessment_question_bank import AssessmentQuestionBank

# TODO update the JSON string below
json = "{}"
# create an instance of AssessmentQuestionBank from a JSON string
assessment_question_bank_instance = AssessmentQuestionBank.from_json(json)
# print the JSON string representation of the object
print(AssessmentQuestionBank.to_json())

# convert the object into a dict
assessment_question_bank_dict = assessment_question_bank_instance.to_dict()
# create an instance of AssessmentQuestionBank from a dict
assessment_question_bank_from_dict = AssessmentQuestionBank.from_dict(assessment_question_bank_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


