# canvas_lms_python_client.RoleOverridesApi

All URIs are relative to *https://canvas.instructure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**role_overrides_activate_role**](RoleOverridesApi.md#role_overrides_activate_role) | **POST** /api/v1/accounts/{account_id}/roles/{id}/activate | Activate a role
[**role_overrides_add_role**](RoleOverridesApi.md#role_overrides_add_role) | **POST** /api/v1/accounts/{account_id}/roles | Create a new role
[**role_overrides_api_index**](RoleOverridesApi.md#role_overrides_api_index) | **GET** /api/v1/accounts/{account_id}/roles | List roles
[**role_overrides_manageable_permissions**](RoleOverridesApi.md#role_overrides_manageable_permissions) | **GET** /api/v1/accounts/{account_id}/roles/permissions | List assignable permissions
[**role_overrides_remove_role**](RoleOverridesApi.md#role_overrides_remove_role) | **DELETE** /api/v1/accounts/{account_id}/roles/{id} | Deactivate a role
[**role_overrides_show**](RoleOverridesApi.md#role_overrides_show) | **GET** /api/v1/accounts/{account_id}/roles/{id} | Get a single role
[**role_overrides_update**](RoleOverridesApi.md#role_overrides_update) | **PUT** /api/v1/accounts/{account_id}/roles/{id} | Update a role


# **role_overrides_activate_role**
> Role role_overrides_activate_role(account_id, id, role_overrides_activate_role_request=role_overrides_activate_role_request)

Activate a role

Re-activates an inactive role (allowing it to be assigned to new users)

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.role import Role
from canvas_lms_python_client.models.role_overrides_activate_role_request import RoleOverridesActivateRoleRequest
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
    api_instance = canvas_lms_python_client.RoleOverridesApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    id = 'id_example' # str | Scope response to id
    role_overrides_activate_role_request = canvas_lms_python_client.RoleOverridesActivateRoleRequest() # RoleOverridesActivateRoleRequest | Request body parameters (optional)

    try:
        # Activate a role
        api_response = await api_instance.role_overrides_activate_role(account_id, id, role_overrides_activate_role_request=role_overrides_activate_role_request)
        print("The response of RoleOverridesApi->role_overrides_activate_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoleOverridesApi->role_overrides_activate_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **id** | **str**| Scope response to id | 
 **role_overrides_activate_role_request** | [**RoleOverridesActivateRoleRequest**](RoleOverridesActivateRoleRequest.md)| Request body parameters | [optional] 

### Return type

[**Role**](Role.md)

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

# **role_overrides_add_role**
> Role role_overrides_add_role(account_id, role_overrides_add_role_request=role_overrides_add_role_request)

Create a new role

Create a new course-level or account-level role.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.role import Role
from canvas_lms_python_client.models.role_overrides_add_role_request import RoleOverridesAddRoleRequest
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
    api_instance = canvas_lms_python_client.RoleOverridesApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    role_overrides_add_role_request = canvas_lms_python_client.RoleOverridesAddRoleRequest() # RoleOverridesAddRoleRequest | Request body parameters  **Example Request:** ``` curl 'https://<canvas>/api/v1/accounts/<account_id>/roles.json' \\      -H \"Authorization: Bearer <token>\" \\      -F 'label=New Role' \\      -F 'permissions[read_course_content][explicit]=1' \\      -F 'permissions[read_course_content][enabled]=1' \\      -F 'permissions[read_course_list][locked]=1' \\      -F 'permissions[read_question_banks][explicit]=1' \\      -F 'permissions[read_question_banks][enabled]=0' \\      -F 'permissions[read_question_banks][locked]=1' ``` (optional)

    try:
        # Create a new role
        api_response = await api_instance.role_overrides_add_role(account_id, role_overrides_add_role_request=role_overrides_add_role_request)
        print("The response of RoleOverridesApi->role_overrides_add_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoleOverridesApi->role_overrides_add_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **role_overrides_add_role_request** | [**RoleOverridesAddRoleRequest**](RoleOverridesAddRoleRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl &#39;https://&lt;canvas&gt;/api/v1/accounts/&lt;account_id&gt;/roles.json&#39; \\      -H \&quot;Authorization: Bearer &lt;token&gt;\&quot; \\      -F &#39;label&#x3D;New Role&#39; \\      -F &#39;permissions[read_course_content][explicit]&#x3D;1&#39; \\      -F &#39;permissions[read_course_content][enabled]&#x3D;1&#39; \\      -F &#39;permissions[read_course_list][locked]&#x3D;1&#39; \\      -F &#39;permissions[read_question_banks][explicit]&#x3D;1&#39; \\      -F &#39;permissions[read_question_banks][enabled]&#x3D;0&#39; \\      -F &#39;permissions[read_question_banks][locked]&#x3D;1&#39; &#x60;&#x60;&#x60; | [optional] 

### Return type

[**Role**](Role.md)

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

# **role_overrides_api_index**
> List[Role] role_overrides_api_index(account_id, state=state, show_inherited=show_inherited, page=page, per_page=per_page)

List roles

A paginated list of the roles available to an account.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.role import Role
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
    api_instance = canvas_lms_python_client.RoleOverridesApi(api_client)
    account_id = 'account_id_example' # str | The id of the account to retrieve roles for.
    state = ['state_example'] # List[str] | Filter by role state. If this argument is omitted, only 'active' roles are returned. (optional)
    show_inherited = True # bool | If this argument is true, all roles inherited from parent accounts will be included. (optional)
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # List roles
        api_response = await api_instance.role_overrides_api_index(account_id, state=state, show_inherited=show_inherited, page=page, per_page=per_page)
        print("The response of RoleOverridesApi->role_overrides_api_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoleOverridesApi->role_overrides_api_index: %s\n" % e)
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

[**List[Role]**](Role.md)

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

# **role_overrides_manageable_permissions**
> List[Permission] role_overrides_manageable_permissions(account_id, search_term=search_term)

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
from canvas_lms_python_client.models.permission import Permission
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
    api_instance = canvas_lms_python_client.RoleOverridesApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    search_term = 'search_term_example' # str | If provided, return only permissions whose key, label, group, or group_label match the search string. (optional)

    try:
        # List assignable permissions
        api_response = await api_instance.role_overrides_manageable_permissions(account_id, search_term=search_term)
        print("The response of RoleOverridesApi->role_overrides_manageable_permissions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoleOverridesApi->role_overrides_manageable_permissions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **search_term** | **str**| If provided, return only permissions whose key, label, group, or group_label match the search string. | [optional] 

### Return type

[**List[Permission]**](Permission.md)

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

# **role_overrides_remove_role**
> Role role_overrides_remove_role(account_id, id, role_id, role=role)

Deactivate a role

Deactivates a custom role.  This hides it in the user interface and prevents it
from being assigned to new users.  Existing users assigned to the role will
continue to function with the same permissions they had previously.
Built-in roles cannot be deactivated.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.role import Role
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
    api_instance = canvas_lms_python_client.RoleOverridesApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    id = 'id_example' # str | Scope response to id
    role_id = 56 # int | The unique identifier for the role
    role = 'role_example' # str | The name for the role (optional)

    try:
        # Deactivate a role
        api_response = await api_instance.role_overrides_remove_role(account_id, id, role_id, role=role)
        print("The response of RoleOverridesApi->role_overrides_remove_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoleOverridesApi->role_overrides_remove_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **id** | **str**| Scope response to id | 
 **role_id** | **int**| The unique identifier for the role | 
 **role** | **str**| The name for the role | [optional] 

### Return type

[**Role**](Role.md)

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

# **role_overrides_show**
> Role role_overrides_show(account_id, id, role_id, role=role)

Get a single role

Retrieve information about a single role

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.role import Role
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
    api_instance = canvas_lms_python_client.RoleOverridesApi(api_client)
    account_id = 'account_id_example' # str | The id of the account containing the role
    id = 'id_example' # str | Scope response to id
    role_id = 56 # int | The unique identifier for the role
    role = 'role_example' # str | The name for the role (optional)

    try:
        # Get a single role
        api_response = await api_instance.role_overrides_show(account_id, id, role_id, role=role)
        print("The response of RoleOverridesApi->role_overrides_show:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoleOverridesApi->role_overrides_show: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The id of the account containing the role | 
 **id** | **str**| Scope response to id | 
 **role_id** | **int**| The unique identifier for the role | 
 **role** | **str**| The name for the role | [optional] 

### Return type

[**Role**](Role.md)

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

# **role_overrides_update**
> Role role_overrides_update(account_id, id, role_overrides_update_request=role_overrides_update_request)

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
from canvas_lms_python_client.models.role import Role
from canvas_lms_python_client.models.role_overrides_update_request import RoleOverridesUpdateRequest
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
    api_instance = canvas_lms_python_client.RoleOverridesApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    id = 'id_example' # str | Scope response to id
    role_overrides_update_request = canvas_lms_python_client.RoleOverridesUpdateRequest() # RoleOverridesUpdateRequest | Request body parameters  **Example Request:** ``` curl https://<canvas>/api/v1/accounts/:account_id/roles/2 \\   -X PUT \\   -H 'Authorization: Bearer <access_token>' \\   -F 'label=New Role Name' \\   -F 'permissions[manage_groups][explicit]=1' \\   -F 'permissions[manage_groups][enabled]=1' \\   -F 'permissions[manage_groups][locked]=1' \\   -F 'permissions[send_messages][explicit]=1' \\   -F 'permissions[send_messages][enabled]=0' ``` (optional)

    try:
        # Update a role
        api_response = await api_instance.role_overrides_update(account_id, id, role_overrides_update_request=role_overrides_update_request)
        print("The response of RoleOverridesApi->role_overrides_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoleOverridesApi->role_overrides_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **id** | **str**| Scope response to id | 
 **role_overrides_update_request** | [**RoleOverridesUpdateRequest**](RoleOverridesUpdateRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl https://&lt;canvas&gt;/api/v1/accounts/:account_id/roles/2 \\   -X PUT \\   -H &#39;Authorization: Bearer &lt;access_token&gt;&#39; \\   -F &#39;label&#x3D;New Role Name&#39; \\   -F &#39;permissions[manage_groups][explicit]&#x3D;1&#39; \\   -F &#39;permissions[manage_groups][enabled]&#x3D;1&#39; \\   -F &#39;permissions[manage_groups][locked]&#x3D;1&#39; \\   -F &#39;permissions[send_messages][explicit]&#x3D;1&#39; \\   -F &#39;permissions[send_messages][enabled]&#x3D;0&#39; &#x60;&#x60;&#x60; | [optional] 

### Return type

[**Role**](Role.md)

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

