# RegistrationsValidateLtiConfigurationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lti_configuration** | **str** | The LTI 1.3 JSON config to validate. | [optional] 
**url** | **str** | The URL to fetch the LTI 1.3 JSON config from. | [optional] 

## Example

```python
from canvas_lms_python_client.models.registrations_validate_lti_configuration_request import RegistrationsValidateLtiConfigurationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RegistrationsValidateLtiConfigurationRequest from a JSON string
registrations_validate_lti_configuration_request_instance = RegistrationsValidateLtiConfigurationRequest.from_json(json)
# print the JSON string representation of the object
print(RegistrationsValidateLtiConfigurationRequest.to_json())

# convert the object into a dict
registrations_validate_lti_configuration_request_dict = registrations_validate_lti_configuration_request_instance.to_dict()
# create an instance of RegistrationsValidateLtiConfigurationRequest from a dict
registrations_validate_lti_configuration_request_from_dict = RegistrationsValidateLtiConfigurationRequest.from_dict(registrations_validate_lti_configuration_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


