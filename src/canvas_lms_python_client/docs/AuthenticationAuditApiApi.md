# canvas_lms_python_client.AuthenticationAuditApiApi

All URIs are relative to *https://canvas.instructure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**authentication_audit_api_for_account**](AuthenticationAuditApiApi.md#authentication_audit_api_for_account) | **GET** /api/v1/audit/authentication/accounts/{account_id} | Query by account.
[**authentication_audit_api_for_login**](AuthenticationAuditApiApi.md#authentication_audit_api_for_login) | **GET** /api/v1/audit/authentication/logins/{login_id} | Query by login.
[**authentication_audit_api_for_user**](AuthenticationAuditApiApi.md#authentication_audit_api_for_user) | **GET** /api/v1/audit/authentication/users/{user_id} | Query by user.


# **authentication_audit_api_for_account**
> authentication_audit_api_for_account(account_id, start_time=start_time, end_time=end_time, page=page, per_page=per_page)

Query by account.

List authentication events for a given account.

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
    api_instance = canvas_lms_python_client.AuthenticationAuditApiApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    start_time = 'start_time_example' # str | The beginning of the time range from which you want events. Events are stored for one year. (optional)
    end_time = 'end_time_example' # str | The end of the time range from which you want events. (optional)
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # Query by account.
        await api_instance.authentication_audit_api_for_account(account_id, start_time=start_time, end_time=end_time, page=page, per_page=per_page)
    except Exception as e:
        print("Exception when calling AuthenticationAuditApiApi->authentication_audit_api_for_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **start_time** | **str**| The beginning of the time range from which you want events. Events are stored for one year. | [optional] 
 **end_time** | **str**| The end of the time range from which you want events. | [optional] 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

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
**0** | Query by account. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **authentication_audit_api_for_login**
> authentication_audit_api_for_login(login_id, start_time=start_time, end_time=end_time, page=page, per_page=per_page)

Query by login.

List authentication events for a given login.

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
    api_instance = canvas_lms_python_client.AuthenticationAuditApiApi(api_client)
    login_id = 'login_id_example' # str | Scope response to login_id
    start_time = 'start_time_example' # str | The beginning of the time range from which you want events. Events are stored for one year. (optional)
    end_time = 'end_time_example' # str | The end of the time range from which you want events. (optional)
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # Query by login.
        await api_instance.authentication_audit_api_for_login(login_id, start_time=start_time, end_time=end_time, page=page, per_page=per_page)
    except Exception as e:
        print("Exception when calling AuthenticationAuditApiApi->authentication_audit_api_for_login: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login_id** | **str**| Scope response to login_id | 
 **start_time** | **str**| The beginning of the time range from which you want events. Events are stored for one year. | [optional] 
 **end_time** | **str**| The end of the time range from which you want events. | [optional] 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

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
**0** | Query by login. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **authentication_audit_api_for_user**
> authentication_audit_api_for_user(user_id, start_time=start_time, end_time=end_time, page=page, per_page=per_page)

Query by user.

List authentication events for a given user.

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
    api_instance = canvas_lms_python_client.AuthenticationAuditApiApi(api_client)
    user_id = 'user_id_example' # str | Scope response to user_id
    start_time = 'start_time_example' # str | The beginning of the time range from which you want events. Events are stored for one year. (optional)
    end_time = 'end_time_example' # str | The end of the time range from which you want events. (optional)
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # Query by user.
        await api_instance.authentication_audit_api_for_user(user_id, start_time=start_time, end_time=end_time, page=page, per_page=per_page)
    except Exception as e:
        print("Exception when calling AuthenticationAuditApiApi->authentication_audit_api_for_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| Scope response to user_id | 
 **start_time** | **str**| The beginning of the time range from which you want events. Events are stored for one year. | [optional] 
 **end_time** | **str**| The end of the time range from which you want events. | [optional] 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

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
**0** | Query by user. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

