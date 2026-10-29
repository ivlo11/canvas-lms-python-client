# SubmissionsApiUpdateAnonymousRequestSubmission


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**posted_grade** | **str** | [String] Assign a score to the submission, updating both the \&quot;score\&quot; and \&quot;grade\&quot; fields on the submission record. This parameter can be passed in a few different formats:  points:: A floating point or integral value, such as \&quot;13.5\&quot;. The grade   will be interpreted directly as the score of the assignment.   Values above assignment.points_possible are allowed, for awarding   extra credit. percentage:: A floating point value appended with a percent sign, such as    \&quot;40%\&quot;. The grade will be interpreted as a percentage score on the    assignment, where 100% &#x3D;&#x3D; assignment.points_possible. Values above 100%    are allowed, for awarding extra credit. letter grade:: A letter grade, following the assignment&#39;s defined letter    grading scheme. For example, \&quot;A-\&quot;. The resulting score will be the high    end of the defined range for the letter grade. For instance, if \&quot;B\&quot; is    defined as 86% to 84%, a letter grade of \&quot;B\&quot; will be worth 86%. The    letter grade will be rejected if the assignment does not have a defined    letter grading scheme. For more fine-grained control of scores, pass in    points or percentage rather than the letter grade. \&quot;pass/complete/fail/incomplete\&quot;:: A string value of \&quot;pass\&quot; or \&quot;complete\&quot;    will give a score of 100%. \&quot;fail\&quot; or \&quot;incomplete\&quot; will give a score of    0.  Note that assignments with grading_type of \&quot;pass_fail\&quot; can only be assigned a score of 0 or assignment.points_possible, nothing inbetween. If a posted_grade in the \&quot;points\&quot; or \&quot;percentage\&quot; format is sent, the grade will only be accepted if the grade equals one of those two values. | [optional] 
**excuse** | **bool** | [Boolean] Sets the \&quot;excused\&quot; status of an assignment. | [optional] 
**late_policy_status** | **str** | [String] Sets the late policy status to either \&quot;late\&quot;, \&quot;missing\&quot;, \&quot;extended\&quot;, \&quot;none\&quot;, or null.   NB: \&quot;extended\&quot; values can only be set in the UI when the \&quot;UI features for &#39;extended&#39; Submissions\&quot; Account Feature is on | [optional] 
**seconds_late_override** | **int** | [Integer] Sets the seconds late if late policy status is \&quot;late\&quot; | [optional] 

## Example

```python
from canvas_lms_python_client.models.submissions_api_update_anonymous_request_submission import SubmissionsApiUpdateAnonymousRequestSubmission

# TODO update the JSON string below
json = "{}"
# create an instance of SubmissionsApiUpdateAnonymousRequestSubmission from a JSON string
submissions_api_update_anonymous_request_submission_instance = SubmissionsApiUpdateAnonymousRequestSubmission.from_json(json)
# print the JSON string representation of the object
print(SubmissionsApiUpdateAnonymousRequestSubmission.to_json())

# convert the object into a dict
submissions_api_update_anonymous_request_submission_dict = submissions_api_update_anonymous_request_submission_instance.to_dict()
# create an instance of SubmissionsApiUpdateAnonymousRequestSubmission from a dict
submissions_api_update_anonymous_request_submission_from_dict = SubmissionsApiUpdateAnonymousRequestSubmission.from_dict(submissions_api_update_anonymous_request_submission_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


