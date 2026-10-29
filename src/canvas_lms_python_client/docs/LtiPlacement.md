# LtiPlacement

The tool's configuration for a specific placement

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**placement** | **str** | The name of the placement. | [optional] 
**enabled** | **bool** | If true, the tool will show in this placement. If false, it will not. | [optional] 
**message_type** | **str** | Default message type for all placements | [optional] 
**text** | **str** | The text of the link to the tool (if applicable). | [optional] 
**labels** | **object** | Canvas-specific i18n for placement text. See the Navigation Placement docs. | [optional] 
**custom_fields** | **object** | Placement-specific custom fields to send in the launch. Merged with tool-level custom fields. | [optional] 
**selection_height** | **float** | Default iframe height. Not valid for all placements. Overrides tool-level launch_height. | [optional] 
**selection_width** | **float** | Default iframe width. Not valid for all placements. Overrides tool-level launch_width. | [optional] 
**launch_height** | **float** | Default iframe height. Not valid for all placements. Overrides tool-level launch_height. | [optional] 
**launch_width** | **float** | Default iframe width. Not valid for all placements. Overrides tool-level launch_width. | [optional] 
**icon_url** | **str** | Default icon URL. Not valid for all placements. Overrides tool-level icon_url. | [optional] 
**canvas_icon_class** | **str** | The HTML class name of an InstUI Icon. Used instead of an icon_url in select placements. | [optional] 
**required_permissions** | **str** | Comma-separated list of Canvas permission short names required for a user to launch from this placement. | [optional] 
**window_target** | **str** | When set to &#39;_blank&#39;, opens placement in a new tab. | [optional] 
**display_type** | **str** | The Canvas layout to use when launching the tool. See the Navigation Placement docs. | [optional] 
**url** | **str** | The 1.1 launch URL for this placement. Overrides tool-level url. | [optional] 
**target_link_uri** | **str** | The 1.3 launch URL for this placement. Overrides tool-level target_link_uri. | [optional] 
**visibility** | **str** | Specifies types of users that can see this placement. Only valid for some placements like course_navigation. | [optional] 
**prefer_sis_email** | **bool** | 1.1 specific. If true, the tool will send the SIS email in the lis_person_contact_email_primary launch property | [optional] 
**oauth_compliant** | **bool** | 1.1 specific. If true, query parameters from the launch URL will not be copied to the POST body. | [optional] 
**icon_svg_path_64** | **str** | An SVG to use instead of an icon_url. Only valid for global_navigation. | [optional] 
**default** | **str** | Default display state for course_navigation. If &#39;enabled&#39;, will show in course sidebar. If &#39;disabled&#39;, will be hidden. | [optional] 
**accept_media_types** | **str** | Comma-separated list of media types that the tool can accept. Only valid for file_item. | [optional] 
**use_tray** | **bool** | If true, the tool will be launched in the tray. Only used by the editor_button placement. | [optional] 

## Example

```python
from canvas_lms_python_client.models.lti_placement import LtiPlacement

# TODO update the JSON string below
json = "{}"
# create an instance of LtiPlacement from a JSON string
lti_placement_instance = LtiPlacement.from_json(json)
# print the JSON string representation of the object
print(LtiPlacement.to_json())

# convert the object into a dict
lti_placement_dict = lti_placement_instance.to_dict()
# create an instance of LtiPlacement from a dict
lti_placement_from_dict = LtiPlacement.from_dict(lti_placement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


