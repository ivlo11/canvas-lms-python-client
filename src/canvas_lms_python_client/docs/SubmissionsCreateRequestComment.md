# SubmissionsCreateRequestComment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text_comment** | **str** | [String] Include a textual comment with the submission. | [optional] 

## Example

```python
from canvas_lms_python_client.models.submissions_create_request_comment import SubmissionsCreateRequestComment

# TODO update the JSON string below
json = "{}"
# create an instance of SubmissionsCreateRequestComment from a JSON string
submissions_create_request_comment_instance = SubmissionsCreateRequestComment.from_json(json)
# print the JSON string representation of the object
print(SubmissionsCreateRequestComment.to_json())

# convert the object into a dict
submissions_create_request_comment_dict = submissions_create_request_comment_instance.to_dict()
# create an instance of SubmissionsCreateRequestComment from a dict
submissions_create_request_comment_from_dict = SubmissionsCreateRequestComment.from_dict(submissions_create_request_comment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


