# LtiLegacyConfigurationExtensionsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**platform** | **str** | Must be canvas.instructure.com | 
**domain** | **str** | The domain of the tool | [optional] 
**tool_id** | **str** | Tool-provided identifier, can be anything | [optional] 
**privacy_level** | **str** | Canvas-defined privacy level for the tool | [optional] 
**settings** | [**LtiLegacyConfigurationExtensionsInnerSettings**](LtiLegacyConfigurationExtensionsInnerSettings.md) |  | 

## Example

```python
from canvas_lms_python_client.models.lti_legacy_configuration_extensions_inner import LtiLegacyConfigurationExtensionsInner

# TODO update the JSON string below
json = "{}"
# create an instance of LtiLegacyConfigurationExtensionsInner from a JSON string
lti_legacy_configuration_extensions_inner_instance = LtiLegacyConfigurationExtensionsInner.from_json(json)
# print the JSON string representation of the object
print(LtiLegacyConfigurationExtensionsInner.to_json())

# convert the object into a dict
lti_legacy_configuration_extensions_inner_dict = lti_legacy_configuration_extensions_inner_instance.to_dict()
# create an instance of LtiLegacyConfigurationExtensionsInner from a dict
lti_legacy_configuration_extensions_inner_from_dict = LtiLegacyConfigurationExtensionsInner.from_dict(lti_legacy_configuration_extensions_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


