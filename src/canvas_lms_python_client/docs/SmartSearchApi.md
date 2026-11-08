# canvas_lms_python_client.SmartSearchApi

All URIs are relative to *https://canvas.instructure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**smart_search_search**](SmartSearchApi.md#smart_search_search) | **GET** /api/v1/courses/{course_id}/smartsearch | Search course content


# **smart_search_search**
> SmartSearchSearchResponse smart_search_search(course_id, q, filter=filter, include=include, page=page, per_page=per_page)

Search course content

Find course content using a meaning-based search

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.smart_search_search_response import SmartSearchSearchResponse
from canvas_lms_python_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://canvas.instructure.com
# See configuration.py for a list of all supported configuration parameters.
configuration = canvas_lms_python_client.Configuration(
    host = "https://canvas.instructure.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (token): bearer
configuration = canvas_lms_python_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with canvas_lms_python_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = canvas_lms_python_client.SmartSearchApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    q = 'q_example' # str | The search query
    filter = ['filter_example'] # List[str] | Types of objects to search. By default, all supported types are searched. Supported types include +pages+, +assignments+, +announcements+, and +discussion_topics+. (optional)
    include = ['include_example'] # List[str] | Optional information to include with each search result: modules:: An array of module objects that the search result belongs to. status:: The published status for all results and the due_date for all assignments. (optional)
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # Search course content
        api_response = await api_instance.smart_search_search(course_id, q, filter=filter, include=include, page=page, per_page=per_page)
        print("The response of SmartSearchApi->smart_search_search:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SmartSearchApi->smart_search_search: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **q** | **str**| The search query | 
 **filter** | [**List[str]**](str.md)| Types of objects to search. By default, all supported types are searched. Supported types include +pages+, +assignments+, +announcements+, and +discussion_topics+. | [optional] 
 **include** | [**List[str]**](str.md)| Optional information to include with each search result: modules:: An array of module objects that the search result belongs to. status:: The published status for all results and the due_date for all assignments. | [optional] 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**SmartSearchSearchResponse**](SmartSearchSearchResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

