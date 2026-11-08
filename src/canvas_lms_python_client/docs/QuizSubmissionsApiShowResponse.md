# QuizSubmissionsApiShowResponse

Object response with `quiz_submissions`, `quizzes`, `submissions`, `users`, `meta` (from the Canvas `@returns`).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quiz_submissions** | [**List[QuizSubmission]**](QuizSubmission.md) |  | [optional] 
**quizzes** | [**List[Quiz]**](Quiz.md) |  | [optional] 
**submissions** | [**List[Submission]**](Submission.md) |  | [optional] 
**users** | [**List[User]**](User.md) |  | [optional] 
**meta** | **object** |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.quiz_submissions_api_show_response import QuizSubmissionsApiShowResponse

# TODO update the JSON string below
json = "{}"
# create an instance of QuizSubmissionsApiShowResponse from a JSON string
quiz_submissions_api_show_response_instance = QuizSubmissionsApiShowResponse.from_json(json)
# print the JSON string representation of the object
print(QuizSubmissionsApiShowResponse.to_json())

# convert the object into a dict
quiz_submissions_api_show_response_dict = quiz_submissions_api_show_response_instance.to_dict()
# create an instance of QuizSubmissionsApiShowResponse from a dict
quiz_submissions_api_show_response_from_dict = QuizSubmissionsApiShowResponse.from_dict(quiz_submissions_api_show_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


