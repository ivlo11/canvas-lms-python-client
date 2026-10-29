# DiscussionTopicsApiRateEntryRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rating** | **int** | A rating to set on this entry. Only 0 and 1 are accepted. | [optional] 

## Example

```python
from canvas_lms_python_client.models.discussion_topics_api_rate_entry_request import DiscussionTopicsApiRateEntryRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DiscussionTopicsApiRateEntryRequest from a JSON string
discussion_topics_api_rate_entry_request_instance = DiscussionTopicsApiRateEntryRequest.from_json(json)
# print the JSON string representation of the object
print(DiscussionTopicsApiRateEntryRequest.to_json())

# convert the object into a dict
discussion_topics_api_rate_entry_request_dict = discussion_topics_api_rate_entry_request_instance.to_dict()
# create an instance of DiscussionTopicsApiRateEntryRequest from a dict
discussion_topics_api_rate_entry_request_from_dict = DiscussionTopicsApiRateEntryRequest.from_dict(discussion_topics_api_rate_entry_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


