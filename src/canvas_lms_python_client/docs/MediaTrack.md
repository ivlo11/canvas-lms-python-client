# MediaTrack

Closed captions added to a video media object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The media track&#39;s id | 
**user_id** | **int** | The id of the user who added the track | [optional] 
**media_object_id** | **int** | The id of the track&#39;s media object | [optional] 
**kind** | **str** | The kind of track, for example captions or subtitles | 
**locale** | **str** | The track&#39;s locale | 
**workflow_state** | **str** | The track&#39;s state | [optional] 
**asr** | **bool** | Whether the track was created by automatic speech recognition | [optional] 
**content** | **str** | The track&#39;s content. Only included with include[]&#x3D;content | [optional] 
**webvtt_content** | **str** | The track&#39;s content as WebVTT. Only included with include[]&#x3D;webvtt_content | [optional] 
**created_at** | **datetime** | When the track was created. Only included with include[]&#x3D;created_at | [optional] 
**updated_at** | **datetime** | When the track was last updated. Only included with include[]&#x3D;updated_at | [optional] 

## Example

```python
from canvas_lms_python_client.models.media_track import MediaTrack

# TODO update the JSON string below
json = "{}"
# create an instance of MediaTrack from a JSON string
media_track_instance = MediaTrack.from_json(json)
# print the JSON string representation of the object
print(MediaTrack.to_json())

# convert the object into a dict
media_track_dict = media_track_instance.to_dict()
# create an instance of MediaTrack from a dict
media_track_from_dict = MediaTrack.from_dict(media_track_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


