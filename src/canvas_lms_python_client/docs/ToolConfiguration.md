# ToolConfiguration

A tool configuration associated with a developer key

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**developer_key_id** | **int** | The tool configuration&#39;s developer key id | [optional] 
**settings** | **object** | The tool configuration JSON | [optional] 

## Example

```python
from canvas_lms_python_client.models.tool_configuration import ToolConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of ToolConfiguration from a JSON string
tool_configuration_instance = ToolConfiguration.from_json(json)
# print the JSON string representation of the object
print(ToolConfiguration.to_json())

# convert the object into a dict
tool_configuration_dict = tool_configuration_instance.to_dict()
# create an instance of ToolConfiguration from a dict
tool_configuration_from_dict = ToolConfiguration.from_dict(tool_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


