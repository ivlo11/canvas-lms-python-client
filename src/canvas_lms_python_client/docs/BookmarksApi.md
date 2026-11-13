# canvas_lms_python_client.BookmarksApi

All URIs are relative to *https://canvas.instructure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bookmarks_create**](BookmarksApi.md#bookmarks_create) | **POST** /api/v1/users/self/bookmarks | Create bookmark
[**bookmarks_destroy**](BookmarksApi.md#bookmarks_destroy) | **DELETE** /api/v1/users/self/bookmarks/{id} | Delete bookmark
[**bookmarks_index**](BookmarksApi.md#bookmarks_index) | **GET** /api/v1/users/self/bookmarks | List bookmarks
[**bookmarks_show**](BookmarksApi.md#bookmarks_show) | **GET** /api/v1/users/self/bookmarks/{id} | Get bookmark
[**bookmarks_update**](BookmarksApi.md#bookmarks_update) | **PUT** /api/v1/users/self/bookmarks/{id} | Update bookmark


# **bookmarks_create**
> Bookmark bookmarks_create(bookmarks_create_request=bookmarks_create_request)

Create bookmark

Creates a bookmark.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.bookmark import Bookmark
from canvas_lms_python_client.models.bookmarks_create_request import BookmarksCreateRequest
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
    api_instance = canvas_lms_python_client.BookmarksApi(api_client)
    bookmarks_create_request = canvas_lms_python_client.BookmarksCreateRequest() # BookmarksCreateRequest | Request body parameters  **Example Request:** ``` curl 'https://<canvas>/api/v1/users/self/bookmarks' \\      -F 'name=Biology 101' \\      -F 'url=/courses/1' \\      -H 'Authorization: Bearer <token>' ``` (optional)

    try:
        # Create bookmark
        api_response = await api_instance.bookmarks_create(bookmarks_create_request=bookmarks_create_request)
        print("The response of BookmarksApi->bookmarks_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BookmarksApi->bookmarks_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bookmarks_create_request** | [**BookmarksCreateRequest**](BookmarksCreateRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl &#39;https://&lt;canvas&gt;/api/v1/users/self/bookmarks&#39; \\      -F &#39;name&#x3D;Biology 101&#39; \\      -F &#39;url&#x3D;/courses/1&#39; \\      -H &#39;Authorization: Bearer &lt;token&gt;&#39; &#x60;&#x60;&#x60; | [optional] 

### Return type

[**Bookmark**](Bookmark.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Bookmark |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bookmarks_destroy**
> Bookmark bookmarks_destroy(id)

Delete bookmark

Deletes a bookmark

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.bookmark import Bookmark
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
    api_instance = canvas_lms_python_client.BookmarksApi(api_client)
    id = 'id_example' # str | Scope response to id

    try:
        # Delete bookmark
        api_response = await api_instance.bookmarks_destroy(id)
        print("The response of BookmarksApi->bookmarks_destroy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BookmarksApi->bookmarks_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Scope response to id | 

### Return type

[**Bookmark**](Bookmark.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Bookmark |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bookmarks_index**
> List[Bookmark] bookmarks_index(page=page, per_page=per_page)

List bookmarks

Returns the paginated list of bookmarks.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.bookmark import Bookmark
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
    api_instance = canvas_lms_python_client.BookmarksApi(api_client)
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # List bookmarks
        api_response = await api_instance.bookmarks_index(page=page, per_page=per_page)
        print("The response of BookmarksApi->bookmarks_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BookmarksApi->bookmarks_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**List[Bookmark]**](Bookmark.md)

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

# **bookmarks_show**
> Bookmark bookmarks_show(id)

Get bookmark

Returns the details for a bookmark.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.bookmark import Bookmark
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
    api_instance = canvas_lms_python_client.BookmarksApi(api_client)
    id = 'id_example' # str | Scope response to id

    try:
        # Get bookmark
        api_response = await api_instance.bookmarks_show(id)
        print("The response of BookmarksApi->bookmarks_show:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BookmarksApi->bookmarks_show: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Scope response to id | 

### Return type

[**Bookmark**](Bookmark.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Bookmark |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bookmarks_update**
> Folder bookmarks_update(id, bookmarks_create_request=bookmarks_create_request)

Update bookmark

Updates a bookmark

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.bookmarks_create_request import BookmarksCreateRequest
from canvas_lms_python_client.models.folder import Folder
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
    api_instance = canvas_lms_python_client.BookmarksApi(api_client)
    id = 'id_example' # str | Scope response to id
    bookmarks_create_request = canvas_lms_python_client.BookmarksCreateRequest() # BookmarksCreateRequest | Request body parameters  **Example Request:** ``` curl -X PUT 'https://<canvas>/api/v1/users/self/bookmarks/1' \\      -F 'name=Biology 101' \\      -F 'url=/courses/1' \\      -H 'Authorization: Bearer <token>' ``` (optional)

    try:
        # Update bookmark
        api_response = await api_instance.bookmarks_update(id, bookmarks_create_request=bookmarks_create_request)
        print("The response of BookmarksApi->bookmarks_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BookmarksApi->bookmarks_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Scope response to id | 
 **bookmarks_create_request** | [**BookmarksCreateRequest**](BookmarksCreateRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl -X PUT &#39;https://&lt;canvas&gt;/api/v1/users/self/bookmarks/1&#39; \\      -F &#39;name&#x3D;Biology 101&#39; \\      -F &#39;url&#x3D;/courses/1&#39; \\      -H &#39;Authorization: Bearer &lt;token&gt;&#39; &#x60;&#x60;&#x60; | [optional] 

### Return type

[**Folder**](Folder.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Folder |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

