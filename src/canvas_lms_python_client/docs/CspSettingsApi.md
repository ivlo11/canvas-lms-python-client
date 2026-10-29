# canvas_lms_python_client.CspSettingsApi

All URIs are relative to *https://canvas.instructure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**csp_settings_add_domain**](CspSettingsApi.md#csp_settings_add_domain) | **POST** /api/v1/accounts/{account_id}/csp_settings/domains | Add an allowed domain to account
[**csp_settings_add_multiple_domains**](CspSettingsApi.md#csp_settings_add_multiple_domains) | **POST** /api/v1/accounts/{account_id}/csp_settings/domains/batch_create | Add multiple allowed domains to an account
[**csp_settings_get_csp_settings**](CspSettingsApi.md#csp_settings_get_csp_settings) | **GET** /api/v1/courses/{course_id}/csp_settings | Get current settings for account or course
[**csp_settings_get_csp_settings_for_accounts**](CspSettingsApi.md#csp_settings_get_csp_settings_for_accounts) | **GET** /api/v1/accounts/{account_id}/csp_settings | Get current settings for account or course
[**csp_settings_remove_domain**](CspSettingsApi.md#csp_settings_remove_domain) | **DELETE** /api/v1/accounts/{account_id}/csp_settings/domains | Remove a domain from account
[**csp_settings_set_csp_lock**](CspSettingsApi.md#csp_settings_set_csp_lock) | **PUT** /api/v1/accounts/{account_id}/csp_settings/lock | Lock or unlock current CSP settings for sub-accounts and courses
[**csp_settings_set_csp_setting**](CspSettingsApi.md#csp_settings_set_csp_setting) | **PUT** /api/v1/courses/{course_id}/csp_settings | Enable, disable, or clear explicit CSP setting
[**csp_settings_set_csp_setting_for_accounts**](CspSettingsApi.md#csp_settings_set_csp_setting_for_accounts) | **PUT** /api/v1/accounts/{account_id}/csp_settings | Enable, disable, or clear explicit CSP setting


# **csp_settings_add_domain**
> csp_settings_add_domain(account_id, csp_settings_add_domain_request=csp_settings_add_domain_request)

Add an allowed domain to account

Adds an allowed domain for the current account. Note: this will not take effect
unless CSP is explicitly enabled on this account.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.csp_settings_add_domain_request import CspSettingsAddDomainRequest
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
    api_instance = canvas_lms_python_client.CspSettingsApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    csp_settings_add_domain_request = canvas_lms_python_client.CspSettingsAddDomainRequest() # CspSettingsAddDomainRequest | Request body parameters (optional)

    try:
        # Add an allowed domain to account
        await api_instance.csp_settings_add_domain(account_id, csp_settings_add_domain_request=csp_settings_add_domain_request)
    except Exception as e:
        print("Exception when calling CspSettingsApi->csp_settings_add_domain: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **csp_settings_add_domain_request** | [**CspSettingsAddDomainRequest**](CspSettingsAddDomainRequest.md)| Request body parameters | [optional] 

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
**0** | Add an allowed domain to account |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **csp_settings_add_multiple_domains**
> csp_settings_add_multiple_domains(account_id, csp_settings_add_multiple_domains_request=csp_settings_add_multiple_domains_request)

Add multiple allowed domains to an account

Adds multiple allowed domains for the current account. Note: this will not take effect
unless CSP is explicitly enabled on this account.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.csp_settings_add_multiple_domains_request import CspSettingsAddMultipleDomainsRequest
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
    api_instance = canvas_lms_python_client.CspSettingsApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    csp_settings_add_multiple_domains_request = canvas_lms_python_client.CspSettingsAddMultipleDomainsRequest() # CspSettingsAddMultipleDomainsRequest | Request body parameters (optional)

    try:
        # Add multiple allowed domains to an account
        await api_instance.csp_settings_add_multiple_domains(account_id, csp_settings_add_multiple_domains_request=csp_settings_add_multiple_domains_request)
    except Exception as e:
        print("Exception when calling CspSettingsApi->csp_settings_add_multiple_domains: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **csp_settings_add_multiple_domains_request** | [**CspSettingsAddMultipleDomainsRequest**](CspSettingsAddMultipleDomainsRequest.md)| Request body parameters | [optional] 

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
**0** | Add multiple allowed domains to an account |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **csp_settings_get_csp_settings**
> csp_settings_get_csp_settings(course_id)

Get current settings for account or course

Update multiple modules in an account.

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
    api_instance = canvas_lms_python_client.CspSettingsApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id

    try:
        # Get current settings for account or course
        await api_instance.csp_settings_get_csp_settings(course_id)
    except Exception as e:
        print("Exception when calling CspSettingsApi->csp_settings_get_csp_settings: %s\n" % e)
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
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Get current settings for account or course |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **csp_settings_get_csp_settings_for_accounts**
> csp_settings_get_csp_settings_for_accounts(account_id)

Get current settings for account or course

Update multiple modules in an account.

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
    api_instance = canvas_lms_python_client.CspSettingsApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id

    try:
        # Get current settings for account or course
        await api_instance.csp_settings_get_csp_settings_for_accounts(account_id)
    except Exception as e:
        print("Exception when calling CspSettingsApi->csp_settings_get_csp_settings_for_accounts: %s\n" % e)
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
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Get current settings for account or course |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **csp_settings_remove_domain**
> csp_settings_remove_domain(account_id, domain)

Remove a domain from account

Removes an allowed domain from the current account.

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
    api_instance = canvas_lms_python_client.CspSettingsApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    domain = 'domain_example' # str | 

    try:
        # Remove a domain from account
        await api_instance.csp_settings_remove_domain(account_id, domain)
    except Exception as e:
        print("Exception when calling CspSettingsApi->csp_settings_remove_domain: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **domain** | **str**|  | 

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
**0** | Remove a domain from account |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **csp_settings_set_csp_lock**
> csp_settings_set_csp_lock(account_id, csp_settings_set_csp_lock_request=csp_settings_set_csp_lock_request)

Lock or unlock current CSP settings for sub-accounts and courses

Can only be set if CSP is explicitly enabled or disabled on this account (i.e. "inherited" is false).

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.csp_settings_set_csp_lock_request import CspSettingsSetCspLockRequest
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
    api_instance = canvas_lms_python_client.CspSettingsApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    csp_settings_set_csp_lock_request = canvas_lms_python_client.CspSettingsSetCspLockRequest() # CspSettingsSetCspLockRequest | Request body parameters (optional)

    try:
        # Lock or unlock current CSP settings for sub-accounts and courses
        await api_instance.csp_settings_set_csp_lock(account_id, csp_settings_set_csp_lock_request=csp_settings_set_csp_lock_request)
    except Exception as e:
        print("Exception when calling CspSettingsApi->csp_settings_set_csp_lock: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **csp_settings_set_csp_lock_request** | [**CspSettingsSetCspLockRequest**](CspSettingsSetCspLockRequest.md)| Request body parameters | [optional] 

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
**0** | Lock or unlock current CSP settings for sub-accounts and courses |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **csp_settings_set_csp_setting**
> csp_settings_set_csp_setting(course_id, csp_settings_set_csp_setting_request=csp_settings_set_csp_setting_request)

Enable, disable, or clear explicit CSP setting

Either explicitly sets CSP to be on or off for courses and sub-accounts,
or clear the explicit settings to default to those set by a parent account

Note: If "inherited" and "settings_locked" are both true for this account or course,
then the CSP setting cannot be modified.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.csp_settings_set_csp_setting_request import CspSettingsSetCspSettingRequest
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
    api_instance = canvas_lms_python_client.CspSettingsApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    csp_settings_set_csp_setting_request = canvas_lms_python_client.CspSettingsSetCspSettingRequest() # CspSettingsSetCspSettingRequest | Request body parameters (optional)

    try:
        # Enable, disable, or clear explicit CSP setting
        await api_instance.csp_settings_set_csp_setting(course_id, csp_settings_set_csp_setting_request=csp_settings_set_csp_setting_request)
    except Exception as e:
        print("Exception when calling CspSettingsApi->csp_settings_set_csp_setting: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **csp_settings_set_csp_setting_request** | [**CspSettingsSetCspSettingRequest**](CspSettingsSetCspSettingRequest.md)| Request body parameters | [optional] 

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
**0** | Enable, disable, or clear explicit CSP setting |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **csp_settings_set_csp_setting_for_accounts**
> csp_settings_set_csp_setting_for_accounts(account_id, csp_settings_set_csp_setting_request=csp_settings_set_csp_setting_request)

Enable, disable, or clear explicit CSP setting

Either explicitly sets CSP to be on or off for courses and sub-accounts,
or clear the explicit settings to default to those set by a parent account

Note: If "inherited" and "settings_locked" are both true for this account or course,
then the CSP setting cannot be modified.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.csp_settings_set_csp_setting_request import CspSettingsSetCspSettingRequest
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
    api_instance = canvas_lms_python_client.CspSettingsApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    csp_settings_set_csp_setting_request = canvas_lms_python_client.CspSettingsSetCspSettingRequest() # CspSettingsSetCspSettingRequest | Request body parameters (optional)

    try:
        # Enable, disable, or clear explicit CSP setting
        await api_instance.csp_settings_set_csp_setting_for_accounts(account_id, csp_settings_set_csp_setting_request=csp_settings_set_csp_setting_request)
    except Exception as e:
        print("Exception when calling CspSettingsApi->csp_settings_set_csp_setting_for_accounts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **csp_settings_set_csp_setting_request** | [**CspSettingsSetCspSettingRequest**](CspSettingsSetCspSettingRequest.md)| Request body parameters | [optional] 

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
**0** | Enable, disable, or clear explicit CSP setting |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

