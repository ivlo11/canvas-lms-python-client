# DiscussionTopicsFindOrCreateSummaryResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**text** | **str** |  | [optional] 
**usage** | **object** |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.discussion_topics_find_or_create_summary_response import DiscussionTopicsFindOrCreateSummaryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DiscussionTopicsFindOrCreateSummaryResponse from a JSON string
discussion_topics_find_or_create_summary_response_instance = DiscussionTopicsFindOrCreateSummaryResponse.from_json(json)
# print the JSON string representation of the object
print(DiscussionTopicsFindOrCreateSummaryResponse.to_json())

# convert the object into a dict
discussion_topics_find_or_create_summary_response_dict = discussion_topics_find_or_create_summary_response_instance.to_dict()
# create an instance of DiscussionTopicsFindOrCreateSummaryResponse from a dict
discussion_topics_find_or_create_summary_response_from_dict = DiscussionTopicsFindOrCreateSummaryResponse.from_dict(discussion_topics_find_or_create_summary_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


