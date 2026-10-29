# DiscussionTopicsReorderRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order** | **List[int]** | The ids of the pinned discussion topics in the desired order. (For example, \&quot;order&#x3D;104,102,103\&quot;.) | 

## Example

```python
from canvas_lms_python_client.models.discussion_topics_reorder_request import DiscussionTopicsReorderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DiscussionTopicsReorderRequest from a JSON string
discussion_topics_reorder_request_instance = DiscussionTopicsReorderRequest.from_json(json)
# print the JSON string representation of the object
print(DiscussionTopicsReorderRequest.to_json())

# convert the object into a dict
discussion_topics_reorder_request_dict = discussion_topics_reorder_request_instance.to_dict()
# create an instance of DiscussionTopicsReorderRequest from a dict
discussion_topics_reorder_request_from_dict = DiscussionTopicsReorderRequest.from_dict(discussion_topics_reorder_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


