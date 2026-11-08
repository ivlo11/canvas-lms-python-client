# QuizSubmissionQuestionsAnswerResponse

Object response with `quiz_submission_questions` (from the Canvas `@returns`).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quiz_submission_questions** | [**List[QuizSubmissionQuestion]**](QuizSubmissionQuestion.md) |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.quiz_submission_questions_answer_response import QuizSubmissionQuestionsAnswerResponse

# TODO update the JSON string below
json = "{}"
# create an instance of QuizSubmissionQuestionsAnswerResponse from a JSON string
quiz_submission_questions_answer_response_instance = QuizSubmissionQuestionsAnswerResponse.from_json(json)
# print the JSON string representation of the object
print(QuizSubmissionQuestionsAnswerResponse.to_json())

# convert the object into a dict
quiz_submission_questions_answer_response_dict = quiz_submission_questions_answer_response_instance.to_dict()
# create an instance of QuizSubmissionQuestionsAnswerResponse from a dict
quiz_submission_questions_answer_response_from_dict = QuizSubmissionQuestionsAnswerResponse.from_dict(quiz_submission_questions_answer_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


