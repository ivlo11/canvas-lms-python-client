# MediaComment



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content_type** | **str** |  | [optional] 
**display_name** | **str** |  | [optional] 
**media_id** | **str** |  | [optional] 
**media_type** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.media_comment import MediaComment

# TODO update the JSON string below
json = "{}"
# create an instance of MediaComment from a JSON string
media_comment_instance = MediaComment.from_json(json)
# print the JSON string representation of the object
print(MediaComment.to_json())

# convert the object into a dict
media_comment_dict = media_comment_instance.to_dict()
# create an instance of MediaComment from a dict
media_comment_from_dict = MediaComment.from_dict(media_comment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


