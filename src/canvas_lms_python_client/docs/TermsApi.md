# canvas_lms_python_client.TermsApi

All URIs are relative to *https://canvas.instructure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**terms_create**](TermsApi.md#terms_create) | **POST** /api/v1/accounts/{account_id}/terms | Create enrollment term
[**terms_destroy**](TermsApi.md#terms_destroy) | **DELETE** /api/v1/accounts/{account_id}/terms/{id} | Delete enrollment term
[**terms_update**](TermsApi.md#terms_update) | **PUT** /api/v1/accounts/{account_id}/terms/{id} | Update enrollment term


# **terms_create**
> EnrollmentTerm terms_create(account_id, terms_create_request=terms_create_request)

Create enrollment term

Create a new enrollment term for the specified account.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.enrollment_term import EnrollmentTerm
from canvas_lms_python_client.models.terms_create_request import TermsCreateRequest
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
    api_instance = canvas_lms_python_client.TermsApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    terms_create_request = canvas_lms_python_client.TermsCreateRequest() # TermsCreateRequest | Request body parameters (optional)

    try:
        # Create enrollment term
        api_response = await api_instance.terms_create(account_id, terms_create_request=terms_create_request)
        print("The response of TermsApi->terms_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TermsApi->terms_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **terms_create_request** | [**TermsCreateRequest**](TermsCreateRequest.md)| Request body parameters | [optional] 

### Return type

[**EnrollmentTerm**](EnrollmentTerm.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | EnrollmentTerm |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **terms_destroy**
> EnrollmentTerm terms_destroy(account_id, id)

Delete enrollment term

Delete the specified enrollment term.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.enrollment_term import EnrollmentTerm
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
    api_instance = canvas_lms_python_client.TermsApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    id = 'id_example' # str | Scope response to id

    try:
        # Delete enrollment term
        api_response = await api_instance.terms_destroy(account_id, id)
        print("The response of TermsApi->terms_destroy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TermsApi->terms_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **id** | **str**| Scope response to id | 

### Return type

[**EnrollmentTerm**](EnrollmentTerm.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | EnrollmentTerm |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **terms_update**
> EnrollmentTerm terms_update(account_id, id, terms_update_request=terms_update_request)

Update enrollment term

Update an existing enrollment term for the specified account.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.enrollment_term import EnrollmentTerm
from canvas_lms_python_client.models.terms_update_request import TermsUpdateRequest
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
    api_instance = canvas_lms_python_client.TermsApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    id = 'id_example' # str | Scope response to id
    terms_update_request = canvas_lms_python_client.TermsUpdateRequest() # TermsUpdateRequest | Request body parameters (optional)

    try:
        # Update enrollment term
        api_response = await api_instance.terms_update(account_id, id, terms_update_request=terms_update_request)
        print("The response of TermsApi->terms_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TermsApi->terms_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **id** | **str**| Scope response to id | 
 **terms_update_request** | [**TermsUpdateRequest**](TermsUpdateRequest.md)| Request body parameters | [optional] 

### Return type

[**EnrollmentTerm**](EnrollmentTerm.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | EnrollmentTerm |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

