# canvas_lms_python_client.EportfoliosApiApi

All URIs are relative to *https://canvas.instructure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**eportfolios_api_delete**](EportfoliosApiApi.md#eportfolios_api_delete) | **DELETE** /api/v1/eportfolios/{id} | Delete an ePortfolio
[**eportfolios_api_index**](EportfoliosApiApi.md#eportfolios_api_index) | **GET** /api/v1/users/{user_id}/eportfolios | Get all ePortfolios for a User
[**eportfolios_api_moderate**](EportfoliosApiApi.md#eportfolios_api_moderate) | **PUT** /api/v1/eportfolios/{eportfolio_id}/moderate | Moderate an ePortfolio
[**eportfolios_api_moderate_all**](EportfoliosApiApi.md#eportfolios_api_moderate_all) | **PUT** /api/v1/users/{user_id}/eportfolios | Moderate all ePortfolios for a User
[**eportfolios_api_pages**](EportfoliosApiApi.md#eportfolios_api_pages) | **GET** /api/v1/eportfolios/{eportfolio_id}/pages | Get ePortfolio Pages
[**eportfolios_api_restore**](EportfoliosApiApi.md#eportfolios_api_restore) | **PUT** /api/v1/eportfolios/{eportfolio_id}/restore | Restore a deleted ePortfolio
[**eportfolios_api_show**](EportfoliosApiApi.md#eportfolios_api_show) | **GET** /api/v1/eportfolios/{id} | Get an ePortfolio


# **eportfolios_api_delete**
> EPortfolio eportfolios_api_delete(id)

Delete an ePortfolio

Mark an ePortfolio as deleted.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.e_portfolio import EPortfolio
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
    api_instance = canvas_lms_python_client.EportfoliosApiApi(api_client)
    id = 'id_example' # str | Scope response to id

    try:
        # Delete an ePortfolio
        api_response = await api_instance.eportfolios_api_delete(id)
        print("The response of EportfoliosApiApi->eportfolios_api_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EportfoliosApiApi->eportfolios_api_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Scope response to id | 

### Return type

[**EPortfolio**](EPortfolio.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | ePortfolio |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **eportfolios_api_index**
> List[EPortfolio] eportfolios_api_index(user_id, include=include, page=page, per_page=per_page)

Get all ePortfolios for a User

Get a list of all ePortfolios for the specified user.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.e_portfolio import EPortfolio
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
    api_instance = canvas_lms_python_client.EportfoliosApiApi(api_client)
    user_id = 'user_id_example' # str | Scope response to user_id
    include = ['include_example'] # List[str] | deleted:: Include deleted ePortfolios. Only available to admins who can moderate_user_content. (optional)
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # Get all ePortfolios for a User
        api_response = await api_instance.eportfolios_api_index(user_id, include=include, page=page, per_page=per_page)
        print("The response of EportfoliosApiApi->eportfolios_api_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EportfoliosApiApi->eportfolios_api_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| Scope response to user_id | 
 **include** | [**List[str]**](str.md)| deleted:: Include deleted ePortfolios. Only available to admins who can moderate_user_content. | [optional] 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**List[EPortfolio]**](EPortfolio.md)

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

# **eportfolios_api_moderate**
> EPortfolio eportfolios_api_moderate(eportfolio_id, eportfolios_api_moderate_request=eportfolios_api_moderate_request)

Moderate an ePortfolio

Update the spam_status of an eportfolio. Only available to admins who can
moderate_user_content.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.e_portfolio import EPortfolio
from canvas_lms_python_client.models.eportfolios_api_moderate_request import EportfoliosApiModerateRequest
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
    api_instance = canvas_lms_python_client.EportfoliosApiApi(api_client)
    eportfolio_id = 'eportfolio_id_example' # str | Scope response to eportfolio_id
    eportfolios_api_moderate_request = canvas_lms_python_client.EportfoliosApiModerateRequest() # EportfoliosApiModerateRequest | Request body parameters (optional)

    try:
        # Moderate an ePortfolio
        api_response = await api_instance.eportfolios_api_moderate(eportfolio_id, eportfolios_api_moderate_request=eportfolios_api_moderate_request)
        print("The response of EportfoliosApiApi->eportfolios_api_moderate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EportfoliosApiApi->eportfolios_api_moderate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **eportfolio_id** | **str**| Scope response to eportfolio_id | 
 **eportfolios_api_moderate_request** | [**EportfoliosApiModerateRequest**](EportfoliosApiModerateRequest.md)| Request body parameters | [optional] 

### Return type

[**EPortfolio**](EPortfolio.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | ePortfolio |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **eportfolios_api_moderate_all**
> eportfolios_api_moderate_all(user_id, eportfolios_api_moderate_all_request=eportfolios_api_moderate_all_request)

Moderate all ePortfolios for a User

Update the spam_status for all active eportfolios of a user. Only available to
admins who can moderate_user_content.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.eportfolios_api_moderate_all_request import EportfoliosApiModerateAllRequest
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
    api_instance = canvas_lms_python_client.EportfoliosApiApi(api_client)
    user_id = 'user_id_example' # str | Scope response to user_id
    eportfolios_api_moderate_all_request = canvas_lms_python_client.EportfoliosApiModerateAllRequest() # EportfoliosApiModerateAllRequest | Request body parameters (optional)

    try:
        # Moderate all ePortfolios for a User
        await api_instance.eportfolios_api_moderate_all(user_id, eportfolios_api_moderate_all_request=eportfolios_api_moderate_all_request)
    except Exception as e:
        print("Exception when calling EportfoliosApiApi->eportfolios_api_moderate_all: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| Scope response to user_id | 
 **eportfolios_api_moderate_all_request** | [**EportfoliosApiModerateAllRequest**](EportfoliosApiModerateAllRequest.md)| Request body parameters | [optional] 

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
**0** | Moderate all ePortfolios for a User |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **eportfolios_api_pages**
> List[EPortfolioPage] eportfolios_api_pages(eportfolio_id, page=page, per_page=per_page)

Get ePortfolio Pages

Get details for the pages of an ePortfolio

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.e_portfolio_page import EPortfolioPage
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
    api_instance = canvas_lms_python_client.EportfoliosApiApi(api_client)
    eportfolio_id = 'eportfolio_id_example' # str | Scope response to eportfolio_id
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # Get ePortfolio Pages
        api_response = await api_instance.eportfolios_api_pages(eportfolio_id, page=page, per_page=per_page)
        print("The response of EportfoliosApiApi->eportfolios_api_pages:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EportfoliosApiApi->eportfolios_api_pages: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **eportfolio_id** | **str**| Scope response to eportfolio_id | 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**List[EPortfolioPage]**](EPortfolioPage.md)

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

# **eportfolios_api_restore**
> EPortfolio eportfolios_api_restore(eportfolio_id)

Restore a deleted ePortfolio

Restore an ePortfolio back to active that was previously deleted. Only
available to admins who can moderate_user_content.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.e_portfolio import EPortfolio
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
    api_instance = canvas_lms_python_client.EportfoliosApiApi(api_client)
    eportfolio_id = 'eportfolio_id_example' # str | Scope response to eportfolio_id

    try:
        # Restore a deleted ePortfolio
        api_response = await api_instance.eportfolios_api_restore(eportfolio_id)
        print("The response of EportfoliosApiApi->eportfolios_api_restore:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EportfoliosApiApi->eportfolios_api_restore: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **eportfolio_id** | **str**| Scope response to eportfolio_id | 

### Return type

[**EPortfolio**](EPortfolio.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | ePortfolio |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **eportfolios_api_show**
> EPortfolio eportfolios_api_show(id)

Get an ePortfolio

Get details for a single ePortfolio.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.e_portfolio import EPortfolio
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
    api_instance = canvas_lms_python_client.EportfoliosApiApi(api_client)
    id = 'id_example' # str | Scope response to id

    try:
        # Get an ePortfolio
        api_response = await api_instance.eportfolios_api_show(id)
        print("The response of EportfoliosApiApi->eportfolios_api_show:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EportfoliosApiApi->eportfolios_api_show: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Scope response to id | 

### Return type

[**EPortfolio**](EPortfolio.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | ePortfolio |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

