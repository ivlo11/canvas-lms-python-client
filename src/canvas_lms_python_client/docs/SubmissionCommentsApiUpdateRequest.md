# SubmissionCommentsApiUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** | If this argument is present, edit the text of a comment. | [optional] 

## Example

```python
from canvas_lms_python_client.models.submission_comments_api_update_request import SubmissionCommentsApiUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SubmissionCommentsApiUpdateRequest from a JSON string
submission_comments_api_update_request_instance = SubmissionCommentsApiUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(SubmissionCommentsApiUpdateRequest.to_json())

# convert the object into a dict
submission_comments_api_update_request_dict = submission_comments_api_update_request_instance.to_dict()
# create an instance of SubmissionCommentsApiUpdateRequest from a dict
submission_comments_api_update_request_from_dict = SubmissionCommentsApiUpdateRequest.from_dict(submission_comments_api_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


