# ConversationsUpdateRequestConversation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workflow_state** | **str** | [String, \&quot;read\&quot;|\&quot;unread\&quot;|\&quot;archived\&quot;] Change the state of this conversation | [optional] 
**subscribed** | **bool** | [Boolean] Toggle the current user&#39;s subscription to the conversation (only valid for group conversations). If unsubscribed, the user will still have access to the latest messages, but the conversation won&#39;t be automatically flagged as unread, nor will it jump to the top of the inbox. | [optional] 
**starred** | **bool** | [Boolean] Toggle the starred state of the current user&#39;s view of the conversation. | [optional] 

## Example

```python
from canvas_lms_python_client.models.conversations_update_request_conversation import ConversationsUpdateRequestConversation

# TODO update the JSON string below
json = "{}"
# create an instance of ConversationsUpdateRequestConversation from a JSON string
conversations_update_request_conversation_instance = ConversationsUpdateRequestConversation.from_json(json)
# print the JSON string representation of the object
print(ConversationsUpdateRequestConversation.to_json())

# convert the object into a dict
conversations_update_request_conversation_dict = conversations_update_request_conversation_instance.to_dict()
# create an instance of ConversationsUpdateRequestConversation from a dict
conversations_update_request_conversation_from_dict = ConversationsUpdateRequestConversation.from_dict(conversations_update_request_conversation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


