# CommunicationChannelsCreateRequestCommunicationChannel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | [Required, String] An email address or SMS number. Not required for \&quot;push\&quot; type channels. | 
**type** | **str** | [Required, String, \&quot;email\&quot;|\&quot;sms\&quot;|\&quot;push\&quot;] The type of communication channel.  In order to enable push notification support, the server must be properly configured (via &#x60;sns_creds&#x60; in Vault) to communicate with Amazon Simple Notification Services, and the developer key used to create the access token from this request must have an SNS ARN configured on it. | 
**token** | **str** | [String] A registration id, device token, or equivalent token given to an app when registering with a push notification provider. Only valid for \&quot;push\&quot; type channels. | [optional] 

## Example

```python
from canvas_lms_python_client.models.communication_channels_create_request_communication_channel import CommunicationChannelsCreateRequestCommunicationChannel

# TODO update the JSON string below
json = "{}"
# create an instance of CommunicationChannelsCreateRequestCommunicationChannel from a JSON string
communication_channels_create_request_communication_channel_instance = CommunicationChannelsCreateRequestCommunicationChannel.from_json(json)
# print the JSON string representation of the object
print(CommunicationChannelsCreateRequestCommunicationChannel.to_json())

# convert the object into a dict
communication_channels_create_request_communication_channel_dict = communication_channels_create_request_communication_channel_instance.to_dict()
# create an instance of CommunicationChannelsCreateRequestCommunicationChannel from a dict
communication_channels_create_request_communication_channel_from_dict = CommunicationChannelsCreateRequestCommunicationChannel.from_dict(communication_channels_create_request_communication_channel_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


