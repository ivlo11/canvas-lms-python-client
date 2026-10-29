# canvas_lms_python_client.ContentSharesApi

All URIs are relative to *https://canvas.instructure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**content_shares_add_users**](ContentSharesApi.md#content_shares_add_users) | **POST** /api/v1/users/{user_id}/content_shares/{id}/add_users | Add users to content share
[**content_shares_create**](ContentSharesApi.md#content_shares_create) | **POST** /api/v1/users/{user_id}/content_shares | Create a content share
[**content_shares_destroy**](ContentSharesApi.md#content_shares_destroy) | **DELETE** /api/v1/users/{user_id}/content_shares/{id} | Remove content share
[**content_shares_index**](ContentSharesApi.md#content_shares_index) | **GET** /api/v1/users/{user_id}/content_shares/sent | List content shares
[**content_shares_index_for_users**](ContentSharesApi.md#content_shares_index_for_users) | **GET** /api/v1/users/{user_id}/content_shares/received | List content shares
[**content_shares_show**](ContentSharesApi.md#content_shares_show) | **GET** /api/v1/users/{user_id}/content_shares/{id} | Get content share
[**content_shares_unread_count**](ContentSharesApi.md#content_shares_unread_count) | **GET** /api/v1/users/{user_id}/content_shares/unread_count | Get unread shares count
[**content_shares_update**](ContentSharesApi.md#content_shares_update) | **PUT** /api/v1/users/{user_id}/content_shares/{id} | Update a content share


# **content_shares_add_users**
> ContentShare content_shares_add_users(id, user_id, content_shares_add_users_request=content_shares_add_users_request)

Add users to content share

Send a previously created content share to additional users

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.content_share import ContentShare
from canvas_lms_python_client.models.content_shares_add_users_request import ContentSharesAddUsersRequest
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
    api_instance = canvas_lms_python_client.ContentSharesApi(api_client)
    id = 'id_example' # str | Scope response to id
    user_id = 'user_id_example' # str | Scope response to user_id
    content_shares_add_users_request = canvas_lms_python_client.ContentSharesAddUsersRequest() # ContentSharesAddUsersRequest | Request body parameters  **Example Request:** ``` curl -X POST 'https://<canvas>/api/v1/users/self/content_shares/123/add_users?receiver_ids[]=789' ``` (optional)

    try:
        # Add users to content share
        api_response = await api_instance.content_shares_add_users(id, user_id, content_shares_add_users_request=content_shares_add_users_request)
        print("The response of ContentSharesApi->content_shares_add_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContentSharesApi->content_shares_add_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Scope response to id | 
 **user_id** | **str**| Scope response to user_id | 
 **content_shares_add_users_request** | [**ContentSharesAddUsersRequest**](ContentSharesAddUsersRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl -X POST &#39;https://&lt;canvas&gt;/api/v1/users/self/content_shares/123/add_users?receiver_ids[]&#x3D;789&#39; &#x60;&#x60;&#x60; | [optional] 

### Return type

[**ContentShare**](ContentShare.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | ContentShare |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **content_shares_create**
> ContentShare content_shares_create(user_id, content_shares_create_request=content_shares_create_request)

Create a content share

Share content directly between two or more users

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.content_share import ContentShare
from canvas_lms_python_client.models.content_shares_create_request import ContentSharesCreateRequest
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
    api_instance = canvas_lms_python_client.ContentSharesApi(api_client)
    user_id = 'user_id_example' # str | Scope response to user_id
    content_shares_create_request = canvas_lms_python_client.ContentSharesCreateRequest() # ContentSharesCreateRequest | Request body parameters  **Example Request:** ``` curl 'https://<canvas>/api/v1/users/self/content_shares \\       -d 'content_type=assignment' \\       -d 'content_id=1' \\       -H 'Authorization: Bearer <token>' \\       -X POST ``` (optional)

    try:
        # Create a content share
        api_response = await api_instance.content_shares_create(user_id, content_shares_create_request=content_shares_create_request)
        print("The response of ContentSharesApi->content_shares_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContentSharesApi->content_shares_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| Scope response to user_id | 
 **content_shares_create_request** | [**ContentSharesCreateRequest**](ContentSharesCreateRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl &#39;https://&lt;canvas&gt;/api/v1/users/self/content_shares \\       -d &#39;content_type&#x3D;assignment&#39; \\       -d &#39;content_id&#x3D;1&#39; \\       -H &#39;Authorization: Bearer &lt;token&gt;&#39; \\       -X POST &#x60;&#x60;&#x60; | [optional] 

### Return type

[**ContentShare**](ContentShare.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | ContentShare |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **content_shares_destroy**
> content_shares_destroy(id, user_id)

Remove content share

Remove a content share from your list. Use +self+ as the user_id. Note that this endpoint does not delete other users'
copies of the content share.

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
    api_instance = canvas_lms_python_client.ContentSharesApi(api_client)
    id = 'id_example' # str | Scope response to id
    user_id = 'user_id_example' # str | Scope response to user_id

    try:
        # Remove content share
        await api_instance.content_shares_destroy(id, user_id)
    except Exception as e:
        print("Exception when calling ContentSharesApi->content_shares_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Scope response to id | 
 **user_id** | **str**| Scope response to user_id | 

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
**0** | Remove content share |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **content_shares_index**
> List[ContentShare] content_shares_index(user_id, page=page, per_page=per_page)

List content shares

Return a paginated list of content shares a user has sent or received. Use +self+ as the user_id
to retrieve your own content shares. Only linked observers and administrators may view other users'
content shares.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.content_share import ContentShare
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
    api_instance = canvas_lms_python_client.ContentSharesApi(api_client)
    user_id = 'user_id_example' # str | Scope response to user_id
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # List content shares
        api_response = await api_instance.content_shares_index(user_id, page=page, per_page=per_page)
        print("The response of ContentSharesApi->content_shares_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContentSharesApi->content_shares_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| Scope response to user_id | 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**List[ContentShare]**](ContentShare.md)

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

# **content_shares_index_for_users**
> List[ContentShare] content_shares_index_for_users(user_id, page=page, per_page=per_page)

List content shares

Return a paginated list of content shares a user has sent or received. Use +self+ as the user_id
to retrieve your own content shares. Only linked observers and administrators may view other users'
content shares.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.content_share import ContentShare
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
    api_instance = canvas_lms_python_client.ContentSharesApi(api_client)
    user_id = 'user_id_example' # str | Scope response to user_id
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # List content shares
        api_response = await api_instance.content_shares_index_for_users(user_id, page=page, per_page=per_page)
        print("The response of ContentSharesApi->content_shares_index_for_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContentSharesApi->content_shares_index_for_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| Scope response to user_id | 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**List[ContentShare]**](ContentShare.md)

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

# **content_shares_show**
> ContentShare content_shares_show(id, user_id)

Get content share

Return information about a single content share. You may use +self+ as the user_id to retrieve your own content share.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.content_share import ContentShare
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
    api_instance = canvas_lms_python_client.ContentSharesApi(api_client)
    id = 'id_example' # str | Scope response to id
    user_id = 'user_id_example' # str | Scope response to user_id

    try:
        # Get content share
        api_response = await api_instance.content_shares_show(id, user_id)
        print("The response of ContentSharesApi->content_shares_show:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContentSharesApi->content_shares_show: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Scope response to id | 
 **user_id** | **str**| Scope response to user_id | 

### Return type

[**ContentShare**](ContentShare.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | ContentShare |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **content_shares_unread_count**
> List[object] content_shares_unread_count(user_id)

Get unread shares count

Return the number of content shares a user has received that have not yet been read. Use +self+ as the user_id
to retrieve your own content shares. Only linked observers and administrators may view other users'
content shares.

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
    api_instance = canvas_lms_python_client.ContentSharesApi(api_client)
    user_id = 'user_id_example' # str | Scope response to user_id

    try:
        # Get unread shares count
        api_response = await api_instance.content_shares_unread_count(user_id)
        print("The response of ContentSharesApi->content_shares_unread_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContentSharesApi->content_shares_unread_count: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| Scope response to user_id | 

### Return type

**List[object]**

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

# **content_shares_update**
> ContentShare content_shares_update(id, user_id, content_shares_update_request=content_shares_update_request)

Update a content share

Mark a content share read or unread

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.content_share import ContentShare
from canvas_lms_python_client.models.content_shares_update_request import ContentSharesUpdateRequest
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
    api_instance = canvas_lms_python_client.ContentSharesApi(api_client)
    id = 'id_example' # str | Scope response to id
    user_id = 'user_id_example' # str | Scope response to user_id
    content_shares_update_request = canvas_lms_python_client.ContentSharesUpdateRequest() # ContentSharesUpdateRequest | Request body parameters  **Example Request:** ``` curl -X PUT 'https://<canvas>/api/v1/users/self/content_shares/123?read_state=read' ``` (optional)

    try:
        # Update a content share
        api_response = await api_instance.content_shares_update(id, user_id, content_shares_update_request=content_shares_update_request)
        print("The response of ContentSharesApi->content_shares_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContentSharesApi->content_shares_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Scope response to id | 
 **user_id** | **str**| Scope response to user_id | 
 **content_shares_update_request** | [**ContentSharesUpdateRequest**](ContentSharesUpdateRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl -X PUT &#39;https://&lt;canvas&gt;/api/v1/users/self/content_shares/123?read_state&#x3D;read&#39; &#x60;&#x60;&#x60; | [optional] 

### Return type

[**ContentShare**](ContentShare.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | ContentShare |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

