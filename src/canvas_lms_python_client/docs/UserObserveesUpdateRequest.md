# UserObserveesUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**root_account_id** | **int** | The ID for the root account to associate with the observation link. If not specified, a link will be created for each root account associated to both the observer and observee. | [optional] 

## Example

```python
from canvas_lms_python_client.models.user_observees_update_request import UserObserveesUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UserObserveesUpdateRequest from a JSON string
user_observees_update_request_instance = UserObserveesUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(UserObserveesUpdateRequest.to_json())

# convert the object into a dict
user_observees_update_request_dict = user_observees_update_request_instance.to_dict()
# create an instance of UserObserveesUpdateRequest from a dict
user_observees_update_request_from_dict = UserObserveesUpdateRequest.from_dict(user_observees_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


