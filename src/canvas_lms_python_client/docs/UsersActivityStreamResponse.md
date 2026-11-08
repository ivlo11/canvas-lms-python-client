# UsersActivityStreamResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**announcement_id** | **int** |  | [optional] 
**assessment_request_id** | **int** |  | [optional] 
**assignment** | **object** |  | [optional] 
**assignment_id** | **int** |  | [optional] 
**attempt** | **int** |  | [optional] 
**author_name** | **str** |  | [optional] 
**body** | **str** |  | [optional] 
**cached_due_date** | **str** |  | [optional] 
**collaboration_id** | **int** |  | [optional] 
**context_type** | **str** |  | [optional] 
**conversation_id** | **int** |  | [optional] 
**course** | **object** |  | [optional] 
**course_id** | **int** |  | [optional] 
**created_at** | **str** |  | [optional] 
**custom_grade_status_id** | **object** |  | [optional] 
**discussion_entries** | **List[object]** |  | [optional] 
**discussion_topic_id** | **int** |  | [optional] 
**entered_grade** | **str** |  | [optional] 
**entered_score** | **float** |  | [optional] 
**excused** | **bool** |  | [optional] 
**extra_attempts** | **object** |  | [optional] 
**grade** | **str** |  | [optional] 
**grade_matches_current_submission** | **bool** |  | [optional] 
**graded_at** | **str** |  | [optional] 
**grader_id** | **int** |  | [optional] 
**grading_period_id** | **int** |  | [optional] 
**group_id** | **int** |  | [optional] 
**html_url** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**late** | **bool** |  | [optional] 
**late_policy_status** | **object** |  | [optional] 
**latest_messages** | **List[object]** |  | [optional] 
**message** | **str** |  | [optional] 
**message_id** | **int** |  | [optional] 
**missing** | **bool** |  | [optional] 
**notification_category** | **str** |  | [optional] 
**participant_count** | **int** |  | [optional] 
**points_deducted** | **float** |  | [optional] 
**posted_at** | **str** |  | [optional] 
**preview_url** | **str** |  | [optional] 
**private** | **bool** |  | [optional] 
**read_state** | **bool** |  | [optional] 
**redo_request** | **bool** |  | [optional] 
**require_initial_post** | **bool** |  | [optional] 
**root_discussion_entries** | **List[object]** |  | [optional] 
**score** | **float** |  | [optional] 
**seconds_late** | **int** |  | [optional] 
**sticker** | **object** |  | [optional] 
**submission_comments** | **List[object]** |  | [optional] 
**submission_id** | **int** |  | [optional] 
**submission_type** | **str** |  | [optional] 
**submitted_at** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**total_root_discussion_entries** | **int** |  | [optional] 
**type** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**user** | **object** |  | [optional] 
**user_has_posted** | **bool** |  | [optional] 
**user_id** | **int** |  | [optional] 
**web_conference_id** | **int** |  | [optional] 
**workflow_state** | **str** |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.users_activity_stream_response import UsersActivityStreamResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UsersActivityStreamResponse from a JSON string
users_activity_stream_response_instance = UsersActivityStreamResponse.from_json(json)
# print the JSON string representation of the object
print(UsersActivityStreamResponse.to_json())

# convert the object into a dict
users_activity_stream_response_dict = users_activity_stream_response_instance.to_dict()
# create an instance of UsersActivityStreamResponse from a dict
users_activity_stream_response_from_dict = UsersActivityStreamResponse.from_dict(users_activity_stream_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


