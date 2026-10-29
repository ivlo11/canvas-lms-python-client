# PageViewLinks

The links of a page view access in Canvas

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | **int** | The ID of the user for this page view | [optional] 
**context** | **int** | The ID of the context for the request (course id if context_type is Course, etc) | [optional] 
**asset** | **int** | The ID of the asset for the request, if any. Not available in history CSV. | [optional] 
**real_user** | **int** | The ID of the actual user who made this request, if the request was made by a user who was masquerading | [optional] 
**account** | **int** | The ID of the account context for this page view | [optional] 

## Example

```python
from canvas_lms_python_client.models.page_view_links import PageViewLinks

# TODO update the JSON string below
json = "{}"
# create an instance of PageViewLinks from a JSON string
page_view_links_instance = PageViewLinks.from_json(json)
# print the JSON string representation of the object
print(PageViewLinks.to_json())

# convert the object into a dict
page_view_links_dict = page_view_links_instance.to_dict()
# create an instance of PageViewLinks from a dict
page_view_links_from_dict = PageViewLinks.from_dict(page_view_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


