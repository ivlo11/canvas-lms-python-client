# ConversationsCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recipients** | **List[str]** | An array of recipient ids. These may be user ids | 
**subject** | **str** | The subject of the conversation. This is ignored when reusing a conversation. Maximum length is 255 characters. | [optional] 
**body** | **str** | The message to be sent | 
**force_new** | **bool** | Forces a new message to be created, even if there is an existing private conversation. | [optional] 
**group_conversation** | **bool** | Defaults to false.  When false, individual private conversations will be created with each recipient. If true, this will be a group conversation (i.e. all recipients may see all messages and replies). Must be set true if the number of recipients is over the set maximum (default is 100). | [optional] 
**attachment_ids** | **List[str]** | An array of attachments ids. These must be files that have been previously uploaded to the sender&#39;s \&quot;conversation attachments\&quot; folder. | [optional] 
**media_comment_id** | **str** | Media comment id of an audio or video file to be associated with this message. | [optional] 
**media_comment_type** | **str** | Type of the associated media file | [optional] 
**mode** | **str** | Determines whether the messages will be created/sent synchronously or asynchronously. Defaults to sync, and this option is ignored if this is a group conversation or there is just one recipient (i.e. it must be a bulk private message). When sent async, the response will be an empty array (batch status can be queried via the {api:ConversationsController#batches batches API}) | [optional] 
**scope** | **str** | Used when generating \&quot;visible\&quot; in the API response. See the explanation under the {api:ConversationsController#index index API action} | [optional] 
**filter** | **List[str]** | Used when generating \&quot;visible\&quot; in the API response. See the explanation under the {api:ConversationsController#index index API action} | [optional] 
**context_code** | **str** | The course or group that is the context for this conversation. Same format as courses or groups in the recipients argument. | [optional] 
**include** | **List[str]** | \&quot;uuid\&quot;:: Optionally include an \&quot;uuid\&quot; key for each user participating in the conversation | [optional] 
**filter_mode** | [**ConversationsCreateRequestFilterMode**](ConversationsCreateRequestFilterMode.md) |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.conversations_create_request import ConversationsCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ConversationsCreateRequest from a JSON string
conversations_create_request_instance = ConversationsCreateRequest.from_json(json)
# print the JSON string representation of the object
print(ConversationsCreateRequest.to_json())

# convert the object into a dict
conversations_create_request_dict = conversations_create_request_instance.to_dict()
# create an instance of ConversationsCreateRequest from a dict
conversations_create_request_from_dict = ConversationsCreateRequest.from_dict(conversations_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


