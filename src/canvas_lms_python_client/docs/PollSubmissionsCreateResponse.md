# PollSubmissionsCreateResponse

Object response with `poll_submissions`, `meta` (from the Canvas `@returns`).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**poll_submissions** | [**List[PollSubmission]**](PollSubmission.md) |  | [optional] 
**meta** | **object** |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.poll_submissions_create_response import PollSubmissionsCreateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PollSubmissionsCreateResponse from a JSON string
poll_submissions_create_response_instance = PollSubmissionsCreateResponse.from_json(json)
# print the JSON string representation of the object
print(PollSubmissionsCreateResponse.to_json())

# convert the object into a dict
poll_submissions_create_response_dict = poll_submissions_create_response_instance.to_dict()
# create an instance of PollSubmissionsCreateResponse from a dict
poll_submissions_create_response_from_dict = PollSubmissionsCreateResponse.from_dict(poll_submissions_create_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


