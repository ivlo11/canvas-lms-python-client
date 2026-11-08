# UsersPandataEventsTokenResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_token** | **str** |  | [optional] 
**expires_at** | **float** |  | [optional] 
**props_token** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.users_pandata_events_token_response import UsersPandataEventsTokenResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UsersPandataEventsTokenResponse from a JSON string
users_pandata_events_token_response_instance = UsersPandataEventsTokenResponse.from_json(json)
# print the JSON string representation of the object
print(UsersPandataEventsTokenResponse.to_json())

# convert the object into a dict
users_pandata_events_token_response_dict = users_pandata_events_token_response_instance.to_dict()
# create an instance of UsersPandataEventsTokenResponse from a dict
users_pandata_events_token_response_from_dict = UsersPandataEventsTokenResponse.from_dict(users_pandata_events_token_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


