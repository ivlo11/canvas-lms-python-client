# ExternalToolTagAttributes



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | URL to the external tool | [optional] 
**new_tab** | **bool** | Whether or not there is a new tab for the external tool | [optional] 
**resource_link_id** | **str** | the identifier for this tool_tag | [optional] 
**content_id** | **int** |  | [optional] 
**content_type** | **str** |  | [optional] 
**custom_params** | **object** |  | [optional] 
**external_data** | **str** |  | [optional] 
**resource_link_title** | **object** |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.external_tool_tag_attributes import ExternalToolTagAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalToolTagAttributes from a JSON string
external_tool_tag_attributes_instance = ExternalToolTagAttributes.from_json(json)
# print the JSON string representation of the object
print(ExternalToolTagAttributes.to_json())

# convert the object into a dict
external_tool_tag_attributes_dict = external_tool_tag_attributes_instance.to_dict()
# create an instance of ExternalToolTagAttributes from a dict
external_tool_tag_attributes_from_dict = ExternalToolTagAttributes.from_dict(external_tool_tag_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


