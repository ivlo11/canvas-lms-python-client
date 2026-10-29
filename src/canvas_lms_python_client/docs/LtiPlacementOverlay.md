# LtiPlacementOverlay

Changes made by a Canvas admin to a tool's configuration for a specific placement.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** | The text of the link to the tool (if applicable). | [optional] 
**target_link_uri** | **str** | The default launch URL for the tool. Overridable by placements. | [optional] 
**message_type** | **str** | Default message type for all placements | [optional] 
**launch_height** | **float** | Default iframe height. Not valid for all placements. Overrides tool-level launch_height. | [optional] 
**launch_width** | **float** | Default iframe width. Not valid for all placements. Overrides tool-level launch_width. | [optional] 
**icon_url** | **str** | Default icon URL. Not valid for all placements. Overrides tool-level icon_url. | [optional] 
**default** | **str** | Default display state for course_navigation. If &#39;enabled&#39;, will show in course sidebar. If &#39;disabled&#39;, will be hidden. | [optional] 

## Example

```python
from canvas_lms_python_client.models.lti_placement_overlay import LtiPlacementOverlay

# TODO update the JSON string below
json = "{}"
# create an instance of LtiPlacementOverlay from a JSON string
lti_placement_overlay_instance = LtiPlacementOverlay.from_json(json)
# print the JSON string representation of the object
print(LtiPlacementOverlay.to_json())

# convert the object into a dict
lti_placement_overlay_dict = lti_placement_overlay_instance.to_dict()
# create an instance of LtiPlacementOverlay from a dict
lti_placement_overlay_from_dict = LtiPlacementOverlay.from_dict(lti_placement_overlay_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


