# QuizSubmissionUsersMessageRequestConversations


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quiz_user_conversation** | **str** | - Body and recipients to send the message to. | [optional] 

## Example

```python
from canvas_lms_python_client.models.quiz_submission_users_message_request_conversations import QuizSubmissionUsersMessageRequestConversations

# TODO update the JSON string below
json = "{}"
# create an instance of QuizSubmissionUsersMessageRequestConversations from a JSON string
quiz_submission_users_message_request_conversations_instance = QuizSubmissionUsersMessageRequestConversations.from_json(json)
# print the JSON string representation of the object
print(QuizSubmissionUsersMessageRequestConversations.to_json())

# convert the object into a dict
quiz_submission_users_message_request_conversations_dict = quiz_submission_users_message_request_conversations_instance.to_dict()
# create an instance of QuizSubmissionUsersMessageRequestConversations from a dict
quiz_submission_users_message_request_conversations_from_dict = QuizSubmissionUsersMessageRequestConversations.from_dict(quiz_submission_users_message_request_conversations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


