# DiscussionTopicsApiAddEntryRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | The body of the entry. | [optional] 
**attachment** | **str** | a multipart/form-data form-field-style attachment. Attachments larger than 1 kilobyte are subject to quota restrictions. | [optional] 

## Example

```python
from canvas_lms_python_client.models.discussion_topics_api_add_entry_request import DiscussionTopicsApiAddEntryRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DiscussionTopicsApiAddEntryRequest from a JSON string
discussion_topics_api_add_entry_request_instance = DiscussionTopicsApiAddEntryRequest.from_json(json)
# print the JSON string representation of the object
print(DiscussionTopicsApiAddEntryRequest.to_json())

# convert the object into a dict
discussion_topics_api_add_entry_request_dict = discussion_topics_api_add_entry_request_instance.to_dict()
# create an instance of DiscussionTopicsApiAddEntryRequest from a dict
discussion_topics_api_add_entry_request_from_dict = DiscussionTopicsApiAddEntryRequest.from_dict(discussion_topics_api_add_entry_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


