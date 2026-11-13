# LtiImsDynamicRegistrationCreateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_type** | **str** |  | [optional] 
**client_id** | **str** |  | [optional] 
**client_name** | **str** |  | [optional] 
**deployment_id** | **str** |  | [optional] 
**grant_types** | **List[str]** |  | [optional] 
**initiate_login_uri** | **str** |  | [optional] 
**jwks_uri** | **str** |  | [optional] 
**logo_uri** | **str** |  | [optional] 
**redirect_uris** | **List[str]** |  | [optional] 
**registration_client_uri** | **str** |  | [optional] 
**response_types** | **List[str]** |  | [optional] 
**scope** | **str** |  | [optional] 
**token_endpoint_auth_method** | **str** |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.lti_ims_dynamic_registration_create_response import LtiImsDynamicRegistrationCreateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LtiImsDynamicRegistrationCreateResponse from a JSON string
lti_ims_dynamic_registration_create_response_instance = LtiImsDynamicRegistrationCreateResponse.from_json(json)
# print the JSON string representation of the object
print(LtiImsDynamicRegistrationCreateResponse.to_json())

# convert the object into a dict
lti_ims_dynamic_registration_create_response_dict = lti_ims_dynamic_registration_create_response_instance.to_dict()
# create an instance of LtiImsDynamicRegistrationCreateResponse from a dict
lti_ims_dynamic_registration_create_response_from_dict = LtiImsDynamicRegistrationCreateResponse.from_dict(lti_ims_dynamic_registration_create_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


