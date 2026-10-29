# CommunicationChannelsCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**skip_confirmation** | **bool** | Only valid for site admins and account admins making requests; If true, the channel is automatically validated and no confirmation email or SMS is sent. Otherwise, the user must respond to a confirmation message to confirm the channel. | [optional] 
**communication_channel** | [**CommunicationChannelsCreateRequestCommunicationChannel**](CommunicationChannelsCreateRequestCommunicationChannel.md) |  | 

## Example

```python
from canvas_lms_python_client.models.communication_channels_create_request import CommunicationChannelsCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CommunicationChannelsCreateRequest from a JSON string
communication_channels_create_request_instance = CommunicationChannelsCreateRequest.from_json(json)
# print the JSON string representation of the object
print(CommunicationChannelsCreateRequest.to_json())

# convert the object into a dict
communication_channels_create_request_dict = communication_channels_create_request_instance.to_dict()
# create an instance of CommunicationChannelsCreateRequest from a dict
communication_channels_create_request_from_dict = CommunicationChannelsCreateRequest.from_dict(communication_channels_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


