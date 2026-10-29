# canvas_lms_python_client.RecordAlreadyExistsApi

All URIs are relative to *https://canvas.instructure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**record_already_exists_create**](RecordAlreadyExistsApi.md#record_already_exists_create) | **POST** /api/v1/courses/{id}/late_policy | Create a late policy
[**record_already_exists_show**](RecordAlreadyExistsApi.md#record_already_exists_show) | **GET** /api/v1/courses/{id}/late_policy | Get a late policy
[**record_already_exists_update**](RecordAlreadyExistsApi.md#record_already_exists_update) | **PATCH** /api/v1/courses/{id}/late_policy | Patch a late policy


# **record_already_exists_create**
> record_already_exists_create(id, record_already_exists_create_request=record_already_exists_create_request)

Create a late policy

Create a late policy. If the course already has a late policy, a
bad_request is returned since there can only be one late policy
per course.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.record_already_exists_create_request import RecordAlreadyExistsCreateRequest
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
    api_instance = canvas_lms_python_client.RecordAlreadyExistsApi(api_client)
    id = 'id_example' # str | Scope response to id
    record_already_exists_create_request = canvas_lms_python_client.RecordAlreadyExistsCreateRequest() # RecordAlreadyExistsCreateRequest | Request body parameters (optional)

    try:
        # Create a late policy
        await api_instance.record_already_exists_create(id, record_already_exists_create_request=record_already_exists_create_request)
    except Exception as e:
        print("Exception when calling RecordAlreadyExistsApi->record_already_exists_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Scope response to id | 
 **record_already_exists_create_request** | [**RecordAlreadyExistsCreateRequest**](RecordAlreadyExistsCreateRequest.md)| Request body parameters | [optional] 

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
**0** | Create a late policy |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **record_already_exists_show**
> record_already_exists_show(id)

Get a late policy

Returns the late policy for a course.

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
    api_instance = canvas_lms_python_client.RecordAlreadyExistsApi(api_client)
    id = 'id_example' # str | Scope response to id

    try:
        # Get a late policy
        await api_instance.record_already_exists_show(id)
    except Exception as e:
        print("Exception when calling RecordAlreadyExistsApi->record_already_exists_show: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Scope response to id | 

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
**0** | Get a late policy |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **record_already_exists_update**
> record_already_exists_update(id, record_already_exists_create_request=record_already_exists_create_request)

Patch a late policy

Patch a late policy. No body is returned upon success.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.record_already_exists_create_request import RecordAlreadyExistsCreateRequest
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
    api_instance = canvas_lms_python_client.RecordAlreadyExistsApi(api_client)
    id = 'id_example' # str | Scope response to id
    record_already_exists_create_request = canvas_lms_python_client.RecordAlreadyExistsCreateRequest() # RecordAlreadyExistsCreateRequest | Request body parameters (optional)

    try:
        # Patch a late policy
        await api_instance.record_already_exists_update(id, record_already_exists_create_request=record_already_exists_create_request)
    except Exception as e:
        print("Exception when calling RecordAlreadyExistsApi->record_already_exists_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Scope response to id | 
 **record_already_exists_create_request** | [**RecordAlreadyExistsCreateRequest**](RecordAlreadyExistsCreateRequest.md)| Request body parameters | [optional] 

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
**0** | Patch a late policy |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

