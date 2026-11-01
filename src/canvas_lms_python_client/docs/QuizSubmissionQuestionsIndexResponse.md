# QuizSubmissionQuestionsIndexResponse

Paginated `quiz_submission_questions` list response (from the Canvas example response).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quiz_submission_questions** | [**List[QuizSubmissionQuestion]**](QuizSubmissionQuestion.md) |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.quiz_submission_questions_index_response import QuizSubmissionQuestionsIndexResponse

# TODO update the JSON string below
json = "{}"
# create an instance of QuizSubmissionQuestionsIndexResponse from a JSON string
quiz_submission_questions_index_response_instance = QuizSubmissionQuestionsIndexResponse.from_json(json)
# print the JSON string representation of the object
print(QuizSubmissionQuestionsIndexResponse.to_json())

# convert the object into a dict
quiz_submission_questions_index_response_dict = quiz_submission_questions_index_response_instance.to_dict()
# create an instance of QuizSubmissionQuestionsIndexResponse from a dict
quiz_submission_questions_index_response_from_dict = QuizSubmissionQuestionsIndexResponse.from_dict(quiz_submission_questions_index_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


