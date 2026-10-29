# LtiPlacementLaunchDefinition

A bare-bones LTI configuration for a specific placement

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message_type** | **str** | The LTI launch message type | [optional] 
**url** | **str** | The launch URL for this placement | [optional] 
**title** | **str** | The title of the tool for this placement | [optional] 

## Example

```python
from canvas_lms_python_client.models.lti_placement_launch_definition import LtiPlacementLaunchDefinition

# TODO update the JSON string below
json = "{}"
# create an instance of LtiPlacementLaunchDefinition from a JSON string
lti_placement_launch_definition_instance = LtiPlacementLaunchDefinition.from_json(json)
# print the JSON string representation of the object
print(LtiPlacementLaunchDefinition.to_json())

# convert the object into a dict
lti_placement_launch_definition_dict = lti_placement_launch_definition_instance.to_dict()
# create an instance of LtiPlacementLaunchDefinition from a dict
lti_placement_launch_definition_from_dict = LtiPlacementLaunchDefinition.from_dict(lti_placement_launch_definition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


