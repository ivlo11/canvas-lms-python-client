# QuizSubmissionQuestionAnswer

The provided answer (if any) for this question. The format of this parameter depends on the type of the question, see the Appendix for more information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from canvas_lms_python_client.models.quiz_submission_question_answer import QuizSubmissionQuestionAnswer

# TODO update the JSON string below
json = "{}"
# create an instance of QuizSubmissionQuestionAnswer from a JSON string
quiz_submission_question_answer_instance = QuizSubmissionQuestionAnswer.from_json(json)
# print the JSON string representation of the object
print(QuizSubmissionQuestionAnswer.to_json())

# convert the object into a dict
quiz_submission_question_answer_dict = quiz_submission_question_answer_instance.to_dict()
# create an instance of QuizSubmissionQuestionAnswer from a dict
quiz_submission_question_answer_from_dict = QuizSubmissionQuestionAnswer.from_dict(quiz_submission_question_answer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


