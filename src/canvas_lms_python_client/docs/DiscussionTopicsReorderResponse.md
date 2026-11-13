# DiscussionTopicsReorderResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order** | **List[str]** |  | [optional] 
**reorder** | **bool** |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.discussion_topics_reorder_response import DiscussionTopicsReorderResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DiscussionTopicsReorderResponse from a JSON string
discussion_topics_reorder_response_instance = DiscussionTopicsReorderResponse.from_json(json)
# print the JSON string representation of the object
print(DiscussionTopicsReorderResponse.to_json())

# convert the object into a dict
discussion_topics_reorder_response_dict = discussion_topics_reorder_response_instance.to_dict()
# create an instance of DiscussionTopicsReorderResponse from a dict
discussion_topics_reorder_response_from_dict = DiscussionTopicsReorderResponse.from_dict(discussion_topics_reorder_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


