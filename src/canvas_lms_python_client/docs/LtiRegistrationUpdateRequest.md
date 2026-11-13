# LtiRegistrationUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accepted_at** | **str** |  | [optional] 
**comment** | **object** |  | [optional] 
**created_at** | **str** |  | [optional] 
**created_by** | **object** |  | [optional] 
**id** | **int** |  | [optional] 
**internal_lti_configuration** | **object** |  | [optional] 
**lti_registration_id** | **int** |  | [optional] 
**reinstall** | **bool** |  | [optional] 
**rejected_at** | **str** |  | [optional] 
**root_account_id** | **int** |  | [optional] 
**status** | **str** |  | [optional] 
**tool_initiated** | **bool** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**uuid** | **str** |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.lti_registration_update_request import LtiRegistrationUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LtiRegistrationUpdateRequest from a JSON string
lti_registration_update_request_instance = LtiRegistrationUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(LtiRegistrationUpdateRequest.to_json())

# convert the object into a dict
lti_registration_update_request_dict = lti_registration_update_request_instance.to_dict()
# create an instance of LtiRegistrationUpdateRequest from a dict
lti_registration_update_request_from_dict = LtiRegistrationUpdateRequest.from_dict(lti_registration_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


