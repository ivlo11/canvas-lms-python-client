# ConversationBatch

A bulk private message that is being sent asynchronously.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The ID of the batch. | [optional] 
**workflow_state** | **str** | The state of the batch: created or sending while it is running. | [optional] 
**completion** | **float** | How much of the batch has been sent, from 0 to 1. | [optional] 
**recipient_count** | **int** | The number of recipients the batch is sent to. | [optional] 
**message** | **object** | The batch&#39;s root conversation message. | [optional] 
**tags** | **List[str]** | The batch&#39;s tags (context asset strings). | [optional] 

## Example

```python
from canvas_lms_python_client.models.conversation_batch import ConversationBatch

# TODO update the JSON string below
json = "{}"
# create an instance of ConversationBatch from a JSON string
conversation_batch_instance = ConversationBatch.from_json(json)
# print the JSON string representation of the object
print(ConversationBatch.to_json())

# convert the object into a dict
conversation_batch_dict = conversation_batch_instance.to_dict()
# create an instance of ConversationBatch from a dict
conversation_batch_from_dict = ConversationBatch.from_dict(conversation_batch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


