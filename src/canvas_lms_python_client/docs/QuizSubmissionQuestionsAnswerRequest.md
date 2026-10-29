# QuizSubmissionQuestionsAnswerRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attempt** | **int** | The attempt number of the quiz submission being taken. Note that this must be the latest attempt index, as questions for earlier attempts can not be modified. | 
**validation_token** | **str** | The unique validation token you received when the Quiz Submission was created. | 
**access_code** | **str** | Access code for the Quiz, if any. | [optional] 
**quiz_questions_quiz_submission_question** | **str** | Set of question IDs and the answer value.  See {Appendix: Question Answer Formats} for the accepted answer formats for each question type. | [optional] 

## Example

```python
from canvas_lms_python_client.models.quiz_submission_questions_answer_request import QuizSubmissionQuestionsAnswerRequest

# TODO update the JSON string below
json = "{}"
# create an instance of QuizSubmissionQuestionsAnswerRequest from a JSON string
quiz_submission_questions_answer_request_instance = QuizSubmissionQuestionsAnswerRequest.from_json(json)
# print the JSON string representation of the object
print(QuizSubmissionQuestionsAnswerRequest.to_json())

# convert the object into a dict
quiz_submission_questions_answer_request_dict = quiz_submission_questions_answer_request_instance.to_dict()
# create an instance of QuizSubmissionQuestionsAnswerRequest from a dict
quiz_submission_questions_answer_request_from_dict = QuizSubmissionQuestionsAnswerRequest.from_dict(quiz_submission_questions_answer_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


