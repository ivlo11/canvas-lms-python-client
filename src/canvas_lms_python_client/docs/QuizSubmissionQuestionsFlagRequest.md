# QuizSubmissionQuestionsFlagRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attempt** | **int** | The attempt number of the quiz submission being taken. Note that this must be the latest attempt index, as questions for earlier attempts can not be modified. | 
**validation_token** | **str** | The unique validation token you received when the Quiz Submission was created. | 
**access_code** | **str** | Access code for the Quiz, if any. | [optional] 

## Example

```python
from canvas_lms_python_client.models.quiz_submission_questions_flag_request import QuizSubmissionQuestionsFlagRequest

# TODO update the JSON string below
json = "{}"
# create an instance of QuizSubmissionQuestionsFlagRequest from a JSON string
quiz_submission_questions_flag_request_instance = QuizSubmissionQuestionsFlagRequest.from_json(json)
# print the JSON string representation of the object
print(QuizSubmissionQuestionsFlagRequest.to_json())

# convert the object into a dict
quiz_submission_questions_flag_request_dict = quiz_submission_questions_flag_request_instance.to_dict()
# create an instance of QuizSubmissionQuestionsFlagRequest from a dict
quiz_submission_questions_flag_request_from_dict = QuizSubmissionQuestionsFlagRequest.from_dict(quiz_submission_questions_flag_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


