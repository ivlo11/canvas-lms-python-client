# SubmissionsCreateFileResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_param** | **str** |  | [optional] 
**progress** | **object** |  | [optional] 
**upload_params** | **object** |  | [optional] 
**upload_url** | **str** |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.submissions_create_file_response import SubmissionsCreateFileResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SubmissionsCreateFileResponse from a JSON string
submissions_create_file_response_instance = SubmissionsCreateFileResponse.from_json(json)
# print the JSON string representation of the object
print(SubmissionsCreateFileResponse.to_json())

# convert the object into a dict
submissions_create_file_response_dict = submissions_create_file_response_instance.to_dict()
# create an instance of SubmissionsCreateFileResponse from a dict
submissions_create_file_response_from_dict = SubmissionsCreateFileResponse.from_dict(submissions_create_file_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


