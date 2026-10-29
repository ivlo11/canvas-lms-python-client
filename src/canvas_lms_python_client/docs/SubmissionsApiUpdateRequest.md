# SubmissionsApiUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include** | **List[str]** | Associations to include with the submission. \&quot;submission_comments\&quot; is always included by default. - \&quot;submission_comments\&quot;: Comments on the submission (always included) - \&quot;visibility\&quot;: Whether the assignment is visible to the owner of the submission - \&quot;sub_assignment_submissions\&quot;: Sub-assignment submissions for discussion checkpoints - \&quot;peer_review_submissions\&quot;: Peer review submission data when peer review allocation and grading is enabled - \&quot;provisional_grades\&quot;: Provisional grades (only available for moderated assignments) - \&quot;group\&quot;: Group information (id and name) for group assignments | [optional] 
**prefer_points_over_scheme** | **bool** | Treat posted_grade as points if the value matches a grading scheme value | [optional] 
**comment** | [**SubmissionsApiUpdateRequestComment**](SubmissionsApiUpdateRequestComment.md) |  | [optional] 
**submission** | [**SubmissionsApiUpdateRequestSubmission**](SubmissionsApiUpdateRequestSubmission.md) |  | [optional] 
**rubric_assessment** | [**SubmissionsApiUpdateRequestRubricAssessment**](SubmissionsApiUpdateRequestRubricAssessment.md) |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.submissions_api_update_request import SubmissionsApiUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SubmissionsApiUpdateRequest from a JSON string
submissions_api_update_request_instance = SubmissionsApiUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(SubmissionsApiUpdateRequest.to_json())

# convert the object into a dict
submissions_api_update_request_dict = submissions_api_update_request_instance.to_dict()
# create an instance of SubmissionsApiUpdateRequest from a dict
submissions_api_update_request_from_dict = SubmissionsApiUpdateRequest.from_dict(submissions_api_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


