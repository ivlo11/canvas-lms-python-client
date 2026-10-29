# PageViewsQueryRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **str** | The start date for the page views query in YYYY-MM-DD format. Must be the first day of a month. | [optional] 
**end_date** | **str** | The end date for the page views query in YYYY-MM-DD format. Must be the first day of a month and after start_date. | [optional] 
**results_format** | **str** | The desired format for the query results. Supported formats: \&quot;csv\&quot;, \&quot;jsonl\&quot; | [optional] 

## Example

```python
from canvas_lms_python_client.models.page_views_query_request import PageViewsQueryRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PageViewsQueryRequest from a JSON string
page_views_query_request_instance = PageViewsQueryRequest.from_json(json)
# print the JSON string representation of the object
print(PageViewsQueryRequest.to_json())

# convert the object into a dict
page_views_query_request_dict = page_views_query_request_instance.to_dict()
# create an instance of PageViewsQueryRequest from a dict
page_views_query_request_from_dict = PageViewsQueryRequest.from_dict(page_views_query_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


