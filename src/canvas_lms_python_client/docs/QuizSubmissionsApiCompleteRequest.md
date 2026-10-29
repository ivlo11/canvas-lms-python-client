# QuizSubmissionsApiCompleteRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attempt** | **int** | The attempt number of the quiz submission that should be completed. Note that this must be the latest attempt index, as earlier attempts can not be modified. | 
**validation_token** | **str** | The unique validation token you received when this Quiz Submission was created. | 
**access_code** | **str** | Access code for the Quiz, if any. | [optional] 

## Example

```python
from canvas_lms_python_client.models.quiz_submissions_api_complete_request import QuizSubmissionsApiCompleteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of QuizSubmissionsApiCompleteRequest from a JSON string
quiz_submissions_api_complete_request_instance = QuizSubmissionsApiCompleteRequest.from_json(json)
# print the JSON string representation of the object
print(QuizSubmissionsApiCompleteRequest.to_json())

# convert the object into a dict
quiz_submissions_api_complete_request_dict = quiz_submissions_api_complete_request_instance.to_dict()
# create an instance of QuizSubmissionsApiCompleteRequest from a dict
quiz_submissions_api_complete_request_from_dict = QuizSubmissionsApiCompleteRequest.from_dict(quiz_submissions_api_complete_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


