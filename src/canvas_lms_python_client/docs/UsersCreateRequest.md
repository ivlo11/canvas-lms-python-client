# UsersCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | [**UsersCreateRequestUser**](UsersCreateRequestUser.md) |  | [optional] 
**force_validations** | **bool** | If true, validations are performed on the newly created user (and their associated pseudonym) even if the request is made by a privileged user like an admin. When set to false, or not included in the request parameters, any newly created users are subject to validations unless the request is made by a user with a &#39;manage_user_logins&#39; right. In which case, certain validations such as &#39;require_acceptance_of_terms&#39; and &#39;require_presence_of_name&#39; are not enforced. Use this parameter to return helpful json errors while building users with an admin request. | [optional] 
**enable_sis_reactivation** | **bool** | When true, will first try to re-activate a deleted user with matching sis_user_id if possible. This is commonly done with +user[skip_registration]+ and +communication_channel[skip_confirmation]+ so that the default communication_channel is also restored. | [optional] 
**initial_enrollment_type** | **str** | &#x60;observer&#x60; if doing a self-registration with a pairing code. This allows setting the password during user creation. | [optional] 
**pseudonym** | [**UsersCreateRequestPseudonym**](UsersCreateRequestPseudonym.md) |  | 
**communication_channel** | [**UsersCreateRequestCommunicationChannel**](UsersCreateRequestCommunicationChannel.md) |  | [optional] 
**destination** | [**UsersCreateRequestDestination**](UsersCreateRequestDestination.md) |  | [optional] 
**pairing_code** | [**UsersCreateRequestPairingCode**](UsersCreateRequestPairingCode.md) |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.users_create_request import UsersCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UsersCreateRequest from a JSON string
users_create_request_instance = UsersCreateRequest.from_json(json)
# print the JSON string representation of the object
print(UsersCreateRequest.to_json())

# convert the object into a dict
users_create_request_dict = users_create_request_instance.to_dict()
# create an instance of UsersCreateRequest from a dict
users_create_request_from_dict = UsersCreateRequest.from_dict(users_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


