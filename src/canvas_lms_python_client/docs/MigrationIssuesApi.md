# canvas_lms_python_client.MigrationIssuesApi

All URIs are relative to *https://canvas.instructure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**migration_issues_index**](MigrationIssuesApi.md#migration_issues_index) | **GET** /api/v1/accounts/{account_id}/content_migrations/{content_migration_id}/migration_issues | List migration issues
[**migration_issues_index_for_courses**](MigrationIssuesApi.md#migration_issues_index_for_courses) | **GET** /api/v1/courses/{course_id}/content_migrations/{content_migration_id}/migration_issues | List migration issues
[**migration_issues_index_for_groups**](MigrationIssuesApi.md#migration_issues_index_for_groups) | **GET** /api/v1/groups/{group_id}/content_migrations/{content_migration_id}/migration_issues | List migration issues
[**migration_issues_index_for_users**](MigrationIssuesApi.md#migration_issues_index_for_users) | **GET** /api/v1/users/{user_id}/content_migrations/{content_migration_id}/migration_issues | List migration issues
[**migration_issues_show**](MigrationIssuesApi.md#migration_issues_show) | **GET** /api/v1/accounts/{account_id}/content_migrations/{content_migration_id}/migration_issues/{id} | Get a migration issue
[**migration_issues_show_for_courses**](MigrationIssuesApi.md#migration_issues_show_for_courses) | **GET** /api/v1/courses/{course_id}/content_migrations/{content_migration_id}/migration_issues/{id} | Get a migration issue
[**migration_issues_show_for_groups**](MigrationIssuesApi.md#migration_issues_show_for_groups) | **GET** /api/v1/groups/{group_id}/content_migrations/{content_migration_id}/migration_issues/{id} | Get a migration issue
[**migration_issues_show_for_users**](MigrationIssuesApi.md#migration_issues_show_for_users) | **GET** /api/v1/users/{user_id}/content_migrations/{content_migration_id}/migration_issues/{id} | Get a migration issue
[**migration_issues_update**](MigrationIssuesApi.md#migration_issues_update) | **PUT** /api/v1/accounts/{account_id}/content_migrations/{content_migration_id}/migration_issues/{id} | Update a migration issue
[**migration_issues_update_for_courses**](MigrationIssuesApi.md#migration_issues_update_for_courses) | **PUT** /api/v1/courses/{course_id}/content_migrations/{content_migration_id}/migration_issues/{id} | Update a migration issue
[**migration_issues_update_for_groups**](MigrationIssuesApi.md#migration_issues_update_for_groups) | **PUT** /api/v1/groups/{group_id}/content_migrations/{content_migration_id}/migration_issues/{id} | Update a migration issue
[**migration_issues_update_for_users**](MigrationIssuesApi.md#migration_issues_update_for_users) | **PUT** /api/v1/users/{user_id}/content_migrations/{content_migration_id}/migration_issues/{id} | Update a migration issue


# **migration_issues_index**
> List[MigrationIssue] migration_issues_index(account_id, content_migration_id, page=page, per_page=per_page)

List migration issues

Returns paginated migration issues

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.migration_issue import MigrationIssue
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
    api_instance = canvas_lms_python_client.MigrationIssuesApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    content_migration_id = 'content_migration_id_example' # str | Scope response to content_migration_id
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # List migration issues
        api_response = await api_instance.migration_issues_index(account_id, content_migration_id, page=page, per_page=per_page)
        print("The response of MigrationIssuesApi->migration_issues_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MigrationIssuesApi->migration_issues_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **content_migration_id** | **str**| Scope response to content_migration_id | 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**List[MigrationIssue]**](MigrationIssue.md)

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

# **migration_issues_index_for_courses**
> List[MigrationIssue] migration_issues_index_for_courses(content_migration_id, course_id, page=page, per_page=per_page)

List migration issues

Returns paginated migration issues

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.migration_issue import MigrationIssue
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
    api_instance = canvas_lms_python_client.MigrationIssuesApi(api_client)
    content_migration_id = 'content_migration_id_example' # str | Scope response to content_migration_id
    course_id = 'course_id_example' # str | Scope response to course_id
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # List migration issues
        api_response = await api_instance.migration_issues_index_for_courses(content_migration_id, course_id, page=page, per_page=per_page)
        print("The response of MigrationIssuesApi->migration_issues_index_for_courses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MigrationIssuesApi->migration_issues_index_for_courses: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_migration_id** | **str**| Scope response to content_migration_id | 
 **course_id** | **str**| Scope response to course_id | 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**List[MigrationIssue]**](MigrationIssue.md)

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

# **migration_issues_index_for_groups**
> List[MigrationIssue] migration_issues_index_for_groups(content_migration_id, group_id, page=page, per_page=per_page)

List migration issues

Returns paginated migration issues

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.migration_issue import MigrationIssue
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
    api_instance = canvas_lms_python_client.MigrationIssuesApi(api_client)
    content_migration_id = 'content_migration_id_example' # str | Scope response to content_migration_id
    group_id = 'group_id_example' # str | Scope response to group_id
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # List migration issues
        api_response = await api_instance.migration_issues_index_for_groups(content_migration_id, group_id, page=page, per_page=per_page)
        print("The response of MigrationIssuesApi->migration_issues_index_for_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MigrationIssuesApi->migration_issues_index_for_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_migration_id** | **str**| Scope response to content_migration_id | 
 **group_id** | **str**| Scope response to group_id | 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**List[MigrationIssue]**](MigrationIssue.md)

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

# **migration_issues_index_for_users**
> List[MigrationIssue] migration_issues_index_for_users(content_migration_id, user_id, page=page, per_page=per_page)

List migration issues

Returns paginated migration issues

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.migration_issue import MigrationIssue
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
    api_instance = canvas_lms_python_client.MigrationIssuesApi(api_client)
    content_migration_id = 'content_migration_id_example' # str | Scope response to content_migration_id
    user_id = 'user_id_example' # str | Scope response to user_id
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # List migration issues
        api_response = await api_instance.migration_issues_index_for_users(content_migration_id, user_id, page=page, per_page=per_page)
        print("The response of MigrationIssuesApi->migration_issues_index_for_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MigrationIssuesApi->migration_issues_index_for_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_migration_id** | **str**| Scope response to content_migration_id | 
 **user_id** | **str**| Scope response to user_id | 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**List[MigrationIssue]**](MigrationIssue.md)

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

# **migration_issues_show**
> MigrationIssue migration_issues_show(account_id, content_migration_id, id)

Get a migration issue

Returns data on an individual migration issue

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.migration_issue import MigrationIssue
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
    api_instance = canvas_lms_python_client.MigrationIssuesApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    content_migration_id = 'content_migration_id_example' # str | Scope response to content_migration_id
    id = 'id_example' # str | Scope response to id

    try:
        # Get a migration issue
        api_response = await api_instance.migration_issues_show(account_id, content_migration_id, id)
        print("The response of MigrationIssuesApi->migration_issues_show:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MigrationIssuesApi->migration_issues_show: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **content_migration_id** | **str**| Scope response to content_migration_id | 
 **id** | **str**| Scope response to id | 

### Return type

[**MigrationIssue**](MigrationIssue.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | MigrationIssue |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **migration_issues_show_for_courses**
> MigrationIssue migration_issues_show_for_courses(content_migration_id, course_id, id)

Get a migration issue

Returns data on an individual migration issue

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.migration_issue import MigrationIssue
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
    api_instance = canvas_lms_python_client.MigrationIssuesApi(api_client)
    content_migration_id = 'content_migration_id_example' # str | Scope response to content_migration_id
    course_id = 'course_id_example' # str | Scope response to course_id
    id = 'id_example' # str | Scope response to id

    try:
        # Get a migration issue
        api_response = await api_instance.migration_issues_show_for_courses(content_migration_id, course_id, id)
        print("The response of MigrationIssuesApi->migration_issues_show_for_courses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MigrationIssuesApi->migration_issues_show_for_courses: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_migration_id** | **str**| Scope response to content_migration_id | 
 **course_id** | **str**| Scope response to course_id | 
 **id** | **str**| Scope response to id | 

### Return type

[**MigrationIssue**](MigrationIssue.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | MigrationIssue |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **migration_issues_show_for_groups**
> MigrationIssue migration_issues_show_for_groups(content_migration_id, group_id, id)

Get a migration issue

Returns data on an individual migration issue

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.migration_issue import MigrationIssue
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
    api_instance = canvas_lms_python_client.MigrationIssuesApi(api_client)
    content_migration_id = 'content_migration_id_example' # str | Scope response to content_migration_id
    group_id = 'group_id_example' # str | Scope response to group_id
    id = 'id_example' # str | Scope response to id

    try:
        # Get a migration issue
        api_response = await api_instance.migration_issues_show_for_groups(content_migration_id, group_id, id)
        print("The response of MigrationIssuesApi->migration_issues_show_for_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MigrationIssuesApi->migration_issues_show_for_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_migration_id** | **str**| Scope response to content_migration_id | 
 **group_id** | **str**| Scope response to group_id | 
 **id** | **str**| Scope response to id | 

### Return type

[**MigrationIssue**](MigrationIssue.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | MigrationIssue |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **migration_issues_show_for_users**
> MigrationIssue migration_issues_show_for_users(content_migration_id, id, user_id)

Get a migration issue

Returns data on an individual migration issue

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.migration_issue import MigrationIssue
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
    api_instance = canvas_lms_python_client.MigrationIssuesApi(api_client)
    content_migration_id = 'content_migration_id_example' # str | Scope response to content_migration_id
    id = 'id_example' # str | Scope response to id
    user_id = 'user_id_example' # str | Scope response to user_id

    try:
        # Get a migration issue
        api_response = await api_instance.migration_issues_show_for_users(content_migration_id, id, user_id)
        print("The response of MigrationIssuesApi->migration_issues_show_for_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MigrationIssuesApi->migration_issues_show_for_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_migration_id** | **str**| Scope response to content_migration_id | 
 **id** | **str**| Scope response to id | 
 **user_id** | **str**| Scope response to user_id | 

### Return type

[**MigrationIssue**](MigrationIssue.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | MigrationIssue |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **migration_issues_update**
> MigrationIssue migration_issues_update(account_id, content_migration_id, id, migration_issues_update_request=migration_issues_update_request)

Update a migration issue

Update the workflow_state of a migration issue

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.migration_issue import MigrationIssue
from canvas_lms_python_client.models.migration_issues_update_request import MigrationIssuesUpdateRequest
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
    api_instance = canvas_lms_python_client.MigrationIssuesApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    content_migration_id = 'content_migration_id_example' # str | Scope response to content_migration_id
    id = 'id_example' # str | Scope response to id
    migration_issues_update_request = canvas_lms_python_client.MigrationIssuesUpdateRequest() # MigrationIssuesUpdateRequest | Request body parameters  **Example Request:** ``` curl -X PUT https://<canvas>/api/v1/courses/<course_id>/content_migrations/<content_migration_id>/migration_issues/<id> \\      -H 'Authorization: Bearer <token>' \\      -F 'workflow_state=resolved' ``` (optional)

    try:
        # Update a migration issue
        api_response = await api_instance.migration_issues_update(account_id, content_migration_id, id, migration_issues_update_request=migration_issues_update_request)
        print("The response of MigrationIssuesApi->migration_issues_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MigrationIssuesApi->migration_issues_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **content_migration_id** | **str**| Scope response to content_migration_id | 
 **id** | **str**| Scope response to id | 
 **migration_issues_update_request** | [**MigrationIssuesUpdateRequest**](MigrationIssuesUpdateRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl -X PUT https://&lt;canvas&gt;/api/v1/courses/&lt;course_id&gt;/content_migrations/&lt;content_migration_id&gt;/migration_issues/&lt;id&gt; \\      -H &#39;Authorization: Bearer &lt;token&gt;&#39; \\      -F &#39;workflow_state&#x3D;resolved&#39; &#x60;&#x60;&#x60; | [optional] 

### Return type

[**MigrationIssue**](MigrationIssue.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | MigrationIssue |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **migration_issues_update_for_courses**
> MigrationIssue migration_issues_update_for_courses(content_migration_id, course_id, id, migration_issues_update_request=migration_issues_update_request)

Update a migration issue

Update the workflow_state of a migration issue

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.migration_issue import MigrationIssue
from canvas_lms_python_client.models.migration_issues_update_request import MigrationIssuesUpdateRequest
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
    api_instance = canvas_lms_python_client.MigrationIssuesApi(api_client)
    content_migration_id = 'content_migration_id_example' # str | Scope response to content_migration_id
    course_id = 'course_id_example' # str | Scope response to course_id
    id = 'id_example' # str | Scope response to id
    migration_issues_update_request = canvas_lms_python_client.MigrationIssuesUpdateRequest() # MigrationIssuesUpdateRequest | Request body parameters  **Example Request:** ``` curl -X PUT https://<canvas>/api/v1/courses/<course_id>/content_migrations/<content_migration_id>/migration_issues/<id> \\      -H 'Authorization: Bearer <token>' \\      -F 'workflow_state=resolved' ``` (optional)

    try:
        # Update a migration issue
        api_response = await api_instance.migration_issues_update_for_courses(content_migration_id, course_id, id, migration_issues_update_request=migration_issues_update_request)
        print("The response of MigrationIssuesApi->migration_issues_update_for_courses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MigrationIssuesApi->migration_issues_update_for_courses: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_migration_id** | **str**| Scope response to content_migration_id | 
 **course_id** | **str**| Scope response to course_id | 
 **id** | **str**| Scope response to id | 
 **migration_issues_update_request** | [**MigrationIssuesUpdateRequest**](MigrationIssuesUpdateRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl -X PUT https://&lt;canvas&gt;/api/v1/courses/&lt;course_id&gt;/content_migrations/&lt;content_migration_id&gt;/migration_issues/&lt;id&gt; \\      -H &#39;Authorization: Bearer &lt;token&gt;&#39; \\      -F &#39;workflow_state&#x3D;resolved&#39; &#x60;&#x60;&#x60; | [optional] 

### Return type

[**MigrationIssue**](MigrationIssue.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | MigrationIssue |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **migration_issues_update_for_groups**
> MigrationIssue migration_issues_update_for_groups(content_migration_id, group_id, id, migration_issues_update_request=migration_issues_update_request)

Update a migration issue

Update the workflow_state of a migration issue

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.migration_issue import MigrationIssue
from canvas_lms_python_client.models.migration_issues_update_request import MigrationIssuesUpdateRequest
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
    api_instance = canvas_lms_python_client.MigrationIssuesApi(api_client)
    content_migration_id = 'content_migration_id_example' # str | Scope response to content_migration_id
    group_id = 'group_id_example' # str | Scope response to group_id
    id = 'id_example' # str | Scope response to id
    migration_issues_update_request = canvas_lms_python_client.MigrationIssuesUpdateRequest() # MigrationIssuesUpdateRequest | Request body parameters  **Example Request:** ``` curl -X PUT https://<canvas>/api/v1/courses/<course_id>/content_migrations/<content_migration_id>/migration_issues/<id> \\      -H 'Authorization: Bearer <token>' \\      -F 'workflow_state=resolved' ``` (optional)

    try:
        # Update a migration issue
        api_response = await api_instance.migration_issues_update_for_groups(content_migration_id, group_id, id, migration_issues_update_request=migration_issues_update_request)
        print("The response of MigrationIssuesApi->migration_issues_update_for_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MigrationIssuesApi->migration_issues_update_for_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_migration_id** | **str**| Scope response to content_migration_id | 
 **group_id** | **str**| Scope response to group_id | 
 **id** | **str**| Scope response to id | 
 **migration_issues_update_request** | [**MigrationIssuesUpdateRequest**](MigrationIssuesUpdateRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl -X PUT https://&lt;canvas&gt;/api/v1/courses/&lt;course_id&gt;/content_migrations/&lt;content_migration_id&gt;/migration_issues/&lt;id&gt; \\      -H &#39;Authorization: Bearer &lt;token&gt;&#39; \\      -F &#39;workflow_state&#x3D;resolved&#39; &#x60;&#x60;&#x60; | [optional] 

### Return type

[**MigrationIssue**](MigrationIssue.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | MigrationIssue |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **migration_issues_update_for_users**
> MigrationIssue migration_issues_update_for_users(content_migration_id, id, user_id, migration_issues_update_request=migration_issues_update_request)

Update a migration issue

Update the workflow_state of a migration issue

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.migration_issue import MigrationIssue
from canvas_lms_python_client.models.migration_issues_update_request import MigrationIssuesUpdateRequest
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
    api_instance = canvas_lms_python_client.MigrationIssuesApi(api_client)
    content_migration_id = 'content_migration_id_example' # str | Scope response to content_migration_id
    id = 'id_example' # str | Scope response to id
    user_id = 'user_id_example' # str | Scope response to user_id
    migration_issues_update_request = canvas_lms_python_client.MigrationIssuesUpdateRequest() # MigrationIssuesUpdateRequest | Request body parameters  **Example Request:** ``` curl -X PUT https://<canvas>/api/v1/courses/<course_id>/content_migrations/<content_migration_id>/migration_issues/<id> \\      -H 'Authorization: Bearer <token>' \\      -F 'workflow_state=resolved' ``` (optional)

    try:
        # Update a migration issue
        api_response = await api_instance.migration_issues_update_for_users(content_migration_id, id, user_id, migration_issues_update_request=migration_issues_update_request)
        print("The response of MigrationIssuesApi->migration_issues_update_for_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MigrationIssuesApi->migration_issues_update_for_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_migration_id** | **str**| Scope response to content_migration_id | 
 **id** | **str**| Scope response to id | 
 **user_id** | **str**| Scope response to user_id | 
 **migration_issues_update_request** | [**MigrationIssuesUpdateRequest**](MigrationIssuesUpdateRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl -X PUT https://&lt;canvas&gt;/api/v1/courses/&lt;course_id&gt;/content_migrations/&lt;content_migration_id&gt;/migration_issues/&lt;id&gt; \\      -H &#39;Authorization: Bearer &lt;token&gt;&#39; \\      -F &#39;workflow_state&#x3D;resolved&#39; &#x60;&#x60;&#x60; | [optional] 

### Return type

[**MigrationIssue**](MigrationIssue.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | MigrationIssue |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

