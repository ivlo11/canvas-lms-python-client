# RegistrationsUpdateRequestOverlay


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lti__overlay** | **str** | The overlay configuration for the tool. Overrides values in the base configuration. Note that updating the overlay of a registration associated with a Dynamic Registration IS allowed. | [optional] 

## Example

```python
from canvas_lms_python_client.models.registrations_update_request_overlay import RegistrationsUpdateRequestOverlay

# TODO update the JSON string below
json = "{}"
# create an instance of RegistrationsUpdateRequestOverlay from a JSON string
registrations_update_request_overlay_instance = RegistrationsUpdateRequestOverlay.from_json(json)
# print the JSON string representation of the object
print(RegistrationsUpdateRequestOverlay.to_json())

# convert the object into a dict
registrations_update_request_overlay_dict = registrations_update_request_overlay_instance.to_dict()
# create an instance of RegistrationsUpdateRequestOverlay from a dict
registrations_update_request_overlay_from_dict = RegistrationsUpdateRequestOverlay.from_dict(registrations_update_request_overlay_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


