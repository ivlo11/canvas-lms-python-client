# RegistrationsApplyRegistrationUpdateRequestRequestOverlay


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lti_configuration_overlay** | **str** | Optional overlay data to apply on top of the new configuration. | [optional] 

## Example

```python
from canvas_lms_python_client.models.registrations_apply_registration_update_request_request_overlay import RegistrationsApplyRegistrationUpdateRequestRequestOverlay

# TODO update the JSON string below
json = "{}"
# create an instance of RegistrationsApplyRegistrationUpdateRequestRequestOverlay from a JSON string
registrations_apply_registration_update_request_request_overlay_instance = RegistrationsApplyRegistrationUpdateRequestRequestOverlay.from_json(json)
# print the JSON string representation of the object
print(RegistrationsApplyRegistrationUpdateRequestRequestOverlay.to_json())

# convert the object into a dict
registrations_apply_registration_update_request_request_overlay_dict = registrations_apply_registration_update_request_request_overlay_instance.to_dict()
# create an instance of RegistrationsApplyRegistrationUpdateRequestRequestOverlay from a dict
registrations_apply_registration_update_request_request_overlay_from_dict = RegistrationsApplyRegistrationUpdateRequestRequestOverlay.from_dict(registrations_apply_registration_update_request_request_overlay_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


