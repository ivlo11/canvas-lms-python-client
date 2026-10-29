# ToolSetting



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_type_code** | **str** | the resource type code of the resource handler to use to display originality reports | [optional] 
**resource_url** | **str** | a URL that may be used to override the launch URL inferred by the specified resource_type_code. If used a &#39;resource_type_code&#39; must also be specified. | [optional] 

## Example

```python
from canvas_lms_python_client.models.tool_setting import ToolSetting

# TODO update the JSON string below
json = "{}"
# create an instance of ToolSetting from a JSON string
tool_setting_instance = ToolSetting.from_json(json)
# print the JSON string representation of the object
print(ToolSetting.to_json())

# convert the object into a dict
tool_setting_dict = tool_setting_instance.to_dict()
# create an instance of ToolSetting from a dict
tool_setting_from_dict = ToolSetting.from_dict(tool_setting_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


