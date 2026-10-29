# LtiOverlay

Changes made by a Canvas admin to a tool's configuration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | The display name of the tool | [optional] 
**description** | **str** | The description of the tool | [optional] 
**custom_fields** | **object** | A key-value listing of all custom fields the tool has requested | [optional] 
**target_link_uri** | **str** | The default launch URL for the tool. Overridable by placements. | [optional] 
**domain** | **str** | The tool&#39;s main domain. Highly recommended for deep linking, used to match links to the tool. | [optional] 
**privacy_level** | **str** | Canvas-defined privacy level for the tool | [optional] 
**oidc_initiation_url** | **str** | 1.3 specific. URL used for initial login request | [optional] 
**disabled_scopes** | **List[str]** | 1.3 specific. List of LTI scopes that the tool has requested but an admin has disabled | [optional] 
**disabled_placements** | **List[str]** | List of placements that the tool has requested but an admin has disabled | [optional] 
**placements** | **object** | Placement-specific settings changed by an admin | [optional] 

## Example

```python
from canvas_lms_python_client.models.lti_overlay import LtiOverlay

# TODO update the JSON string below
json = "{}"
# create an instance of LtiOverlay from a JSON string
lti_overlay_instance = LtiOverlay.from_json(json)
# print the JSON string representation of the object
print(LtiOverlay.to_json())

# convert the object into a dict
lti_overlay_dict = lti_overlay_instance.to_dict()
# create an instance of LtiOverlay from a dict
lti_overlay_from_dict = LtiOverlay.from_dict(lti_overlay_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


