# ConversationParticipant



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The user ID for the participant. | [optional] 
**name** | **str** | A short name the user has selected, for use in conversations or other less formal places through the site. | [optional] 
**full_name** | **str** | The full name of the user. | [optional] 
**avatar_url** | **str** | If requested, this field will be included and contain a url to retrieve the user&#39;s avatar. | [optional] 
**uuid** | **str** | The Canvas UUID for the participant. | [optional] 
**pronouns** | **object** |  | [optional] 
**common_courses** | **object** |  | [optional] 
**common_groups** | **object** |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.conversation_participant import ConversationParticipant

# TODO update the JSON string below
json = "{}"
# create an instance of ConversationParticipant from a JSON string
conversation_participant_instance = ConversationParticipant.from_json(json)
# print the JSON string representation of the object
print(ConversationParticipant.to_json())

# convert the object into a dict
conversation_participant_dict = conversation_participant_instance.to_dict()
# create an instance of ConversationParticipant from a dict
conversation_participant_from_dict = ConversationParticipant.from_dict(conversation_participant_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


