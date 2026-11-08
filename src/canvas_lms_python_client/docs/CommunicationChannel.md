# CommunicationChannel



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The ID of the communication channel. | [optional] 
**address** | **str** | The address, or path, of the communication channel. | [optional] 
**type** | **str** | The type of communcation channel being described. Possible values are: &#39;email&#39;, &#39;push&#39;, &#39;sms&#39;. This field determines the type of value seen in &#39;address&#39;. | [optional] 
**position** | **int** | The position of this communication channel relative to the user&#39;s other channels when they are ordered. | [optional] 
**user_id** | **int** | The ID of the user that owns this communication channel. | [optional] 
**bounce_count** | **int** | The number of bounces the channel has experienced. This is reset if the channel sends successfully. | [optional] 
**last_bounce_at** | **datetime** | The time the last bounce occurred. | [optional] 
**workflow_state** | **str** | The current state of the communication channel. Possible values are: &#39;unconfirmed&#39; or &#39;active&#39;. | [optional] 
**created_at** | **str** |  | [optional] 
**last_bounce_summary** | **object** |  | [optional] 
**last_suppression_bounce_at** | **str** |  | [optional] 
**last_transient_bounce_at** | **str** |  | [optional] 
**last_transient_bounce_summary** | **object** |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.communication_channel import CommunicationChannel

# TODO update the JSON string below
json = "{}"
# create an instance of CommunicationChannel from a JSON string
communication_channel_instance = CommunicationChannel.from_json(json)
# print the JSON string representation of the object
print(CommunicationChannel.to_json())

# convert the object into a dict
communication_channel_dict = communication_channel_instance.to_dict()
# create an instance of CommunicationChannel from a dict
communication_channel_from_dict = CommunicationChannel.from_dict(communication_channel_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


