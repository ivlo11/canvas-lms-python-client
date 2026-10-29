# ConversationsAddMessageRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | **str** | The message to be sent. | 
**attachment_ids** | **List[str]** | An array of attachments ids. These must be files that have been previously uploaded to the sender&#39;s \&quot;conversation attachments\&quot; folder. | [optional] 
**media_comment_id** | **str** | Media comment id of an audio of video file to be associated with this message. | [optional] 
**media_comment_type** | **str** | Type of the associated media file. | [optional] 
**recipients** | **List[str]** |  | [optional] 
**included_messages** | **List[str]** |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.conversations_add_message_request import ConversationsAddMessageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ConversationsAddMessageRequest from a JSON string
conversations_add_message_request_instance = ConversationsAddMessageRequest.from_json(json)
# print the JSON string representation of the object
print(ConversationsAddMessageRequest.to_json())

# convert the object into a dict
conversations_add_message_request_dict = conversations_add_message_request_instance.to_dict()
# create an instance of ConversationsAddMessageRequest from a dict
conversations_add_message_request_from_dict = ConversationsAddMessageRequest.from_dict(conversations_add_message_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


