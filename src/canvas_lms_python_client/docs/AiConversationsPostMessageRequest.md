# AiConversationsPostMessageRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | The user&#39;s message to send to the AI | 

## Example

```python
from canvas_lms_python_client.models.ai_conversations_post_message_request import AiConversationsPostMessageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AiConversationsPostMessageRequest from a JSON string
ai_conversations_post_message_request_instance = AiConversationsPostMessageRequest.from_json(json)
# print the JSON string representation of the object
print(AiConversationsPostMessageRequest.to_json())

# convert the object into a dict
ai_conversations_post_message_request_dict = ai_conversations_post_message_request_instance.to_dict()
# create an instance of AiConversationsPostMessageRequest from a dict
ai_conversations_post_message_request_from_dict = AiConversationsPostMessageRequest.from_dict(ai_conversations_post_message_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


