# DiscussionTopicsDestroyResponse

Object response with `discussion_topic` (from the Canvas `@returns`).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**discussion_topic** | [**DiscussionTopic**](DiscussionTopic.md) |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.discussion_topics_destroy_response import DiscussionTopicsDestroyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DiscussionTopicsDestroyResponse from a JSON string
discussion_topics_destroy_response_instance = DiscussionTopicsDestroyResponse.from_json(json)
# print the JSON string representation of the object
print(DiscussionTopicsDestroyResponse.to_json())

# convert the object into a dict
discussion_topics_destroy_response_dict = discussion_topics_destroy_response_instance.to_dict()
# create an instance of DiscussionTopicsDestroyResponse from a dict
discussion_topics_destroy_response_from_dict = DiscussionTopicsDestroyResponse.from_dict(discussion_topics_destroy_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


