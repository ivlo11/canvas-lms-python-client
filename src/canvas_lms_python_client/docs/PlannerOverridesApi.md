# canvas_lms_python_client.PlannerOverridesApi

All URIs are relative to *https://canvas.instructure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**planner_overrides_create**](PlannerOverridesApi.md#planner_overrides_create) | **POST** /api/v1/planner/overrides | Create a planner override
[**planner_overrides_destroy**](PlannerOverridesApi.md#planner_overrides_destroy) | **DELETE** /api/v1/planner/overrides/{id} | Delete a planner override
[**planner_overrides_index**](PlannerOverridesApi.md#planner_overrides_index) | **GET** /api/v1/planner/overrides | List planner overrides
[**planner_overrides_show**](PlannerOverridesApi.md#planner_overrides_show) | **GET** /api/v1/planner/overrides/{id} | Show a planner override
[**planner_overrides_update**](PlannerOverridesApi.md#planner_overrides_update) | **PUT** /api/v1/planner/overrides/{id} | Update a planner override


# **planner_overrides_create**
> PlannerOverride planner_overrides_create(planner_overrides_create_request=planner_overrides_create_request)

Create a planner override

Create a planner override for the current user

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.planner_override import PlannerOverride
from canvas_lms_python_client.models.planner_overrides_create_request import PlannerOverridesCreateRequest
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
    api_instance = canvas_lms_python_client.PlannerOverridesApi(api_client)
    planner_overrides_create_request = canvas_lms_python_client.PlannerOverridesCreateRequest() # PlannerOverridesCreateRequest | Request body parameters (optional)

    try:
        # Create a planner override
        api_response = await api_instance.planner_overrides_create(planner_overrides_create_request=planner_overrides_create_request)
        print("The response of PlannerOverridesApi->planner_overrides_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlannerOverridesApi->planner_overrides_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **planner_overrides_create_request** | [**PlannerOverridesCreateRequest**](PlannerOverridesCreateRequest.md)| Request body parameters | [optional] 

### Return type

[**PlannerOverride**](PlannerOverride.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | PlannerOverride |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **planner_overrides_destroy**
> PlannerOverride planner_overrides_destroy(id)

Delete a planner override

Delete a planner override for the current user

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.planner_override import PlannerOverride
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
    api_instance = canvas_lms_python_client.PlannerOverridesApi(api_client)
    id = 'id_example' # str | Scope response to id

    try:
        # Delete a planner override
        api_response = await api_instance.planner_overrides_destroy(id)
        print("The response of PlannerOverridesApi->planner_overrides_destroy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlannerOverridesApi->planner_overrides_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Scope response to id | 

### Return type

[**PlannerOverride**](PlannerOverride.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | PlannerOverride |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **planner_overrides_index**
> List[PlannerOverride] planner_overrides_index(page=page, per_page=per_page)

List planner overrides

Retrieve a planner override for the current user

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.planner_override import PlannerOverride
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
    api_instance = canvas_lms_python_client.PlannerOverridesApi(api_client)
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # List planner overrides
        api_response = await api_instance.planner_overrides_index(page=page, per_page=per_page)
        print("The response of PlannerOverridesApi->planner_overrides_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlannerOverridesApi->planner_overrides_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**List[PlannerOverride]**](PlannerOverride.md)

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

# **planner_overrides_show**
> PlannerOverride planner_overrides_show(id)

Show a planner override

Retrieve a planner override for the current user

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.planner_override import PlannerOverride
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
    api_instance = canvas_lms_python_client.PlannerOverridesApi(api_client)
    id = 'id_example' # str | Scope response to id

    try:
        # Show a planner override
        api_response = await api_instance.planner_overrides_show(id)
        print("The response of PlannerOverridesApi->planner_overrides_show:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlannerOverridesApi->planner_overrides_show: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Scope response to id | 

### Return type

[**PlannerOverride**](PlannerOverride.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | PlannerOverride |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **planner_overrides_update**
> PlannerOverride planner_overrides_update(id, planner_overrides_update_request=planner_overrides_update_request)

Update a planner override

Update a planner override's visibilty for the current user

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.planner_override import PlannerOverride
from canvas_lms_python_client.models.planner_overrides_update_request import PlannerOverridesUpdateRequest
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
    api_instance = canvas_lms_python_client.PlannerOverridesApi(api_client)
    id = 'id_example' # str | Scope response to id
    planner_overrides_update_request = canvas_lms_python_client.PlannerOverridesUpdateRequest() # PlannerOverridesUpdateRequest | Request body parameters (optional)

    try:
        # Update a planner override
        api_response = await api_instance.planner_overrides_update(id, planner_overrides_update_request=planner_overrides_update_request)
        print("The response of PlannerOverridesApi->planner_overrides_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlannerOverridesApi->planner_overrides_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Scope response to id | 
 **planner_overrides_update_request** | [**PlannerOverridesUpdateRequest**](PlannerOverridesUpdateRequest.md)| Request body parameters | [optional] 

### Return type

[**PlannerOverride**](PlannerOverride.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | PlannerOverride |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

