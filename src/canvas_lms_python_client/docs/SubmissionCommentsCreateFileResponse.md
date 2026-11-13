# SubmissionCommentsCreateFileResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_param** | **str** |  | [optional] 
**progress** | **object** |  | [optional] 
**upload_params** | **object** |  | [optional] 
**upload_url** | **str** |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.submission_comments_create_file_response import SubmissionCommentsCreateFileResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SubmissionCommentsCreateFileResponse from a JSON string
submission_comments_create_file_response_instance = SubmissionCommentsCreateFileResponse.from_json(json)
# print the JSON string representation of the object
print(SubmissionCommentsCreateFileResponse.to_json())

# convert the object into a dict
submission_comments_create_file_response_dict = submission_comments_create_file_response_instance.to_dict()
# create an instance of SubmissionCommentsCreateFileResponse from a dict
submission_comments_create_file_response_from_dict = SubmissionCommentsCreateFileResponse.from_dict(submission_comments_create_file_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


