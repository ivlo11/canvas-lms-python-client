# LtiLegacyConfiguration

A legacy configuration format for LTI 1.3 tools.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | The display name of the tool | [optional] 
**description** | **str** | The description of the tool | [optional] 
**custom_fields** | **object** | A key-value listing of all custom fields the tool has requested | [optional] 
**target_link_uri** | **str** | The default launch URL for the tool. Overridable by placements. | [optional] 
**oidc_initiation_url** | **str** | 1.3 specific. URL used for initial login request | [optional] 
**oidc_initiation_urls** | **object** | 1.3 specific. Region-specific login URLs for data protection compliance | [optional] 
**public_jwk** | **object** | 1.3 specific. The tool&#39;s public JWK in JSON format. Discouraged in favor of a url hosting a JWK set. | [optional] 
**public_jwk_url** | **str** | 1.3 specific. The tool-hosted URL containing its public JWK keyset. Canvas may cache JWKs up to 5 minutes. | [optional] 
**scopes** | **List[str]** | 1.3 specific. List of LTI scopes requested by the tool | [optional] 
**extensions** | [**List[LtiLegacyConfigurationExtensionsInner]**](LtiLegacyConfigurationExtensionsInner.md) | Array of extensions for the tool | [optional] 

## Example

```python
from canvas_lms_python_client.models.lti_legacy_configuration import LtiLegacyConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of LtiLegacyConfiguration from a JSON string
lti_legacy_configuration_instance = LtiLegacyConfiguration.from_json(json)
# print the JSON string representation of the object
print(LtiLegacyConfiguration.to_json())

# convert the object into a dict
lti_legacy_configuration_dict = lti_legacy_configuration_instance.to_dict()
# create an instance of LtiLegacyConfiguration from a dict
lti_legacy_configuration_from_dict = LtiLegacyConfiguration.from_dict(lti_legacy_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


