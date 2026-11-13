# ConversationsUnreadCountResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unread_count** | **str** |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.conversations_unread_count_response import ConversationsUnreadCountResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ConversationsUnreadCountResponse from a JSON string
conversations_unread_count_response_instance = ConversationsUnreadCountResponse.from_json(json)
# print the JSON string representation of the object
print(ConversationsUnreadCountResponse.to_json())

# convert the object into a dict
conversations_unread_count_response_dict = conversations_unread_count_response_instance.to_dict()
# create an instance of ConversationsUnreadCountResponse from a dict
conversations_unread_count_response_from_dict = ConversationsUnreadCountResponse.from_dict(conversations_unread_count_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


