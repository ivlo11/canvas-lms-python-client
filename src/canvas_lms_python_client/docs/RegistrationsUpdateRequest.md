# RegistrationsUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the tool | [optional] 
**admin_nickname** | **str** | The admin-configured friendly display name for the registration | [optional] 
**description** | **str** | A description of the tool. Cannot exceed 2048 bytes. | [optional] 
**workflow_state** | **str** | \&quot;on\&quot;/\&quot;off\&quot;/\&quot;allow\&quot; set the account binding state directly (binding vocabulary) and will be deprecated soon. \&quot;active\&quot;/\&quot;inactive\&quot; set the registration state directly (registration vocabulary). All five values update both the binding and the registration to equivalent states. \&quot;allow\&quot; is only valid for Site Admin registrations. | [optional] 
**lock_deploying** | **bool** | When true, no new deployments of this registration can be created. | [optional] 
**configuration** | [**RegistrationsUpdateRequestConfiguration**](RegistrationsUpdateRequestConfiguration.md) |  | [optional] 
**overlay** | [**RegistrationsUpdateRequestOverlay**](RegistrationsUpdateRequestOverlay.md) |  | [optional] 
**comment** | [**RegistrationsUpdateRequestComment**](RegistrationsUpdateRequestComment.md) |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.registrations_update_request import RegistrationsUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RegistrationsUpdateRequest from a JSON string
registrations_update_request_instance = RegistrationsUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(RegistrationsUpdateRequest.to_json())

# convert the object into a dict
registrations_update_request_dict = registrations_update_request_instance.to_dict()
# create an instance of RegistrationsUpdateRequest from a dict
registrations_update_request_from_dict = RegistrationsUpdateRequest.from_dict(registrations_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


