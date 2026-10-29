# Conference



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The id of the conference | [optional] 
**conference_type** | **str** | The type of conference | [optional] 
**conference_key** | **str** | The 3rd party&#39;s ID for the conference | [optional] 
**description** | **str** | The description for the conference | [optional] 
**duration** | **int** | The expected duration the conference is supposed to last | [optional] 
**ended_at** | **datetime** | The date that the conference ended at, null if it hasn&#39;t ended | [optional] 
**started_at** | **datetime** | The date the conference started at, null if it hasn&#39;t started | [optional] 
**title** | **str** | The title of the conference | [optional] 
**users** | **List[int]** | Array of user ids that are participants in the conference | [optional] 
**invitees** | **List[int]** | Array of user ids that are invitees in the conference | [optional] 
**attendees** | **List[int]** | Array of user ids that are attendees in the conference | [optional] 
**has_advanced_settings** | **bool** | True if the conference type has advanced settings. | [optional] 
**long_running** | **bool** | If true the conference is long running and has no expected end time | [optional] 
**user_settings** | **object** | A collection of settings specific to the conference type | [optional] 
**recordings** | [**List[ConferenceRecording]**](ConferenceRecording.md) | A List of recordings for the conference | [optional] 
**url** | **str** | URL for the conference, may be null if the conference type doesn&#39;t set it | [optional] 
**join_url** | **str** | URL to join the conference, may be null if the conference type doesn&#39;t set it | [optional] 
**context_type** | **str** | The type of this conference&#39;s context, typically &#39;Course&#39; or &#39;Group&#39;. | [optional] 
**context_id** | **int** | The ID of this conference&#39;s context. | [optional] 

## Example

```python
from canvas_lms_python_client.models.conference import Conference

# TODO update the JSON string below
json = "{}"
# create an instance of Conference from a JSON string
conference_instance = Conference.from_json(json)
# print the JSON string representation of the object
print(Conference.to_json())

# convert the object into a dict
conference_dict = conference_instance.to_dict()
# create an instance of Conference from a dict
conference_from_dict = Conference.from_dict(conference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


