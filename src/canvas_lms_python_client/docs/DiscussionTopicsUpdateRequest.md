# DiscussionTopicsUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**discussion_type** | **str** | The type of discussion. Defaults to side_comment or not_threaded if not value is given. Accepted values are &#39;side_comment&#39;, &#39;not_threaded&#39; for discussions that only allow one level of nested comments, and &#39;threaded&#39; for fully threaded discussions. | [optional] 
**published** | **bool** | Whether this topic is published (true) or draft state (false). Only teachers and TAs have the ability to create draft state topics. | [optional] 
**delayed_post_at** | **str** | If a timestamp is given, the topic will not be published until that time. | [optional] 
**lock_at** | **str** | If a timestamp is given, the topic will be scheduled to lock at the provided timestamp. If the timestamp is in the past, the topic will be locked. | [optional] 
**podcast_enabled** | **bool** | If true, the topic will have an associated podcast feed. | [optional] 
**podcast_has_student_posts** | **bool** | If true, the podcast will include posts from students as well. Implies podcast_enabled. | [optional] 
**require_initial_post** | **bool** | If true then a user may not respond to other replies until that user has made an initial reply. Defaults to false. | [optional] 
**is_announcement** | **bool** | If true, this topic is an announcement. It will appear in the announcement&#39;s section rather than the discussions section. This requires announcment-posting permissions. | [optional] 
**pinned** | **bool** | If true, this topic will be listed in the \&quot;Pinned Discussion\&quot; section | [optional] 
**position_after** | **str** | By default, discussions are sorted chronologically by creation date, you can pass the id of another topic to have this one show up after the other when they are listed. | [optional] 
**group_category_id** | **int** | If present, the topic will become a group discussion assigned to the group. | [optional] 
**allow_rating** | **bool** | If true, users will be allowed to rate entries. | [optional] 
**only_graders_can_rate** | **bool** | If true, only graders will be allowed to rate entries. | [optional] 
**sort_order** | **str** | Default sort order of the discussion. Accepted values are \&quot;asc\&quot;, \&quot;desc\&quot;. | [optional] 
**sort_order_locked** | **bool** | If true, users cannot choose their prefered sort order | [optional] 
**expanded** | **bool** | If true, thread will be expanded by default | [optional] 
**expanded_locked** | **bool** | If true, users cannot choose their prefered thread expansion setting | [optional] 
**sort_by_rating** | **bool** | (DEPRECATED) If true, entries will be sorted by rating. | [optional] 
**specific_sections** | **str** | A comma-separated list of sections ids to which the discussion topic should be made specific too.  If it is not desired to make the discussion topic specific to sections, then this parameter may be omitted or set to \&quot;all\&quot;.  Can only be present only on announcements and only those that are for a course (as opposed to a group). | [optional] 
**lock_comment** | **bool** | If is_announcement and lock_comment are true, ‘Allow Participants to Comment’ setting is disabled. | [optional] 
**assignment** | [**DiscussionTopicsUpdateRequestAssignment**](DiscussionTopicsUpdateRequestAssignment.md) |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.discussion_topics_update_request import DiscussionTopicsUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DiscussionTopicsUpdateRequest from a JSON string
discussion_topics_update_request_instance = DiscussionTopicsUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(DiscussionTopicsUpdateRequest.to_json())

# convert the object into a dict
discussion_topics_update_request_dict = discussion_topics_update_request_instance.to_dict()
# create an instance of DiscussionTopicsUpdateRequest from a dict
discussion_topics_update_request_from_dict = DiscussionTopicsUpdateRequest.from_dict(discussion_topics_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


