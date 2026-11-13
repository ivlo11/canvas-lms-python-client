# UsersCreateSelfRegisteredUserRequestCommunicationChannel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | [String] The communication channel type, e.g. &#39;email&#39; or &#39;sms&#39;. | [optional] 
**address** | **str** | [String] The communication channel address, e.g. the user&#39;s email address. | [optional] 

## Example

```python
from canvas_lms_python_client.models.users_create_self_registered_user_request_communication_channel import UsersCreateSelfRegisteredUserRequestCommunicationChannel

# TODO update the JSON string below
json = "{}"
# create an instance of UsersCreateSelfRegisteredUserRequestCommunicationChannel from a JSON string
users_create_self_registered_user_request_communication_channel_instance = UsersCreateSelfRegisteredUserRequestCommunicationChannel.from_json(json)
# print the JSON string representation of the object
print(UsersCreateSelfRegisteredUserRequestCommunicationChannel.to_json())

# convert the object into a dict
users_create_self_registered_user_request_communication_channel_dict = users_create_self_registered_user_request_communication_channel_instance.to_dict()
# create an instance of UsersCreateSelfRegisteredUserRequestCommunicationChannel from a dict
users_create_self_registered_user_request_communication_channel_from_dict = UsersCreateSelfRegisteredUserRequestCommunicationChannel.from_dict(users_create_self_registered_user_request_communication_channel_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


