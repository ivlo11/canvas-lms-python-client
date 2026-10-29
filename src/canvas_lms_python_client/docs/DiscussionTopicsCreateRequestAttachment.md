# DiscussionTopicsCreateRequestAttachment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file** | **str** | A multipart/form-data form-field-style attachment. Attachments larger than 1 kilobyte are subject to quota restrictions. | [optional] 

## Example

```python
from canvas_lms_python_client.models.discussion_topics_create_request_attachment import DiscussionTopicsCreateRequestAttachment

# TODO update the JSON string below
json = "{}"
# create an instance of DiscussionTopicsCreateRequestAttachment from a JSON string
discussion_topics_create_request_attachment_instance = DiscussionTopicsCreateRequestAttachment.from_json(json)
# print the JSON string representation of the object
print(DiscussionTopicsCreateRequestAttachment.to_json())

# convert the object into a dict
discussion_topics_create_request_attachment_dict = discussion_topics_create_request_attachment_instance.to_dict()
# create an instance of DiscussionTopicsCreateRequestAttachment from a dict
discussion_topics_create_request_attachment_from_dict = DiscussionTopicsCreateRequestAttachment.from_dict(discussion_topics_create_request_attachment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


