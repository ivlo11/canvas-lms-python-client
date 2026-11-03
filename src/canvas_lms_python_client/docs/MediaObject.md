# MediaObject

A media object uploaded or recorded to Canvas's media service

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**media_id** | **str** | The media service&#39;s id for the media object | [optional] 
**created_at** | **datetime** | When the media object was created | [optional] 
**media_type** | **str** | The kind of media, for example video or audio | [optional] 
**title** | **str** | The user-entered title, the file name, or Untitled | [optional] 
**can_add_captions** | **bool** | Whether the current user can upload media tracks (subtitles) to this media object | [optional] 
**embedded_iframe_url** | **str** | The URL of the media player for embedding in an iframe | [optional] 
**auto_caption_status** | **str** | The status of automatic captioning, if requested | [optional] 
**status** | **str** | The media service&#39;s processing status. Only included when the media object has one | [optional] 
**viewer_restrictions** | **object** | Viewer access restrictions for this media, for example show_rolling_transcript | [optional] 
**media_sources** | [**List[MediaObjectMediaSourcesInner]**](MediaObjectMediaSourcesInner.md) | All the transcoded files (flavors) available for this media object. Omitted with exclude[]&#x3D;sources | [optional] 
**media_tracks** | [**List[MediaObjectMediaTracksInner]**](MediaObjectMediaTracksInner.md) | All the media tracks uploaded to this media object. Omitted with exclude[]&#x3D;tracks | [optional] 

## Example

```python
from canvas_lms_python_client.models.media_object import MediaObject

# TODO update the JSON string below
json = "{}"
# create an instance of MediaObject from a JSON string
media_object_instance = MediaObject.from_json(json)
# print the JSON string representation of the object
print(MediaObject.to_json())

# convert the object into a dict
media_object_dict = media_object_instance.to_dict()
# create an instance of MediaObject from a dict
media_object_from_dict = MediaObject.from_dict(media_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


