# canvas_lms_python_client.PaceContextsApiApi

All URIs are relative to *https://canvas.instructure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**pace_contexts_api_index**](PaceContextsApiApi.md#pace_contexts_api_index) | **GET** /api/v1/courses/{course_id}/pace_contexts | List all pace contexts


# **pace_contexts_api_index**
> pace_contexts_api_index(course_id, type=type, sort=sort, order=order, search_term=search_term, contexts=contexts, page=page, per_page=per_page)

List all pace contexts

Returns a paginated list of pace contexts for the given course and context type.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
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
    api_instance = canvas_lms_python_client.PaceContextsApiApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    type = 'type_example' # str | The type of pace context to return. Must be one of \"course\", \"section\", or \"student_enrollment\". Each type will return the corresponding set of items that can be paced. (optional)
    sort = 'sort_example' # str | When included, sorts all pace contexts by the given field. \"name\" is the only supported sort field and will sort sections by their section name and student enrollments by their user's sortable name. (optional)
    order = 'order_example' # str | When included, orders the results in the given order. \"asc\" is the default order and to reverse the order pass \"desc\". Works in conjunction with the \"sort\" argument. (optional)
    search_term = 'search_term_example' # str | When included, filters the results by the course pace name for the given search term. (optional)
    contexts = ['contexts_example'] # List[str] | When included, filters the results for the given context ids. (optional)
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # List all pace contexts
        await api_instance.pace_contexts_api_index(course_id, type=type, sort=sort, order=order, search_term=search_term, contexts=contexts, page=page, per_page=per_page)
    except Exception as e:
        print("Exception when calling PaceContextsApiApi->pace_contexts_api_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **type** | **str**| The type of pace context to return. Must be one of \&quot;course\&quot;, \&quot;section\&quot;, or \&quot;student_enrollment\&quot;. Each type will return the corresponding set of items that can be paced. | [optional] 
 **sort** | **str**| When included, sorts all pace contexts by the given field. \&quot;name\&quot; is the only supported sort field and will sort sections by their section name and student enrollments by their user&#39;s sortable name. | [optional] 
 **order** | **str**| When included, orders the results in the given order. \&quot;asc\&quot; is the default order and to reverse the order pass \&quot;desc\&quot;. Works in conjunction with the \&quot;sort\&quot; argument. | [optional] 
 **search_term** | **str**| When included, filters the results by the course pace name for the given search term. | [optional] 
 **contexts** | [**List[str]**](str.md)| When included, filters the results for the given context ids. | [optional] 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | List all pace contexts |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

