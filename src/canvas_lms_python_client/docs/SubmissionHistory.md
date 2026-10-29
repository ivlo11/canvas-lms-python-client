# SubmissionHistory



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**submission_id** | **int** | the id of the submission | [optional] 
**versions** | [**List[SubmissionVersion]**](SubmissionVersion.md) | an array of all the versions of this submission | [optional] 

## Example

```python
from canvas_lms_python_client.models.submission_history import SubmissionHistory

# TODO update the JSON string below
json = "{}"
# create an instance of SubmissionHistory from a JSON string
submission_history_instance = SubmissionHistory.from_json(json)
# print the JSON string representation of the object
print(SubmissionHistory.to_json())

# convert the object into a dict
submission_history_dict = submission_history_instance.to_dict()
# create an instance of SubmissionHistory from a dict
submission_history_from_dict = SubmissionHistory.from_dict(submission_history_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


