# ResourceLinksBulkCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**post** | **str** | body [Required, Array] The POST body should be a JSON array of objects containing the parameters for each link to create. | [optional] 
**url** | **str** | Each object must contain a launch URL. | 
**title** | **str** | Each object may contain a title. | [optional] 
**custom** | **str** | Custom parameters to be sent to the tool when launching this link. | [optional] 

## Example

```python
from canvas_lms_python_client.models.resource_links_bulk_create_request import ResourceLinksBulkCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceLinksBulkCreateRequest from a JSON string
resource_links_bulk_create_request_instance = ResourceLinksBulkCreateRequest.from_json(json)
# print the JSON string representation of the object
print(ResourceLinksBulkCreateRequest.to_json())

# convert the object into a dict
resource_links_bulk_create_request_dict = resource_links_bulk_create_request_instance.to_dict()
# create an instance of ResourceLinksBulkCreateRequest from a dict
resource_links_bulk_create_request_from_dict = ResourceLinksBulkCreateRequest.from_dict(resource_links_bulk_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


