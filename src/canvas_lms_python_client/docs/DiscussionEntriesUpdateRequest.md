# DiscussionEntriesUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | The updated body of the entry. | [optional] 

## Example

```python
from canvas_lms_python_client.models.discussion_entries_update_request import DiscussionEntriesUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DiscussionEntriesUpdateRequest from a JSON string
discussion_entries_update_request_instance = DiscussionEntriesUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(DiscussionEntriesUpdateRequest.to_json())

# convert the object into a dict
discussion_entries_update_request_dict = discussion_entries_update_request_instance.to_dict()
# create an instance of DiscussionEntriesUpdateRequest from a dict
discussion_entries_update_request_from_dict = DiscussionEntriesUpdateRequest.from_dict(discussion_entries_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


