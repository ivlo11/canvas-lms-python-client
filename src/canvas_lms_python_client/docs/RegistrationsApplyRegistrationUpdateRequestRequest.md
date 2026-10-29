# RegistrationsApplyRegistrationUpdateRequestRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accepted** | **bool** | Whether to accept (true) or reject (false) the registration update request. | 
**comment** | **str** | Optional comment explaining the reason for applying this update. | [optional] 
**overlay** | [**RegistrationsApplyRegistrationUpdateRequestRequestOverlay**](RegistrationsApplyRegistrationUpdateRequestRequestOverlay.md) |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.registrations_apply_registration_update_request_request import RegistrationsApplyRegistrationUpdateRequestRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RegistrationsApplyRegistrationUpdateRequestRequest from a JSON string
registrations_apply_registration_update_request_request_instance = RegistrationsApplyRegistrationUpdateRequestRequest.from_json(json)
# print the JSON string representation of the object
print(RegistrationsApplyRegistrationUpdateRequestRequest.to_json())

# convert the object into a dict
registrations_apply_registration_update_request_request_dict = registrations_apply_registration_update_request_request_instance.to_dict()
# create an instance of RegistrationsApplyRegistrationUpdateRequestRequest from a dict
registrations_apply_registration_update_request_request_from_dict = RegistrationsApplyRegistrationUpdateRequestRequest.from_dict(registrations_apply_registration_update_request_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


