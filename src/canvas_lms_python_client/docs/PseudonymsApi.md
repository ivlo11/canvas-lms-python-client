# canvas_lms_python_client.PseudonymsApi

All URIs are relative to *https://canvas.instructure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**pseudonyms_create**](PseudonymsApi.md#pseudonyms_create) | **POST** /api/v1/accounts/{account_id}/logins | Create a user login
[**pseudonyms_destroy**](PseudonymsApi.md#pseudonyms_destroy) | **DELETE** /api/v1/users/{user_id}/logins/{id} | Delete a user login
[**pseudonyms_forgot_password**](PseudonymsApi.md#pseudonyms_forgot_password) | **POST** /api/v1/users/reset_password | Kickoff password recovery flow
[**pseudonyms_index**](PseudonymsApi.md#pseudonyms_index) | **GET** /api/v1/accounts/{account_id}/logins | List user logins
[**pseudonyms_index_for_users**](PseudonymsApi.md#pseudonyms_index_for_users) | **GET** /api/v1/users/{user_id}/logins | List user logins
[**pseudonyms_update**](PseudonymsApi.md#pseudonyms_update) | **PUT** /api/v1/accounts/{account_id}/logins/{id} | Edit a user login


# **pseudonyms_create**
> pseudonyms_create(account_id, pseudonyms_create_request=pseudonyms_create_request)

Create a user login

Create a new login for an existing user in the given account.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.pseudonyms_create_request import PseudonymsCreateRequest
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
    api_instance = canvas_lms_python_client.PseudonymsApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    pseudonyms_create_request = canvas_lms_python_client.PseudonymsCreateRequest() # PseudonymsCreateRequest | Request body parameters  **Example Request:** ``` #create a facebook login for user with ID 123 curl 'https://<canvas>/api/v1/accounts/<account_id>/logins' \\      -F 'user[id]=123' \\      -F 'login[unique_id]=112233445566' \\      -F 'login[authentication_provider_id]=facebook' \\      -H 'Authorization: Bearer <token>' ``` (optional)

    try:
        # Create a user login
        await api_instance.pseudonyms_create(account_id, pseudonyms_create_request=pseudonyms_create_request)
    except Exception as e:
        print("Exception when calling PseudonymsApi->pseudonyms_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **pseudonyms_create_request** | [**PseudonymsCreateRequest**](PseudonymsCreateRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; #create a facebook login for user with ID 123 curl &#39;https://&lt;canvas&gt;/api/v1/accounts/&lt;account_id&gt;/logins&#39; \\      -F &#39;user[id]&#x3D;123&#39; \\      -F &#39;login[unique_id]&#x3D;112233445566&#39; \\      -F &#39;login[authentication_provider_id]&#x3D;facebook&#39; \\      -H &#39;Authorization: Bearer &lt;token&gt;&#39; &#x60;&#x60;&#x60; | [optional] 

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
**0** | Create a user login |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pseudonyms_destroy**
> pseudonyms_destroy(id, user_id)

Delete a user login

Delete an existing login.

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
    api_instance = canvas_lms_python_client.PseudonymsApi(api_client)
    id = 'id_example' # str | Scope response to id
    user_id = 'user_id_example' # str | Scope response to user_id

    try:
        # Delete a user login
        await api_instance.pseudonyms_destroy(id, user_id)
    except Exception as e:
        print("Exception when calling PseudonymsApi->pseudonyms_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Scope response to id | 
 **user_id** | **str**| Scope response to user_id | 

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
**0** | Delete a user login |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pseudonyms_forgot_password**
> pseudonyms_forgot_password()

Kickoff password recovery flow

Given a user email, generate a nonce and email it to the user

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
    api_instance = canvas_lms_python_client.PseudonymsApi(api_client)

    try:
        # Kickoff password recovery flow
        await api_instance.pseudonyms_forgot_password()
    except Exception as e:
        print("Exception when calling PseudonymsApi->pseudonyms_forgot_password: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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
**0** | Kickoff password recovery flow |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pseudonyms_index**
> pseudonyms_index(account_id, page=page, per_page=per_page)

List user logins

Given a user ID, return a paginated list of that user's logins for the given account.

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
    api_instance = canvas_lms_python_client.PseudonymsApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # List user logins
        await api_instance.pseudonyms_index(account_id, page=page, per_page=per_page)
    except Exception as e:
        print("Exception when calling PseudonymsApi->pseudonyms_index: %s\n" % e)
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
**0** | List user logins |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pseudonyms_index_for_users**
> pseudonyms_index_for_users(user_id, page=page, per_page=per_page)

List user logins

Given a user ID, return a paginated list of that user's logins for the given account.

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
    api_instance = canvas_lms_python_client.PseudonymsApi(api_client)
    user_id = 'user_id_example' # str | Scope response to user_id
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # List user logins
        await api_instance.pseudonyms_index_for_users(user_id, page=page, per_page=per_page)
    except Exception as e:
        print("Exception when calling PseudonymsApi->pseudonyms_index_for_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| Scope response to user_id | 
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
**0** | List user logins |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pseudonyms_update**
> pseudonyms_update(account_id, id, pseudonyms_update_request=pseudonyms_update_request)

Edit a user login

Update an existing login for a user in the given account.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.pseudonyms_update_request import PseudonymsUpdateRequest
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
    api_instance = canvas_lms_python_client.PseudonymsApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    id = 'id_example' # str | Scope response to id
    pseudonyms_update_request = canvas_lms_python_client.PseudonymsUpdateRequest() # PseudonymsUpdateRequest | Request body parameters  **Example Request:** ``` curl https://<canvas>/api/v1/accounts/:account_id/logins/:login_id \\   -H \"Authorization: Bearer <ACCESS-TOKEN>\" \\   -X PUT ``` (optional)

    try:
        # Edit a user login
        await api_instance.pseudonyms_update(account_id, id, pseudonyms_update_request=pseudonyms_update_request)
    except Exception as e:
        print("Exception when calling PseudonymsApi->pseudonyms_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **id** | **str**| Scope response to id | 
 **pseudonyms_update_request** | [**PseudonymsUpdateRequest**](PseudonymsUpdateRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl https://&lt;canvas&gt;/api/v1/accounts/:account_id/logins/:login_id \\   -H \&quot;Authorization: Bearer &lt;ACCESS-TOKEN&gt;\&quot; \\   -X PUT &#x60;&#x60;&#x60; | [optional] 

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
**0** | Edit a user login |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

