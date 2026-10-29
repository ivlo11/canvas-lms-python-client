# canvas_lms_python_client.AdminsApi

All URIs are relative to *https://canvas.instructure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**admins_create**](AdminsApi.md#admins_create) | **POST** /api/v1/accounts/{account_id}/admins | Make an account admin
[**admins_destroy**](AdminsApi.md#admins_destroy) | **DELETE** /api/v1/accounts/{account_id}/admins/{user_id} | Remove account admin
[**admins_index**](AdminsApi.md#admins_index) | **GET** /api/v1/accounts/{account_id}/admins | List account admins
[**admins_self_roles**](AdminsApi.md#admins_self_roles) | **GET** /api/v1/accounts/{account_id}/admins/self | List my admin roles


# **admins_create**
> Admin admins_create(account_id, admins_create_request=admins_create_request)

Make an account admin

Flag an existing user as an admin within the account.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.admin import Admin
from canvas_lms_python_client.models.admins_create_request import AdminsCreateRequest
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
    api_instance = canvas_lms_python_client.AdminsApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    admins_create_request = canvas_lms_python_client.AdminsCreateRequest() # AdminsCreateRequest | Request body parameters (optional)

    try:
        # Make an account admin
        api_response = await api_instance.admins_create(account_id, admins_create_request=admins_create_request)
        print("The response of AdminsApi->admins_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminsApi->admins_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **admins_create_request** | [**AdminsCreateRequest**](AdminsCreateRequest.md)| Request body parameters | [optional] 

### Return type

[**Admin**](Admin.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Admin |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admins_destroy**
> Admin admins_destroy(account_id, user_id, role_id, role=role)

Remove account admin

Remove the rights associated with an account admin role from a user.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.admin import Admin
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
    api_instance = canvas_lms_python_client.AdminsApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    user_id = 'user_id_example' # str | Scope response to user_id
    role_id = 56 # int | The id of the role representing the user's admin relationship with the account.
    role = 'role_example' # str | [DEPRECATED] Account role to remove from the user. (optional)

    try:
        # Remove account admin
        api_response = await api_instance.admins_destroy(account_id, user_id, role_id, role=role)
        print("The response of AdminsApi->admins_destroy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminsApi->admins_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **user_id** | **str**| Scope response to user_id | 
 **role_id** | **int**| The id of the role representing the user&#39;s admin relationship with the account. | 
 **role** | **str**| [DEPRECATED] Account role to remove from the user. | [optional] 

### Return type

[**Admin**](Admin.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Admin |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admins_index**
> List[Admin] admins_index(account_id, user_id__integer=user_id__integer, search_term=search_term, include_deleted=include_deleted, page=page, per_page=per_page)

List account admins

A paginated list of the admins in the account

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.admin import Admin
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
    api_instance = canvas_lms_python_client.AdminsApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    user_id__integer = 'user_id__integer_example' # str | ] Scope the results to those with user IDs equal to any of the IDs specified here. (optional)
    search_term = 'search_term_example' # str | The partial name or full ID of the admins to match and return in the results list. Must be at least 2 characters. (optional)
    include_deleted = True # bool | When set to true, returns admins who have been deleted (optional)
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # List account admins
        api_response = await api_instance.admins_index(account_id, user_id__integer=user_id__integer, search_term=search_term, include_deleted=include_deleted, page=page, per_page=per_page)
        print("The response of AdminsApi->admins_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminsApi->admins_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **user_id__integer** | **str**| ] Scope the results to those with user IDs equal to any of the IDs specified here. | [optional] 
 **search_term** | **str**| The partial name or full ID of the admins to match and return in the results list. Must be at least 2 characters. | [optional] 
 **include_deleted** | **bool**| When set to true, returns admins who have been deleted | [optional] 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**List[Admin]**](Admin.md)

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

# **admins_self_roles**
> List[Admin] admins_self_roles(account_id, page=page, per_page=per_page)

List my admin roles

A paginated list of the current user's roles in the account. The results are the same
as those returned by the {api:AdminsController#index List account admins} endpoint with
+user_id+ set to +self+, except the "Admins - Add / Remove" permission is not required.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.admin import Admin
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
    api_instance = canvas_lms_python_client.AdminsApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # List my admin roles
        api_response = await api_instance.admins_self_roles(account_id, page=page, per_page=per_page)
        print("The response of AdminsApi->admins_self_roles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminsApi->admins_self_roles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**List[Admin]**](Admin.md)

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

