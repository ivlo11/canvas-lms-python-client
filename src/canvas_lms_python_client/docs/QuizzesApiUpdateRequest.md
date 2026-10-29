# QuizzesApiUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quiz** | [**QuizzesApiUpdateRequestQuiz**](QuizzesApiUpdateRequestQuiz.md) |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.quizzes_api_update_request import QuizzesApiUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of QuizzesApiUpdateRequest from a JSON string
quizzes_api_update_request_instance = QuizzesApiUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(QuizzesApiUpdateRequest.to_json())

# convert the object into a dict
quizzes_api_update_request_dict = quizzes_api_update_request_instance.to_dict()
# create an instance of QuizzesApiUpdateRequest from a dict
quizzes_api_update_request_from_dict = QuizzesApiUpdateRequest.from_dict(quizzes_api_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


