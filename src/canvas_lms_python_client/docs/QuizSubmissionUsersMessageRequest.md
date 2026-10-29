# QuizSubmissionUsersMessageRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conversations** | [**QuizSubmissionUsersMessageRequestConversations**](QuizSubmissionUsersMessageRequestConversations.md) |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.quiz_submission_users_message_request import QuizSubmissionUsersMessageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of QuizSubmissionUsersMessageRequest from a JSON string
quiz_submission_users_message_request_instance = QuizSubmissionUsersMessageRequest.from_json(json)
# print the JSON string representation of the object
print(QuizSubmissionUsersMessageRequest.to_json())

# convert the object into a dict
quiz_submission_users_message_request_dict = quiz_submission_users_message_request_instance.to_dict()
# create an instance of QuizSubmissionUsersMessageRequest from a dict
quiz_submission_users_message_request_from_dict = QuizSubmissionUsersMessageRequest.from_dict(quiz_submission_users_message_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


