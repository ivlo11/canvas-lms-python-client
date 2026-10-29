# PageView

The record of a user page view access in Canvas

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | A UUID representing the page view.  This is also the unique request id | 
**app_name** | **str** | If the request is from an API request, the app that generated the access token | [optional] 
**url** | **str** | The URL requested | [optional] 
**context_type** | **str** | The type of context for the request | [optional] 
**asset_type** | **str** | The type of asset in the context for the request, if any | [optional] 
**controller** | **str** | The rails controller that handled the request | [optional] 
**action** | **str** | The rails action that handled the request | [optional] 
**contributed** | **bool** | This field is deprecated, and will always be false | [optional] 
**interaction_seconds** | **float** | An approximation of how long the user spent on the page, in seconds | [optional] 
**created_at** | **datetime** | When the request was made | [optional] 
**user_request** | **bool** | A flag indicating whether the request was user-initiated, or automatic (such as an AJAX call). Not available in history CSV. | [optional] 
**render_time** | **float** | How long the response took to render, in seconds. Not available in history CSV. | [optional] 
**user_agent** | **str** | The user-agent of the browser or program that made the request | [optional] 
**participated** | **bool** | True if the request counted as participating, such as submitting homework | [optional] 
**http_method** | **str** | The HTTP method such as GET or POST | [optional] 
**remote_ip** | **str** | The origin IP address of the request | [optional] 
**session_id** | **UUID** | The session identifier for the user session that made the request | [optional] 
**developer_key_id** | **float** | The ID of the developer key that authorized the API request, if applicable | [optional] 
**asset_user_access_id** | **float** | The ID of the asset (e.g. an assignment) associated with this page view, if applicable | [optional] 
**links** | [**PageViewLinks**](PageViewLinks.md) |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.page_view import PageView

# TODO update the JSON string below
json = "{}"
# create an instance of PageView from a JSON string
page_view_instance = PageView.from_json(json)
# print the JSON string representation of the object
print(PageView.to_json())

# convert the object into a dict
page_view_dict = page_view_instance.to_dict()
# create an instance of PageView from a dict
page_view_from_dict = PageView.from_dict(page_view_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


