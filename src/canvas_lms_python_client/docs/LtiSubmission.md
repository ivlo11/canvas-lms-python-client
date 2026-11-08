# LtiSubmission



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lti_course_id** | **str** |  | [optional] 
**course_id** | **int** |  | [optional] 
**assignment_id** | **int** | The submission&#39;s assignment id | [optional] 
**attempt** | **int** | This is the submission attempt number. | [optional] 
**body** | **str** | The content of the submission, if it was submitted directly in a text field. | [optional] 
**submission_type** | **str** | The types of submission ex: (&#39;online_text_entry&#39;|&#39;online_url&#39;|&#39;online_upload&#39;|&#39;media_recording&#39;|&#39;student_annotation&#39;) | [optional] 
**submitted_at** | **datetime** | The timestamp when the assignment was submitted | [optional] 
**url** | **str** | The URL of the submission (for &#39;online_url&#39; submissions). | [optional] 
**user_id** | [**LtiSubmissionUserId**](LtiSubmissionUserId.md) |  | [optional] 
**eula_agreement_timestamp** | [**LtiSubmissionEulaAgreementTimestamp**](LtiSubmissionEulaAgreementTimestamp.md) |  | [optional] 
**workflow_state** | **str** | The current state of the submission | [optional] 
**attachments** | [**List[File]**](File.md) | Files that are attached to the submission | [optional] 
**id** | **int** |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.lti_submission import LtiSubmission

# TODO update the JSON string below
json = "{}"
# create an instance of LtiSubmission from a JSON string
lti_submission_instance = LtiSubmission.from_json(json)
# print the JSON string representation of the object
print(LtiSubmission.to_json())

# convert the object into a dict
lti_submission_dict = lti_submission_instance.to_dict()
# create an instance of LtiSubmission from a dict
lti_submission_from_dict = LtiSubmission.from_dict(lti_submission_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


