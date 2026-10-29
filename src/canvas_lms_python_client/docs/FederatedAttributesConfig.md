# FederatedAttributesConfig

A mapping of Canvas attribute names to attribute names that a provider may send, in order to update the value of these attributes when a user logs in. The values can be a FederatedAttributeConfig, or a raw string corresponding to the \"attribute\" property of a FederatedAttributeConfig. In responses, full FederatedAttributeConfig objects are returned if JIT provisioning is enabled, otherwise just the attribute names are returned.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**admin_roles** | **str** | A comma separated list of role names to grant to the user. Note that these only apply at the root account level, and not sub-accounts. If the attribute is not marked for provisioning only, the user will also be removed from any other roles they currently hold that are not still specified by the IdP. | [optional] 
**display_name** | **str** | The full display name of the user | [optional] 
**email** | **str** | The user&#39;s e-mail address | [optional] 
**given_name** | **str** | The first, or given, name of the user | [optional] 
**integration_id** | **str** | The secondary unique identifier for SIS purposes | [optional] 
**locale** | **str** | The user&#39;s preferred locale/language | [optional] 
**name** | **str** | The full name of the user | [optional] 
**sis_user_id** | **str** | The unique SIS identifier | [optional] 
**sortable_name** | **str** | The full name of the user for sorting purposes | [optional] 
**surname** | **str** | The surname, or last name, of the user | [optional] 
**timezone** | **str** | The user&#39;s preferred time zone | [optional] 

## Example

```python
from canvas_lms_python_client.models.federated_attributes_config import FederatedAttributesConfig

# TODO update the JSON string below
json = "{}"
# create an instance of FederatedAttributesConfig from a JSON string
federated_attributes_config_instance = FederatedAttributesConfig.from_json(json)
# print the JSON string representation of the object
print(FederatedAttributesConfig.to_json())

# convert the object into a dict
federated_attributes_config_dict = federated_attributes_config_instance.to_dict()
# create an instance of FederatedAttributesConfig from a dict
federated_attributes_config_from_dict = FederatedAttributesConfig.from_dict(federated_attributes_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


