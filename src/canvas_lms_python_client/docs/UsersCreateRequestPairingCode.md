# UsersCreateRequestPairingCode


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | [String] If provided and valid, will link the new user as an observer to the student&#39;s whose pairing code is given. | [optional] 

## Example

```python
from canvas_lms_python_client.models.users_create_request_pairing_code import UsersCreateRequestPairingCode

# TODO update the JSON string below
json = "{}"
# create an instance of UsersCreateRequestPairingCode from a JSON string
users_create_request_pairing_code_instance = UsersCreateRequestPairingCode.from_json(json)
# print the JSON string representation of the object
print(UsersCreateRequestPairingCode.to_json())

# convert the object into a dict
users_create_request_pairing_code_dict = users_create_request_pairing_code_instance.to_dict()
# create an instance of UsersCreateRequestPairingCode from a dict
users_create_request_pairing_code_from_dict = UsersCreateRequestPairingCode.from_dict(users_create_request_pairing_code_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


