# RegistrationsUpdateRequestConfiguration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lti__tool_configuration___lti__legacy_configuration** | **str** | The LTI 1.3 configuration for the tool. Note that updating the base tool configuration of a registration associated with a Dynamic Registration is not allowed. | [optional] 

## Example

```python
from canvas_lms_python_client.models.registrations_update_request_configuration import RegistrationsUpdateRequestConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of RegistrationsUpdateRequestConfiguration from a JSON string
registrations_update_request_configuration_instance = RegistrationsUpdateRequestConfiguration.from_json(json)
# print the JSON string representation of the object
print(RegistrationsUpdateRequestConfiguration.to_json())

# convert the object into a dict
registrations_update_request_configuration_dict = registrations_update_request_configuration_instance.to_dict()
# create an instance of RegistrationsUpdateRequestConfiguration from a dict
registrations_update_request_configuration_from_dict = RegistrationsUpdateRequestConfiguration.from_dict(registrations_update_request_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


