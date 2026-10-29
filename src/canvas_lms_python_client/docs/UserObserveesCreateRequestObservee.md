# UserObserveesCreateRequestObservee


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unique_id** | **str** | [Optional, String] The login id for the user to observe.  Required if access_token is omitted. | [optional] 
**password** | **str** | [Optional, String] The password for the user to observe. Required if access_token is omitted. | [optional] 

## Example

```python
from canvas_lms_python_client.models.user_observees_create_request_observee import UserObserveesCreateRequestObservee

# TODO update the JSON string below
json = "{}"
# create an instance of UserObserveesCreateRequestObservee from a JSON string
user_observees_create_request_observee_instance = UserObserveesCreateRequestObservee.from_json(json)
# print the JSON string representation of the object
print(UserObserveesCreateRequestObservee.to_json())

# convert the object into a dict
user_observees_create_request_observee_dict = user_observees_create_request_observee_instance.to_dict()
# create an instance of UserObserveesCreateRequestObservee from a dict
user_observees_create_request_observee_from_dict = UserObserveesCreateRequestObservee.from_dict(user_observees_create_request_observee_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


