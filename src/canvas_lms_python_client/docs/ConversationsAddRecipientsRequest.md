# ConversationsAddRecipientsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recipients** | **List[str]** | An array of recipient ids. These may be user ids or course/group ids prefixed with \&quot;course_\&quot; or \&quot;group_\&quot; respectively, e.g. recipients[]&#x3D;1&amp;recipients[]&#x3D;2&amp;recipients[]&#x3D;course_3 | 

## Example

```python
from canvas_lms_python_client.models.conversations_add_recipients_request import ConversationsAddRecipientsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ConversationsAddRecipientsRequest from a JSON string
conversations_add_recipients_request_instance = ConversationsAddRecipientsRequest.from_json(json)
# print the JSON string representation of the object
print(ConversationsAddRecipientsRequest.to_json())

# convert the object into a dict
conversations_add_recipients_request_dict = conversations_add_recipients_request_instance.to_dict()
# create an instance of ConversationsAddRecipientsRequest from a dict
conversations_add_recipients_request_from_dict = ConversationsAddRecipientsRequest.from_dict(conversations_add_recipients_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


