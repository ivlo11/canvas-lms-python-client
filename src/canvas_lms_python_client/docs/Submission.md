# Submission



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The submission&#39;s id | [optional] 
**assignment_id** | **int** | The submission&#39;s assignment id | [optional] 
**assignment** | [**Assignment**](Assignment.md) |  | [optional] 
**course** | [**Course**](Course.md) |  | [optional] 
**attempt** | **int** | This is the submission attempt number. | [optional] 
**body** | **str** | The content of the submission, if it was submitted directly in a text field. | [optional] 
**grade** | **str** | The grade for the submission, translated into the assignment grading scheme (so a letter grade, for example). | [optional] 
**grade_matches_current_submission** | **bool** | A boolean flag which is false if the student has re-submitted since the submission was last graded. | [optional] 
**html_url** | **str** | URL to the submission. This will require the user to log in. | [optional] 
**preview_url** | **str** | URL to the submission preview. This will require the user to log in. | [optional] 
**score** | **float** | The raw score | [optional] 
**submission_comments** | [**List[SubmissionComment]**](SubmissionComment.md) | Associated comments for a submission (optional) | [optional] 
**submission_type** | **str** | The types of submission ex: (&#39;online_text_entry&#39;|&#39;online_url&#39;|&#39;online_upload&#39;|&#39;online_quiz&#39;|&#39;media_recording&#39;|&#39;student_annotation&#39;) | [optional] 
**submitted_at** | **datetime** | The timestamp when the assignment was submitted | [optional] 
**url** | **str** | The URL of the submission (for &#39;online_url&#39; submissions). | [optional] 
**user_id** | **int** | The id of the user who created the submission | [optional] 
**grader_id** | **int** | The id of the user who graded the submission. This will be null for submissions that haven&#39;t been graded yet. It will be a positive number if a real user has graded the submission and a negative number if the submission was graded by a process (e.g. Quiz autograder and autograding LTI tools).  Specifically autograded quizzes set grader_id to the negative of the quiz id.  Submissions autograded by LTI tools set grader_id to the negative of the tool id. | [optional] 
**graded_at** | **datetime** |  | [optional] 
**user** | [**User**](User.md) |  | [optional] 
**late** | **bool** | Whether the submission was made after the applicable due date | [optional] 
**assignment_visible** | **bool** | Whether the assignment is visible to the user who submitted the assignment. Submissions where &#x60;assignment_visible&#x60; is false no longer count towards the student&#39;s grade and the assignment can no longer be accessed by the student. &#x60;assignment_visible&#x60; becomes false for submissions that do not have a grade and whose assignment is no longer assigned to the student&#39;s section. | [optional] 
**excused** | **bool** | Whether the assignment is excused.  Excused assignments have no impact on a user&#39;s grade. | [optional] 
**missing** | **bool** | Whether the assignment is missing. | [optional] 
**late_policy_status** | **str** | The status of the submission in relation to the late policy. Can be late, missing, extended, none, or null. | [optional] 
**points_deducted** | **float** | The amount of points automatically deducted from the score by the missing/late policy for a late or missing assignment. | [optional] 
**seconds_late** | **float** | The amount of time, in seconds, that an submission is late by. | [optional] 
**workflow_state** | **str** | The current state of the submission | [optional] 
**extra_attempts** | **float** | Extra submission attempts allowed for the given user and assignment. | [optional] 
**anonymous_id** | **str** | A unique short ID identifying this submission without reference to the owning user. Only included if the caller has administrator access for the current account. | [optional] 
**posted_at** | **datetime** | The date this submission was posted to the student, or nil if it has not been posted. | [optional] 
**read_status** | **str** | The read status of this submission for the given user (optional). Including read_status will mark submission(s) as read. | [optional] 
**redo_request** | **bool** | This indicates whether the submission has been reassigned by the instructor. | [optional] 
**cached_due_date** | **str** |  | [optional] 
**custom_grade_status_id** | **int** |  | [optional] 
**entered_grade** | **str** |  | [optional] 
**entered_score** | **float** |  | [optional] 
**grading_period_id** | **int** |  | [optional] 
**sticker** | **str** |  | [optional] 
**attachments** | **List[object]** |  | [optional] 
**external_tool_url** | **str** |  | [optional] 
**grading_status** | **str** |  | [optional] 
**group** | **object** |  | [optional] 
**media_comment** | **object** |  | [optional] 
**provisional_grades** | **List[object]** |  | [optional] 
**rubric_assessment** | **object** |  | [optional] 
**student_entered_score** | **float** |  | [optional] 
**submission_history** | **List[object]** |  | [optional] 
**submission_status** | **str** |  | [optional] 
**computed_current_score** | **float** |  | [optional] 
**computed_final_score** | **float** |  | [optional] 
**discussion_entries** | **List[object]** |  | [optional] 
**has_originality_report** | **bool** |  | [optional] 
**has_peer_review_submission** | **bool** |  | [optional] 
**integration_id** | **str** |  | [optional] 
**peer_review_submission** | **object** |  | [optional] 
**section_id** | **int** |  | [optional] 
**sis_user_id** | **str** |  | [optional] 
**submissions** | **List[object]** |  | [optional] 
**turnitin_data** | **object** |  | [optional] 
**unposted_current_score** | **float** |  | [optional] 
**unposted_final_score** | **float** |  | [optional] 
**context_type** | **str** |  | [optional] 
**conversation_id** | **int** |  | [optional] 
**course_id** | **int** |  | [optional] 
**created_at** | **str** |  | [optional] 
**discussion_topic_id** | **int** |  | [optional] 
**latest_messages** | **List[object]** |  | [optional] 
**message** | **str** |  | [optional] 
**message_id** | **object** |  | [optional] 
**notification_category** | **str** |  | [optional] 
**participant_count** | **int** |  | [optional] 
**private** | **bool** |  | [optional] 
**read_state** | **bool** |  | [optional] 
**require_initial_post** | **bool** |  | [optional] 
**root_discussion_entries** | **List[object]** |  | [optional] 
**submission_id** | **int** |  | [optional] 
**title** | **str** |  | [optional] 
**total_root_discussion_entries** | **int** |  | [optional] 
**type** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**user_has_posted** | **object** |  | [optional] 
**full_rubric_assessment** | **object** |  | [optional] 
**has_sub_assignment_submissions** | **bool** |  | [optional] 
**sub_assignment_submissions** | **List[object]** |  | [optional] 
**vericite_data** | **object** |  | [optional] 
**all_submissions** | **List[object]** |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.submission import Submission

# TODO update the JSON string below
json = "{}"
# create an instance of Submission from a JSON string
submission_instance = Submission.from_json(json)
# print the JSON string representation of the object
print(Submission.to_json())

# convert the object into a dict
submission_dict = submission_instance.to_dict()
# create an instance of Submission from a dict
submission_from_dict = Submission.from_dict(submission_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


