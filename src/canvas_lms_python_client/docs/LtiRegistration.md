# LtiRegistration

A registration of an LTI tool in Canvas

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | the Canvas ID of the Lti_Registration object | [optional] 
**name** | **str** | Tool-provided registration name | [optional] 
**admin_nickname** | **str** | Admin-configured friendly display name | [optional] 
**icon_url** | **str** | Tool-provided URL to the tool&#39;s icon | [optional] 
**vendor** | **str** | Tool-provided name of the tool vendor | [optional] 
**account_id** | **int** | The Canvas id of the account that owns this registration | [optional] 
**internal_service** | **bool** | Flag indicating if registration is internally-owned | [optional] 
**lock_deploying** | **bool** | Flag indicating if registration is locked for deployment | [optional] 
**inherited** | **bool** | Flag indicating if registration is owned by this account, or inherited from Site Admin | [optional] 
**template_registration_id** | **int** | The Canvas ID of the template registration, if this registration is inherited from a template | [optional] 
**lti_version** | **str** | LTI version of the registration, either 1.1 or 1.3 | [optional] 
**dynamic_registration** | **bool** | Flag indicating if registration was created using LTI Dynamic Registration. Only present if lti_version is 1.3 | [optional] 
**workflow_state** | **str** | The state of the registration | [optional] 
**created_at** | **str** | Timestamp of the registration&#39;s creation | [optional] 
**updated_at** | **str** | Timestamp of the registration&#39;s last update | [optional] 
**created_by** | [**LtiRegistrationCreatedBy**](LtiRegistrationCreatedBy.md) |  | [optional] 
**updated_by** | [**LtiRegistrationCreatedBy**](LtiRegistrationCreatedBy.md) |  | [optional] 
**root_account_id** | **int** | The Canvas id of the root account | [optional] 
**account_binding** | [**LtiRegistrationAccountBinding**](LtiRegistrationAccountBinding.md) |  | [optional] 
**configuration** | [**LtiToolConfiguration**](LtiToolConfiguration.md) |  | [optional] 
**description** | **str** |  | [optional] 
**developer_key_id** | **int** |  | [optional] 
**dynamic_registration_url** | **object** |  | [optional] 
**ims_registration_id** | **int** |  | [optional] 
**manual_configuration_id** | **int** |  | [optional] 
**overlay** | **object** |  | [optional] 
**pending_update** | **str** |  | [optional] 
**reinstall_disabled** | **bool** |  | [optional] 
**overlaid_configuration** | **object** |  | [optional] 
**overlaid_legacy_configuration** | **object** |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.lti_registration import LtiRegistration

# TODO update the JSON string below
json = "{}"
# create an instance of LtiRegistration from a JSON string
lti_registration_instance = LtiRegistration.from_json(json)
# print the JSON string representation of the object
print(LtiRegistration.to_json())

# convert the object into a dict
lti_registration_dict = lti_registration_instance.to_dict()
# create an instance of LtiRegistration from a dict
lti_registration_from_dict = LtiRegistration.from_dict(lti_registration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


