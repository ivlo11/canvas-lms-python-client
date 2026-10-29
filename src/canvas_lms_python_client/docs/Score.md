# Score



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** | The lti_user_id or the Canvas user_id | [optional] 
**score_given** | **float** | The Current score received in the tool for this line item and user, scaled to the scoreMaximum | [optional] 
**score_maximum** | **float** | Maximum possible score for this result; it must be present if scoreGiven is present. | [optional] 
**comment** | **str** | Comment visible to the student about this score. | [optional] 
**timestamp** | **str** | Date and time when the score was modified in the tool. Should use subsecond precision. | [optional] 
**activity_progress** | **str** | Indicate to Canvas the status of the user towards the activity&#39;s completion. Must be one of Initialized, Started, InProgress, Submitted, Completed | [optional] 
**grading_progress** | **str** | Indicate to Canvas the status of the grading process. A value of PendingManual will require intervention by a grader. Values of NotReady, Failed, and Pending will cause the scoreGiven to be ignored. FullyGraded values will require no action. Possible values are NotReady, Failed, Pending, PendingManual, FullyGraded | [optional] 
**submission** | **object** | Contains metadata about the submission attempt, like submittedAt: Date and time that the submission was originally created - should use ISO8601-formatted date with subsecond precision. | [optional] 

## Example

```python
from canvas_lms_python_client.models.score import Score

# TODO update the JSON string below
json = "{}"
# create an instance of Score from a JSON string
score_instance = Score.from_json(json)
# print the JSON string representation of the object
print(Score.to_json())

# convert the object into a dict
score_dict = score_instance.to_dict()
# create an instance of Score from a dict
score_from_dict = Score.from_dict(score_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


