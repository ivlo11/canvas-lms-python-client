# LtiToolConfiguration

A Registration's Canvas-specific tool configuration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | The display name of the tool | [optional] 
**description** | **str** | The description of the tool | [optional] 
**custom_fields** | **object** | A key-value listing of all custom fields the tool has requested | [optional] 
**target_link_uri** | **str** | The default launch URL for the tool. Overridable by placements. | [optional] 
**domain** | **str** | The tool&#39;s main domain. Highly recommended for deep linking, used to match links to the tool. | [optional] 
**tool_id** | **str** | Tool-provided identifier, can be anything | [optional] 
**privacy_level** | **str** | Canvas-defined privacy level for the tool | [optional] 
**oidc_initiation_url** | **str** | 1.3 specific. URL used for initial login request | [optional] 
**oidc_initiation_urls** | **object** | 1.3 specific. Region-specific login URLs for data protection compliance | [optional] 
**public_jwk** | **object** | 1.3 specific. The tool&#39;s public JWK in JSON format. Discouraged in favor of a url hosting a JWK set. | [optional] 
**public_jwk_url** | **str** | 1.3 specific. The tool-hosted URL containing its public JWK keyset. Canvas may cache JWKs up to 5 minutes. | [optional] 
**scopes** | **List[str]** | 1.3 specific. List of LTI scopes requested by the tool | [optional] 
**redirect_uris** | **List[str]** | 1.3 specific. List of possible launch URLs for after the Canvas authorize redirect step | [optional] 
**launch_settings** | [**LtiLaunchSettings**](LtiLaunchSettings.md) |  | [optional] 
**placements** | [**List[LtiPlacement]**](LtiPlacement.md) | List of placements configured by the tool | [optional] 

## Example

```python
from canvas_lms_python_client.models.lti_tool_configuration import LtiToolConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of LtiToolConfiguration from a JSON string
lti_tool_configuration_instance = LtiToolConfiguration.from_json(json)
# print the JSON string representation of the object
print(LtiToolConfiguration.to_json())

# convert the object into a dict
lti_tool_configuration_dict = lti_tool_configuration_instance.to_dict()
# create an instance of LtiToolConfiguration from a dict
lti_tool_configuration_from_dict = LtiToolConfiguration.from_dict(lti_tool_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


