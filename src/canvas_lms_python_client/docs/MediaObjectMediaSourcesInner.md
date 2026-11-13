# MediaObjectMediaSourcesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**height** | **str** | The flavor&#39;s height | [optional] 
**width** | **str** | The flavor&#39;s width | [optional] 
**content_type** | **str** | The flavor&#39;s content type | [optional] 
**container_format** | **str** | The flavor&#39;s container format | [optional] 
**url** | **str** | The URL to download the flavor | [optional] 
**bitrate** | **str** | The flavor&#39;s bitrate | [optional] 
**size** | **str** | The flavor&#39;s size | [optional] 
**is_original** | **str** | Whether the flavor is the original upload (\&quot;1\&quot;) or not (\&quot;0\&quot;) | [optional] 
**file_ext** | **str** | The flavor&#39;s file extension | [optional] 
**src** | **str** | The same as url | [optional] 
**label** | **str** | The bitrate as a label | [optional] 

## Example

```python
from canvas_lms_python_client.models.media_object_media_sources_inner import MediaObjectMediaSourcesInner

# TODO update the JSON string below
json = "{}"
# create an instance of MediaObjectMediaSourcesInner from a JSON string
media_object_media_sources_inner_instance = MediaObjectMediaSourcesInner.from_json(json)
# print the JSON string representation of the object
print(MediaObjectMediaSourcesInner.to_json())

# convert the object into a dict
media_object_media_sources_inner_dict = media_object_media_sources_inner_instance.to_dict()
# create an instance of MediaObjectMediaSourcesInner from a dict
media_object_media_sources_inner_from_dict = MediaObjectMediaSourcesInner.from_dict(media_object_media_sources_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


