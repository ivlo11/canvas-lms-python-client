# canvas_lms_python_client.BlackoutDatesApi

All URIs are relative to *https://canvas.instructure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**blackout_dates_bulk_update**](BlackoutDatesApi.md#blackout_dates_bulk_update) | **PUT** /api/v1/courses/{course_id}/blackout_dates | Update a list of Blackout Dates
[**blackout_dates_create**](BlackoutDatesApi.md#blackout_dates_create) | **POST** /api/v1/courses/{course_id}/blackout_dates | Create Blackout Date
[**blackout_dates_create_for_accounts**](BlackoutDatesApi.md#blackout_dates_create_for_accounts) | **POST** /api/v1/accounts/{account_id}/blackout_dates | Create Blackout Date
[**blackout_dates_destroy**](BlackoutDatesApi.md#blackout_dates_destroy) | **DELETE** /api/v1/courses/{course_id}/blackout_dates/{id} | Delete Blackout Date
[**blackout_dates_destroy_for_accounts**](BlackoutDatesApi.md#blackout_dates_destroy_for_accounts) | **DELETE** /api/v1/accounts/{account_id}/blackout_dates/{id} | Delete Blackout Date
[**blackout_dates_index**](BlackoutDatesApi.md#blackout_dates_index) | **GET** /api/v1/courses/{course_id}/blackout_dates | List blackout dates
[**blackout_dates_index_for_accounts**](BlackoutDatesApi.md#blackout_dates_index_for_accounts) | **GET** /api/v1/accounts/{account_id}/blackout_dates | List blackout dates
[**blackout_dates_new**](BlackoutDatesApi.md#blackout_dates_new) | **GET** /api/v1/courses/{course_id}/blackout_dates/new | New Blackout Date
[**blackout_dates_new_for_accounts**](BlackoutDatesApi.md#blackout_dates_new_for_accounts) | **GET** /api/v1/accounts/{account_id}/blackout_dates/new | New Blackout Date
[**blackout_dates_show**](BlackoutDatesApi.md#blackout_dates_show) | **GET** /api/v1/courses/{course_id}/blackout_dates/{id} | Get a single blackout date
[**blackout_dates_show_for_accounts**](BlackoutDatesApi.md#blackout_dates_show_for_accounts) | **GET** /api/v1/accounts/{account_id}/blackout_dates/{id} | Get a single blackout date
[**blackout_dates_update**](BlackoutDatesApi.md#blackout_dates_update) | **PUT** /api/v1/courses/{course_id}/blackout_dates/{id} | Update Blackout Date
[**blackout_dates_update_for_accounts**](BlackoutDatesApi.md#blackout_dates_update_for_accounts) | **PUT** /api/v1/accounts/{account_id}/blackout_dates/{id} | Update Blackout Date


# **blackout_dates_bulk_update**
> List[BlackoutDate] blackout_dates_bulk_update(course_id, blackout_dates_bulk_update_request=blackout_dates_bulk_update_request)

Update a list of Blackout Dates

Create, update, and delete blackout dates to sync the db with the incoming data.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.blackout_date import BlackoutDate
from canvas_lms_python_client.models.blackout_dates_bulk_update_request import BlackoutDatesBulkUpdateRequest
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
    api_instance = canvas_lms_python_client.BlackoutDatesApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    blackout_dates_bulk_update_request = canvas_lms_python_client.BlackoutDatesBulkUpdateRequest() # BlackoutDatesBulkUpdateRequest | Request body parameters (optional)

    try:
        # Update a list of Blackout Dates
        api_response = await api_instance.blackout_dates_bulk_update(course_id, blackout_dates_bulk_update_request=blackout_dates_bulk_update_request)
        print("The response of BlackoutDatesApi->blackout_dates_bulk_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BlackoutDatesApi->blackout_dates_bulk_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **blackout_dates_bulk_update_request** | [**BlackoutDatesBulkUpdateRequest**](BlackoutDatesBulkUpdateRequest.md)| Request body parameters | [optional] 

### Return type

[**List[BlackoutDate]**](BlackoutDate.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | The result (which should match the input with maybe some different IDs). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **blackout_dates_create**
> BlackoutDatesCreateResponse blackout_dates_create(course_id, blackout_dates_create_request=blackout_dates_create_request)

Create Blackout Date

Create a blackout date for the given context.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.blackout_dates_create_request import BlackoutDatesCreateRequest
from canvas_lms_python_client.models.blackout_dates_create_response import BlackoutDatesCreateResponse
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
    api_instance = canvas_lms_python_client.BlackoutDatesApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    blackout_dates_create_request = canvas_lms_python_client.BlackoutDatesCreateRequest() # BlackoutDatesCreateRequest | Request body parameters (optional)

    try:
        # Create Blackout Date
        api_response = await api_instance.blackout_dates_create(course_id, blackout_dates_create_request=blackout_dates_create_request)
        print("The response of BlackoutDatesApi->blackout_dates_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BlackoutDatesApi->blackout_dates_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **blackout_dates_create_request** | [**BlackoutDatesCreateRequest**](BlackoutDatesCreateRequest.md)| Request body parameters | [optional] 

### Return type

[**BlackoutDatesCreateResponse**](BlackoutDatesCreateResponse.md)

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

# **blackout_dates_create_for_accounts**
> BlackoutDatesCreateResponse blackout_dates_create_for_accounts(account_id, blackout_dates_create_request=blackout_dates_create_request)

Create Blackout Date

Create a blackout date for the given context.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.blackout_dates_create_request import BlackoutDatesCreateRequest
from canvas_lms_python_client.models.blackout_dates_create_response import BlackoutDatesCreateResponse
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
    api_instance = canvas_lms_python_client.BlackoutDatesApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    blackout_dates_create_request = canvas_lms_python_client.BlackoutDatesCreateRequest() # BlackoutDatesCreateRequest | Request body parameters (optional)

    try:
        # Create Blackout Date
        api_response = await api_instance.blackout_dates_create_for_accounts(account_id, blackout_dates_create_request=blackout_dates_create_request)
        print("The response of BlackoutDatesApi->blackout_dates_create_for_accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BlackoutDatesApi->blackout_dates_create_for_accounts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **blackout_dates_create_request** | [**BlackoutDatesCreateRequest**](BlackoutDatesCreateRequest.md)| Request body parameters | [optional] 

### Return type

[**BlackoutDatesCreateResponse**](BlackoutDatesCreateResponse.md)

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

# **blackout_dates_destroy**
> BlackoutDate blackout_dates_destroy(course_id, id)

Delete Blackout Date

Delete a blackout date for the given context.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.blackout_date import BlackoutDate
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
    api_instance = canvas_lms_python_client.BlackoutDatesApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    id = 'id_example' # str | Scope response to id

    try:
        # Delete Blackout Date
        api_response = await api_instance.blackout_dates_destroy(course_id, id)
        print("The response of BlackoutDatesApi->blackout_dates_destroy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BlackoutDatesApi->blackout_dates_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **id** | **str**| Scope response to id | 

### Return type

[**BlackoutDate**](BlackoutDate.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | BlackoutDate |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **blackout_dates_destroy_for_accounts**
> BlackoutDate blackout_dates_destroy_for_accounts(account_id, id)

Delete Blackout Date

Delete a blackout date for the given context.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.blackout_date import BlackoutDate
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
    api_instance = canvas_lms_python_client.BlackoutDatesApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    id = 'id_example' # str | Scope response to id

    try:
        # Delete Blackout Date
        api_response = await api_instance.blackout_dates_destroy_for_accounts(account_id, id)
        print("The response of BlackoutDatesApi->blackout_dates_destroy_for_accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BlackoutDatesApi->blackout_dates_destroy_for_accounts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **id** | **str**| Scope response to id | 

### Return type

[**BlackoutDate**](BlackoutDate.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | BlackoutDate |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **blackout_dates_index**
> List[BlackoutDate] blackout_dates_index(course_id)

List blackout dates

Returns the list of blackout dates for the current context.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.blackout_date import BlackoutDate
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
    api_instance = canvas_lms_python_client.BlackoutDatesApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id

    try:
        # List blackout dates
        api_response = await api_instance.blackout_dates_index(course_id)
        print("The response of BlackoutDatesApi->blackout_dates_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BlackoutDatesApi->blackout_dates_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 

### Return type

[**List[BlackoutDate]**](BlackoutDate.md)

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

# **blackout_dates_index_for_accounts**
> List[BlackoutDate] blackout_dates_index_for_accounts(account_id)

List blackout dates

Returns the list of blackout dates for the current context.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.blackout_date import BlackoutDate
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
    api_instance = canvas_lms_python_client.BlackoutDatesApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id

    try:
        # List blackout dates
        api_response = await api_instance.blackout_dates_index_for_accounts(account_id)
        print("The response of BlackoutDatesApi->blackout_dates_index_for_accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BlackoutDatesApi->blackout_dates_index_for_accounts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 

### Return type

[**List[BlackoutDate]**](BlackoutDate.md)

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

# **blackout_dates_new**
> BlackoutDatesNewResponse blackout_dates_new(course_id)

New Blackout Date

Initialize an unsaved Blackout Date for the given context.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.blackout_dates_new_response import BlackoutDatesNewResponse
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
    api_instance = canvas_lms_python_client.BlackoutDatesApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id

    try:
        # New Blackout Date
        api_response = await api_instance.blackout_dates_new(course_id)
        print("The response of BlackoutDatesApi->blackout_dates_new:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BlackoutDatesApi->blackout_dates_new: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 

### Return type

[**BlackoutDatesNewResponse**](BlackoutDatesNewResponse.md)

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

# **blackout_dates_new_for_accounts**
> BlackoutDatesNewResponse blackout_dates_new_for_accounts(account_id)

New Blackout Date

Initialize an unsaved Blackout Date for the given context.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.blackout_dates_new_response import BlackoutDatesNewResponse
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
    api_instance = canvas_lms_python_client.BlackoutDatesApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id

    try:
        # New Blackout Date
        api_response = await api_instance.blackout_dates_new_for_accounts(account_id)
        print("The response of BlackoutDatesApi->blackout_dates_new_for_accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BlackoutDatesApi->blackout_dates_new_for_accounts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 

### Return type

[**BlackoutDatesNewResponse**](BlackoutDatesNewResponse.md)

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

# **blackout_dates_show**
> BlackoutDatesShowResponse blackout_dates_show(course_id, id)

Get a single blackout date

Returns the blackout date with the given id.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.blackout_dates_show_response import BlackoutDatesShowResponse
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
    api_instance = canvas_lms_python_client.BlackoutDatesApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    id = 'id_example' # str | Scope response to id

    try:
        # Get a single blackout date
        api_response = await api_instance.blackout_dates_show(course_id, id)
        print("The response of BlackoutDatesApi->blackout_dates_show:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BlackoutDatesApi->blackout_dates_show: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **id** | **str**| Scope response to id | 

### Return type

[**BlackoutDatesShowResponse**](BlackoutDatesShowResponse.md)

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

# **blackout_dates_show_for_accounts**
> BlackoutDatesShowResponse blackout_dates_show_for_accounts(account_id, id)

Get a single blackout date

Returns the blackout date with the given id.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.blackout_dates_show_response import BlackoutDatesShowResponse
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
    api_instance = canvas_lms_python_client.BlackoutDatesApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    id = 'id_example' # str | Scope response to id

    try:
        # Get a single blackout date
        api_response = await api_instance.blackout_dates_show_for_accounts(account_id, id)
        print("The response of BlackoutDatesApi->blackout_dates_show_for_accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BlackoutDatesApi->blackout_dates_show_for_accounts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **id** | **str**| Scope response to id | 

### Return type

[**BlackoutDatesShowResponse**](BlackoutDatesShowResponse.md)

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

# **blackout_dates_update**
> BlackoutDatesUpdateResponse blackout_dates_update(course_id, id, blackout_dates_create_request=blackout_dates_create_request)

Update Blackout Date

Update a blackout date for the given context.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.blackout_dates_create_request import BlackoutDatesCreateRequest
from canvas_lms_python_client.models.blackout_dates_update_response import BlackoutDatesUpdateResponse
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
    api_instance = canvas_lms_python_client.BlackoutDatesApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    id = 'id_example' # str | Scope response to id
    blackout_dates_create_request = canvas_lms_python_client.BlackoutDatesCreateRequest() # BlackoutDatesCreateRequest | Request body parameters (optional)

    try:
        # Update Blackout Date
        api_response = await api_instance.blackout_dates_update(course_id, id, blackout_dates_create_request=blackout_dates_create_request)
        print("The response of BlackoutDatesApi->blackout_dates_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BlackoutDatesApi->blackout_dates_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **id** | **str**| Scope response to id | 
 **blackout_dates_create_request** | [**BlackoutDatesCreateRequest**](BlackoutDatesCreateRequest.md)| Request body parameters | [optional] 

### Return type

[**BlackoutDatesUpdateResponse**](BlackoutDatesUpdateResponse.md)

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

# **blackout_dates_update_for_accounts**
> BlackoutDatesUpdateResponse blackout_dates_update_for_accounts(account_id, id, blackout_dates_create_request=blackout_dates_create_request)

Update Blackout Date

Update a blackout date for the given context.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.blackout_dates_create_request import BlackoutDatesCreateRequest
from canvas_lms_python_client.models.blackout_dates_update_response import BlackoutDatesUpdateResponse
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
    api_instance = canvas_lms_python_client.BlackoutDatesApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    id = 'id_example' # str | Scope response to id
    blackout_dates_create_request = canvas_lms_python_client.BlackoutDatesCreateRequest() # BlackoutDatesCreateRequest | Request body parameters (optional)

    try:
        # Update Blackout Date
        api_response = await api_instance.blackout_dates_update_for_accounts(account_id, id, blackout_dates_create_request=blackout_dates_create_request)
        print("The response of BlackoutDatesApi->blackout_dates_update_for_accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BlackoutDatesApi->blackout_dates_update_for_accounts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **id** | **str**| Scope response to id | 
 **blackout_dates_create_request** | [**BlackoutDatesCreateRequest**](BlackoutDatesCreateRequest.md)| Request body parameters | [optional] 

### Return type

[**BlackoutDatesUpdateResponse**](BlackoutDatesUpdateResponse.md)

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

