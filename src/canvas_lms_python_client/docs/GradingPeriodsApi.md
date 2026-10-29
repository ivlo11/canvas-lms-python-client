# canvas_lms_python_client.GradingPeriodsApi

All URIs are relative to *https://canvas.instructure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**grading_periods_batch_update**](GradingPeriodsApi.md#grading_periods_batch_update) | **PATCH** /api/v1/courses/{course_id}/grading_periods/batch_update | Batch update grading periods
[**grading_periods_batch_update_for_other**](GradingPeriodsApi.md#grading_periods_batch_update_for_other) | **PATCH** /api/v1/grading_period_sets/{set_id}/grading_periods/batch_update | Batch update grading periods
[**grading_periods_destroy**](GradingPeriodsApi.md#grading_periods_destroy) | **DELETE** /api/v1/courses/{course_id}/grading_periods/{id} | Delete a grading period
[**grading_periods_destroy_for_accounts**](GradingPeriodsApi.md#grading_periods_destroy_for_accounts) | **DELETE** /api/v1/accounts/{account_id}/grading_periods/{id} | Delete a grading period
[**grading_periods_index**](GradingPeriodsApi.md#grading_periods_index) | **GET** /api/v1/accounts/{account_id}/grading_periods | List grading periods
[**grading_periods_index_for_courses**](GradingPeriodsApi.md#grading_periods_index_for_courses) | **GET** /api/v1/courses/{course_id}/grading_periods | List grading periods
[**grading_periods_show**](GradingPeriodsApi.md#grading_periods_show) | **GET** /api/v1/courses/{course_id}/grading_periods/{id} | Get a single grading period
[**grading_periods_update**](GradingPeriodsApi.md#grading_periods_update) | **PUT** /api/v1/courses/{course_id}/grading_periods/{id} | Update a single grading period


# **grading_periods_batch_update**
> grading_periods_batch_update(course_id, grading_periods_batch_update_request=grading_periods_batch_update_request)

Batch update grading periods

Update multiple grading periods

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.grading_periods_batch_update_request import GradingPeriodsBatchUpdateRequest
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
    api_instance = canvas_lms_python_client.GradingPeriodsApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    grading_periods_batch_update_request = canvas_lms_python_client.GradingPeriodsBatchUpdateRequest() # GradingPeriodsBatchUpdateRequest | Request body parameters (optional)

    try:
        # Batch update grading periods
        await api_instance.grading_periods_batch_update(course_id, grading_periods_batch_update_request=grading_periods_batch_update_request)
    except Exception as e:
        print("Exception when calling GradingPeriodsApi->grading_periods_batch_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **grading_periods_batch_update_request** | [**GradingPeriodsBatchUpdateRequest**](GradingPeriodsBatchUpdateRequest.md)| Request body parameters | [optional] 

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
**0** | Batch update grading periods |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grading_periods_batch_update_for_other**
> grading_periods_batch_update_for_other(set_id, grading_periods_batch_update_for_other_request=grading_periods_batch_update_for_other_request)

Batch update grading periods

Update multiple grading periods

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.grading_periods_batch_update_for_other_request import GradingPeriodsBatchUpdateForOtherRequest
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
    api_instance = canvas_lms_python_client.GradingPeriodsApi(api_client)
    set_id = 'set_id_example' # str | The id of the grading period set.
    grading_periods_batch_update_for_other_request = canvas_lms_python_client.GradingPeriodsBatchUpdateForOtherRequest() # GradingPeriodsBatchUpdateForOtherRequest | Request body parameters (optional)

    try:
        # Batch update grading periods
        await api_instance.grading_periods_batch_update_for_other(set_id, grading_periods_batch_update_for_other_request=grading_periods_batch_update_for_other_request)
    except Exception as e:
        print("Exception when calling GradingPeriodsApi->grading_periods_batch_update_for_other: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **set_id** | **str**| The id of the grading period set. | 
 **grading_periods_batch_update_for_other_request** | [**GradingPeriodsBatchUpdateForOtherRequest**](GradingPeriodsBatchUpdateForOtherRequest.md)| Request body parameters | [optional] 

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
**0** | Batch update grading periods |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grading_periods_destroy**
> grading_periods_destroy(course_id, id)

Delete a grading period

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
    api_instance = canvas_lms_python_client.GradingPeriodsApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    id = 'id_example' # str | Scope response to id

    try:
        # Delete a grading period
        await api_instance.grading_periods_destroy(course_id, id)
    except Exception as e:
        print("Exception when calling GradingPeriodsApi->grading_periods_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
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
**0** | Delete a grading period |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grading_periods_destroy_for_accounts**
> grading_periods_destroy_for_accounts(account_id, id)

Delete a grading period

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
    api_instance = canvas_lms_python_client.GradingPeriodsApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    id = 'id_example' # str | Scope response to id

    try:
        # Delete a grading period
        await api_instance.grading_periods_destroy_for_accounts(account_id, id)
    except Exception as e:
        print("Exception when calling GradingPeriodsApi->grading_periods_destroy_for_accounts: %s\n" % e)
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
**0** | Delete a grading period |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grading_periods_index**
> grading_periods_index(account_id)

List grading periods

Returns the paginated list of grading periods for the current course.

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
    api_instance = canvas_lms_python_client.GradingPeriodsApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id

    try:
        # List grading periods
        await api_instance.grading_periods_index(account_id)
    except Exception as e:
        print("Exception when calling GradingPeriodsApi->grading_periods_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 

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
**0** | List grading periods |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grading_periods_index_for_courses**
> grading_periods_index_for_courses(course_id)

List grading periods

Returns the paginated list of grading periods for the current course.

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
    api_instance = canvas_lms_python_client.GradingPeriodsApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id

    try:
        # List grading periods
        await api_instance.grading_periods_index_for_courses(course_id)
    except Exception as e:
        print("Exception when calling GradingPeriodsApi->grading_periods_index_for_courses: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 

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
**0** | List grading periods |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grading_periods_show**
> grading_periods_show(course_id, id)

Get a single grading period

Returns the grading period with the given id

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
    api_instance = canvas_lms_python_client.GradingPeriodsApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    id = 'id_example' # str | Scope response to id

    try:
        # Get a single grading period
        await api_instance.grading_periods_show(course_id, id)
    except Exception as e:
        print("Exception when calling GradingPeriodsApi->grading_periods_show: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **id** | **str**| Scope response to id | 

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
**0** | Get a single grading period |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grading_periods_update**
> grading_periods_update(course_id, id, grading_periods_update_request=grading_periods_update_request)

Update a single grading period

Update an existing grading period.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.grading_periods_update_request import GradingPeriodsUpdateRequest
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
    api_instance = canvas_lms_python_client.GradingPeriodsApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    id = 'id_example' # str | Scope response to id
    grading_periods_update_request = canvas_lms_python_client.GradingPeriodsUpdateRequest() # GradingPeriodsUpdateRequest | Request body parameters (optional)

    try:
        # Update a single grading period
        await api_instance.grading_periods_update(course_id, id, grading_periods_update_request=grading_periods_update_request)
    except Exception as e:
        print("Exception when calling GradingPeriodsApi->grading_periods_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **id** | **str**| Scope response to id | 
 **grading_periods_update_request** | [**GradingPeriodsUpdateRequest**](GradingPeriodsUpdateRequest.md)| Request body parameters | [optional] 

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
**0** | Update a single grading period |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

