# SubmissionComment



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**author_id** | **int** |  | [optional] 
**author_name** | **str** |  | [optional] 
**author** | [**SubmissionCommentAuthor**](SubmissionCommentAuthor.md) |  | [optional] 
**comment** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**edited_at** | **datetime** |  | [optional] 
**media_comment** | [**MediaComment**](MediaComment.md) |  | [optional] 
**attempt** | **int** |  | [optional] 
**cached_attachments** | **List[object]** |  | [optional] 
**draft** | **bool** |  | [optional] 
**group_comment_id** | **str** |  | [optional] 
**media_comment_id** | **str** |  | [optional] 
**media_comment_type** | **str** |  | [optional] 
**publishable** | **bool** |  | [optional] 
**attachments** | **List[object]** |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.submission_comment import SubmissionComment

# TODO update the JSON string below
json = "{}"
# create an instance of SubmissionComment from a JSON string
submission_comment_instance = SubmissionComment.from_json(json)
# print the JSON string representation of the object
print(SubmissionComment.to_json())

# convert the object into a dict
submission_comment_dict = submission_comment_instance.to_dict()
# create an instance of SubmissionComment from a dict
submission_comment_from_dict = SubmissionComment.from_dict(submission_comment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


