# SubmissionsApiUpdateRequestComment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text_comment** | **str** | [String] Add a textual comment to the submission. | [optional] 
**attempt** | **int** | [Integer] The attempt number (starts at 1) to associate the comment with. | [optional] 
**group_comment** | **bool** | [Boolean] Whether or not this comment should be sent to the entire group (defaults to false). Ignored if this is not a group assignment or if no text_comment is provided. | [optional] 
**media_comment_id** | **str** | [String] Add an audio/video comment to the submission. Media comments can be added via this API, however, note that there is not yet an API to generate or list existing media comments, so this functionality is currently of limited use. | [optional] 
**media_comment_type** | **str** | [String, \&quot;audio\&quot;|\&quot;video\&quot;] The type of media comment being added. | [optional] 
**file_ids** | **str** | [] [Integer] Attach files to this comment that were previously uploaded using the Submission Comment API&#39;s files action | [optional] 

## Example

```python
from canvas_lms_python_client.models.submissions_api_update_request_comment import SubmissionsApiUpdateRequestComment

# TODO update the JSON string below
json = "{}"
# create an instance of SubmissionsApiUpdateRequestComment from a JSON string
submissions_api_update_request_comment_instance = SubmissionsApiUpdateRequestComment.from_json(json)
# print the JSON string representation of the object
print(SubmissionsApiUpdateRequestComment.to_json())

# convert the object into a dict
submissions_api_update_request_comment_dict = submissions_api_update_request_comment_instance.to_dict()
# create an instance of SubmissionsApiUpdateRequestComment from a dict
submissions_api_update_request_comment_from_dict = SubmissionsApiUpdateRequestComment.from_dict(submissions_api_update_request_comment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


