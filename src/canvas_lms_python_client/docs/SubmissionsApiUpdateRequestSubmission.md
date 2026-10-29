# SubmissionsApiUpdateRequestSubmission


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**posted_grade** | **str** | [String] Assign a score to the submission, updating both the \&quot;score\&quot; and \&quot;grade\&quot; fields on the submission record. This parameter can be passed in a few different formats:  points:: A floating point or integral value, such as \&quot;13.5\&quot;. The grade   will be interpreted directly as the score of the assignment.   Values above assignment.points_possible are allowed, for awarding   extra credit. percentage:: A floating point value appended with a percent sign, such as    \&quot;40%\&quot;. The grade will be interpreted as a percentage score on the    assignment, where 100% &#x3D;&#x3D; assignment.points_possible. Values above 100%    are allowed, for awarding extra credit. letter grade:: A letter grade, following the assignment&#39;s defined letter    grading scheme. For example, \&quot;A-\&quot;. The resulting score will be the high    end of the defined range for the letter grade. For instance, if \&quot;B\&quot; is    defined as 86% to 84%, a letter grade of \&quot;B\&quot; will be worth 86%. The    letter grade will be rejected if the assignment does not have a defined    letter grading scheme. For more fine-grained control of scores, pass in    points or percentage rather than the letter grade. \&quot;pass/complete/fail/incomplete\&quot;:: A string value of \&quot;pass\&quot; or \&quot;complete\&quot;    will give a score of 100%. \&quot;fail\&quot; or \&quot;incomplete\&quot; will give a score of    0.  Note that assignments with grading_type of \&quot;pass_fail\&quot; can only be assigned a score of 0 or assignment.points_possible, nothing inbetween. If a posted_grade in the \&quot;points\&quot; or \&quot;percentage\&quot; format is sent, the grade will only be accepted if the grade equals one of those two values. | [optional] 
**excuse** | **bool** | [Boolean] Sets the \&quot;excused\&quot; status of an assignment. | [optional] 
**late_policy_status** | **str** | [String] Sets the late policy status to either \&quot;late\&quot;, \&quot;missing\&quot;, \&quot;extended\&quot;, \&quot;none\&quot;, or null.   NB: \&quot;extended\&quot; values can only be set in the UI when the \&quot;UI features for &#39;extended&#39; Submissions\&quot; Account Feature is on | [optional] 
**sticker** | **str** | [String, \&quot;apple\&quot;|\&quot;basketball\&quot;|\&quot;bell\&quot;|\&quot;book\&quot;|\&quot;bookbag\&quot;|\&quot;briefcase\&quot;|\&quot;bus\&quot;|\&quot;calendar\&quot;|\&quot;chem\&quot;|\&quot;design\&quot;|\&quot;pencil\&quot;|\&quot;beaker\&quot;|\&quot;paintbrush\&quot;|\&quot;computer\&quot;|\&quot;column\&quot;|\&quot;pen\&quot;|\&quot;tablet\&quot;|\&quot;telescope\&quot;|\&quot;calculator\&quot;|\&quot;paperclip\&quot;|\&quot;composite_notebook\&quot;|\&quot;scissors\&quot;|\&quot;ruler\&quot;|\&quot;clock\&quot;|\&quot;globe\&quot;|\&quot;grad\&quot;|\&quot;gym\&quot;|\&quot;mail\&quot;|\&quot;microscope\&quot;|\&quot;mouse\&quot;|\&quot;music\&quot;|\&quot;notebook\&quot;|\&quot;page\&quot;|\&quot;panda1\&quot;|\&quot;panda2\&quot;|\&quot;panda3\&quot;|\&quot;panda4\&quot;|\&quot;panda5\&quot;|\&quot;panda6\&quot;|\&quot;panda7\&quot;|\&quot;panda8\&quot;|\&quot;panda9\&quot;|\&quot;presentation\&quot;|\&quot;science\&quot;|\&quot;science2\&quot;|\&quot;star\&quot;|\&quot;tag\&quot;|\&quot;tape\&quot;|\&quot;target\&quot;|\&quot;trophy\&quot;] Sets the sticker for the submission. | [optional] 
**seconds_late_override** | **int** | [Integer] Sets the seconds late if late policy status is \&quot;late\&quot; | [optional] 
**peer_review** | **bool** | [Boolean] When true, updates the peer review sub assignment submission instead of the parent assignment submission. The parent assignment must have peer reviews enabled, the peer_review_allocation_and_grading feature flag must be enabled for the course, and the assignment must have an associated peer review sub assignment. If any of these conditions are not met, the API will return a 422 error. | [optional] 

## Example

```python
from canvas_lms_python_client.models.submissions_api_update_request_submission import SubmissionsApiUpdateRequestSubmission

# TODO update the JSON string below
json = "{}"
# create an instance of SubmissionsApiUpdateRequestSubmission from a JSON string
submissions_api_update_request_submission_instance = SubmissionsApiUpdateRequestSubmission.from_json(json)
# print the JSON string representation of the object
print(SubmissionsApiUpdateRequestSubmission.to_json())

# convert the object into a dict
submissions_api_update_request_submission_dict = submissions_api_update_request_submission_instance.to_dict()
# create an instance of SubmissionsApiUpdateRequestSubmission from a dict
submissions_api_update_request_submission_from_dict = SubmissionsApiUpdateRequestSubmission.from_dict(submissions_api_update_request_submission_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


