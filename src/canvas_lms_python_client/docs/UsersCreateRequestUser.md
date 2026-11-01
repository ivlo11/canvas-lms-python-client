# UsersCreateRequestUser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | [String] The full name of the user. This name will be used by teacher for grading. Required if this is a self-registration. | [optional] 
**short_name** | **str** | [String] User&#39;s name as it will be displayed in discussions, messages, and comments. | [optional] 
**sortable_name** | **str** | [String] User&#39;s name as used to sort alphabetically in lists. | [optional] 
**locale** | **str** | [String] The user&#39;s preferred language, from the list of languages Canvas supports. This is in RFC-5646 format. | [optional] 
**terms_of_use** | **bool** | [Boolean] Whether the user accepts the terms of use. Required if this is a self-registration and this canvas instance requires users to accept the terms (on by default).  If this is true, it will mark the user as having accepted the terms of use. | [optional] 
**skip_registration** | **bool** | [Boolean] Automatically mark the user as registered.  If this is true, it is recommended to set &lt;tt&gt;\&quot;pseudonym[send_confirmation]\&quot;&lt;/tt&gt; to true as well. Otherwise, the user will not receive any messages about their account creation.  The users communication channel confirmation can be skipped by setting &lt;tt&gt;\&quot;communication_channel[skip_confirmation]\&quot;&lt;/tt&gt; to true as well. | [optional] 

## Example

```python
from canvas_lms_python_client.models.users_create_request_user import UsersCreateRequestUser

# TODO update the JSON string below
json = "{}"
# create an instance of UsersCreateRequestUser from a JSON string
users_create_request_user_instance = UsersCreateRequestUser.from_json(json)
# print the JSON string representation of the object
print(UsersCreateRequestUser.to_json())

# convert the object into a dict
users_create_request_user_dict = users_create_request_user_instance.to_dict()
# create an instance of UsersCreateRequestUser from a dict
users_create_request_user_from_dict = UsersCreateRequestUser.from_dict(users_create_request_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


