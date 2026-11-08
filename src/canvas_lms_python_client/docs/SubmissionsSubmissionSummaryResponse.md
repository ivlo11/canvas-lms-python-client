# SubmissionsSubmissionSummaryResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**graded** | **int** |  | [optional] 
**not_submitted** | **int** |  | [optional] 
**ungraded** | **int** |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.submissions_submission_summary_response import SubmissionsSubmissionSummaryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SubmissionsSubmissionSummaryResponse from a JSON string
submissions_submission_summary_response_instance = SubmissionsSubmissionSummaryResponse.from_json(json)
# print the JSON string representation of the object
print(SubmissionsSubmissionSummaryResponse.to_json())

# convert the object into a dict
submissions_submission_summary_response_dict = submissions_submission_summary_response_instance.to_dict()
# create an instance of SubmissionsSubmissionSummaryResponse from a dict
submissions_submission_summary_response_from_dict = SubmissionsSubmissionSummaryResponse.from_dict(submissions_submission_summary_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


