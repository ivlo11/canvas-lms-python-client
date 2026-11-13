# ConversationAudienceContexts

Most relevant shared contexts (courses and groups) between current user and other participants. If there is only one participant, it will also include that user's enrollment(s)/ membership type(s) in each course/group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from canvas_lms_python_client.models.conversation_audience_contexts import ConversationAudienceContexts

# TODO update the JSON string below
json = "{}"
# create an instance of ConversationAudienceContexts from a JSON string
conversation_audience_contexts_instance = ConversationAudienceContexts.from_json(json)
# print the JSON string representation of the object
print(ConversationAudienceContexts.to_json())

# convert the object into a dict
conversation_audience_contexts_dict = conversation_audience_contexts_instance.to_dict()
# create an instance of ConversationAudienceContexts from a dict
conversation_audience_contexts_from_dict = ConversationAudienceContexts.from_dict(conversation_audience_contexts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


