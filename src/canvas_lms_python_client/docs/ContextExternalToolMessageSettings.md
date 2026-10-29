# ContextExternalToolMessageSettings

Configuration for a placementless message type (message type that doesn't belong to a specific placement)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The message type identifier (e.g., &#39;LtiEulaRequest&#39;) | [optional] 
**enabled** | **bool** | Whether this message type is enabled | [optional] 
**target_link_uri** | **str** | The target URI for launching this message type | [optional] 
**custom_fields** | **object** | Custom fields specific to this message type. | [optional] 

## Example

```python
from canvas_lms_python_client.models.context_external_tool_message_settings import ContextExternalToolMessageSettings

# TODO update the JSON string below
json = "{}"
# create an instance of ContextExternalToolMessageSettings from a JSON string
context_external_tool_message_settings_instance = ContextExternalToolMessageSettings.from_json(json)
# print the JSON string representation of the object
print(ContextExternalToolMessageSettings.to_json())

# convert the object into a dict
context_external_tool_message_settings_dict = context_external_tool_message_settings_instance.to_dict()
# create an instance of ContextExternalToolMessageSettings from a dict
context_external_tool_message_settings_from_dict = ContextExternalToolMessageSettings.from_dict(context_external_tool_message_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


