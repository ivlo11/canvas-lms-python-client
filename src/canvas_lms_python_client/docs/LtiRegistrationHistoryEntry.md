# LtiRegistrationHistoryEntry

A change made to an LTI registration, its configuration or its context controls

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The Canvas id of the history entry | [optional] 
**root_account_id** | **int** | The Canvas id of the root account | [optional] 
**lti_registration_id** | **int** | The id of the registration this entry is for | [optional] 
**created_at** | **datetime** | Timestamp of the entry&#39;s creation | [optional] 
**updated_at** | **datetime** | Timestamp of the entry&#39;s last update | [optional] 
**diff** | [**LtiRegistrationHistoryEntryDiff**](LtiRegistrationHistoryEntryDiff.md) |  | [optional] 
**update_type** | **str** | What caused the change: manual_edit, registration_update, bulk_control_create or control_edit | [optional] 
**comment** | **str** | A comment entered with the change, if any | [optional] 
**old_configuration** | **object** | The registration&#39;s configuration before the change, for configuration changes | [optional] 
**new_configuration** | **object** | The registration&#39;s configuration after the change, for configuration changes | [optional] 
**created_by** | [**LtiRegistrationCreatedBy**](LtiRegistrationCreatedBy.md) |  | [optional] 
**old_controls_by_deployment** | [**List[LtiDeployment]**](LtiDeployment.md) | The affected deployments and their context controls before the change, for control changes | [optional] 
**new_controls_by_deployment** | [**List[LtiDeployment]**](LtiDeployment.md) | The affected deployments and their context controls after the change, for control changes | [optional] 
**accepted_at** | **str** |  | [optional] 
**internal_lti_configuration** | **object** |  | [optional] 
**reinstall** | **bool** |  | [optional] 
**rejected_at** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**tool_initiated** | **bool** |  | [optional] 
**uuid** | **str** |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.lti_registration_history_entry import LtiRegistrationHistoryEntry

# TODO update the JSON string below
json = "{}"
# create an instance of LtiRegistrationHistoryEntry from a JSON string
lti_registration_history_entry_instance = LtiRegistrationHistoryEntry.from_json(json)
# print the JSON string representation of the object
print(LtiRegistrationHistoryEntry.to_json())

# convert the object into a dict
lti_registration_history_entry_dict = lti_registration_history_entry_instance.to_dict()
# create an instance of LtiRegistrationHistoryEntry from a dict
lti_registration_history_entry_from_dict = LtiRegistrationHistoryEntry.from_dict(lti_registration_history_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


