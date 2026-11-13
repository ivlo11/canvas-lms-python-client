# ContextExternalToolPlacement

Configuration for a specific placement of an external tool. If null, no configuration is present.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Whether this placement is enabled | [optional] 
**url** | **str** | The launch URL for this specific placement. Overrides the tool&#39;s default URL. For LTI 1.1 tools only. | [optional] 
**target_link_uri** | **str** | The launch URL for this specific placement. Overrides the tool&#39;s default target_link_uri. For LTI 1.3 tools only. | [optional] 
**text** | **str** | The text/label to display for this placement. Overridable by &#39;labels&#39; in placement configuration. | [optional] 
**label** | **str** | The localized label for this placement. This is the resolved text after applying internationalization. | [optional] 
**labels** | **object** | Internationalization labels for this placement. Keys are locale codes, values are localized text. | [optional] 
**message_type** | **str** | The LTI message type for this placement. Not all placements support all message types. | [optional] 
**selection_width** | **int** | The width of the iframe or popup for this placement | [optional] 
**selection_height** | **int** | The height of the iframe or popup for this placement | [optional] 
**launch_width** | **int** | The width of the launch window. Not standard everywhere yet. | [optional] 
**launch_height** | **int** | The height of the launch window. Not standard everywhere yet. | [optional] 
**icon_url** | **str** | The URL of the icon for this placement | [optional] 
**canvas_icon_class** | **str** | The Canvas icon class to use for this placement instead of an icon URL | [optional] 
**allow_fullscreen** | **bool** | Whether to allow fullscreen mode for this placement (top_navigation placement only) | [optional] 
**custom_fields** | **object** | Custom fields to be sent with this placement&#39;s launch. Merged with tool-level custom fields. | [optional] 
**visibility** | **str** | Controls who can see this placement | [optional] 
**required_permissions** | **str** | Comma-separated list of Canvas permissions required to launch from this placement. The user must have all permissions in order to launch the tool. | [optional] 
**default** | **str** | Default display state for navigation placements. Only applies to account_navigation and course_navigation placements. | [optional] 
**display_type** | **str** | The layout type to use when launching the tool. For global_navigation and analytics_hub, defaults to &#39;full_width&#39;. | [optional] 
**window_target** | **str** | When set to &#39;_blank&#39;, opens placement in a new tab. Only &#39;_blank&#39; is supported. | [optional] 
**accept_media_types** | **str** | Comma-separated list of media types that the tool can accept. Only valid for file_menu placement. | [optional] 
**use_tray** | **bool** | If true, the tool will be launched in the tray. Only used by the editor_button placement. | [optional] 
**icon_svg_path_64** | **str** | An SVG path to use instead of an icon_url. Only valid for global_navigation placement. | [optional] 
**root_account_only** | **bool** | Whether this placement should only be available at the root account level. Only applies to account_navigation placement. | [optional] 
**description** | **str** | A description of this placement. Only valid for submission_type_selection placement. Maximum length of 255 characters. | [optional] 
**require_resource_selection** | **bool** | Whether resource selection is required for this placement. Only valid for submission_type_selection placement. | [optional] 
**prefer_sis_email** | [**ContextExternalToolPlacementPreferSisEmail**](ContextExternalToolPlacementPreferSisEmail.md) |  | [optional] 
**oauth_compliant** | **bool** | If true, query parameters from the launch URL will not be copied to the POST body. LTI 1.1 only. | [optional] 
**placement** | **str** |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.context_external_tool_placement import ContextExternalToolPlacement

# TODO update the JSON string below
json = "{}"
# create an instance of ContextExternalToolPlacement from a JSON string
context_external_tool_placement_instance = ContextExternalToolPlacement.from_json(json)
# print the JSON string representation of the object
print(ContextExternalToolPlacement.to_json())

# convert the object into a dict
context_external_tool_placement_dict = context_external_tool_placement_instance.to_dict()
# create an instance of ContextExternalToolPlacement from a dict
context_external_tool_placement_from_dict = ContextExternalToolPlacement.from_dict(context_external_tool_placement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


