# ConversationsBatchUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conversation_ids** | **List[str]** | List of conversations to update. Limited to 500 conversations. | 
**event** | **str** | The action to take on each conversation. | 

## Example

```python
from canvas_lms_python_client.models.conversations_batch_update_request import ConversationsBatchUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ConversationsBatchUpdateRequest from a JSON string
conversations_batch_update_request_instance = ConversationsBatchUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(ConversationsBatchUpdateRequest.to_json())

# convert the object into a dict
conversations_batch_update_request_dict = conversations_batch_update_request_instance.to_dict()
# create an instance of ConversationsBatchUpdateRequest from a dict
conversations_batch_update_request_from_dict = ConversationsBatchUpdateRequest.from_dict(conversations_batch_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


