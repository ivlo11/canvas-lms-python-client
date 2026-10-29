# QuizSubmissionsApiCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_code** | **str** | Access code for the Quiz, if any. | [optional] 
**preview** | **bool** | Whether this should be a preview QuizSubmission and not count towards the user&#39;s course record. Teachers only. | [optional] 

## Example

```python
from canvas_lms_python_client.models.quiz_submissions_api_create_request import QuizSubmissionsApiCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of QuizSubmissionsApiCreateRequest from a JSON string
quiz_submissions_api_create_request_instance = QuizSubmissionsApiCreateRequest.from_json(json)
# print the JSON string representation of the object
print(QuizSubmissionsApiCreateRequest.to_json())

# convert the object into a dict
quiz_submissions_api_create_request_dict = quiz_submissions_api_create_request_instance.to_dict()
# create an instance of QuizSubmissionsApiCreateRequest from a dict
quiz_submissions_api_create_request_from_dict = QuizSubmissionsApiCreateRequest.from_dict(quiz_submissions_api_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


