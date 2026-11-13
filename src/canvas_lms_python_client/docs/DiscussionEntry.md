# DiscussionEntry

An entry (a root post or a reply) in a discussion topic

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier for the entry. | 
**user_id** | **int** | The unique identifier for the author of the entry. Not returned for deleted entries. | [optional] 
**editor_id** | **int** | The unique identifier for the user who last edited or deleted the entry, if any. | [optional] 
**user_name** | **str** | The author&#39;s display name, or null for anonymous topics when the author is not an instructor. Not returned for deleted entries. | [optional] 
**message** | **str** | The content of the entry (HTML). Not returned for deleted entries. | [optional] 
**deleted** | **bool** | True if the entry has been deleted. user_id, user_name and message are not returned for deleted entries. | [optional] 
**parent_id** | **int** | The unique identifier of the parent entry, or null for a root entry. | [optional] 
**created_at** | **datetime** | The creation time of the entry, in ISO8601 format. | [optional] 
**updated_at** | **datetime** | The time the entry was last updated, in ISO8601 format. | [optional] 
**rating_count** | **int** | The number of ratings the entry has, or null if it has none. | [optional] 
**rating_sum** | **int** | The sum of the entry&#39;s ratings, or null if it has none. | [optional] 
**read_state** | **str** | The read state of the entry, \&quot;read\&quot; or \&quot;unread\&quot;. | [optional] 
**forced_read_state** | **bool** | Whether the read_state was forced (was set manually). | [optional] 
**user** | **object** | The author&#39;s display information (id, display_name, avatar_image_url, html_url, pronouns, anonymous_id). | [optional] 
**attachment** | **object** | The file attached to the entry, if any. | [optional] 
**attachments** | **List[object]** | The files attached to the entry, if any. | [optional] 
**recent_replies** | [**List[DiscussionEntry]**](DiscussionEntry.md) | The 10 most recent replies for a root entry, newest first. Present only if there is at least one reply. | [optional] 
**has_more_replies** | **bool** | True if there are more than 10 replies for a root entry. Present only if there is at least one reply. | [optional] 

## Example

```python
from canvas_lms_python_client.models.discussion_entry import DiscussionEntry

# TODO update the JSON string below
json = "{}"
# create an instance of DiscussionEntry from a JSON string
discussion_entry_instance = DiscussionEntry.from_json(json)
# print the JSON string representation of the object
print(DiscussionEntry.to_json())

# convert the object into a dict
discussion_entry_dict = discussion_entry_instance.to_dict()
# create an instance of DiscussionEntry from a dict
discussion_entry_from_dict = DiscussionEntry.from_dict(discussion_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


