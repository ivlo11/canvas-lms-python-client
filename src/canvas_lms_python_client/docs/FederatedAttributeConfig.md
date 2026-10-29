# FederatedAttributeConfig

A single attribute name to be federated when a user logs in

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute** | **str** | The name of the attribute as it will be sent from the authentication provider | [optional] 
**provisioning_only** | **bool** | If the attribute should be applied only when provisioning a new user, rather than all logins | [optional] 
**autoconfirm** | **bool** | (only for email) If the email address is trusted and should be automatically confirmed | [optional] 

## Example

```python
from canvas_lms_python_client.models.federated_attribute_config import FederatedAttributeConfig

# TODO update the JSON string below
json = "{}"
# create an instance of FederatedAttributeConfig from a JSON string
federated_attribute_config_instance = FederatedAttributeConfig.from_json(json)
# print the JSON string representation of the object
print(FederatedAttributeConfig.to_json())

# convert the object into a dict
federated_attribute_config_dict = federated_attribute_config_instance.to_dict()
# create an instance of FederatedAttributeConfig from a dict
federated_attribute_config_from_dict = FederatedAttributeConfig.from_dict(federated_attribute_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


