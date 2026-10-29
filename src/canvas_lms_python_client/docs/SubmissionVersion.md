# SubmissionVersion

A SubmissionVersion object contains all the fields that a Submission object does, plus additional fields prefixed with current_* new_* and previous_* described below.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assignment_id** | **int** | the id of the assignment this submissions is for | [optional] 
**assignment_name** | **str** | the name of the assignment this submission is for | [optional] 
**body** | **str** | the body text of the submission | [optional] 
**current_grade** | **str** | the most up to date grade for the current version of this submission | [optional] 
**current_graded_at** | **datetime** | the latest time stamp for the grading of this submission | [optional] 
**current_grader** | **str** | the name of the most recent grader for this submission | [optional] 
**grade_matches_current_submission** | **bool** | boolean indicating whether the grade is equal to the current submission grade | [optional] 
**graded_at** | **datetime** | time stamp for the grading of this version of the submission | [optional] 
**grader** | **str** | the name of the user who graded this version of the submission | [optional] 
**grader_id** | **int** | the user id of the user who graded this version of the submission | [optional] 
**id** | **int** | the id of the submission of which this is a version | [optional] 
**new_grade** | **str** | the updated grade provided in this version of the submission | [optional] 
**new_graded_at** | **datetime** | the timestamp for the grading of this version of the submission (alias for graded_at) | [optional] 
**new_grader** | **str** | alias for &#39;grader&#39; | [optional] 
**previous_grade** | **str** | the grade for the submission version immediately preceding this one | [optional] 
**previous_graded_at** | **datetime** | the timestamp for the grading of the submission version immediately preceding this one | [optional] 
**previous_grader** | **str** | the name of the grader who graded the version of this submission immediately preceding this one | [optional] 
**score** | **int** | the score for this version of the submission | [optional] 
**user_name** | **str** | the name of the student who created this submission | [optional] 
**submission_type** | **str** | the type of submission | [optional] 
**url** | **str** | the url of the submission, if there is one | [optional] 
**user_id** | **int** | the user ID of the student who created this submission | [optional] 
**workflow_state** | **str** | the state of the submission at this version | [optional] 

## Example

```python
from canvas_lms_python_client.models.submission_version import SubmissionVersion

# TODO update the JSON string below
json = "{}"
# create an instance of SubmissionVersion from a JSON string
submission_version_instance = SubmissionVersion.from_json(json)
# print the JSON string representation of the object
print(SubmissionVersion.to_json())

# convert the object into a dict
submission_version_dict = submission_version_instance.to_dict()
# create an instance of SubmissionVersion from a dict
submission_version_from_dict = SubmissionVersion.from_dict(submission_version_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


