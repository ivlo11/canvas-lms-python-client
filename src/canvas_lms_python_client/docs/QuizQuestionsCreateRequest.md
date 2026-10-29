# QuizQuestionsCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**question** | [**QuizQuestionsCreateRequestQuestion**](QuizQuestionsCreateRequestQuestion.md) |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.quiz_questions_create_request import QuizQuestionsCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of QuizQuestionsCreateRequest from a JSON string
quiz_questions_create_request_instance = QuizQuestionsCreateRequest.from_json(json)
# print the JSON string representation of the object
print(QuizQuestionsCreateRequest.to_json())

# convert the object into a dict
quiz_questions_create_request_dict = quiz_questions_create_request_instance.to_dict()
# create an instance of QuizQuestionsCreateRequest from a dict
quiz_questions_create_request_from_dict = QuizQuestionsCreateRequest.from_dict(quiz_questions_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


