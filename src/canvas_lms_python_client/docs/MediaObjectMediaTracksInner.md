# MediaObjectMediaTracksInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The media track&#39;s id | [optional] 
**kind** | **str** | The kind of track, for example captions or subtitles | [optional] 
**locale** | **str** | The track&#39;s locale | [optional] 
**workflow_state** | **str** | The track&#39;s state | [optional] 
**asr** | **bool** | Whether the track was created by automatic speech recognition | [optional] 
**url** | **str** | The URL of the track&#39;s content | [optional] 
**inherited** | **bool** | Whether the track is inherited from the original media. Only on media attachment routes | [optional] 
**created_at** | **datetime** | When the track was created | [optional] 
**updated_at** | **datetime** | When the track was last updated | [optional] 

## Example

```python
from canvas_lms_python_client.models.media_object_media_tracks_inner import MediaObjectMediaTracksInner

# TODO update the JSON string below
json = "{}"
# create an instance of MediaObjectMediaTracksInner from a JSON string
media_object_media_tracks_inner_instance = MediaObjectMediaTracksInner.from_json(json)
# print the JSON string representation of the object
print(MediaObjectMediaTracksInner.to_json())

# convert the object into a dict
media_object_media_tracks_inner_dict = media_object_media_tracks_inner_instance.to_dict()
# create an instance of MediaObjectMediaTracksInner from a dict
media_object_media_tracks_inner_from_dict = MediaObjectMediaTracksInner.from_dict(media_object_media_tracks_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


