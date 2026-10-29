# canvas_lms_python_client.ContentExportsApiApi

All URIs are relative to *https://canvas.instructure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**content_exports_api_create**](ContentExportsApiApi.md#content_exports_api_create) | **POST** /api/v1/courses/{course_id}/content_exports | Export content
[**content_exports_api_create_for_groups**](ContentExportsApiApi.md#content_exports_api_create_for_groups) | **POST** /api/v1/groups/{group_id}/content_exports | Export content
[**content_exports_api_create_for_users**](ContentExportsApiApi.md#content_exports_api_create_for_users) | **POST** /api/v1/users/{user_id}/content_exports | Export content
[**content_exports_api_index**](ContentExportsApiApi.md#content_exports_api_index) | **GET** /api/v1/courses/{course_id}/content_exports | List content exports
[**content_exports_api_index_for_groups**](ContentExportsApiApi.md#content_exports_api_index_for_groups) | **GET** /api/v1/groups/{group_id}/content_exports | List content exports
[**content_exports_api_index_for_users**](ContentExportsApiApi.md#content_exports_api_index_for_users) | **GET** /api/v1/users/{user_id}/content_exports | List content exports
[**content_exports_api_show**](ContentExportsApiApi.md#content_exports_api_show) | **GET** /api/v1/courses/{course_id}/content_exports/{id} | Show content export
[**content_exports_api_show_for_groups**](ContentExportsApiApi.md#content_exports_api_show_for_groups) | **GET** /api/v1/groups/{group_id}/content_exports/{id} | Show content export
[**content_exports_api_show_for_users**](ContentExportsApiApi.md#content_exports_api_show_for_users) | **GET** /api/v1/users/{user_id}/content_exports/{id} | Show content export


# **content_exports_api_create**
> ContentExport content_exports_api_create(course_id, content_exports_api_create_request=content_exports_api_create_request)

Export content

Begin a content export job for a course, group, or user.

You can use the {api:ProgressController#show Progress API} to track the
progress of the export. The migration's progress is linked to with the
_progress_url_ value.

When the export completes, use the {api:ContentExportsApiController#show Show content export} endpoint
to retrieve a download URL for the exported content.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.content_export import ContentExport
from canvas_lms_python_client.models.content_exports_api_create_request import ContentExportsApiCreateRequest
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
    api_instance = canvas_lms_python_client.ContentExportsApiApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    content_exports_api_create_request = canvas_lms_python_client.ContentExportsApiCreateRequest() # ContentExportsApiCreateRequest | Request body parameters (optional)

    try:
        # Export content
        api_response = await api_instance.content_exports_api_create(course_id, content_exports_api_create_request=content_exports_api_create_request)
        print("The response of ContentExportsApiApi->content_exports_api_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContentExportsApiApi->content_exports_api_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **content_exports_api_create_request** | [**ContentExportsApiCreateRequest**](ContentExportsApiCreateRequest.md)| Request body parameters | [optional] 

### Return type

[**ContentExport**](ContentExport.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | ContentExport |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **content_exports_api_create_for_groups**
> ContentExport content_exports_api_create_for_groups(group_id, content_exports_api_create_request=content_exports_api_create_request)

Export content

Begin a content export job for a course, group, or user.

You can use the {api:ProgressController#show Progress API} to track the
progress of the export. The migration's progress is linked to with the
_progress_url_ value.

When the export completes, use the {api:ContentExportsApiController#show Show content export} endpoint
to retrieve a download URL for the exported content.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.content_export import ContentExport
from canvas_lms_python_client.models.content_exports_api_create_request import ContentExportsApiCreateRequest
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
    api_instance = canvas_lms_python_client.ContentExportsApiApi(api_client)
    group_id = 'group_id_example' # str | Scope response to group_id
    content_exports_api_create_request = canvas_lms_python_client.ContentExportsApiCreateRequest() # ContentExportsApiCreateRequest | Request body parameters (optional)

    try:
        # Export content
        api_response = await api_instance.content_exports_api_create_for_groups(group_id, content_exports_api_create_request=content_exports_api_create_request)
        print("The response of ContentExportsApiApi->content_exports_api_create_for_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContentExportsApiApi->content_exports_api_create_for_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Scope response to group_id | 
 **content_exports_api_create_request** | [**ContentExportsApiCreateRequest**](ContentExportsApiCreateRequest.md)| Request body parameters | [optional] 

### Return type

[**ContentExport**](ContentExport.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | ContentExport |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **content_exports_api_create_for_users**
> ContentExport content_exports_api_create_for_users(user_id, content_exports_api_create_request=content_exports_api_create_request)

Export content

Begin a content export job for a course, group, or user.

You can use the {api:ProgressController#show Progress API} to track the
progress of the export. The migration's progress is linked to with the
_progress_url_ value.

When the export completes, use the {api:ContentExportsApiController#show Show content export} endpoint
to retrieve a download URL for the exported content.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.content_export import ContentExport
from canvas_lms_python_client.models.content_exports_api_create_request import ContentExportsApiCreateRequest
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
    api_instance = canvas_lms_python_client.ContentExportsApiApi(api_client)
    user_id = 'user_id_example' # str | Scope response to user_id
    content_exports_api_create_request = canvas_lms_python_client.ContentExportsApiCreateRequest() # ContentExportsApiCreateRequest | Request body parameters (optional)

    try:
        # Export content
        api_response = await api_instance.content_exports_api_create_for_users(user_id, content_exports_api_create_request=content_exports_api_create_request)
        print("The response of ContentExportsApiApi->content_exports_api_create_for_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContentExportsApiApi->content_exports_api_create_for_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| Scope response to user_id | 
 **content_exports_api_create_request** | [**ContentExportsApiCreateRequest**](ContentExportsApiCreateRequest.md)| Request body parameters | [optional] 

### Return type

[**ContentExport**](ContentExport.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | ContentExport |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **content_exports_api_index**
> List[ContentExport] content_exports_api_index(course_id, page=page, per_page=per_page)

List content exports

A paginated list of the past and pending content export jobs for a course,
group, or user. Exports are returned newest first.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.content_export import ContentExport
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
    api_instance = canvas_lms_python_client.ContentExportsApiApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # List content exports
        api_response = await api_instance.content_exports_api_index(course_id, page=page, per_page=per_page)
        print("The response of ContentExportsApiApi->content_exports_api_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContentExportsApiApi->content_exports_api_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**List[ContentExport]**](ContentExport.md)

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

# **content_exports_api_index_for_groups**
> List[ContentExport] content_exports_api_index_for_groups(group_id, page=page, per_page=per_page)

List content exports

A paginated list of the past and pending content export jobs for a course,
group, or user. Exports are returned newest first.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.content_export import ContentExport
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
    api_instance = canvas_lms_python_client.ContentExportsApiApi(api_client)
    group_id = 'group_id_example' # str | Scope response to group_id
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # List content exports
        api_response = await api_instance.content_exports_api_index_for_groups(group_id, page=page, per_page=per_page)
        print("The response of ContentExportsApiApi->content_exports_api_index_for_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContentExportsApiApi->content_exports_api_index_for_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Scope response to group_id | 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**List[ContentExport]**](ContentExport.md)

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

# **content_exports_api_index_for_users**
> List[ContentExport] content_exports_api_index_for_users(user_id, page=page, per_page=per_page)

List content exports

A paginated list of the past and pending content export jobs for a course,
group, or user. Exports are returned newest first.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.content_export import ContentExport
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
    api_instance = canvas_lms_python_client.ContentExportsApiApi(api_client)
    user_id = 'user_id_example' # str | Scope response to user_id
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # List content exports
        api_response = await api_instance.content_exports_api_index_for_users(user_id, page=page, per_page=per_page)
        print("The response of ContentExportsApiApi->content_exports_api_index_for_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContentExportsApiApi->content_exports_api_index_for_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| Scope response to user_id | 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**List[ContentExport]**](ContentExport.md)

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

# **content_exports_api_show**
> ContentExport content_exports_api_show(course_id, id)

Show content export

Get information about a single content export.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.content_export import ContentExport
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
    api_instance = canvas_lms_python_client.ContentExportsApiApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    id = 'id_example' # str | Scope response to id

    try:
        # Show content export
        api_response = await api_instance.content_exports_api_show(course_id, id)
        print("The response of ContentExportsApiApi->content_exports_api_show:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContentExportsApiApi->content_exports_api_show: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **id** | **str**| Scope response to id | 

### Return type

[**ContentExport**](ContentExport.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | ContentExport |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **content_exports_api_show_for_groups**
> ContentExport content_exports_api_show_for_groups(group_id, id)

Show content export

Get information about a single content export.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.content_export import ContentExport
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
    api_instance = canvas_lms_python_client.ContentExportsApiApi(api_client)
    group_id = 'group_id_example' # str | Scope response to group_id
    id = 'id_example' # str | Scope response to id

    try:
        # Show content export
        api_response = await api_instance.content_exports_api_show_for_groups(group_id, id)
        print("The response of ContentExportsApiApi->content_exports_api_show_for_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContentExportsApiApi->content_exports_api_show_for_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Scope response to group_id | 
 **id** | **str**| Scope response to id | 

### Return type

[**ContentExport**](ContentExport.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | ContentExport |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **content_exports_api_show_for_users**
> ContentExport content_exports_api_show_for_users(id, user_id)

Show content export

Get information about a single content export.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.content_export import ContentExport
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
    api_instance = canvas_lms_python_client.ContentExportsApiApi(api_client)
    id = 'id_example' # str | Scope response to id
    user_id = 'user_id_example' # str | Scope response to user_id

    try:
        # Show content export
        api_response = await api_instance.content_exports_api_show_for_users(id, user_id)
        print("The response of ContentExportsApiApi->content_exports_api_show_for_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContentExportsApiApi->content_exports_api_show_for_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Scope response to id | 
 **user_id** | **str**| Scope response to user_id | 

### Return type

[**ContentExport**](ContentExport.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | ContentExport |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

