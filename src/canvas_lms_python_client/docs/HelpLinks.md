# HelpLinks



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**help_link_name** | **str** | Help link button title | [optional] 
**help_link_icon** | **str** | Help link button icon | [optional] 
**custom_help_links** | [**List[HelpLink]**](HelpLink.md) | Help links defined by the account. Could include default help links. | [optional] 
**default_help_links** | [**List[HelpLink]**](HelpLink.md) | Default help links provided when account has not set help links of their own. | [optional] 

## Example

```python
from canvas_lms_python_client.models.help_links import HelpLinks

# TODO update the JSON string below
json = "{}"
# create an instance of HelpLinks from a JSON string
help_links_instance = HelpLinks.from_json(json)
# print the JSON string representation of the object
print(HelpLinks.to_json())

# convert the object into a dict
help_links_dict = help_links_instance.to_dict()
# create an instance of HelpLinks from a dict
help_links_from_dict = HelpLinks.from_dict(help_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


