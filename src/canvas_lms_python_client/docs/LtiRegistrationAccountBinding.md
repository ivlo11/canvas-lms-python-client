# LtiRegistrationAccountBinding

A binding between an LTI registration and an account, defining the registration's availability in that account

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | the Canvas ID of the Lti_RegistrationAccountBinding object | [optional] 
**account_id** | **int** | The Canvas id of the account | [optional] 
**root_account_id** | **int** | The Canvas id of the root account | [optional] 
**registration_id** | **int** | The Canvas id of the Lti_Registration | [optional] 
**workflow_state** | **str** | The state of the binding (on, off, allow, deleted) | [optional] 
**created_at** | **str** | Timestamp of the binding&#39;s creation | [optional] 
**updated_at** | **str** | Timestamp of the binding&#39;s last update | [optional] 
**created_by** | [**User**](User.md) |  | [optional] 
**updated_by** | [**User**](User.md) |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.lti_registration_account_binding import LtiRegistrationAccountBinding

# TODO update the JSON string below
json = "{}"
# create an instance of LtiRegistrationAccountBinding from a JSON string
lti_registration_account_binding_instance = LtiRegistrationAccountBinding.from_json(json)
# print the JSON string representation of the object
print(LtiRegistrationAccountBinding.to_json())

# convert the object into a dict
lti_registration_account_binding_dict = lti_registration_account_binding_instance.to_dict()
# create an instance of LtiRegistrationAccountBinding from a dict
lti_registration_account_binding_from_dict = LtiRegistrationAccountBinding.from_dict(lti_registration_account_binding_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


