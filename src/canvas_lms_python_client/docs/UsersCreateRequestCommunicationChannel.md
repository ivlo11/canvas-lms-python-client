# UsersCreateRequestCommunicationChannel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | [String] The communication channel type, e.g. &#39;email&#39; or &#39;sms&#39;. | [optional] 
**address** | **str** | [String] The communication channel address, e.g. the user&#39;s email address. | [optional] 
**confirmation_url** | **bool** | [Boolean] Only valid for account admins. If true, returns the new user account confirmation URL in the response. | [optional] 
**skip_confirmation** | **bool** | [Boolean] Only valid for site admins and account admins making requests; If true, the channel is automatically validated and no confirmation email or SMS is sent. Otherwise, the user must respond to a confirmation message to confirm the channel.  If this is true, it is recommended to set &lt;tt&gt;\&quot;pseudonym[send_confirmation]\&quot;&lt;/tt&gt; to true as well. Otherwise, the user will not receive any messages about their account creation. | [optional] 

## Example

```python
from canvas_lms_python_client.models.users_create_request_communication_channel import UsersCreateRequestCommunicationChannel

# TODO update the JSON string below
json = "{}"
# create an instance of UsersCreateRequestCommunicationChannel from a JSON string
users_create_request_communication_channel_instance = UsersCreateRequestCommunicationChannel.from_json(json)
# print the JSON string representation of the object
print(UsersCreateRequestCommunicationChannel.to_json())

# convert the object into a dict
users_create_request_communication_channel_dict = users_create_request_communication_channel_instance.to_dict()
# create an instance of UsersCreateRequestCommunicationChannel from a dict
users_create_request_communication_channel_from_dict = UsersCreateRequestCommunicationChannel.from_dict(users_create_request_communication_channel_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


