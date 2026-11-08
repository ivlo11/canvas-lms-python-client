# DiscussionTopicsViewResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entry_ratings** | **object** |  | [optional] 
**forced_entries** | **List[object]** |  | [optional] 
**new_entries** | **List[object]** |  | [optional] 
**participants** | **List[object]** |  | [optional] 
**unread_entries** | **List[int]** |  | [optional] 
**view** | **List[object]** |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.discussion_topics_view_response import DiscussionTopicsViewResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DiscussionTopicsViewResponse from a JSON string
discussion_topics_view_response_instance = DiscussionTopicsViewResponse.from_json(json)
# print the JSON string representation of the object
print(DiscussionTopicsViewResponse.to_json())

# convert the object into a dict
discussion_topics_view_response_dict = discussion_topics_view_response_instance.to_dict()
# create an instance of DiscussionTopicsViewResponse from a dict
discussion_topics_view_response_from_dict = DiscussionTopicsViewResponse.from_dict(discussion_topics_view_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


