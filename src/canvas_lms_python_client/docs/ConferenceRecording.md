# ConferenceRecording



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**duration_minutes** | **int** |  | [optional] 
**title** | **str** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**playback_url** | **str** |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.conference_recording import ConferenceRecording

# TODO update the JSON string below
json = "{}"
# create an instance of ConferenceRecording from a JSON string
conference_recording_instance = ConferenceRecording.from_json(json)
# print the JSON string representation of the object
print(ConferenceRecording.to_json())

# convert the object into a dict
conference_recording_dict = conference_recording_instance.to_dict()
# create an instance of ConferenceRecording from a dict
conference_recording_from_dict = ConferenceRecording.from_dict(conference_recording_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


