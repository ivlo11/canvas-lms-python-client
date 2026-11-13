# DiscussionTopicsFindSummaryResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**obsolete** | **bool** |  | [optional] 
**text** | **str** |  | [optional] 
**usage** | **object** |  | [optional] 
**user_input** | **object** |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.discussion_topics_find_summary_response import DiscussionTopicsFindSummaryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DiscussionTopicsFindSummaryResponse from a JSON string
discussion_topics_find_summary_response_instance = DiscussionTopicsFindSummaryResponse.from_json(json)
# print the JSON string representation of the object
print(DiscussionTopicsFindSummaryResponse.to_json())

# convert the object into a dict
discussion_topics_find_summary_response_dict = discussion_topics_find_summary_response_instance.to_dict()
# create an instance of DiscussionTopicsFindSummaryResponse from a dict
discussion_topics_find_summary_response_from_dict = DiscussionTopicsFindSummaryResponse.from_dict(discussion_topics_find_summary_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


