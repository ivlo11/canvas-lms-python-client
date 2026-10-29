# PollSubmissionsCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**poll_submissions_poll_choice_id** | **int** | The chosen poll choice for this submission. | 

## Example

```python
from canvas_lms_python_client.models.poll_submissions_create_request import PollSubmissionsCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PollSubmissionsCreateRequest from a JSON string
poll_submissions_create_request_instance = PollSubmissionsCreateRequest.from_json(json)
# print the JSON string representation of the object
print(PollSubmissionsCreateRequest.to_json())

# convert the object into a dict
poll_submissions_create_request_dict = poll_submissions_create_request_instance.to_dict()
# create an instance of PollSubmissionsCreateRequest from a dict
poll_submissions_create_request_from_dict = PollSubmissionsCreateRequest.from_dict(poll_submissions_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


