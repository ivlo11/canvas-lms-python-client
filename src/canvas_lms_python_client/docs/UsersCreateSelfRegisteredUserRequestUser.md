# UsersCreateSelfRegisteredUserRequestUser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | [Required, String] The full name of the user. This name will be used by teacher for grading. | 
**short_name** | **str** | [String] User&#39;s name as it will be displayed in discussions, messages, and comments. | [optional] 
**sortable_name** | **str** | [String] User&#39;s name as used to sort alphabetically in lists. | [optional] 
**locale** | **str** | [String] The user&#39;s preferred language, from the list of languages Canvas supports. This is in RFC-5646 format. | [optional] 
**terms_of_use** | **bool** | [Required, Boolean] Whether the user accepts the terms of use. | 

## Example

```python
from canvas_lms_python_client.models.users_create_self_registered_user_request_user import UsersCreateSelfRegisteredUserRequestUser

# TODO update the JSON string below
json = "{}"
# create an instance of UsersCreateSelfRegisteredUserRequestUser from a JSON string
users_create_self_registered_user_request_user_instance = UsersCreateSelfRegisteredUserRequestUser.from_json(json)
# print the JSON string representation of the object
print(UsersCreateSelfRegisteredUserRequestUser.to_json())

# convert the object into a dict
users_create_self_registered_user_request_user_dict = users_create_self_registered_user_request_user_instance.to_dict()
# create an instance of UsersCreateSelfRegisteredUserRequestUser from a dict
users_create_self_registered_user_request_user_from_dict = UsersCreateSelfRegisteredUserRequestUser.from_dict(users_create_self_registered_user_request_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


