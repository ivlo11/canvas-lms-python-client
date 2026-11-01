# UsersCreateSelfRegisteredUserRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | [**UsersCreateSelfRegisteredUserRequestUser**](UsersCreateSelfRegisteredUserRequestUser.md) |  | 
**pseudonym** | [**UsersCreateSelfRegisteredUserRequestPseudonym**](UsersCreateSelfRegisteredUserRequestPseudonym.md) |  | 
**communication_channel** | [**UsersCreateSelfRegisteredUserRequestCommunicationChannel**](UsersCreateSelfRegisteredUserRequestCommunicationChannel.md) |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.users_create_self_registered_user_request import UsersCreateSelfRegisteredUserRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UsersCreateSelfRegisteredUserRequest from a JSON string
users_create_self_registered_user_request_instance = UsersCreateSelfRegisteredUserRequest.from_json(json)
# print the JSON string representation of the object
print(UsersCreateSelfRegisteredUserRequest.to_json())

# convert the object into a dict
users_create_self_registered_user_request_dict = users_create_self_registered_user_request_instance.to_dict()
# create an instance of UsersCreateSelfRegisteredUserRequest from a dict
users_create_self_registered_user_request_from_dict = UsersCreateSelfRegisteredUserRequest.from_dict(users_create_self_registered_user_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


