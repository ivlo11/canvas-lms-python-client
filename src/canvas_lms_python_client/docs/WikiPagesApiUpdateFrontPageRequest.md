# WikiPagesApiUpdateFrontPageRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wiki_page** | [**WikiPagesApiUpdateFrontPageRequestWikiPage**](WikiPagesApiUpdateFrontPageRequestWikiPage.md) |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.wiki_pages_api_update_front_page_request import WikiPagesApiUpdateFrontPageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WikiPagesApiUpdateFrontPageRequest from a JSON string
wiki_pages_api_update_front_page_request_instance = WikiPagesApiUpdateFrontPageRequest.from_json(json)
# print the JSON string representation of the object
print(WikiPagesApiUpdateFrontPageRequest.to_json())

# convert the object into a dict
wiki_pages_api_update_front_page_request_dict = wiki_pages_api_update_front_page_request_instance.to_dict()
# create an instance of WikiPagesApiUpdateFrontPageRequest from a dict
wiki_pages_api_update_front_page_request_from_dict = WikiPagesApiUpdateFrontPageRequest.from_dict(wiki_pages_api_update_front_page_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


