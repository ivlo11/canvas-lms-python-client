# DiscussionTopicsSummaryFeedbackResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** |  | [optional] 
**disliked** | **bool** |  | [optional] 
**liked** | **bool** |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.discussion_topics_summary_feedback_response import DiscussionTopicsSummaryFeedbackResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DiscussionTopicsSummaryFeedbackResponse from a JSON string
discussion_topics_summary_feedback_response_instance = DiscussionTopicsSummaryFeedbackResponse.from_json(json)
# print the JSON string representation of the object
print(DiscussionTopicsSummaryFeedbackResponse.to_json())

# convert the object into a dict
discussion_topics_summary_feedback_response_dict = discussion_topics_summary_feedback_response_instance.to_dict()
# create an instance of DiscussionTopicsSummaryFeedbackResponse from a dict
discussion_topics_summary_feedback_response_from_dict = DiscussionTopicsSummaryFeedbackResponse.from_dict(discussion_topics_summary_feedback_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


