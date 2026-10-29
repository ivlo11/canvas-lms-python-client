# canvas_lms_python_client.CustomGradebookColumnsApiApi

All URIs are relative to *https://canvas.instructure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**custom_gradebook_columns_api_create**](CustomGradebookColumnsApiApi.md#custom_gradebook_columns_api_create) | **POST** /api/v1/courses/{course_id}/custom_gradebook_columns | Create a custom gradebook column
[**custom_gradebook_columns_api_destroy**](CustomGradebookColumnsApiApi.md#custom_gradebook_columns_api_destroy) | **DELETE** /api/v1/courses/{course_id}/custom_gradebook_columns/{id} | Delete a custom gradebook column
[**custom_gradebook_columns_api_index**](CustomGradebookColumnsApiApi.md#custom_gradebook_columns_api_index) | **GET** /api/v1/courses/{course_id}/custom_gradebook_columns | List custom gradebook columns
[**custom_gradebook_columns_api_reorder**](CustomGradebookColumnsApiApi.md#custom_gradebook_columns_api_reorder) | **POST** /api/v1/courses/{course_id}/custom_gradebook_columns/reorder | Reorder custom columns
[**custom_gradebook_columns_api_update**](CustomGradebookColumnsApiApi.md#custom_gradebook_columns_api_update) | **PUT** /api/v1/courses/{course_id}/custom_gradebook_columns/{id} | Update a custom gradebook column


# **custom_gradebook_columns_api_create**
> CustomColumn custom_gradebook_columns_api_create(course_id, custom_gradebook_columns_api_create_request=custom_gradebook_columns_api_create_request)

Create a custom gradebook column

Create a custom gradebook column

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.custom_column import CustomColumn
from canvas_lms_python_client.models.custom_gradebook_columns_api_create_request import CustomGradebookColumnsApiCreateRequest
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
    api_instance = canvas_lms_python_client.CustomGradebookColumnsApiApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    custom_gradebook_columns_api_create_request = canvas_lms_python_client.CustomGradebookColumnsApiCreateRequest() # CustomGradebookColumnsApiCreateRequest | Request body parameters (optional)

    try:
        # Create a custom gradebook column
        api_response = await api_instance.custom_gradebook_columns_api_create(course_id, custom_gradebook_columns_api_create_request=custom_gradebook_columns_api_create_request)
        print("The response of CustomGradebookColumnsApiApi->custom_gradebook_columns_api_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomGradebookColumnsApiApi->custom_gradebook_columns_api_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **custom_gradebook_columns_api_create_request** | [**CustomGradebookColumnsApiCreateRequest**](CustomGradebookColumnsApiCreateRequest.md)| Request body parameters | [optional] 

### Return type

[**CustomColumn**](CustomColumn.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | CustomColumn |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_gradebook_columns_api_destroy**
> CustomColumn custom_gradebook_columns_api_destroy(course_id, id)

Delete a custom gradebook column

Permanently deletes a custom column and its associated data

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.custom_column import CustomColumn
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
    api_instance = canvas_lms_python_client.CustomGradebookColumnsApiApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    id = 'id_example' # str | Scope response to id

    try:
        # Delete a custom gradebook column
        api_response = await api_instance.custom_gradebook_columns_api_destroy(course_id, id)
        print("The response of CustomGradebookColumnsApiApi->custom_gradebook_columns_api_destroy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomGradebookColumnsApiApi->custom_gradebook_columns_api_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **id** | **str**| Scope response to id | 

### Return type

[**CustomColumn**](CustomColumn.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | CustomColumn |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_gradebook_columns_api_index**
> List[CustomColumn] custom_gradebook_columns_api_index(course_id, include_hidden=include_hidden, page=page, per_page=per_page)

List custom gradebook columns

A paginated list of all custom gradebook columns for a course

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.custom_column import CustomColumn
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
    api_instance = canvas_lms_python_client.CustomGradebookColumnsApiApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    include_hidden = True # bool | Include hidden parameters (defaults to false) (optional)
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # List custom gradebook columns
        api_response = await api_instance.custom_gradebook_columns_api_index(course_id, include_hidden=include_hidden, page=page, per_page=per_page)
        print("The response of CustomGradebookColumnsApiApi->custom_gradebook_columns_api_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomGradebookColumnsApiApi->custom_gradebook_columns_api_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **include_hidden** | **bool**| Include hidden parameters (defaults to false) | [optional] 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**List[CustomColumn]**](CustomColumn.md)

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

# **custom_gradebook_columns_api_reorder**
> custom_gradebook_columns_api_reorder(course_id, custom_gradebook_columns_api_reorder_request=custom_gradebook_columns_api_reorder_request)

Reorder custom columns

Puts the given columns in the specified order

<b>200 OK</b> is returned if successful

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.custom_gradebook_columns_api_reorder_request import CustomGradebookColumnsApiReorderRequest
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
    api_instance = canvas_lms_python_client.CustomGradebookColumnsApiApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    custom_gradebook_columns_api_reorder_request = canvas_lms_python_client.CustomGradebookColumnsApiReorderRequest() # CustomGradebookColumnsApiReorderRequest | Request body parameters (optional)

    try:
        # Reorder custom columns
        await api_instance.custom_gradebook_columns_api_reorder(course_id, custom_gradebook_columns_api_reorder_request=custom_gradebook_columns_api_reorder_request)
    except Exception as e:
        print("Exception when calling CustomGradebookColumnsApiApi->custom_gradebook_columns_api_reorder: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **custom_gradebook_columns_api_reorder_request** | [**CustomGradebookColumnsApiReorderRequest**](CustomGradebookColumnsApiReorderRequest.md)| Request body parameters | [optional] 

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Reorder custom columns |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_gradebook_columns_api_update**
> CustomColumn custom_gradebook_columns_api_update(course_id, id)

Update a custom gradebook column

Accepts the same parameters as custom gradebook column creation

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.custom_column import CustomColumn
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
    api_instance = canvas_lms_python_client.CustomGradebookColumnsApiApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    id = 'id_example' # str | Scope response to id

    try:
        # Update a custom gradebook column
        api_response = await api_instance.custom_gradebook_columns_api_update(course_id, id)
        print("The response of CustomGradebookColumnsApiApi->custom_gradebook_columns_api_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomGradebookColumnsApiApi->custom_gradebook_columns_api_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **id** | **str**| Scope response to id | 

### Return type

[**CustomColumn**](CustomColumn.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | CustomColumn |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

