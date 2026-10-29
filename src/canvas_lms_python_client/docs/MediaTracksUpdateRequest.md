# MediaTracksUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include** | **List[str]** | By default, an update returns id, locale, kind, media_object_id, and user_id for each of the result MediaTracks. Use include[] to add additional fields. For example include[]&#x3D;content | [optional] 

## Example

```python
from canvas_lms_python_client.models.media_tracks_update_request import MediaTracksUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MediaTracksUpdateRequest from a JSON string
media_tracks_update_request_instance = MediaTracksUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(MediaTracksUpdateRequest.to_json())

# convert the object into a dict
media_tracks_update_request_dict = media_tracks_update_request_instance.to_dict()
# create an instance of MediaTracksUpdateRequest from a dict
media_tracks_update_request_from_dict = MediaTracksUpdateRequest.from_dict(media_tracks_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


