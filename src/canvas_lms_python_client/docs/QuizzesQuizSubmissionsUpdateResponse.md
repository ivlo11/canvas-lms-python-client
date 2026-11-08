# QuizzesQuizSubmissionsUpdateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quiz_submissions** | [**List[QuizSubmission]**](QuizSubmission.md) |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.quizzes_quiz_submissions_update_response import QuizzesQuizSubmissionsUpdateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of QuizzesQuizSubmissionsUpdateResponse from a JSON string
quizzes_quiz_submissions_update_response_instance = QuizzesQuizSubmissionsUpdateResponse.from_json(json)
# print the JSON string representation of the object
print(QuizzesQuizSubmissionsUpdateResponse.to_json())

# convert the object into a dict
quizzes_quiz_submissions_update_response_dict = quizzes_quiz_submissions_update_response_instance.to_dict()
# create an instance of QuizzesQuizSubmissionsUpdateResponse from a dict
quizzes_quiz_submissions_update_response_from_dict = QuizzesQuizSubmissionsUpdateResponse.from_dict(quizzes_quiz_submissions_update_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


