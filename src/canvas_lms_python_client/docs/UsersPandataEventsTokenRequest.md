# UsersPandataEventsTokenRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_key** | **str** | The pandata events appKey for this mobile app | [optional] 

## Example

```python
from canvas_lms_python_client.models.users_pandata_events_token_request import UsersPandataEventsTokenRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UsersPandataEventsTokenRequest from a JSON string
users_pandata_events_token_request_instance = UsersPandataEventsTokenRequest.from_json(json)
# print the JSON string representation of the object
print(UsersPandataEventsTokenRequest.to_json())

# convert the object into a dict
users_pandata_events_token_request_dict = users_pandata_events_token_request_instance.to_dict()
# create an instance of UsersPandataEventsTokenRequest from a dict
users_pandata_events_token_request_from_dict = UsersPandataEventsTokenRequest.from_dict(users_pandata_events_token_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


