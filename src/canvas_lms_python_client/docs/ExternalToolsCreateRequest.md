# ExternalToolsCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **str** | The client id is attached to the developer key. If supplied all other parameters are unnecessary and will be ignored | 
**name** | **str** | The name of the tool | 
**privacy_level** | **str** | How much user information to send to the external tool. | 
**consumer_key** | **str** | The consumer key for the external tool | 
**shared_secret** | **str** | The shared secret with the external tool | 
**description** | **str** | A description of the tool | [optional] 
**url** | **str** | The url to match links against. Either \&quot;url\&quot; or \&quot;domain\&quot; should be set, not both. | [optional] 
**domain** | **str** | The domain to match links against. Either \&quot;url\&quot; or \&quot;domain\&quot; should be set, not both. | [optional] 
**icon_url** | **str** | The url of the icon to show for this tool | [optional] 
**text** | **str** | The default text to show for this tool | [optional] 
**is_rce_favorite** | **bool** | (Deprecated in favor of {api:ExternalToolsController#mark_rce_favorite Mark tool to RCE Favorites} and {api:ExternalToolsController#unmark_rce_favorite Unmark tool from RCE Favorites}) Whether this tool should appear in a preferred location in the RCE. This only applies to tools in root account contexts that have an editor button placement. | [optional] 
**placement_configuration_key_placement_name** | **str** | [variable] Set the &lt;placement_configuration_key&gt; value for a specific placement. | [optional] 
**config_type** | **str** | Configuration can be passed in as Common Cartridge XML instead of using query parameters. If this value is \&quot;by_url\&quot; or \&quot;by_xml\&quot; then an XML configuration will be expected in either the \&quot;config_xml\&quot; or \&quot;config_url\&quot; parameter. Note that the name parameter overrides the tool name provided in the XML. | [optional] 
**config_xml** | **str** | XML tool configuration, as specified in the Common Cartridge XML specification. This is required if \&quot;config_type\&quot; is set to \&quot;by_xml\&quot; | [optional] 
**config_url** | **str** | URL where the server can retrieve an XML tool configuration, as specified in the Common Cartridge XML specification. This is required if \&quot;config_type\&quot; is set to \&quot;by_url\&quot; | [optional] 
**not_selectable** | **bool** | Default: false. If set to true, and if resource_selection is set to false, the tool won&#39;t show up in the external tool selection UI in modules and assignments | [optional] 
**oauth_compliant** | **bool** | Default: false, if set to true LTI query params will not be copied to the post body. | [optional] 
**unified_tool_id** | **str** | The unique identifier for the tool in LearnPlatform | [optional] 
**custom_fields** | [**ExternalToolsCreateRequestCustomFields**](ExternalToolsCreateRequestCustomFields.md) |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.external_tools_create_request import ExternalToolsCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalToolsCreateRequest from a JSON string
external_tools_create_request_instance = ExternalToolsCreateRequest.from_json(json)
# print the JSON string representation of the object
print(ExternalToolsCreateRequest.to_json())

# convert the object into a dict
external_tools_create_request_dict = external_tools_create_request_instance.to_dict()
# create an instance of ExternalToolsCreateRequest from a dict
external_tools_create_request_from_dict = ExternalToolsCreateRequest.from_dict(external_tools_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


