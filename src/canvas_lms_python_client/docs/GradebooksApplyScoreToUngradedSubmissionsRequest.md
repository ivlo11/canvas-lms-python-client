# GradebooksApplyScoreToUngradedSubmissionsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**percent** | **float** | A percentage value between 0 and 100 representing the percent score to apply. Exactly one of this parameter or the \&quot;excused\&quot; parameter (with a true value) must be specified. | [optional] 
**excused** | **bool** | If true, mark ungraded submissions as excused. Exactly one of this parameter (with a true value) or the \&quot;percent\&quot; parameter must be specified. | [optional] 
**mark_as_missing** | **bool** | If true, mark all affected submissions as missing in addition to issuing a grade. | [optional] 
**only_past_due** | **bool** | If true, only operate on submissions whose due date has passed. | [optional] 
**assignment_ids** | **List[str]** | An array of assignment ids to apply score to ungraded submissions. | 
**student_ids** | **List[str]** | An array of student ids to apply score to ungraded submissions. | 

## Example

```python
from canvas_lms_python_client.models.gradebooks_apply_score_to_ungraded_submissions_request import GradebooksApplyScoreToUngradedSubmissionsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GradebooksApplyScoreToUngradedSubmissionsRequest from a JSON string
gradebooks_apply_score_to_ungraded_submissions_request_instance = GradebooksApplyScoreToUngradedSubmissionsRequest.from_json(json)
# print the JSON string representation of the object
print(GradebooksApplyScoreToUngradedSubmissionsRequest.to_json())

# convert the object into a dict
gradebooks_apply_score_to_ungraded_submissions_request_dict = gradebooks_apply_score_to_ungraded_submissions_request_instance.to_dict()
# create an instance of GradebooksApplyScoreToUngradedSubmissionsRequest from a dict
gradebooks_apply_score_to_ungraded_submissions_request_from_dict = GradebooksApplyScoreToUngradedSubmissionsRequest.from_dict(gradebooks_apply_score_to_ungraded_submissions_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


