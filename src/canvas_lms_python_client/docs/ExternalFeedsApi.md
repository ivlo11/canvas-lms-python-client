# canvas_lms_python_client.ExternalFeedsApi

All URIs are relative to *https://canvas.instructure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**external_feeds_create**](ExternalFeedsApi.md#external_feeds_create) | **POST** /api/v1/courses/{course_id}/external_feeds | Create an external feed
[**external_feeds_create_for_groups**](ExternalFeedsApi.md#external_feeds_create_for_groups) | **POST** /api/v1/groups/{group_id}/external_feeds | Create an external feed
[**external_feeds_destroy**](ExternalFeedsApi.md#external_feeds_destroy) | **DELETE** /api/v1/courses/{course_id}/external_feeds/{external_feed_id} | Delete an external feed
[**external_feeds_destroy_for_groups**](ExternalFeedsApi.md#external_feeds_destroy_for_groups) | **DELETE** /api/v1/groups/{group_id}/external_feeds/{external_feed_id} | Delete an external feed
[**external_feeds_index**](ExternalFeedsApi.md#external_feeds_index) | **GET** /api/v1/courses/{course_id}/external_feeds | List external feeds
[**external_feeds_index_for_groups**](ExternalFeedsApi.md#external_feeds_index_for_groups) | **GET** /api/v1/groups/{group_id}/external_feeds | List external feeds


# **external_feeds_create**
> ExternalFeed external_feeds_create(course_id, external_feeds_create_request=external_feeds_create_request)

Create an external feed

Create a new external feed for the course or group.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.external_feed import ExternalFeed
from canvas_lms_python_client.models.external_feeds_create_request import ExternalFeedsCreateRequest
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
    api_instance = canvas_lms_python_client.ExternalFeedsApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    external_feeds_create_request = canvas_lms_python_client.ExternalFeedsCreateRequest() # ExternalFeedsCreateRequest | Request body parameters  **Example Request:** ``` curl https://<canvas>/api/v1/courses/<course_id>/external_feeds \\     -F url='http://example.com/rss.xml' \\     -F header_match='news flash!' \\     -F verbosity='full' \\     -H 'Authorization: Bearer <token>' ``` (optional)

    try:
        # Create an external feed
        api_response = await api_instance.external_feeds_create(course_id, external_feeds_create_request=external_feeds_create_request)
        print("The response of ExternalFeedsApi->external_feeds_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExternalFeedsApi->external_feeds_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **external_feeds_create_request** | [**ExternalFeedsCreateRequest**](ExternalFeedsCreateRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl https://&lt;canvas&gt;/api/v1/courses/&lt;course_id&gt;/external_feeds \\     -F url&#x3D;&#39;http://example.com/rss.xml&#39; \\     -F header_match&#x3D;&#39;news flash!&#39; \\     -F verbosity&#x3D;&#39;full&#39; \\     -H &#39;Authorization: Bearer &lt;token&gt;&#39; &#x60;&#x60;&#x60; | [optional] 

### Return type

[**ExternalFeed**](ExternalFeed.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | ExternalFeed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **external_feeds_create_for_groups**
> ExternalFeed external_feeds_create_for_groups(group_id, external_feeds_create_request=external_feeds_create_request)

Create an external feed

Create a new external feed for the course or group.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.external_feed import ExternalFeed
from canvas_lms_python_client.models.external_feeds_create_request import ExternalFeedsCreateRequest
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
    api_instance = canvas_lms_python_client.ExternalFeedsApi(api_client)
    group_id = 'group_id_example' # str | Scope response to group_id
    external_feeds_create_request = canvas_lms_python_client.ExternalFeedsCreateRequest() # ExternalFeedsCreateRequest | Request body parameters  **Example Request:** ``` curl https://<canvas>/api/v1/courses/<course_id>/external_feeds \\     -F url='http://example.com/rss.xml' \\     -F header_match='news flash!' \\     -F verbosity='full' \\     -H 'Authorization: Bearer <token>' ``` (optional)

    try:
        # Create an external feed
        api_response = await api_instance.external_feeds_create_for_groups(group_id, external_feeds_create_request=external_feeds_create_request)
        print("The response of ExternalFeedsApi->external_feeds_create_for_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExternalFeedsApi->external_feeds_create_for_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Scope response to group_id | 
 **external_feeds_create_request** | [**ExternalFeedsCreateRequest**](ExternalFeedsCreateRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl https://&lt;canvas&gt;/api/v1/courses/&lt;course_id&gt;/external_feeds \\     -F url&#x3D;&#39;http://example.com/rss.xml&#39; \\     -F header_match&#x3D;&#39;news flash!&#39; \\     -F verbosity&#x3D;&#39;full&#39; \\     -H &#39;Authorization: Bearer &lt;token&gt;&#39; &#x60;&#x60;&#x60; | [optional] 

### Return type

[**ExternalFeed**](ExternalFeed.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | ExternalFeed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **external_feeds_destroy**
> ExternalFeed external_feeds_destroy(course_id, external_feed_id)

Delete an external feed

Deletes the external feed.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.external_feed import ExternalFeed
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
    api_instance = canvas_lms_python_client.ExternalFeedsApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    external_feed_id = 'external_feed_id_example' # str | Scope response to external_feed_id

    try:
        # Delete an external feed
        api_response = await api_instance.external_feeds_destroy(course_id, external_feed_id)
        print("The response of ExternalFeedsApi->external_feeds_destroy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExternalFeedsApi->external_feeds_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **external_feed_id** | **str**| Scope response to external_feed_id | 

### Return type

[**ExternalFeed**](ExternalFeed.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | ExternalFeed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **external_feeds_destroy_for_groups**
> ExternalFeed external_feeds_destroy_for_groups(external_feed_id, group_id)

Delete an external feed

Deletes the external feed.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.external_feed import ExternalFeed
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
    api_instance = canvas_lms_python_client.ExternalFeedsApi(api_client)
    external_feed_id = 'external_feed_id_example' # str | Scope response to external_feed_id
    group_id = 'group_id_example' # str | Scope response to group_id

    try:
        # Delete an external feed
        api_response = await api_instance.external_feeds_destroy_for_groups(external_feed_id, group_id)
        print("The response of ExternalFeedsApi->external_feeds_destroy_for_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExternalFeedsApi->external_feeds_destroy_for_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_feed_id** | **str**| Scope response to external_feed_id | 
 **group_id** | **str**| Scope response to group_id | 

### Return type

[**ExternalFeed**](ExternalFeed.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | ExternalFeed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **external_feeds_index**
> List[ExternalFeed] external_feeds_index(course_id, page=page, per_page=per_page)

List external feeds

Returns the paginated list of External Feeds this course or group.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.external_feed import ExternalFeed
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
    api_instance = canvas_lms_python_client.ExternalFeedsApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # List external feeds
        api_response = await api_instance.external_feeds_index(course_id, page=page, per_page=per_page)
        print("The response of ExternalFeedsApi->external_feeds_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExternalFeedsApi->external_feeds_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**List[ExternalFeed]**](ExternalFeed.md)

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

# **external_feeds_index_for_groups**
> List[ExternalFeed] external_feeds_index_for_groups(group_id, page=page, per_page=per_page)

List external feeds

Returns the paginated list of External Feeds this course or group.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.external_feed import ExternalFeed
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
    api_instance = canvas_lms_python_client.ExternalFeedsApi(api_client)
    group_id = 'group_id_example' # str | Scope response to group_id
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # List external feeds
        api_response = await api_instance.external_feeds_index_for_groups(group_id, page=page, per_page=per_page)
        print("The response of ExternalFeedsApi->external_feeds_index_for_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExternalFeedsApi->external_feeds_index_for_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Scope response to group_id | 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**List[ExternalFeed]**](ExternalFeed.md)

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

