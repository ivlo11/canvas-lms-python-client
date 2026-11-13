# UsersUpdateRequestUser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | [String] The full name of the user. This name will be used by teacher for grading. | [optional] 
**short_name** | **str** | [String] User&#39;s name as it will be displayed in discussions, messages, and comments. | [optional] 
**sortable_name** | **str** | [String] User&#39;s name as used to sort alphabetically in lists. | [optional] 
**email** | **str** | [String] The default email address of the user. | [optional] 
**locale** | **str** | [String] The user&#39;s preferred language, from the list of languages Canvas supports. This is in RFC-5646 format. | [optional] 
**avatar** | **str** | [state] [String, \&quot;none\&quot;, \&quot;submitted\&quot;, \&quot;approved\&quot;, \&quot;locked\&quot;, \&quot;reported\&quot;, \&quot;re_reported\&quot;] To set the state of user&#39;s avatar. Only valid for account administrator. | [optional] 
**title** | **str** | [String] Sets a title on the user profile. (See {api:ProfileController#settings Get user profile}.) Profiles must be enabled on the root account. | [optional] 
**bio** | **str** | [String] Sets a bio on the user profile. (See {api:ProfileController#settings Get user profile}.) Profiles must be enabled on the root account. | [optional] 
**pronunciation** | **str** | [String] Sets name pronunciation on the user profile. (See {api:ProfileController#settings Get user profile}.) Profiles and name pronunciation must be enabled on the root account. | [optional] 
**pronouns** | **str** | [String] Sets pronouns on the user profile. Passing an empty string will empty the user&#39;s pronouns Only Available Pronouns set on the root account are allowed Adding and changing pronouns must be enabled on the root account. | [optional] 
**event** | **str** | [String, \&quot;suspend\&quot;|\&quot;unsuspend\&quot;] Suspends or unsuspends all logins for this user that the calling user has permission to | [optional] 

## Example

```python
from canvas_lms_python_client.models.users_update_request_user import UsersUpdateRequestUser

# TODO update the JSON string below
json = "{}"
# create an instance of UsersUpdateRequestUser from a JSON string
users_update_request_user_instance = UsersUpdateRequestUser.from_json(json)
# print the JSON string representation of the object
print(UsersUpdateRequestUser.to_json())

# convert the object into a dict
users_update_request_user_dict = users_update_request_user_instance.to_dict()
# create an instance of UsersUpdateRequestUser from a dict
users_update_request_user_from_dict = UsersUpdateRequestUser.from_dict(users_update_request_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


