# SubmissionsCreateRequestSubmission


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_comment** | **bool** | [Boolean] Whether or not this comment should be sent to the entire group (defaults to false). Ignored if this is not a group assignment or if no text_comment is provided. | [optional] 
**submission_type** | **str** | [Required, String, \&quot;online_text_entry\&quot;|\&quot;online_url\&quot;|\&quot;online_upload\&quot;|\&quot;media_recording\&quot;|\&quot;basic_lti_launch\&quot;|\&quot;student_annotation\&quot;] The type of submission being made. The assignment submission_types must include this submission type as an allowed option, or the submission will be rejected with a 400 error.  The submission_type given determines which of the following parameters is used. For instance, to submit a URL, +submission[submission_type]+ must be set to \&quot;online_url\&quot;, otherwise the +submission[url]+ parameter will be ignored.  \&quot;basic_lti_launch\&quot; requires the assignment submission_type \&quot;online\&quot; or \&quot;external_tool\&quot; | 
**body** | **str** | [String] Submit the assignment as an HTML document snippet. Note this HTML snippet will be sanitized using the same ruleset as a submission made from the Canvas web UI. The sanitized HTML will be returned in the response as the submission body. Requires a submission_type of \&quot;online_text_entry\&quot;. | [optional] 
**url** | **str** | [String] Submit the assignment as a URL. The URL scheme must be \&quot;http\&quot; or \&quot;https\&quot;, no \&quot;ftp\&quot; or other URL schemes are allowed. If no scheme is given (e.g. \&quot;www.example.com\&quot;) then \&quot;http\&quot; will be assumed. Requires a submission_type of \&quot;online_url\&quot; or \&quot;basic_lti_launch\&quot;. | [optional] 
**file_ids** | **str** | [] [Integer] Submit the assignment as a set of one or more previously uploaded files residing in the submitting user&#39;s files section (or the group&#39;s files section, for group assignments).  To upload a new file to submit, see the submissions {api:SubmissionsApiController#create_file Upload a file API}.  Requires a submission_type of \&quot;online_upload\&quot;. | [optional] 
**media_comment_id** | **str** | [String] The media comment id to submit. Media comment ids can be submitted via this API, however, note that there is not yet an API to generate or list existing media comments, so this functionality is currently of limited use.  Requires a submission_type of \&quot;media_recording\&quot;. | [optional] 
**media_comment_type** | **str** | [String, \&quot;audio\&quot;|\&quot;video\&quot;] The type of media comment being submitted. | [optional] 
**user_id** | **int** | [Integer] Submit on behalf of the given user. Requires grading permission. | [optional] 
**annotatable_attachment_id** | **int** | [Integer] The Attachment ID of the document being annotated. This should match the annotatable_attachment_id on the assignment.  Requires a submission_type of \&quot;student_annotation\&quot;. | [optional] 
**submitted_at** | **str** | [DateTime] Choose the time the submission is listed as submitted at.  Requires grading permission. | [optional] 

## Example

```python
from canvas_lms_python_client.models.submissions_create_request_submission import SubmissionsCreateRequestSubmission

# TODO update the JSON string below
json = "{}"
# create an instance of SubmissionsCreateRequestSubmission from a JSON string
submissions_create_request_submission_instance = SubmissionsCreateRequestSubmission.from_json(json)
# print the JSON string representation of the object
print(SubmissionsCreateRequestSubmission.to_json())

# convert the object into a dict
submissions_create_request_submission_dict = submissions_create_request_submission_instance.to_dict()
# create an instance of SubmissionsCreateRequestSubmission from a dict
submissions_create_request_submission_from_dict = SubmissionsCreateRequestSubmission.from_dict(submissions_create_request_submission_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


