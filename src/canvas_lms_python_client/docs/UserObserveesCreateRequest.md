# UserObserveesCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** | The access token for the user to observe.  Required if &lt;tt&gt;observee[unique_id]&lt;/tt&gt; or &lt;tt&gt;observee[password]&lt;/tt&gt; are omitted. | [optional] 
**pairing_code** | **str** | A generated pairing code for the user to observe. Required if the Observer pairing code feature flag is enabled | [optional] 
**root_account_id** | **int** | The ID for the root account to associate with the observation link. Defaults to the current domain account. If &#39;all&#39; is specified, a link will be created for each root account associated to both the observer and observee. | [optional] 
**observee** | [**UserObserveesCreateRequestObservee**](UserObserveesCreateRequestObservee.md) |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.user_observees_create_request import UserObserveesCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UserObserveesCreateRequest from a JSON string
user_observees_create_request_instance = UserObserveesCreateRequest.from_json(json)
# print the JSON string representation of the object
print(UserObserveesCreateRequest.to_json())

# convert the object into a dict
user_observees_create_request_dict = user_observees_create_request_instance.to_dict()
# create an instance of UserObserveesCreateRequest from a dict
user_observees_create_request_from_dict = UserObserveesCreateRequest.from_dict(user_observees_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


