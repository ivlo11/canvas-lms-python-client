# PollSubmission


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier for the poll submission. | 
**poll_choice_id** | **int** | The unique identifier of the poll choice chosen for this submission. | [optional] 
**user_id** | **int** | the unique identifier of the user who submitted this poll submission. | [optional] 
**created_at** | **datetime** | The date and time the poll submission was submitted. | [optional] 

## Example

```python
from canvas_lms_python_client.models.poll_submission import PollSubmission

# TODO update the JSON string below
json = "{}"
# create an instance of PollSubmission from a JSON string
poll_submission_instance = PollSubmission.from_json(json)
# print the JSON string representation of the object
print(PollSubmission.to_json())

# convert the object into a dict
poll_submission_dict = poll_submission_instance.to_dict()
# create an instance of PollSubmission from a dict
poll_submission_from_dict = PollSubmission.from_dict(poll_submission_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


