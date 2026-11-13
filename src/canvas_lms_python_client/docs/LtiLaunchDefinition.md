# LtiLaunchDefinition

A bare-bones representation of an LTI tool used by Canvas to launch the tool

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**definition_type** | **str** | The type of the launch definition. Always &#39;ContextExternalTool&#39; | [optional] 
**definition_id** | **int** | The Canvas ID of the tool | [optional] 
**name** | **str** | The display name of the tool for the given placement | [optional] 
**description** | **str** | The description of the tool for the given placement. | [optional] 
**url** | **str** | The launch URL for the tool | [optional] 
**domain** | **str** | The domain of the tool | [optional] 
**placements** | **object** | Placement-specific config for given placements | [optional] 
**context_name** | **str** | The name of the account or course where the tool is deployed. Only included if requested via include_context_name parameter. | [optional] 

## Example

```python
from canvas_lms_python_client.models.lti_launch_definition import LtiLaunchDefinition

# TODO update the JSON string below
json = "{}"
# create an instance of LtiLaunchDefinition from a JSON string
lti_launch_definition_instance = LtiLaunchDefinition.from_json(json)
# print the JSON string representation of the object
print(LtiLaunchDefinition.to_json())

# convert the object into a dict
lti_launch_definition_dict = lti_launch_definition_instance.to_dict()
# create an instance of LtiLaunchDefinition from a dict
lti_launch_definition_from_dict = LtiLaunchDefinition.from_dict(lti_launch_definition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


