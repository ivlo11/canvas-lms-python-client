# QuizQuestionsCreateRequestQuestion


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**question_name** | **str** | [String] The name of the question. | [optional] 
**question_text** | **str** | [String] The text of the question. | [optional] 
**quiz_group_id** | **int** | [Integer] The id of the quiz group to assign the question to. | [optional] 
**question_type** | **str** | [\&quot;calculated_question\&quot;|\&quot;essay_question\&quot;|\&quot;file_upload_question\&quot;|\&quot;fill_in_multiple_blanks_question\&quot;|\&quot;matching_question\&quot;|\&quot;multiple_answers_question\&quot;|\&quot;multiple_choice_question\&quot;|\&quot;multiple_dropdowns_question\&quot;|\&quot;numerical_question\&quot;|\&quot;short_answer_question\&quot;|\&quot;text_only_question\&quot;|\&quot;true_false_question\&quot;] The type of question. Multiple optional fields depend upon the type of question to be used. | [optional] 
**position** | **int** | [Integer] The order in which the question will be displayed in the quiz in relation to other questions. | [optional] 
**points_possible** | **int** | [Integer] The maximum amount of points received for answering this question correctly. | [optional] 
**correct_comments** | **str** | [String] The comment to display if the student answers the question correctly. | [optional] 
**incorrect_comments** | **str** | [String] The comment to display if the student answers incorrectly. | [optional] 
**neutral_comments** | **str** | [String] The comment to display regardless of how the student answered. | [optional] 
**text_after_answers** | **str** | [String] | [optional] 
**answers** | **str** | [[Answer]] | [optional] 

## Example

```python
from canvas_lms_python_client.models.quiz_questions_create_request_question import QuizQuestionsCreateRequestQuestion

# TODO update the JSON string below
json = "{}"
# create an instance of QuizQuestionsCreateRequestQuestion from a JSON string
quiz_questions_create_request_question_instance = QuizQuestionsCreateRequestQuestion.from_json(json)
# print the JSON string representation of the object
print(QuizQuestionsCreateRequestQuestion.to_json())

# convert the object into a dict
quiz_questions_create_request_question_dict = quiz_questions_create_request_question_instance.to_dict()
# create an instance of QuizQuestionsCreateRequestQuestion from a dict
quiz_questions_create_request_question_from_dict = QuizQuestionsCreateRequestQuestion.from_dict(quiz_questions_create_request_question_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


