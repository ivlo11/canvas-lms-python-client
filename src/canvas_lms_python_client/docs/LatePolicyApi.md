# canvas_lms_python_client.LatePolicyApi

All URIs are relative to *https://canvas.instructure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**late_policy_create**](LatePolicyApi.md#late_policy_create) | **POST** /api/v1/courses/{id}/late_policy | Create a late policy
[**late_policy_show**](LatePolicyApi.md#late_policy_show) | **GET** /api/v1/courses/{id}/late_policy | Get a late policy
[**late_policy_update**](LatePolicyApi.md#late_policy_update) | **PATCH** /api/v1/courses/{id}/late_policy | Patch a late policy


# **late_policy_create**
> LatePolicyCreateResponse late_policy_create(id, late_policy_create_request=late_policy_create_request)

Create a late policy

Create a late policy. If the course already has a late policy, a
bad_request is returned since there can only be one late policy
per course.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.late_policy_create_request import LatePolicyCreateRequest
from canvas_lms_python_client.models.late_policy_create_response import LatePolicyCreateResponse
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
    api_instance = canvas_lms_python_client.LatePolicyApi(api_client)
    id = 'id_example' # str | Scope response to id
    late_policy_create_request = canvas_lms_python_client.LatePolicyCreateRequest() # LatePolicyCreateRequest | Request body parameters (optional)

    try:
        # Create a late policy
        api_response = await api_instance.late_policy_create(id, late_policy_create_request=late_policy_create_request)
        print("The response of LatePolicyApi->late_policy_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LatePolicyApi->late_policy_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Scope response to id | 
 **late_policy_create_request** | [**LatePolicyCreateRequest**](LatePolicyCreateRequest.md)| Request body parameters | [optional] 

### Return type

[**LatePolicyCreateResponse**](LatePolicyCreateResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **late_policy_show**
> LatePolicyShowResponse late_policy_show(id)

Get a late policy

Returns the late policy for a course.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.late_policy_show_response import LatePolicyShowResponse
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
    api_instance = canvas_lms_python_client.LatePolicyApi(api_client)
    id = 'id_example' # str | Scope response to id

    try:
        # Get a late policy
        api_response = await api_instance.late_policy_show(id)
        print("The response of LatePolicyApi->late_policy_show:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LatePolicyApi->late_policy_show: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Scope response to id | 

### Return type

[**LatePolicyShowResponse**](LatePolicyShowResponse.md)

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

# **late_policy_update**
> late_policy_update(id, late_policy_create_request=late_policy_create_request)

Patch a late policy

Patch a late policy. No body is returned upon success.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.late_policy_create_request import LatePolicyCreateRequest
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
    api_instance = canvas_lms_python_client.LatePolicyApi(api_client)
    id = 'id_example' # str | Scope response to id
    late_policy_create_request = canvas_lms_python_client.LatePolicyCreateRequest() # LatePolicyCreateRequest | Request body parameters (optional)

    try:
        # Patch a late policy
        await api_instance.late_policy_update(id, late_policy_create_request=late_policy_create_request)
    except Exception as e:
        print("Exception when calling LatePolicyApi->late_policy_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Scope response to id | 
 **late_policy_create_request** | [**LatePolicyCreateRequest**](LatePolicyCreateRequest.md)| Request body parameters | [optional] 

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

