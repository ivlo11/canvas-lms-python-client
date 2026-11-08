# Conversation



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | the unique identifier for the conversation. | [optional] 
**subject** | **str** | the subject of the conversation. | [optional] 
**workflow_state** | **str** | The current state of the conversation (read, unread or archived). | [optional] 
**last_message** | **str** | A &lt;&#x3D;100 character preview from the most recent message. | [optional] 
**start_at** | **datetime** | the date and time at which the last message was sent. | [optional] 
**message_count** | **int** | the number of messages in the conversation. | [optional] 
**subscribed** | **bool** | whether the current user is subscribed to the conversation. | [optional] 
**private** | **bool** | whether the conversation is private. | [optional] 
**starred** | **bool** | whether the conversation is starred. | [optional] 
**properties** | **List[str]** | Additional conversation flags (last_author, attachments, media_objects). Each listed property means the flag is set to true (i.e. the current user is the most recent author, there are attachments, or there are media objects) | [optional] 
**audience** | **List[int]** | Array of user ids who are involved in the conversation, ordered by participation level, then alphabetical. Excludes current user, unless this is a monologue. | [optional] 
**audience_contexts** | [**ConversationAudienceContexts**](ConversationAudienceContexts.md) |  | [optional] 
**avatar_url** | **str** | URL to appropriate icon for this conversation (custom, individual or group avatar, depending on audience). | [optional] 
**participants** | [**List[ConversationParticipant]**](ConversationParticipant.md) | Array of users participating in the conversation. Includes current user. | [optional] 
**visible** | **bool** | indicates whether the conversation is visible under the current scope and filter. This attribute is always true in the index API response, and is primarily useful in create/update responses so that you can know if the record should be displayed in the UI. The default scope is assumed, unless a scope or filter is passed to the create/update API call. | [optional] 
**context_name** | **str** | Name of the course or group in which the conversation is occurring. | [optional] 
**context_code** | **str** |  | [optional] 
**last_authored_message** | **str** |  | [optional] 
**last_authored_message_at** | **str** |  | [optional] 
**last_message_at** | **str** |  | [optional] 
**messages** | **List[object]** |  | [optional] 
**cannot_reply** | **bool** |  | [optional] 
**submissions** | **List[object]** |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.conversation import Conversation

# TODO update the JSON string below
json = "{}"
# create an instance of Conversation from a JSON string
conversation_instance = Conversation.from_json(json)
# print the JSON string representation of the object
print(Conversation.to_json())

# convert the object into a dict
conversation_dict = conversation_instance.to_dict()
# create an instance of Conversation from a dict
conversation_from_dict = Conversation.from_dict(conversation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


