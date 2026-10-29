# ResourceLinksUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | The launch URL for this resource link. &lt;b&gt;Caution!&lt;/b&gt; URL must match the URL or domain of the tool associated with this resource link | [optional] 
**custom** | **str** | Custom parameters to be sent to the tool when launching this link. &lt;b&gt;Caution!&lt;/b&gt; Changing these from what the tool provided could result in errors if the tool doesn&#39;t see what it&#39;s expecting. | [optional] 
**include_deleted** | **bool** | Update link even if it is deleted. Default is false. | [optional] 
**context_external_tool_id** | **int** | The Canvas identifier for the LTI 1.3 External Tool that the LTI Resource Link was originally installed from. &lt;b&gt;Caution!&lt;/b&gt; The resource link url must match the tool&#39;s domain or url. | [optional] 

## Example

```python
from canvas_lms_python_client.models.resource_links_update_request import ResourceLinksUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceLinksUpdateRequest from a JSON string
resource_links_update_request_instance = ResourceLinksUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(ResourceLinksUpdateRequest.to_json())

# convert the object into a dict
resource_links_update_request_dict = resource_links_update_request_instance.to_dict()
# create an instance of ResourceLinksUpdateRequest from a dict
resource_links_update_request_from_dict = ResourceLinksUpdateRequest.from_dict(resource_links_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


