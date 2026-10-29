# DiscussionTopicsApiMarkAllReadRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**forced_read_state** | **bool** | A boolean value to set all of the entries&#39; forced_read_state. No change is made if this argument is not specified. | [optional] 

## Example

```python
from canvas_lms_python_client.models.discussion_topics_api_mark_all_read_request import DiscussionTopicsApiMarkAllReadRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DiscussionTopicsApiMarkAllReadRequest from a JSON string
discussion_topics_api_mark_all_read_request_instance = DiscussionTopicsApiMarkAllReadRequest.from_json(json)
# print the JSON string representation of the object
print(DiscussionTopicsApiMarkAllReadRequest.to_json())

# convert the object into a dict
discussion_topics_api_mark_all_read_request_dict = discussion_topics_api_mark_all_read_request_instance.to_dict()
# create an instance of DiscussionTopicsApiMarkAllReadRequest from a dict
discussion_topics_api_mark_all_read_request_from_dict = DiscussionTopicsApiMarkAllReadRequest.from_dict(discussion_topics_api_mark_all_read_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


