# canvas_lms_python_client.BadPermissionSettingErrorApi

All URIs are relative to *https://canvas.instructure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bad_permission_setting_error_activate_role**](BadPermissionSettingErrorApi.md#bad_permission_setting_error_activate_role) | **POST** /api/v1/accounts/{account_id}/roles/{id}/activate | Activate a role
[**bad_permission_setting_error_add_role**](BadPermissionSettingErrorApi.md#bad_permission_setting_error_add_role) | **POST** /api/v1/accounts/{account_id}/roles | Create a new role
[**bad_permission_setting_error_api_index**](BadPermissionSettingErrorApi.md#bad_permission_setting_error_api_index) | **GET** /api/v1/accounts/{account_id}/roles | List roles
[**bad_permission_setting_error_manageable_permissions**](BadPermissionSettingErrorApi.md#bad_permission_setting_error_manageable_permissions) | **GET** /api/v1/accounts/{account_id}/roles/permissions | List assignable permissions
[**bad_permission_setting_error_remove_role**](BadPermissionSettingErrorApi.md#bad_permission_setting_error_remove_role) | **DELETE** /api/v1/accounts/{account_id}/roles/{id} | Deactivate a role
[**bad_permission_setting_error_show**](BadPermissionSettingErrorApi.md#bad_permission_setting_error_show) | **GET** /api/v1/accounts/{account_id}/roles/{id} | Get a single role
[**bad_permission_setting_error_update**](BadPermissionSettingErrorApi.md#bad_permission_setting_error_update) | **PUT** /api/v1/accounts/{account_id}/roles/{id} | Update a role


# **bad_permission_setting_error_activate_role**
> object bad_permission_setting_error_activate_role(account_id, id, bad_permission_setting_error_activate_role_request=bad_permission_setting_error_activate_role_request)

Activate a role

Re-activates an inactive role (allowing it to be assigned to new users)

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.bad_permission_setting_error_activate_role_request import BadPermissionSettingErrorActivateRoleRequest
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
    api_instance = canvas_lms_python_client.BadPermissionSettingErrorApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    id = 'id_example' # str | Scope response to id
    bad_permission_setting_error_activate_role_request = canvas_lms_python_client.BadPermissionSettingErrorActivateRoleRequest() # BadPermissionSettingErrorActivateRoleRequest | Request body parameters (optional)

    try:
        # Activate a role
        api_response = await api_instance.bad_permission_setting_error_activate_role(account_id, id, bad_permission_setting_error_activate_role_request=bad_permission_setting_error_activate_role_request)
        print("The response of BadPermissionSettingErrorApi->bad_permission_setting_error_activate_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BadPermissionSettingErrorApi->bad_permission_setting_error_activate_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **id** | **str**| Scope response to id | 
 **bad_permission_setting_error_activate_role_request** | [**BadPermissionSettingErrorActivateRoleRequest**](BadPermissionSettingErrorActivateRoleRequest.md)| Request body parameters | [optional] 

### Return type

**object**

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Role |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bad_permission_setting_error_add_role**
> object bad_permission_setting_error_add_role(account_id, bad_permission_setting_error_add_role_request=bad_permission_setting_error_add_role_request)

Create a new role

Create a new course-level or account-level role.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.bad_permission_setting_error_add_role_request import BadPermissionSettingErrorAddRoleRequest
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
    api_instance = canvas_lms_python_client.BadPermissionSettingErrorApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    bad_permission_setting_error_add_role_request = canvas_lms_python_client.BadPermissionSettingErrorAddRoleRequest() # BadPermissionSettingErrorAddRoleRequest | Request body parameters (optional)

    try:
        # Create a new role
        api_response = await api_instance.bad_permission_setting_error_add_role(account_id, bad_permission_setting_error_add_role_request=bad_permission_setting_error_add_role_request)
        print("The response of BadPermissionSettingErrorApi->bad_permission_setting_error_add_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BadPermissionSettingErrorApi->bad_permission_setting_error_add_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **bad_permission_setting_error_add_role_request** | [**BadPermissionSettingErrorAddRoleRequest**](BadPermissionSettingErrorAddRoleRequest.md)| Request body parameters | [optional] 

### Return type

**object**

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Role |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bad_permission_setting_error_api_index**
> List[object] bad_permission_setting_error_api_index(account_id, state=state, show_inherited=show_inherited, page=page, per_page=per_page)

List roles

A paginated list of the roles available to an account.

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
    api_instance = canvas_lms_python_client.BadPermissionSettingErrorApi(api_client)
    account_id = 'account_id_example' # str | The id of the account to retrieve roles for.
    state = ['state_example'] # List[str] | Filter by role state. If this argument is omitted, only 'active' roles are returned. (optional)
    show_inherited = True # bool | If this argument is true, all roles inherited from parent accounts will be included. (optional)
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # List roles
        api_response = await api_instance.bad_permission_setting_error_api_index(account_id, state=state, show_inherited=show_inherited, page=page, per_page=per_page)
        print("The response of BadPermissionSettingErrorApi->bad_permission_setting_error_api_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BadPermissionSettingErrorApi->bad_permission_setting_error_api_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The id of the account to retrieve roles for. | 
 **state** | [**List[str]**](str.md)| Filter by role state. If this argument is omitted, only &#39;active&#39; roles are returned. | [optional] 
 **show_inherited** | **bool**| If this argument is true, all roles inherited from parent accounts will be included. | [optional] 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

**List[object]**

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

# **bad_permission_setting_error_manageable_permissions**
> List[object] bad_permission_setting_error_manageable_permissions(account_id, search_term=search_term)

List assignable permissions

List all permissions that can be granted to roles in the given account.

This returns largely the same information documented on the {file:file.permissions.html Permissions list page},
with a few caveats:
* Permission labels and group labels returned by this API are localized (the same text visible in the web UI).
* This API includes permissions added by plugins.
* This API excludes permissions that are disabled in or otherwise do not apply to the given account.

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
    api_instance = canvas_lms_python_client.BadPermissionSettingErrorApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    search_term = 'search_term_example' # str | If provided, return only permissions whose key, label, group, or group_label match the search string. (optional)

    try:
        # List assignable permissions
        api_response = await api_instance.bad_permission_setting_error_manageable_permissions(account_id, search_term=search_term)
        print("The response of BadPermissionSettingErrorApi->bad_permission_setting_error_manageable_permissions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BadPermissionSettingErrorApi->bad_permission_setting_error_manageable_permissions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **search_term** | **str**| If provided, return only permissions whose key, label, group, or group_label match the search string. | [optional] 

### Return type

**List[object]**

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

# **bad_permission_setting_error_remove_role**
> object bad_permission_setting_error_remove_role(account_id, id, role_id, role=role)

Deactivate a role

Deactivates a custom role.  This hides it in the user interface and prevents it
from being assigned to new users.  Existing users assigned to the role will
continue to function with the same permissions they had previously.
Built-in roles cannot be deactivated.

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
    api_instance = canvas_lms_python_client.BadPermissionSettingErrorApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    id = 'id_example' # str | Scope response to id
    role_id = 56 # int | The unique identifier for the role
    role = 'role_example' # str | The name for the role (optional)

    try:
        # Deactivate a role
        api_response = await api_instance.bad_permission_setting_error_remove_role(account_id, id, role_id, role=role)
        print("The response of BadPermissionSettingErrorApi->bad_permission_setting_error_remove_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BadPermissionSettingErrorApi->bad_permission_setting_error_remove_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **id** | **str**| Scope response to id | 
 **role_id** | **int**| The unique identifier for the role | 
 **role** | **str**| The name for the role | [optional] 

### Return type

**object**

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Role |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bad_permission_setting_error_show**
> object bad_permission_setting_error_show(account_id, id, role_id, role=role)

Get a single role

Retrieve information about a single role

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
    api_instance = canvas_lms_python_client.BadPermissionSettingErrorApi(api_client)
    account_id = 'account_id_example' # str | The id of the account containing the role
    id = 'id_example' # str | Scope response to id
    role_id = 56 # int | The unique identifier for the role
    role = 'role_example' # str | The name for the role (optional)

    try:
        # Get a single role
        api_response = await api_instance.bad_permission_setting_error_show(account_id, id, role_id, role=role)
        print("The response of BadPermissionSettingErrorApi->bad_permission_setting_error_show:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BadPermissionSettingErrorApi->bad_permission_setting_error_show: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The id of the account containing the role | 
 **id** | **str**| Scope response to id | 
 **role_id** | **int**| The unique identifier for the role | 
 **role** | **str**| The name for the role | [optional] 

### Return type

**object**

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Role |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bad_permission_setting_error_update**
> object bad_permission_setting_error_update(account_id, id, bad_permission_setting_error_update_request=bad_permission_setting_error_update_request)

Update a role

Update permissions for an existing role.

Recognized roles are:
* TeacherEnrollment
* StudentEnrollment
* TaEnrollment
* ObserverEnrollment
* DesignerEnrollment
* AccountAdmin
* Any previously created custom role

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.bad_permission_setting_error_update_request import BadPermissionSettingErrorUpdateRequest
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
    api_instance = canvas_lms_python_client.BadPermissionSettingErrorApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    id = 'id_example' # str | Scope response to id
    bad_permission_setting_error_update_request = canvas_lms_python_client.BadPermissionSettingErrorUpdateRequest() # BadPermissionSettingErrorUpdateRequest | Request body parameters (optional)

    try:
        # Update a role
        api_response = await api_instance.bad_permission_setting_error_update(account_id, id, bad_permission_setting_error_update_request=bad_permission_setting_error_update_request)
        print("The response of BadPermissionSettingErrorApi->bad_permission_setting_error_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BadPermissionSettingErrorApi->bad_permission_setting_error_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **id** | **str**| Scope response to id | 
 **bad_permission_setting_error_update_request** | [**BadPermissionSettingErrorUpdateRequest**](BadPermissionSettingErrorUpdateRequest.md)| Request body parameters | [optional] 

### Return type

**object**

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Role |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

