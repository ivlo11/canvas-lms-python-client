# AiConversationsCreateFeedbackRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vote** | **str** | \&quot;liked\&quot; or \&quot;disliked\&quot; | 
**feedback_message** | **str** | optional text for dislike | [optional] 

## Example

```python
from canvas_lms_python_client.models.ai_conversations_create_feedback_request import AiConversationsCreateFeedbackRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AiConversationsCreateFeedbackRequest from a JSON string
ai_conversations_create_feedback_request_instance = AiConversationsCreateFeedbackRequest.from_json(json)
# print the JSON string representation of the object
print(AiConversationsCreateFeedbackRequest.to_json())

# convert the object into a dict
ai_conversations_create_feedback_request_dict = ai_conversations_create_feedback_request_instance.to_dict()
# create an instance of AiConversationsCreateFeedbackRequest from a dict
ai_conversations_create_feedback_request_from_dict = AiConversationsCreateFeedbackRequest.from_dict(ai_conversations_create_feedback_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


