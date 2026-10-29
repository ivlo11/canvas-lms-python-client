# ContentShare

Content shared between users

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The id of the content share for the current user | [optional] 
**name** | **str** | The name of the shared content | [optional] 
**content_type** | **str** | The type of content that was shared. Can be assignment, discussion_topic, page, quiz, module, or module_item. | [optional] 
**created_at** | **datetime** | The datetime the content was shared with this user. | [optional] 
**updated_at** | **datetime** | The datetime the content was updated. | [optional] 
**user_id** | **int** | The id of the user who sent or received the content share. | [optional] 
**sender** | **object** | The user who shared the content. This field is provided only to receivers; it is not populated in the sender&#39;s list of sent content shares. | [optional] 
**receivers** | **List[object]** | An Array of users the content is shared with.  This field is provided only to senders; an empty array will be returned for the receiving users. | [optional] 
**source_course** | **object** | The course the content was originally shared from. | [optional] 
**read_state** | **str** | Whether the recipient has viewed the content share. | [optional] 
**content_export** | [**ContentExport**](ContentExport.md) |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.content_share import ContentShare

# TODO update the JSON string below
json = "{}"
# create an instance of ContentShare from a JSON string
content_share_instance = ContentShare.from_json(json)
# print the JSON string representation of the object
print(ContentShare.to_json())

# convert the object into a dict
content_share_dict = content_share_instance.to_dict()
# create an instance of ContentShare from a dict
content_share_from_dict = ContentShare.from_dict(content_share_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


