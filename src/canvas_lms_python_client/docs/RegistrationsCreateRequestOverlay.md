# RegistrationsCreateRequestOverlay


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lti__overlay** | **str** | The overlay configuration for the tool. Overrides values in the base configuration. | [optional] 

## Example

```python
from canvas_lms_python_client.models.registrations_create_request_overlay import RegistrationsCreateRequestOverlay

# TODO update the JSON string below
json = "{}"
# create an instance of RegistrationsCreateRequestOverlay from a JSON string
registrations_create_request_overlay_instance = RegistrationsCreateRequestOverlay.from_json(json)
# print the JSON string representation of the object
print(RegistrationsCreateRequestOverlay.to_json())

# convert the object into a dict
registrations_create_request_overlay_dict = registrations_create_request_overlay_instance.to_dict()
# create an instance of RegistrationsCreateRequestOverlay from a dict
registrations_create_request_overlay_from_dict = RegistrationsCreateRequestOverlay.from_dict(registrations_create_request_overlay_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


