# WikiPagesApiUpdateFrontPageRequestWikiPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | [String] The title for the new page. NOTE: changing a page&#39;s title will change its url. The updated url will be returned in the result. | [optional] 
**body** | **str** | [String] The content for the new page. | [optional] 
**editing_roles** | **str** | [String, \&quot;teachers\&quot;|\&quot;students\&quot;|\&quot;members\&quot;|\&quot;public\&quot;] Which user roles are allowed to edit this page. Any combination of these roles is allowed (separated by commas).  \&quot;teachers\&quot;:: Allows editing by teachers in the course. \&quot;students\&quot;:: Allows editing by students in the course. \&quot;members\&quot;:: For group wikis, allows editing by members of the group. \&quot;public\&quot;:: Allows editing by any user. | [optional] 
**notify_of_update** | **bool** | [Boolean] Whether participants should be notified when this page changes. | [optional] 
**published** | **bool** | [Boolean] Whether the page is published (true) or draft state (false). | [optional] 

## Example

```python
from canvas_lms_python_client.models.wiki_pages_api_update_front_page_request_wiki_page import WikiPagesApiUpdateFrontPageRequestWikiPage

# TODO update the JSON string below
json = "{}"
# create an instance of WikiPagesApiUpdateFrontPageRequestWikiPage from a JSON string
wiki_pages_api_update_front_page_request_wiki_page_instance = WikiPagesApiUpdateFrontPageRequestWikiPage.from_json(json)
# print the JSON string representation of the object
print(WikiPagesApiUpdateFrontPageRequestWikiPage.to_json())

# convert the object into a dict
wiki_pages_api_update_front_page_request_wiki_page_dict = wiki_pages_api_update_front_page_request_wiki_page_instance.to_dict()
# create an instance of WikiPagesApiUpdateFrontPageRequestWikiPage from a dict
wiki_pages_api_update_front_page_request_wiki_page_from_dict = WikiPagesApiUpdateFrontPageRequestWikiPage.from_dict(wiki_pages_api_update_front_page_request_wiki_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


