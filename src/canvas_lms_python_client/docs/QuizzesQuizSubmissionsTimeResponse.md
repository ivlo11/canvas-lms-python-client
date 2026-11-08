# QuizzesQuizSubmissionsTimeResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end_at** | **str** |  | [optional] 
**time_left** | **int** |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.quizzes_quiz_submissions_time_response import QuizzesQuizSubmissionsTimeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of QuizzesQuizSubmissionsTimeResponse from a JSON string
quizzes_quiz_submissions_time_response_instance = QuizzesQuizSubmissionsTimeResponse.from_json(json)
# print the JSON string representation of the object
print(QuizzesQuizSubmissionsTimeResponse.to_json())

# convert the object into a dict
quizzes_quiz_submissions_time_response_dict = quizzes_quiz_submissions_time_response_instance.to_dict()
# create an instance of QuizzesQuizSubmissionsTimeResponse from a dict
quizzes_quiz_submissions_time_response_from_dict = QuizzesQuizSubmissionsTimeResponse.from_dict(quizzes_quiz_submissions_time_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


