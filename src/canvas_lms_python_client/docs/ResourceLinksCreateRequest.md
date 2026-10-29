# ResourceLinksCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | The launch URL for this resource link. | 
**title** | **str** | The title of the resource link. | [optional] 
**custom** | **str** | Custom parameters to be sent to the tool when launching this link. | [optional] 

## Example

```python
from canvas_lms_python_client.models.resource_links_create_request import ResourceLinksCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceLinksCreateRequest from a JSON string
resource_links_create_request_instance = ResourceLinksCreateRequest.from_json(json)
# print the JSON string representation of the object
print(ResourceLinksCreateRequest.to_json())

# convert the object into a dict
resource_links_create_request_dict = resource_links_create_request_instance.to_dict()
# create an instance of ResourceLinksCreateRequest from a dict
resource_links_create_request_from_dict = ResourceLinksCreateRequest.from_dict(resource_links_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


