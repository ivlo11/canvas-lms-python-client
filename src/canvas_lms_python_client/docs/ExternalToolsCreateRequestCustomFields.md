# ExternalToolsCreateRequestCustomFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field_name** | **str** | [String] Custom fields that will be sent to the tool consumer; can be used multiple times | [optional] 

## Example

```python
from canvas_lms_python_client.models.external_tools_create_request_custom_fields import ExternalToolsCreateRequestCustomFields

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalToolsCreateRequestCustomFields from a JSON string
external_tools_create_request_custom_fields_instance = ExternalToolsCreateRequestCustomFields.from_json(json)
# print the JSON string representation of the object
print(ExternalToolsCreateRequestCustomFields.to_json())

# convert the object into a dict
external_tools_create_request_custom_fields_dict = external_tools_create_request_custom_fields_instance.to_dict()
# create an instance of ExternalToolsCreateRequestCustomFields from a dict
external_tools_create_request_custom_fields_from_dict = ExternalToolsCreateRequestCustomFields.from_dict(external_tools_create_request_custom_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


