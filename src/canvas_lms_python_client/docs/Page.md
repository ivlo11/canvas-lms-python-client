# Page



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page_id** | **int** | the ID of the page | [optional] 
**url** | **str** | the unique locator for the page | [optional] 
**title** | **str** | the title of the page | [optional] 
**created_at** | **datetime** | the creation date for the page | [optional] 
**updated_at** | **datetime** | the date the page was last updated | [optional] 
**hide_from_students** | **bool** | (DEPRECATED) whether this page is hidden from students (note: this is always reflected as the inverse of the published value) | [optional] 
**editing_roles** | **str** | roles allowed to edit the page; comma-separated list comprising a combination of &#39;teachers&#39;, &#39;students&#39;, &#39;members&#39;, and/or &#39;public&#39; if not supplied, course defaults are used | [optional] 
**last_edited_by** | [**User**](User.md) |  | [optional] 
**body** | **str** | the page content, in HTML (present when requesting a single page; optionally included when listing pages) | [optional] 
**published** | **bool** | whether the page is published (true) or draft state (false). | [optional] 
**publish_at** | **datetime** | scheduled publication date for this page | [optional] 
**front_page** | **bool** | whether this page is the front page for the wiki | [optional] 
**locked_for_user** | **bool** | Whether or not this is locked for the user. | [optional] 
**lock_info** | [**LockInfo**](LockInfo.md) |  | [optional] 
**lock_explanation** | **str** | (Optional) An explanation of why this is locked for the user. Present when locked_for_user is true. | [optional] 
**editor** | **str** | The editor used to create and edit this page. May be one of &#39;rce&#39; or &#39;block_editor&#39;. | [optional] 
**block_editor_attributes** | **object** | The block editor attributes for this page. (optionally included, and only if this is a block editor created page) | [optional] 

## Example

```python
from canvas_lms_python_client.models.page import Page

# TODO update the JSON string below
json = "{}"
# create an instance of Page from a JSON string
page_instance = Page.from_json(json)
# print the JSON string representation of the object
print(Page.to_json())

# convert the object into a dict
page_dict = page_instance.to_dict()
# create an instance of Page from a dict
page_from_dict = Page.from_dict(page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


