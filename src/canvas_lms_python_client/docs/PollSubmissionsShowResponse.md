# PollSubmissionsShowResponse

Paginated `poll_submissions` list response (from the Canvas example response).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**poll_submissions** | [**List[PollSubmission]**](PollSubmission.md) |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.poll_submissions_show_response import PollSubmissionsShowResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PollSubmissionsShowResponse from a JSON string
poll_submissions_show_response_instance = PollSubmissionsShowResponse.from_json(json)
# print the JSON string representation of the object
print(PollSubmissionsShowResponse.to_json())

# convert the object into a dict
poll_submissions_show_response_dict = poll_submissions_show_response_instance.to_dict()
# create an instance of PollSubmissionsShowResponse from a dict
poll_submissions_show_response_from_dict = PollSubmissionsShowResponse.from_dict(poll_submissions_show_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


