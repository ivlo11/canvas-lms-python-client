# QuizzesApiCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quiz** | [**QuizzesApiCreateRequestQuiz**](QuizzesApiCreateRequestQuiz.md) |  | 

## Example

```python
from canvas_lms_python_client.models.quizzes_api_create_request import QuizzesApiCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of QuizzesApiCreateRequest from a JSON string
quizzes_api_create_request_instance = QuizzesApiCreateRequest.from_json(json)
# print the JSON string representation of the object
print(QuizzesApiCreateRequest.to_json())

# convert the object into a dict
quizzes_api_create_request_dict = quizzes_api_create_request_instance.to_dict()
# create an instance of QuizzesApiCreateRequest from a dict
quizzes_api_create_request_from_dict = QuizzesApiCreateRequest.from_dict(quizzes_api_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


