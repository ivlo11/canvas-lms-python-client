# DiscussionTopic

A discussion topic

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The ID of this topic. | [optional] 
**title** | **str** | The topic title. | [optional] 
**message** | **str** | The HTML content of the message body. | [optional] 
**html_url** | **str** | The URL to the discussion topic in canvas. | [optional] 
**posted_at** | **datetime** | The datetime the topic was posted. If it is null it hasn&#39;t been posted yet. (see delayed_post_at) | [optional] 
**last_reply_at** | **datetime** | The datetime for when the last reply was in the topic. | [optional] 
**require_initial_post** | **bool** | If true then a user may not respond to other replies until that user has made an initial reply. Defaults to false. | [optional] 
**user_can_see_posts** | **bool** | Whether or not posts in this topic are visible to the user. | [optional] 
**discussion_subentry_count** | **int** | The count of entries in the topic. | [optional] 
**read_state** | **str** | The read_state of the topic for the current user, &#39;read&#39; or &#39;unread&#39;. | [optional] 
**unread_count** | **int** | The count of unread entries of this topic for the current user. | [optional] 
**subscribed** | **bool** | Whether or not the current user is subscribed to this topic. | [optional] 
**subscription_hold** | **str** | (Optional) Why the user cannot subscribe to this topic. Only one reason will be returned even if multiple apply. Can be one of: &#39;initial_post_required&#39;: The user must post a reply first; &#39;not_in_group_set&#39;: The user is not in the group set for this graded group discussion; &#39;not_in_group&#39;: The user is not in this topic&#39;s group; &#39;topic_is_announcement&#39;: This topic is an announcement | [optional] 
**assignment_id** | **int** | The unique identifier of the assignment if the topic is for grading, otherwise null. | [optional] 
**delayed_post_at** | **datetime** | The datetime to publish the topic (if not right away). | [optional] 
**published** | **bool** | Whether this discussion topic is published (true) or draft state (false) | [optional] 
**lock_at** | **datetime** | The datetime to lock the topic (if ever). | [optional] 
**locked** | **bool** | Whether or not the discussion is &#39;closed for comments&#39;. | [optional] 
**pinned** | **bool** | Whether or not the discussion has been &#39;pinned&#39; by an instructor | [optional] 
**locked_for_user** | **bool** | Whether or not this is locked for the user. | [optional] 
**lock_info** | [**LockInfo**](LockInfo.md) |  | [optional] 
**lock_explanation** | **str** | (Optional) An explanation of why this is locked for the user. Present when locked_for_user is true. | [optional] 
**user_name** | **str** | The username of the topic creator. | [optional] 
**topic_children** | **List[int]** | DEPRECATED An array of topic_ids for the group discussions the user is a part of. | [optional] 
**group_topic_children** | **List[object]** | An array of group discussions the user is a part of. Fields include: id, group_id | [optional] 
**root_topic_id** | **int** | If the topic is for grading and a group assignment this will point to the original topic in the course. | [optional] 
**podcast_url** | **str** | If the topic is a podcast topic this is the feed url for the current user. | [optional] 
**discussion_type** | **str** | The type of discussion. Values are &#39;side_comment&#39; or &#39;not_threaded&#39;, for discussions that only allow one level of nested comments, and &#39;threaded&#39; for fully threaded discussions. | [optional] 
**group_category_id** | **int** | The unique identifier of the group category if the topic is a group discussion, otherwise null. | [optional] 
**attachments** | [**List[FileAttachment]**](FileAttachment.md) | Array of file attachments. | [optional] 
**permissions** | **object** | The current user&#39;s permissions on this topic. | [optional] 
**allow_rating** | **bool** | Whether or not users can rate entries in this topic. | [optional] 
**only_graders_can_rate** | **bool** | Whether or not grade permissions are required to rate entries. | [optional] 
**sort_by_rating** | **bool** | DEPRECATED, Whether or not entries should be sorted by rating. | [optional] 
**sort_order** | **str** | How entries should be sorted by default. | [optional] 
**sort_order_locked** | **bool** | Can users decide their preferred sort order. | [optional] 
**expand** | **bool** | Threaded replies should be expanded by default. | [optional] 
**expand_locked** | **bool** | Can users decide their preferred thread expand setting. | [optional] 
**anonymous_state** | **str** |  | [optional] 
**author** | **object** |  | [optional] 
**can_group** | **bool** |  | [optional] 
**can_lock** | **bool** |  | [optional] 
**can_unpublish** | **bool** |  | [optional] 
**comments_disabled** | **bool** |  | [optional] 
**context_code** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**expanded** | **bool** |  | [optional] 
**expanded_locked** | **bool** |  | [optional] 
**is_announcement** | **bool** |  | [optional] 
**is_section_specific** | **bool** |  | [optional] 
**podcast_has_student_posts** | **bool** |  | [optional] 
**position** | **int** |  | [optional] 
**sections** | **List[object]** |  | [optional] 
**summary_enabled** | **bool** |  | [optional] 
**todo_date** | **str** |  | [optional] 
**ungraded_discussion_overrides** | **List[object]** |  | [optional] 
**url** | **str** |  | [optional] 
**new_positions** | **object** |  | [optional] 
**assignment** | **object** |  | [optional] 
**in_paced_course** | **bool** |  | [optional] 
**user_count** | **int** |  | [optional] 
**is_checkpointed** | **bool** |  | [optional] 
**reply_to_entry_required_count** | **int** |  | [optional] 
**attachment_id** | **int** |  | [optional] 
**cloned_item_id** | **int** |  | [optional] 
**context_id** | **int** |  | [optional] 
**context_type** | **str** |  | [optional] 
**could_be_locked** | **bool** |  | [optional] 
**deleted_at** | **str** |  | [optional] 
**edited_at** | **object** |  | [optional] 
**editor_id** | **int** |  | [optional] 
**external_feed_id** | **int** |  | [optional] 
**is_anonymous_author** | **bool** |  | [optional] 
**last_assignment_id** | **int** |  | [optional] 
**migration_id** | **str** |  | [optional] 
**old_assignment_id** | **int** |  | [optional] 
**only_visible_to_overrides** | **bool** |  | [optional] 
**ordered_pinned_posts** | **List[object]** |  | [optional] 
**podcast_enabled** | **bool** |  | [optional] 
**root_account_id** | **int** |  | [optional] 
**subtopics_refreshed_at** | **str** |  | [optional] 
**unlock_at** | **object** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**user** | **object** |  | [optional] 
**user_id** | **int** |  | [optional] 
**workflow_state** | **str** |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.discussion_topic import DiscussionTopic

# TODO update the JSON string below
json = "{}"
# create an instance of DiscussionTopic from a JSON string
discussion_topic_instance = DiscussionTopic.from_json(json)
# print the JSON string representation of the object
print(DiscussionTopic.to_json())

# convert the object into a dict
discussion_topic_dict = discussion_topic_instance.to_dict()
# create an instance of DiscussionTopic from a dict
discussion_topic_from_dict = DiscussionTopic.from_dict(discussion_topic_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


