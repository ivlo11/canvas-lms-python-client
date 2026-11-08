# canvas_lms_python_client.TemporaryEnrollmentPairingsApiApi

All URIs are relative to *https://canvas.instructure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**temporary_enrollment_pairings_api_create**](TemporaryEnrollmentPairingsApiApi.md#temporary_enrollment_pairings_api_create) | **POST** /api/v1/accounts/{account_id}/temporary_enrollment_pairings | Create Temporary Enrollment Pairing
[**temporary_enrollment_pairings_api_destroy**](TemporaryEnrollmentPairingsApiApi.md#temporary_enrollment_pairings_api_destroy) | **DELETE** /api/v1/accounts/{account_id}/temporary_enrollment_pairings/{id} | Delete Temporary Enrollment Pairing
[**temporary_enrollment_pairings_api_index**](TemporaryEnrollmentPairingsApiApi.md#temporary_enrollment_pairings_api_index) | **GET** /api/v1/accounts/{account_id}/temporary_enrollment_pairings | List temporary enrollment pairings
[**temporary_enrollment_pairings_api_new**](TemporaryEnrollmentPairingsApiApi.md#temporary_enrollment_pairings_api_new) | **GET** /api/v1/accounts/{account_id}/temporary_enrollment_pairings/new | New TemporaryEnrollmentPairing
[**temporary_enrollment_pairings_api_show**](TemporaryEnrollmentPairingsApiApi.md#temporary_enrollment_pairings_api_show) | **GET** /api/v1/accounts/{account_id}/temporary_enrollment_pairings/{id} | Get a single temporary enrollment pairing


# **temporary_enrollment_pairings_api_create**
> TemporaryEnrollmentPairingsApiCreateResponse temporary_enrollment_pairings_api_create(account_id, temporary_enrollment_pairings_api_create_request=temporary_enrollment_pairings_api_create_request)

Create Temporary Enrollment Pairing

Create a Temporary Enrollment Pairing.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.temporary_enrollment_pairings_api_create_request import TemporaryEnrollmentPairingsApiCreateRequest
from canvas_lms_python_client.models.temporary_enrollment_pairings_api_create_response import TemporaryEnrollmentPairingsApiCreateResponse
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
    api_instance = canvas_lms_python_client.TemporaryEnrollmentPairingsApiApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    temporary_enrollment_pairings_api_create_request = canvas_lms_python_client.TemporaryEnrollmentPairingsApiCreateRequest() # TemporaryEnrollmentPairingsApiCreateRequest | Request body parameters (optional)

    try:
        # Create Temporary Enrollment Pairing
        api_response = await api_instance.temporary_enrollment_pairings_api_create(account_id, temporary_enrollment_pairings_api_create_request=temporary_enrollment_pairings_api_create_request)
        print("The response of TemporaryEnrollmentPairingsApiApi->temporary_enrollment_pairings_api_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemporaryEnrollmentPairingsApiApi->temporary_enrollment_pairings_api_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **temporary_enrollment_pairings_api_create_request** | [**TemporaryEnrollmentPairingsApiCreateRequest**](TemporaryEnrollmentPairingsApiCreateRequest.md)| Request body parameters | [optional] 

### Return type

[**TemporaryEnrollmentPairingsApiCreateResponse**](TemporaryEnrollmentPairingsApiCreateResponse.md)

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

# **temporary_enrollment_pairings_api_destroy**
> TemporaryEnrollmentPairing temporary_enrollment_pairings_api_destroy(account_id, id)

Delete Temporary Enrollment Pairing

Delete a temporary enrollment pairing

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.temporary_enrollment_pairing import TemporaryEnrollmentPairing
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
    api_instance = canvas_lms_python_client.TemporaryEnrollmentPairingsApiApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    id = 'id_example' # str | Scope response to id

    try:
        # Delete Temporary Enrollment Pairing
        api_response = await api_instance.temporary_enrollment_pairings_api_destroy(account_id, id)
        print("The response of TemporaryEnrollmentPairingsApiApi->temporary_enrollment_pairings_api_destroy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemporaryEnrollmentPairingsApiApi->temporary_enrollment_pairings_api_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **id** | **str**| Scope response to id | 

### Return type

[**TemporaryEnrollmentPairing**](TemporaryEnrollmentPairing.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | TemporaryEnrollmentPairing |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **temporary_enrollment_pairings_api_index**
> List[TemporaryEnrollmentPairing] temporary_enrollment_pairings_api_index(account_id)

List temporary enrollment pairings

Returns the list of temporary enrollment pairings for a root account.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.temporary_enrollment_pairing import TemporaryEnrollmentPairing
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
    api_instance = canvas_lms_python_client.TemporaryEnrollmentPairingsApiApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id

    try:
        # List temporary enrollment pairings
        api_response = await api_instance.temporary_enrollment_pairings_api_index(account_id)
        print("The response of TemporaryEnrollmentPairingsApiApi->temporary_enrollment_pairings_api_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemporaryEnrollmentPairingsApiApi->temporary_enrollment_pairings_api_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 

### Return type

[**List[TemporaryEnrollmentPairing]**](TemporaryEnrollmentPairing.md)

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

# **temporary_enrollment_pairings_api_new**
> TemporaryEnrollmentPairingsApiNewResponse temporary_enrollment_pairings_api_new(account_id)

New TemporaryEnrollmentPairing

Initialize an unsaved Temporary Enrollment Pairing.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.temporary_enrollment_pairings_api_new_response import TemporaryEnrollmentPairingsApiNewResponse
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
    api_instance = canvas_lms_python_client.TemporaryEnrollmentPairingsApiApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id

    try:
        # New TemporaryEnrollmentPairing
        api_response = await api_instance.temporary_enrollment_pairings_api_new(account_id)
        print("The response of TemporaryEnrollmentPairingsApiApi->temporary_enrollment_pairings_api_new:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemporaryEnrollmentPairingsApiApi->temporary_enrollment_pairings_api_new: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 

### Return type

[**TemporaryEnrollmentPairingsApiNewResponse**](TemporaryEnrollmentPairingsApiNewResponse.md)

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

# **temporary_enrollment_pairings_api_show**
> TemporaryEnrollmentPairingsApiShowResponse temporary_enrollment_pairings_api_show(account_id, id)

Get a single temporary enrollment pairing

Returns the temporary enrollment pairing with the given id.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.temporary_enrollment_pairings_api_show_response import TemporaryEnrollmentPairingsApiShowResponse
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
    api_instance = canvas_lms_python_client.TemporaryEnrollmentPairingsApiApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    id = 'id_example' # str | Scope response to id

    try:
        # Get a single temporary enrollment pairing
        api_response = await api_instance.temporary_enrollment_pairings_api_show(account_id, id)
        print("The response of TemporaryEnrollmentPairingsApiApi->temporary_enrollment_pairings_api_show:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemporaryEnrollmentPairingsApiApi->temporary_enrollment_pairings_api_show: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **id** | **str**| Scope response to id | 

### Return type

[**TemporaryEnrollmentPairingsApiShowResponse**](TemporaryEnrollmentPairingsApiShowResponse.md)

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

