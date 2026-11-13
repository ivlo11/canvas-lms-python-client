# CommunicationChannelsDeletePushTokenResponse

Object response with `success` (from the Canvas `@returns`).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.communication_channels_delete_push_token_response import CommunicationChannelsDeletePushTokenResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CommunicationChannelsDeletePushTokenResponse from a JSON string
communication_channels_delete_push_token_response_instance = CommunicationChannelsDeletePushTokenResponse.from_json(json)
# print the JSON string representation of the object
print(CommunicationChannelsDeletePushTokenResponse.to_json())

# convert the object into a dict
communication_channels_delete_push_token_response_dict = communication_channels_delete_push_token_response_instance.to_dict()
# create an instance of CommunicationChannelsDeletePushTokenResponse from a dict
communication_channels_delete_push_token_response_from_dict = CommunicationChannelsDeletePushTokenResponse.from_dict(communication_channels_delete_push_token_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


