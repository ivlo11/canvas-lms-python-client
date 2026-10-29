# SubmissionsCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | [**SubmissionsCreateRequestComment**](SubmissionsCreateRequestComment.md) |  | [optional] 
**submission** | [**SubmissionsCreateRequestSubmission**](SubmissionsCreateRequestSubmission.md) |  | 

## Example

```python
from canvas_lms_python_client.models.submissions_create_request import SubmissionsCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SubmissionsCreateRequest from a JSON string
submissions_create_request_instance = SubmissionsCreateRequest.from_json(json)
# print the JSON string representation of the object
print(SubmissionsCreateRequest.to_json())

# convert the object into a dict
submissions_create_request_dict = submissions_create_request_instance.to_dict()
# create an instance of SubmissionsCreateRequest from a dict
submissions_create_request_from_dict = SubmissionsCreateRequest.from_dict(submissions_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


