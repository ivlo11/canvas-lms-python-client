# HelpLink



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of the help link | [optional] 
**text** | **str** | The name of the help link | [optional] 
**subtext** | **str** | The description of the help link | [optional] 
**url** | **str** | The URL of the help link | [optional] 
**type** | **str** | The type of the help link | [optional] 
**available_to** | **List[str]** | The roles that have access to this help link | [optional] 
**feature_headline** | **str** |  | [optional] 
**is_featured** | **bool** |  | [optional] 
**is_new** | **bool** |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.help_link import HelpLink

# TODO update the JSON string below
json = "{}"
# create an instance of HelpLink from a JSON string
help_link_instance = HelpLink.from_json(json)
# print the JSON string representation of the object
print(HelpLink.to_json())

# convert the object into a dict
help_link_dict = help_link_instance.to_dict()
# create an instance of HelpLink from a dict
help_link_from_dict = HelpLink.from_dict(help_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


