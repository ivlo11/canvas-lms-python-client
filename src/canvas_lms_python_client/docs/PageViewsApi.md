# canvas_lms_python_client.PageViewsApi

All URIs are relative to *https://canvas.instructure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**page_views_batch_query**](PageViewsApi.md#page_views_batch_query) | **POST** /api/v1/users/page_views/query | BETA - Initiate batch page views query
[**page_views_batch_query_results**](PageViewsApi.md#page_views_batch_query_results) | **GET** /api/v1/users/page_views/query/{query_id}/results | BETA - Get batch query results
[**page_views_index**](PageViewsApi.md#page_views_index) | **GET** /api/v1/users/{user_id}/page_views | List user page views
[**page_views_poll_batch_query**](PageViewsApi.md#page_views_poll_batch_query) | **GET** /api/v1/users/page_views/query/{query_id} | BETA - Poll batch query status
[**page_views_poll_query**](PageViewsApi.md#page_views_poll_query) | **GET** /api/v1/users/{user_id}/page_views/query/{query_id} | BETA - Poll query status
[**page_views_query**](PageViewsApi.md#page_views_query) | **POST** /api/v1/users/{user_id}/page_views/query | BETA - Initiate page views query
[**page_views_query_results**](PageViewsApi.md#page_views_query_results) | **GET** /api/v1/users/{user_id}/page_views/query/{query_id}/results | BETA - Get query results


# **page_views_batch_query**
> AsyncApiErrorResponse page_views_batch_query(page_views_batch_query_request=page_views_batch_query_request)

BETA - Initiate batch page views query

Initiates an asynchronous query for page views data across multiple users.
This method enqueues a background job to process the batch page views query and returns
a polling URL that can be used to check the query status and retrieve results when ready.

As this is a beta endpoint, it is subject to change or removal at any time without the standard notice periods outlined in the API policy.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.async_api_error_response import AsyncApiErrorResponse
from canvas_lms_python_client.models.page_views_batch_query_request import PageViewsBatchQueryRequest
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
    api_instance = canvas_lms_python_client.PageViewsApi(api_client)
    page_views_batch_query_request = canvas_lms_python_client.PageViewsBatchQueryRequest() # PageViewsBatchQueryRequest | Request body parameters  **Example Request:** ``` curl https://<canvas>/api/v1/users/page_views/query \\   -X POST \\   -H 'Authorization: Bearer <token>' \\   -H 'Content-Type: application/json' \\   -d '{     \"user_ids\": [123, 456, 789],     \"start_date\": \"2023-01-01\",     \"end_date\": \"2023-02-01\",     \"results_format\": \"csv\"   }' ``` (optional)

    try:
        # BETA - Initiate batch page views query
        api_response = await api_instance.page_views_batch_query(page_views_batch_query_request=page_views_batch_query_request)
        print("The response of PageViewsApi->page_views_batch_query:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PageViewsApi->page_views_batch_query: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_views_batch_query_request** | [**PageViewsBatchQueryRequest**](PageViewsBatchQueryRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl https://&lt;canvas&gt;/api/v1/users/page_views/query \\   -X POST \\   -H &#39;Authorization: Bearer &lt;token&gt;&#39; \\   -H &#39;Content-Type: application/json&#39; \\   -d &#39;{     \&quot;user_ids\&quot;: [123, 456, 789],     \&quot;start_date\&quot;: \&quot;2023-01-01\&quot;,     \&quot;end_date\&quot;: \&quot;2023-02-01\&quot;,     \&quot;results_format\&quot;: \&quot;csv\&quot;   }&#39; &#x60;&#x60;&#x60; | [optional] 

### Return type

[**AsyncApiErrorResponse**](AsyncApiErrorResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | AsyncApiErrorResponse |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **page_views_batch_query_results**
> AsyncApiErrorResponse page_views_batch_query_results(query_id)

BETA - Get batch query results

Retrieves the results of a completed batch page views query. Returns the data in the
format specified when the query was initiated (CSV or JSON). The response may
be compressed with gzip encoding.

As this is a beta endpoint, it is subject to change or removal at any time without the standard notice periods outlined in the API policy.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.async_api_error_response import AsyncApiErrorResponse
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
    api_instance = canvas_lms_python_client.PageViewsApi(api_client)
    query_id = 'query_id_example' # str | The UUID of the completed query to retrieve results for

    try:
        # BETA - Get batch query results
        api_response = await api_instance.page_views_batch_query_results(query_id)
        print("The response of PageViewsApi->page_views_batch_query_results:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PageViewsApi->page_views_batch_query_results: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_id** | **str**| The UUID of the completed query to retrieve results for | 

### Return type

[**AsyncApiErrorResponse**](AsyncApiErrorResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | AsyncApiErrorResponse |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **page_views_index**
> List[PageView] page_views_index(user_id, start_time=start_time, end_time=end_time, page=page, per_page=per_page)

List user page views

Return a paginated list of the user's page view history in json format,
similar to the available CSV download. Page views are returned in
descending order, newest to oldest.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.page_view import PageView
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
    api_instance = canvas_lms_python_client.PageViewsApi(api_client)
    user_id = 'user_id_example' # str | Scope response to user_id
    start_time = 'start_time_example' # str | The beginning of the time range from which you want page views. (optional)
    end_time = 'end_time_example' # str | The end of the time range from which you want page views. (optional)
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # List user page views
        api_response = await api_instance.page_views_index(user_id, start_time=start_time, end_time=end_time, page=page, per_page=per_page)
        print("The response of PageViewsApi->page_views_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PageViewsApi->page_views_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| Scope response to user_id | 
 **start_time** | **str**| The beginning of the time range from which you want page views. | [optional] 
 **end_time** | **str**| The end of the time range from which you want page views. | [optional] 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**List[PageView]**](PageView.md)

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

# **page_views_poll_batch_query**
> AsyncApiErrorResponse page_views_poll_batch_query(query_id)

BETA - Poll batch query status

Checks the status of a previously initiated batch page views query. Returns the current
processing status and provides a result URL when the query is complete.

As this is a beta endpoint, it is subject to change or removal at any time without the standard notice periods outlined in the API policy.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.async_api_error_response import AsyncApiErrorResponse
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
    api_instance = canvas_lms_python_client.PageViewsApi(api_client)
    query_id = 'query_id_example' # str | The UUID of the query to check status for

    try:
        # BETA - Poll batch query status
        api_response = await api_instance.page_views_poll_batch_query(query_id)
        print("The response of PageViewsApi->page_views_poll_batch_query:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PageViewsApi->page_views_poll_batch_query: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_id** | **str**| The UUID of the query to check status for | 

### Return type

[**AsyncApiErrorResponse**](AsyncApiErrorResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | AsyncApiErrorResponse |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **page_views_poll_query**
> AsyncApiErrorResponse page_views_poll_query(query_id, user_id)

BETA - Poll query status

Checks the status of a previously initiated page views query. Returns the current
processing status and provides a result URL when the query is complete.

The query may fail with status "failed" and error_code
"RESULT_SIZE_LIMIT_EXCEEDED" if the result exceeds 500 MB.
If this happens, narrow the date range or query smaller
time intervals.

As this is a beta endpoint, it is subject to change or removal at any time without the standard notice periods outlined in the API policy.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.async_api_error_response import AsyncApiErrorResponse
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
    api_instance = canvas_lms_python_client.PageViewsApi(api_client)
    query_id = 'query_id_example' # str | The UUID of the query to check status for
    user_id = 'user_id_example' # str | Scope response to user_id

    try:
        # BETA - Poll query status
        api_response = await api_instance.page_views_poll_query(query_id, user_id)
        print("The response of PageViewsApi->page_views_poll_query:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PageViewsApi->page_views_poll_query: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_id** | **str**| The UUID of the query to check status for | 
 **user_id** | **str**| Scope response to user_id | 

### Return type

[**AsyncApiErrorResponse**](AsyncApiErrorResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | AsyncApiErrorResponse |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **page_views_query**
> AsyncApiErrorResponse page_views_query(user_id, page_views_query_request=page_views_query_request)

BETA - Initiate page views query

Initiates an asynchronous query for user page views data within a specified date range.
This method enqueues a background job to process the page views query and returns
a polling URL that can be used to check the query status and retrieve results when ready.

As this is a beta endpoint, it is subject to change or removal at any time without the standard notice periods outlined in the API policy.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.async_api_error_response import AsyncApiErrorResponse
from canvas_lms_python_client.models.page_views_query_request import PageViewsQueryRequest
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
    api_instance = canvas_lms_python_client.PageViewsApi(api_client)
    user_id = 'user_id_example' # str | Scope response to user_id
    page_views_query_request = canvas_lms_python_client.PageViewsQueryRequest() # PageViewsQueryRequest | Request body parameters  **Example Request:** ``` curl https://<canvas>/api/v1/users/:user_id/page_views/query \\   -X POST \\   -H 'Authorization: Bearer <token>' \\   -H 'Content-Type: application/json' \\   -d '{     \"start_date\": \"2023-01-01\",     \"end_date\": \"2023-02-01\",     \"results_format\": \"csv\"   }' ``` (optional)

    try:
        # BETA - Initiate page views query
        api_response = await api_instance.page_views_query(user_id, page_views_query_request=page_views_query_request)
        print("The response of PageViewsApi->page_views_query:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PageViewsApi->page_views_query: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| Scope response to user_id | 
 **page_views_query_request** | [**PageViewsQueryRequest**](PageViewsQueryRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl https://&lt;canvas&gt;/api/v1/users/:user_id/page_views/query \\   -X POST \\   -H &#39;Authorization: Bearer &lt;token&gt;&#39; \\   -H &#39;Content-Type: application/json&#39; \\   -d &#39;{     \&quot;start_date\&quot;: \&quot;2023-01-01\&quot;,     \&quot;end_date\&quot;: \&quot;2023-02-01\&quot;,     \&quot;results_format\&quot;: \&quot;csv\&quot;   }&#39; &#x60;&#x60;&#x60; | [optional] 

### Return type

[**AsyncApiErrorResponse**](AsyncApiErrorResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | AsyncApiErrorResponse |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **page_views_query_results**
> AsyncApiErrorResponse page_views_query_results(query_id, user_id)

BETA - Get query results

Retrieves the results of a completed page views query. Returns the data in the
format specified when the query was initiated (CSV or JSON). The response may
be compressed with gzip encoding.

As this is a beta endpoint, it is subject to change or removal at any time without the standard notice periods outlined in the API policy.

Note: PageView payloads use two types of identifiers: globalId and localId. Global identifier is equal to (shardId*10000000000000)+localId.
Please note our global identifiers might change if your Canvas instance goes through shard migration process, in this case your current
shardId in the global identifier will change to a new shardId. Local identifiers do not change after shard migration and stay unique in the
context of the Canvas account. The following fields in the PageView payload are global identifiers: `links_user`, `links_context`, `links_asset`,
`links_real_user`, `links_account`, `developer_key_id`, `asset_user_access_id`.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.async_api_error_response import AsyncApiErrorResponse
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
    api_instance = canvas_lms_python_client.PageViewsApi(api_client)
    query_id = 'query_id_example' # str | The UUID of the completed query to retrieve results for
    user_id = 'user_id_example' # str | Scope response to user_id

    try:
        # BETA - Get query results
        api_response = await api_instance.page_views_query_results(query_id, user_id)
        print("The response of PageViewsApi->page_views_query_results:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PageViewsApi->page_views_query_results: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_id** | **str**| The UUID of the completed query to retrieve results for | 
 **user_id** | **str**| Scope response to user_id | 

### Return type

[**AsyncApiErrorResponse**](AsyncApiErrorResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | AsyncApiErrorResponse |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

