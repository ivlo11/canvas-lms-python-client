# DiscussionTopicsApiSummaryFeedbackRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | Required The action to take on the summary. Possible values are: - \&quot;seen\&quot;: Marks the summary as seen. This action saves the feedback if it&#39;s not already persisted. - \&quot;like\&quot;: Marks the summary as liked. - \&quot;dislike\&quot;: Marks the summary as disliked. - \&quot;add_comment\&quot;: Adds a written comment to a disliked summary. Requires the \&quot;comment\&quot; parameter. - \&quot;reset_like\&quot;: Resets the like status of the summary. - \&quot;regenerate\&quot;: Regenerates the summary feedback. - \&quot;disable_summary\&quot;: Disables the summary feedback. Any other value will result in an error response. | [optional] 
**comment** | **str** | Optional A written explanation for the dislike. Only used with the \&quot;add_comment\&quot; action. Maximum 1024 characters. | [optional] 

## Example

```python
from canvas_lms_python_client.models.discussion_topics_api_summary_feedback_request import DiscussionTopicsApiSummaryFeedbackRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DiscussionTopicsApiSummaryFeedbackRequest from a JSON string
discussion_topics_api_summary_feedback_request_instance = DiscussionTopicsApiSummaryFeedbackRequest.from_json(json)
# print the JSON string representation of the object
print(DiscussionTopicsApiSummaryFeedbackRequest.to_json())

# convert the object into a dict
discussion_topics_api_summary_feedback_request_dict = discussion_topics_api_summary_feedback_request_instance.to_dict()
# create an instance of DiscussionTopicsApiSummaryFeedbackRequest from a dict
discussion_topics_api_summary_feedback_request_from_dict = DiscussionTopicsApiSummaryFeedbackRequest.from_dict(discussion_topics_api_summary_feedback_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


