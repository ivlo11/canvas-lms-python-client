# ConversationsRemoveMessagesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**remove** | **List[str]** | Array of message ids to be deleted | 

## Example

```python
from canvas_lms_python_client.models.conversations_remove_messages_request import ConversationsRemoveMessagesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ConversationsRemoveMessagesRequest from a JSON string
conversations_remove_messages_request_instance = ConversationsRemoveMessagesRequest.from_json(json)
# print the JSON string representation of the object
print(ConversationsRemoveMessagesRequest.to_json())

# convert the object into a dict
conversations_remove_messages_request_dict = conversations_remove_messages_request_instance.to_dict()
# create an instance of ConversationsRemoveMessagesRequest from a dict
conversations_remove_messages_request_from_dict = ConversationsRemoveMessagesRequest.from_dict(conversations_remove_messages_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


