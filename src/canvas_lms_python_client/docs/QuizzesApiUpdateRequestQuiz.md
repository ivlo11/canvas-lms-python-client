# QuizzesApiUpdateRequestQuiz


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**notify_of_update** | **bool** | [Boolean] If true, notifies users that the quiz has changed. Defaults to true | [optional] 

## Example

```python
from canvas_lms_python_client.models.quizzes_api_update_request_quiz import QuizzesApiUpdateRequestQuiz

# TODO update the JSON string below
json = "{}"
# create an instance of QuizzesApiUpdateRequestQuiz from a JSON string
quizzes_api_update_request_quiz_instance = QuizzesApiUpdateRequestQuiz.from_json(json)
# print the JSON string representation of the object
print(QuizzesApiUpdateRequestQuiz.to_json())

# convert the object into a dict
quizzes_api_update_request_quiz_dict = quizzes_api_update_request_quiz_instance.to_dict()
# create an instance of QuizzesApiUpdateRequestQuiz from a dict
quizzes_api_update_request_quiz_from_dict = QuizzesApiUpdateRequestQuiz.from_dict(quizzes_api_update_request_quiz_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


