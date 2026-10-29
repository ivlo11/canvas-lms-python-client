# DiscussionTopicsApiFindOrCreateSummaryRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_input** | **str** | Areas or topics for the summary to focus on. | [optional] 

## Example

```python
from canvas_lms_python_client.models.discussion_topics_api_find_or_create_summary_request import DiscussionTopicsApiFindOrCreateSummaryRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DiscussionTopicsApiFindOrCreateSummaryRequest from a JSON string
discussion_topics_api_find_or_create_summary_request_instance = DiscussionTopicsApiFindOrCreateSummaryRequest.from_json(json)
# print the JSON string representation of the object
print(DiscussionTopicsApiFindOrCreateSummaryRequest.to_json())

# convert the object into a dict
discussion_topics_api_find_or_create_summary_request_dict = discussion_topics_api_find_or_create_summary_request_instance.to_dict()
# create an instance of DiscussionTopicsApiFindOrCreateSummaryRequest from a dict
discussion_topics_api_find_or_create_summary_request_from_dict = DiscussionTopicsApiFindOrCreateSummaryRequest.from_dict(discussion_topics_api_find_or_create_summary_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


