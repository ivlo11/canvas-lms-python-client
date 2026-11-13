# UsersCreateSelfRegisteredUserRequestPseudonym


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unique_id** | **str** | [Required, String] User&#39;s login ID. Must be a valid email address. | 

## Example

```python
from canvas_lms_python_client.models.users_create_self_registered_user_request_pseudonym import UsersCreateSelfRegisteredUserRequestPseudonym

# TODO update the JSON string below
json = "{}"
# create an instance of UsersCreateSelfRegisteredUserRequestPseudonym from a JSON string
users_create_self_registered_user_request_pseudonym_instance = UsersCreateSelfRegisteredUserRequestPseudonym.from_json(json)
# print the JSON string representation of the object
print(UsersCreateSelfRegisteredUserRequestPseudonym.to_json())

# convert the object into a dict
users_create_self_registered_user_request_pseudonym_dict = users_create_self_registered_user_request_pseudonym_instance.to_dict()
# create an instance of UsersCreateSelfRegisteredUserRequestPseudonym from a dict
users_create_self_registered_user_request_pseudonym_from_dict = UsersCreateSelfRegisteredUserRequestPseudonym.from_dict(users_create_self_registered_user_request_pseudonym_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


