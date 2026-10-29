# AssignmentsApiCreateRequestAssignment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | [Required, String] The assignment name. | 
**position** | **int** | [Integer] The position of this assignment in the group when displaying assignment lists. | [optional] 
**submission_types** | **str** | [] [String, \&quot;online_quiz\&quot;|\&quot;none\&quot;|\&quot;on_paper\&quot;|\&quot;discussion_topic\&quot;|\&quot;external_tool\&quot;|\&quot;online_upload\&quot;|\&quot;online_text_entry\&quot;|\&quot;online_url\&quot;|\&quot;media_recording\&quot;|\&quot;student_annotation\&quot;] List of supported submission types for the assignment. Unless the assignment is allowing online submissions, the array should only have one element.  If not allowing online submissions, your options are:   \&quot;online_quiz\&quot;   \&quot;none\&quot;   \&quot;on_paper\&quot;   \&quot;discussion_topic\&quot;   \&quot;external_tool\&quot;  If you are allowing online submissions, you can have one or many allowed submission types:    \&quot;online_upload\&quot;   \&quot;online_text_entry\&quot;   \&quot;online_url\&quot;   \&quot;media_recording\&quot; (Only valid when the Kaltura plugin is enabled)   \&quot;student_annotation\&quot; | [optional] 
**allowed_extensions** | **str** | [] [String] Allowed extensions if submission_types includes \&quot;online_upload\&quot;  Example:   allowed_extensions: [\&quot;docx\&quot;,\&quot;ppt\&quot;] | [optional] 
**turnitin_enabled** | **bool** | [Boolean] Only applies when the Turnitin plugin is enabled for a course and the submission_types array includes \&quot;online_upload\&quot;. Toggles Turnitin submissions for the assignment. Will be ignored if Turnitin is not available for the course. | [optional] 
**vericite_enabled** | **bool** | [Boolean] Only applies when the VeriCite plugin is enabled for a course and the submission_types array includes \&quot;online_upload\&quot;. Toggles VeriCite submissions for the assignment. Will be ignored if VeriCite is not available for the course. | [optional] 
**turnitin_settings** | **str** | Settings to send along to turnitin. See Assignment object definition for format. | [optional] 
**integration_data** | **str** | Data used for SIS integrations. Requires admin-level token with the \&quot;Manage SIS\&quot; permission. JSON string required. | [optional] 
**integration_id** | **str** | Unique ID from third party integrations | [optional] 
**peer_reviews** | **bool** | [Boolean] If submission_types does not include external_tool,discussion_topic, online_quiz, or on_paper, determines whether or not peer reviews will be turned on for the assignment. | [optional] 
**automatic_peer_reviews** | **bool** | [Boolean] Whether peer reviews will be assigned automatically by Canvas or if teachers must manually assign peer reviews. Does not apply if peer reviews are not enabled. | [optional] 
**notify_of_update** | **bool** | [Boolean] If true, Canvas will send a notification to students in the class notifying them that the content has changed. | [optional] 
**group_category_id** | **int** | [Integer] If present, the assignment will become a group assignment assigned to the group. | [optional] 
**grade_group_students_individually** | **int** | [Integer] If this is a group assignment, teachers have the options to grade students individually. If false, Canvas will apply the assignment&#39;s score to each member of the group. If true, the teacher can manually assign scores to each member of the group. | [optional] 
**external_tool_tag_attributes** | **str** | Hash of external tool parameters if submission_types is [\&quot;external_tool\&quot;]. See Assignment object definition for format. | [optional] 
**points_possible** | **float** | [Float] The maximum points possible on the assignment. | [optional] 
**grading_type** | **str** | [\&quot;pass_fail\&quot;|\&quot;percent\&quot;|\&quot;letter_grade\&quot;|\&quot;gpa_scale\&quot;|\&quot;points\&quot;|\&quot;not_graded\&quot;] The strategy used for grading the assignment. The assignment defaults to \&quot;points\&quot; if this field is omitted. | [optional] 
**due_at** | **str** | [DateTime] The day/time the assignment is due. Must be between the lock dates if there are lock dates. Accepts times in ISO 8601 format, e.g. 2014-10-21T18:48:00Z. | [optional] 
**lock_at** | **str** | [DateTime] The day/time the assignment is locked after. Must be after the due date if there is a due date. Accepts times in ISO 8601 format, e.g. 2014-10-21T18:48:00Z. | [optional] 
**unlock_at** | **str** | [DateTime] The day/time the assignment is unlocked. Must be before the due date if there is a due date. Accepts times in ISO 8601 format, e.g. 2014-10-21T18:48:00Z. | [optional] 
**description** | **str** | [String] The assignment&#39;s description, supports HTML. | [optional] 
**assignment_group_id** | **int** | [Integer] The assignment group id to put the assignment in. Defaults to the top assignment group in the course. | [optional] 
**assignment_overrides** | **str** | [] [AssignmentOverride] List of overrides for the assignment. | [optional] 
**only_visible_to_overrides** | **bool** | [Boolean] Whether this assignment is only visible to overrides (Only useful if &#39;differentiated assignments&#39; account setting is on) | [optional] 
**published** | **bool** | [Boolean] Whether this assignment is published. (Only useful if &#39;draft state&#39; account setting is on) Unpublished assignments are not visible to students. | [optional] 
**grading_standard_id** | **int** | [Integer] The grading standard id to set for the course.  If no value is provided for this argument the current grading_standard will be un-set from this course. This will update the grading_type for the course to &#39;letter_grade&#39; unless it is already &#39;gpa_scale&#39;. | [optional] 
**omit_from_final_grade** | **bool** | [Boolean] Whether this assignment is counted towards a student&#39;s final grade. | [optional] 
**hide_in_gradebook** | **bool** | [Boolean] Whether this assignment is shown in the gradebook. | [optional] 
**quiz_lti** | **bool** | [Boolean] Whether this assignment should use the Quizzes 2 LTI tool. Sets the submission type to &#39;external_tool&#39; and configures the external tool attributes to use the Quizzes 2 LTI tool configured for this course. Has no effect if no Quizzes 2 LTI tool is configured. | [optional] 
**moderated_grading** | **bool** | [Boolean] Whether this assignment is moderated. | [optional] 
**grader_count** | **int** | [Integer] The maximum number of provisional graders who may issue grades for this assignment. Only relevant for moderated assignments. Must be a positive value, and must be set to 1 if the course has fewer than two active instructors. Otherwise, the maximum value is the number of active instructors in the course minus one, or 10 if the course has more than 11 active instructors. | [optional] 
**final_grader_id** | **int** | [Integer] The user ID of the grader responsible for choosing final grades for this assignment. Only relevant for moderated assignments. | [optional] 
**grader_comments_visible_to_graders** | **bool** | [Boolean] Boolean indicating if provisional graders&#39; comments are visible to other provisional graders. Only relevant for moderated assignments. | [optional] 
**graders_anonymous_to_graders** | **bool** | [Boolean] Boolean indicating if provisional graders&#39; identities are hidden from other provisional graders. Only relevant for moderated assignments. | [optional] 
**graders_names_visible_to_final_grader** | **bool** | [Boolean] Boolean indicating if provisional grader identities are visible to the the final grader. Only relevant for moderated assignments. | [optional] 
**anonymous_grading** | **bool** | [Boolean] Boolean indicating if the assignment is graded anonymously. If true, graders cannot see student identities. | [optional] 
**allowed_attempts** | **int** | [Integer] The number of submission attempts allowed for this assignment. Set to -1 for unlimited attempts. | [optional] 
**annotatable_attachment_id** | **int** | [Integer] The Attachment ID of the document being annotated.  Only applies when submission_types includes \&quot;student_annotation\&quot;. | [optional] 
**asset_processors** | **str** | [] [Array] Document processors for this assignment. New document processors can only be added via the interactive LTI Deep Linking flow (in a browser), not via API token or JWT authentication. Deletion of document processors (passing an empty array) is allowed via API. | [optional] 
**peer_review** | **str** | [peer_review_overrides][] [AssignmentOverride] List of overrides for the peer reviews. | [optional] 

## Example

```python
from canvas_lms_python_client.models.assignments_api_create_request_assignment import AssignmentsApiCreateRequestAssignment

# TODO update the JSON string below
json = "{}"
# create an instance of AssignmentsApiCreateRequestAssignment from a JSON string
assignments_api_create_request_assignment_instance = AssignmentsApiCreateRequestAssignment.from_json(json)
# print the JSON string representation of the object
print(AssignmentsApiCreateRequestAssignment.to_json())

# convert the object into a dict
assignments_api_create_request_assignment_dict = assignments_api_create_request_assignment_instance.to_dict()
# create an instance of AssignmentsApiCreateRequestAssignment from a dict
assignments_api_create_request_assignment_from_dict = AssignmentsApiCreateRequestAssignment.from_dict(assignments_api_create_request_assignment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


