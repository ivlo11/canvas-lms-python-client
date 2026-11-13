# QuizSubmissionsApiCreateResponse

Paginated `quiz_submissions` list response (from the Canvas example response).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quiz_submissions** | [**List[QuizSubmission]**](QuizSubmission.md) |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.quiz_submissions_api_create_response import QuizSubmissionsApiCreateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of QuizSubmissionsApiCreateResponse from a JSON string
quiz_submissions_api_create_response_instance = QuizSubmissionsApiCreateResponse.from_json(json)
# print the JSON string representation of the object
print(QuizSubmissionsApiCreateResponse.to_json())

# convert the object into a dict
quiz_submissions_api_create_response_dict = quiz_submissions_api_create_response_instance.to_dict()
# create an instance of QuizSubmissionsApiCreateResponse from a dict
quiz_submissions_api_create_response_from_dict = QuizSubmissionsApiCreateResponse.from_dict(quiz_submissions_api_create_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


