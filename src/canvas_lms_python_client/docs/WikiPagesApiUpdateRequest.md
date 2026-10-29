# WikiPagesApiUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wiki_page** | [**WikiPagesApiUpdateRequestWikiPage**](WikiPagesApiUpdateRequestWikiPage.md) |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.wiki_pages_api_update_request import WikiPagesApiUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WikiPagesApiUpdateRequest from a JSON string
wiki_pages_api_update_request_instance = WikiPagesApiUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(WikiPagesApiUpdateRequest.to_json())

# convert the object into a dict
wiki_pages_api_update_request_dict = wiki_pages_api_update_request_instance.to_dict()
# create an instance of WikiPagesApiUpdateRequest from a dict
wiki_pages_api_update_request_from_dict = WikiPagesApiUpdateRequest.from_dict(wiki_pages_api_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


