# MediaObjectsUpdateMediaObjectRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_entered_title** | **str** | The new title. | [optional] 
**viewer_restrictions** | **str** | A JSON object describing viewer access restrictions for this media. - show_rolling_transcript [Optional, Boolean]: Whether to show the rolling transcripts of the media during playback, or not. | [optional] 

## Example

```python
from canvas_lms_python_client.models.media_objects_update_media_object_request import MediaObjectsUpdateMediaObjectRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MediaObjectsUpdateMediaObjectRequest from a JSON string
media_objects_update_media_object_request_instance = MediaObjectsUpdateMediaObjectRequest.from_json(json)
# print the JSON string representation of the object
print(MediaObjectsUpdateMediaObjectRequest.to_json())

# convert the object into a dict
media_objects_update_media_object_request_dict = media_objects_update_media_object_request_instance.to_dict()
# create an instance of MediaObjectsUpdateMediaObjectRequest from a dict
media_objects_update_media_object_request_from_dict = MediaObjectsUpdateMediaObjectRequest.from_dict(media_objects_update_media_object_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


