# Assignment



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | the ID of the assignment | [optional] 
**name** | **str** | the name of the assignment | [optional] 
**description** | **str** | the assignment description, in an HTML fragment | [optional] 
**created_at** | **datetime** | The time at which this assignment was originally created | [optional] 
**updated_at** | **datetime** | The time at which this assignment was last modified in any way | [optional] 
**due_at** | **datetime** | the due date for the assignment. returns null if not present. NOTE: If this assignment has assignment overrides, this field will be the due date as it applies to the user requesting information from the API. | [optional] 
**lock_at** | **datetime** | the lock date (assignment is locked after this date). returns null if not present. NOTE: If this assignment has assignment overrides, this field will be the lock date as it applies to the user requesting information from the API. | [optional] 
**unlock_at** | **datetime** | the unlock date (assignment is unlocked after this date) returns null if not present NOTE: If this assignment has assignment overrides, this field will be the unlock date as it applies to the user requesting information from the API. | [optional] 
**has_overrides** | **bool** | whether this assignment has overrides | [optional] 
**all_dates** | [**List[AssignmentDate]**](AssignmentDate.md) | (Optional) all dates associated with the assignment, if applicable | [optional] 
**course_id** | **int** | the ID of the course the assignment belongs to | [optional] 
**html_url** | **str** | the URL to the assignment&#39;s web page | [optional] 
**submissions_download_url** | **str** | the URL to download all submissions as a zip | [optional] 
**assignment_group_id** | **int** | the ID of the assignment&#39;s group | [optional] 
**due_date_required** | **bool** | Boolean flag indicating whether the assignment requires a due date based on the account level setting | [optional] 
**allowed_extensions** | **List[str]** | Allowed file extensions, which take effect if submission_types includes &#39;online_upload&#39;. | [optional] 
**max_name_length** | **int** | An integer indicating the maximum length an assignment&#39;s name may be | [optional] 
**turnitin_enabled** | **bool** | Boolean flag indicating whether or not Turnitin has been enabled for the assignment. NOTE: This flag will not appear unless your account has the Turnitin plugin available | [optional] 
**vericite_enabled** | **bool** | Boolean flag indicating whether or not VeriCite has been enabled for the assignment. NOTE: This flag will not appear unless your account has the VeriCite plugin available | [optional] 
**turnitin_settings** | [**TurnitinSettings**](TurnitinSettings.md) |  | [optional] 
**grade_group_students_individually** | **bool** | If this is a group assignment, boolean flag indicating whether or not students will be graded individually. | [optional] 
**external_tool_tag_attributes** | [**ExternalToolTagAttributes**](ExternalToolTagAttributes.md) |  | [optional] 
**peer_reviews** | **bool** | Boolean indicating if peer reviews are required for this assignment | [optional] 
**automatic_peer_reviews** | **bool** | Boolean indicating peer reviews are assigned automatically. If false, the teacher is expected to manually assign peer reviews. | [optional] 
**peer_review_count** | **int** | Integer representing the amount of reviews each user is assigned. NOTE: This key is NOT present unless you have automatic_peer_reviews set to true. | [optional] 
**peer_reviews_assign_at** | **datetime** | String representing a date the reviews are due by. Must be a date that occurs after the default due date. If blank, or date is not after the assignment&#39;s due date, the assignment&#39;s due date will be used. NOTE: This key is NOT present unless you have automatic_peer_reviews set to true. | [optional] 
**intra_group_peer_reviews** | **bool** | Boolean representing whether or not members from within the same group on a group assignment can be assigned to peer review their own group&#39;s work | [optional] 
**group_category_id** | **int** | The ID of the assignment’s group set, if this is a group assignment. For group discussions, set group_category_id on the discussion topic, not the linked assignment. | [optional] 
**needs_grading_count** | **int** | if the requesting user has grading rights, the number of submissions that need grading. | [optional] 
**needs_grading_count_by_section** | [**List[NeedsGradingCount]**](NeedsGradingCount.md) | if the requesting user has grading rights and the &#39;needs_grading_count_by_section&#39; flag is specified, the number of submissions that need grading split out by section. NOTE: This key is NOT present unless you pass the &#39;needs_grading_count_by_section&#39; argument as true.  ANOTHER NOTE: it&#39;s possible to be enrolled in multiple sections, and if a student is setup that way they will show an assignment that needs grading in multiple sections (effectively the count will be duplicated between sections) | [optional] 
**position** | **int** | the sorting order of the assignment in the group | [optional] 
**post_to_sis** | **bool** | (optional, present if Sync Grades to SIS feature is enabled) | [optional] 
**integration_id** | **str** | (optional, Third Party unique identifier for Assignment) | [optional] 
**integration_data** | **object** | (optional, Third Party integration data for assignment) | [optional] 
**points_possible** | **float** | the maximum points possible for the assignment | [optional] 
**submission_types** | **List[str]** | the types of submissions allowed for this assignment list containing one or more of the following: &#39;discussion_topic&#39;, &#39;online_quiz&#39;, &#39;on_paper&#39;, &#39;none&#39;, &#39;external_tool&#39;, &#39;online_text_entry&#39;, &#39;online_url&#39;, &#39;online_upload&#39;, &#39;media_recording&#39;, &#39;student_annotation&#39; | [optional] 
**has_submitted_submissions** | **bool** | If true, the assignment has been submitted to by at least one student | [optional] 
**grading_type** | **str** | The type of grading the assignment receives; one of &#39;pass_fail&#39;, &#39;percent&#39;, &#39;letter_grade&#39;, &#39;gpa_scale&#39;, &#39;points&#39; | [optional] 
**grading_standard_id** | **int** | The id of the grading standard being applied to this assignment. Valid if grading_type is &#39;letter_grade&#39; or &#39;gpa_scale&#39;. | [optional] 
**published** | **bool** | Whether the assignment is published | [optional] 
**unpublishable** | **bool** | Whether the assignment&#39;s &#39;published&#39; state can be changed to false. Will be false if there are student submissions for the assignment. | [optional] 
**only_visible_to_overrides** | **bool** | Whether the assignment is only visible to overrides. | [optional] 
**locked_for_user** | **bool** | Whether or not this is locked for the user. | [optional] 
**lock_info** | [**LockInfo**](LockInfo.md) |  | [optional] 
**lock_explanation** | **str** | (Optional) An explanation of why this is locked for the user. Present when locked_for_user is true. | [optional] 
**quiz_id** | **int** | (Optional) id of the associated quiz (applies only when submission_types is [&#39;online_quiz&#39;]) | [optional] 
**anonymous_submissions** | **bool** | (Optional) whether anonymous submissions are accepted (applies only to quiz assignments) | [optional] 
**discussion_topic** | [**DiscussionTopic**](DiscussionTopic.md) |  | [optional] 
**freeze_on_copy** | **bool** | (Optional) Boolean indicating if assignment will be frozen when it is copied. NOTE: This field will only be present if the AssignmentFreezer plugin is available for your account. | [optional] 
**frozen** | **bool** | (Optional) Boolean indicating if assignment is frozen for the calling user. NOTE: This field will only be present if the AssignmentFreezer plugin is available for your account. | [optional] 
**frozen_attributes** | **List[str]** | (Optional) Array of frozen attributes for the assignment. Only account administrators currently have permission to change an attribute in this list. Will be empty if no attributes are frozen for this assignment. Possible frozen attributes are: title, description, lock_at, points_possible, grading_type, submission_types, assignment_group_id, allowed_extensions, group_category_id, notify_of_update, peer_reviews NOTE: This field will only be present if the AssignmentFreezer plugin is available for your account. | [optional] 
**submission** | [**Submission**](Submission.md) |  | [optional] 
**use_rubric_for_grading** | **bool** | (Optional) If true, the rubric is directly tied to grading the assignment. Otherwise, it is only advisory. Included if there is an associated rubric. | [optional] 
**rubric_settings** | **object** | (Optional) An object describing the basic attributes of the rubric, including the point total. Included if there is an associated rubric. | [optional] 
**rubric** | [**List[RubricCriteria]**](RubricCriteria.md) | (Optional) A list of scoring criteria and ratings for each rubric criterion. Included if there is an associated rubric. | [optional] 
**assignment_visibility** | **List[int]** | (Optional) If &#39;assignment_visibility&#39; is included in the &#39;include&#39; parameter, includes an array of student IDs who can see this assignment. | [optional] 
**overrides** | [**List[AssignmentOverride]**](AssignmentOverride.md) | (Optional) If &#39;overrides&#39; is included in the &#39;include&#39; parameter, includes an array of assignment override objects. | [optional] 
**omit_from_final_grade** | **bool** | (Optional) If true, the assignment will be omitted from the student&#39;s final grade | [optional] 
**hide_in_gradebook** | **bool** | (Optional) If true, the assignment will not be shown in any gradebooks | [optional] 
**moderated_grading** | **bool** | Boolean indicating if the assignment is moderated. | [optional] 
**grader_count** | **int** | The maximum number of provisional graders who may issue grades for this assignment. Only relevant for moderated assignments. Must be a positive value, and must be set to 1 if the course has fewer than two active instructors. Otherwise, the maximum value is the number of active instructors in the course minus one, or 10 if the course has more than 11 active instructors. | [optional] 
**final_grader_id** | **int** | The user ID of the grader responsible for choosing final grades for this assignment. Only relevant for moderated assignments. | [optional] 
**grader_comments_visible_to_graders** | **bool** | Boolean indicating if provisional graders&#39; comments are visible to other provisional graders. Only relevant for moderated assignments. | [optional] 
**graders_anonymous_to_graders** | **bool** | Boolean indicating if provisional graders&#39; identities are hidden from other provisional graders. Only relevant for moderated assignments with grader_comments_visible_to_graders set to true. | [optional] 
**grader_names_visible_to_final_grader** | **bool** | Boolean indicating if provisional grader identities are visible to the final grader. Only relevant for moderated assignments. | [optional] 
**anonymous_grading** | **bool** | Boolean indicating if the assignment is graded anonymously. If true, graders cannot see student identities. | [optional] 
**allowed_attempts** | **int** | The number of submission attempts a student can make for this assignment. -1 is considered unlimited. | [optional] 
**post_manually** | **bool** | Whether the assignment has manual posting enabled. Only relevant for courses using New Gradebook. | [optional] 
**score_statistics** | [**ScoreStatistic**](ScoreStatistic.md) |  | [optional] 
**can_submit** | **bool** | (Optional) If retrieving a single assignment and &#39;can_submit&#39; is included in the &#39;include&#39; parameter, flags whether user has the right to submit the assignment (i.e. checks enrollment dates, submission types, locked status, attempts remaining, etc...). Including &#39;can submit&#39; automatically includes &#39;submission&#39; in the include parameter. Not available when observed_users are included. | [optional] 
**ab_guid** | **List[str]** | (Optional) The academic benchmark(s) associated with the assignment or the assignment&#39;s rubric. Only included if &#39;ab_guid&#39; is included in the &#39;include&#39; parameter. | [optional] 
**annotatable_attachment_id** | **int** | The id of the attachment to be annotated by students. Relevant only if submission_types includes &#39;student_annotation&#39;. | [optional] 
**anonymize_students** | **bool** | (Optional) Boolean indicating whether student names are anonymized | [optional] 
**require_lockdown_browser** | **bool** | (Optional) Boolean indicating whether the Respondus LockDown Browser® is required for this assignment. | [optional] 
**important_dates** | **bool** | (Optional) Boolean indicating whether this assignment has important dates. | [optional] 
**muted** | **bool** | (Optional, Deprecated) Boolean indicating whether notifications are muted for this assignment. | [optional] 
**anonymous_peer_reviews** | **bool** | Boolean indicating whether peer reviews are anonymous. | [optional] 
**anonymous_instructor_annotations** | **bool** | Boolean indicating whether instructor anotations are anonymous. | [optional] 
**graded_submissions_exist** | **bool** | Boolean indicating whether this assignment has graded submissions. | [optional] 
**is_quiz_assignment** | **bool** | Boolean indicating whether this is a quiz lti assignment. | [optional] 
**in_closed_grading_period** | **bool** | Boolean indicating whether this assignment is in a closed grading period. | [optional] 
**can_duplicate** | **bool** | Boolean indicating whether this assignment can be duplicated. | [optional] 
**original_course_id** | **int** | If this assignment is a duplicate, it is the original assignment&#39;s course_id | [optional] 
**original_assignment_id** | **int** | If this assignment is a duplicate, it is the original assignment&#39;s id | [optional] 
**original_lti_resource_link_id** | **int** | If this assignment is a duplicate, it is the original assignment&#39;s lti_resource_link_id | [optional] 
**original_assignment_name** | **str** | If this assignment is a duplicate, it is the original assignment&#39;s name | [optional] 
**original_quiz_id** | **int** | If this assignment is a duplicate, it is the original assignment&#39;s quiz_id | [optional] 
**workflow_state** | **str** | String indicating what state this assignment is in. | [optional] 

## Example

```python
from canvas_lms_python_client.models.assignment import Assignment

# TODO update the JSON string below
json = "{}"
# create an instance of Assignment from a JSON string
assignment_instance = Assignment.from_json(json)
# print the JSON string representation of the object
print(Assignment.to_json())

# convert the object into a dict
assignment_dict = assignment_instance.to_dict()
# create an instance of Assignment from a dict
assignment_from_dict = Assignment.from_dict(assignment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


