# WikiPagesApiCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wiki_page** | [**WikiPagesApiCreateRequestWikiPage**](WikiPagesApiCreateRequestWikiPage.md) |  | 

## Example

```python
from canvas_lms_python_client.models.wiki_pages_api_create_request import WikiPagesApiCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WikiPagesApiCreateRequest from a JSON string
wiki_pages_api_create_request_instance = WikiPagesApiCreateRequest.from_json(json)
# print the JSON string representation of the object
print(WikiPagesApiCreateRequest.to_json())

# convert the object into a dict
wiki_pages_api_create_request_dict = wiki_pages_api_create_request_instance.to_dict()
# create an instance of WikiPagesApiCreateRequest from a dict
wiki_pages_api_create_request_from_dict = WikiPagesApiCreateRequest.from_dict(wiki_pages_api_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


