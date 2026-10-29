# canvas_lms_python_client.GradingPeriodSetsApi

All URIs are relative to *https://canvas.instructure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**grading_period_sets_create**](GradingPeriodSetsApi.md#grading_period_sets_create) | **POST** /api/v1/accounts/{account_id}/grading_period_sets | Create a grading period set
[**grading_period_sets_destroy**](GradingPeriodSetsApi.md#grading_period_sets_destroy) | **DELETE** /api/v1/accounts/{account_id}/grading_period_sets/{id} | Delete a grading period set
[**grading_period_sets_index**](GradingPeriodSetsApi.md#grading_period_sets_index) | **GET** /api/v1/accounts/{account_id}/grading_period_sets | List grading period sets
[**grading_period_sets_update**](GradingPeriodSetsApi.md#grading_period_sets_update) | **PATCH** /api/v1/accounts/{account_id}/grading_period_sets/{id} | Update a grading period set


# **grading_period_sets_create**
> grading_period_sets_create(account_id, grading_period_sets_create_request=grading_period_sets_create_request)

Create a grading period set

Create and return a new grading period set

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.grading_period_sets_create_request import GradingPeriodSetsCreateRequest
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
    api_instance = canvas_lms_python_client.GradingPeriodSetsApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    grading_period_sets_create_request = canvas_lms_python_client.GradingPeriodSetsCreateRequest() # GradingPeriodSetsCreateRequest | Request body parameters (optional)

    try:
        # Create a grading period set
        await api_instance.grading_period_sets_create(account_id, grading_period_sets_create_request=grading_period_sets_create_request)
    except Exception as e:
        print("Exception when calling GradingPeriodSetsApi->grading_period_sets_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **grading_period_sets_create_request** | [**GradingPeriodSetsCreateRequest**](GradingPeriodSetsCreateRequest.md)| Request body parameters | [optional] 

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Create a grading period set |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grading_period_sets_destroy**
> grading_period_sets_destroy(account_id, id)

Delete a grading period set

<b>204 No Content</b> response code is returned if the deletion was
successful.

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
    api_instance = canvas_lms_python_client.GradingPeriodSetsApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    id = 'id_example' # str | Scope response to id

    try:
        # Delete a grading period set
        await api_instance.grading_period_sets_destroy(account_id, id)
    except Exception as e:
        print("Exception when calling GradingPeriodSetsApi->grading_period_sets_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
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
**0** | Delete a grading period set |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grading_period_sets_index**
> grading_period_sets_index(account_id, page=page, per_page=per_page)

List grading period sets

Returns the paginated list of grading period sets

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
    api_instance = canvas_lms_python_client.GradingPeriodSetsApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # List grading period sets
        await api_instance.grading_period_sets_index(account_id, page=page, per_page=per_page)
    except Exception as e:
        print("Exception when calling GradingPeriodSetsApi->grading_period_sets_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | List grading period sets |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grading_period_sets_update**
> grading_period_sets_update(account_id, id, grading_period_sets_update_request=grading_period_sets_update_request)

Update a grading period set

Update an existing grading period set

<b>204 No Content</b> response code is returned if the update was
successful.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.grading_period_sets_update_request import GradingPeriodSetsUpdateRequest
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
    api_instance = canvas_lms_python_client.GradingPeriodSetsApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    id = 'id_example' # str | Scope response to id
    grading_period_sets_update_request = canvas_lms_python_client.GradingPeriodSetsUpdateRequest() # GradingPeriodSetsUpdateRequest | Request body parameters (optional)

    try:
        # Update a grading period set
        await api_instance.grading_period_sets_update(account_id, id, grading_period_sets_update_request=grading_period_sets_update_request)
    except Exception as e:
        print("Exception when calling GradingPeriodSetsApi->grading_period_sets_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **id** | **str**| Scope response to id | 
 **grading_period_sets_update_request** | [**GradingPeriodSetsUpdateRequest**](GradingPeriodSetsUpdateRequest.md)| Request body parameters | [optional] 

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
**0** | Update a grading period set |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

