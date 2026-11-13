# UsersTerminateSessionsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.users_terminate_sessions_response import UsersTerminateSessionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UsersTerminateSessionsResponse from a JSON string
users_terminate_sessions_response_instance = UsersTerminateSessionsResponse.from_json(json)
# print the JSON string representation of the object
print(UsersTerminateSessionsResponse.to_json())

# convert the object into a dict
users_terminate_sessions_response_dict = users_terminate_sessions_response_instance.to_dict()
# create an instance of UsersTerminateSessionsResponse from a dict
users_terminate_sessions_response_from_dict = UsersTerminateSessionsResponse.from_dict(users_terminate_sessions_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


