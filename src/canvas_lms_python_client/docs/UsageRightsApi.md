# canvas_lms_python_client.UsageRightsApi

All URIs are relative to *https://canvas.instructure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**usage_rights_licenses**](UsageRightsApi.md#usage_rights_licenses) | **GET** /api/v1/courses/{course_id}/content_licenses | List licenses
[**usage_rights_licenses_for_groups**](UsageRightsApi.md#usage_rights_licenses_for_groups) | **GET** /api/v1/groups/{group_id}/content_licenses | List licenses
[**usage_rights_licenses_for_users**](UsageRightsApi.md#usage_rights_licenses_for_users) | **GET** /api/v1/users/{user_id}/content_licenses | List licenses
[**usage_rights_remove_usage_rights**](UsageRightsApi.md#usage_rights_remove_usage_rights) | **DELETE** /api/v1/courses/{course_id}/usage_rights | Remove usage rights
[**usage_rights_remove_usage_rights_for_groups**](UsageRightsApi.md#usage_rights_remove_usage_rights_for_groups) | **DELETE** /api/v1/groups/{group_id}/usage_rights | Remove usage rights
[**usage_rights_remove_usage_rights_for_users**](UsageRightsApi.md#usage_rights_remove_usage_rights_for_users) | **DELETE** /api/v1/users/{user_id}/usage_rights | Remove usage rights
[**usage_rights_set_usage_rights**](UsageRightsApi.md#usage_rights_set_usage_rights) | **PUT** /api/v1/courses/{course_id}/usage_rights | Set usage rights
[**usage_rights_set_usage_rights_for_groups**](UsageRightsApi.md#usage_rights_set_usage_rights_for_groups) | **PUT** /api/v1/groups/{group_id}/usage_rights | Set usage rights
[**usage_rights_set_usage_rights_for_users**](UsageRightsApi.md#usage_rights_set_usage_rights_for_users) | **PUT** /api/v1/users/{user_id}/usage_rights | Set usage rights


# **usage_rights_licenses**
> List[License] usage_rights_licenses(course_id)

List licenses

A paginated list of licenses that can be applied

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.license import License
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
    api_instance = canvas_lms_python_client.UsageRightsApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id

    try:
        # List licenses
        api_response = await api_instance.usage_rights_licenses(course_id)
        print("The response of UsageRightsApi->usage_rights_licenses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsageRightsApi->usage_rights_licenses: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 

### Return type

[**List[License]**](License.md)

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

# **usage_rights_licenses_for_groups**
> List[License] usage_rights_licenses_for_groups(group_id)

List licenses

A paginated list of licenses that can be applied

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.license import License
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
    api_instance = canvas_lms_python_client.UsageRightsApi(api_client)
    group_id = 'group_id_example' # str | Scope response to group_id

    try:
        # List licenses
        api_response = await api_instance.usage_rights_licenses_for_groups(group_id)
        print("The response of UsageRightsApi->usage_rights_licenses_for_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsageRightsApi->usage_rights_licenses_for_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Scope response to group_id | 

### Return type

[**List[License]**](License.md)

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

# **usage_rights_licenses_for_users**
> List[License] usage_rights_licenses_for_users(user_id)

List licenses

A paginated list of licenses that can be applied

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.license import License
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
    api_instance = canvas_lms_python_client.UsageRightsApi(api_client)
    user_id = 'user_id_example' # str | Scope response to user_id

    try:
        # List licenses
        api_response = await api_instance.usage_rights_licenses_for_users(user_id)
        print("The response of UsageRightsApi->usage_rights_licenses_for_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsageRightsApi->usage_rights_licenses_for_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| Scope response to user_id | 

### Return type

[**List[License]**](License.md)

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

# **usage_rights_remove_usage_rights**
> usage_rights_remove_usage_rights(course_id, file_ids, folder_ids=folder_ids)

Remove usage rights

Removes copyright and license information associated with one or more files

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
    api_instance = canvas_lms_python_client.UsageRightsApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    file_ids = ['file_ids_example'] # List[str] | List of ids of files to remove associated usage rights from.
    folder_ids = ['folder_ids_example'] # List[str] | List of ids of folders. Usage rights will be removed from all files in these folders. (optional)

    try:
        # Remove usage rights
        await api_instance.usage_rights_remove_usage_rights(course_id, file_ids, folder_ids=folder_ids)
    except Exception as e:
        print("Exception when calling UsageRightsApi->usage_rights_remove_usage_rights: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **file_ids** | [**List[str]**](str.md)| List of ids of files to remove associated usage rights from. | 
 **folder_ids** | [**List[str]**](str.md)| List of ids of folders. Usage rights will be removed from all files in these folders. | [optional] 

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
**0** | Remove usage rights |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **usage_rights_remove_usage_rights_for_groups**
> usage_rights_remove_usage_rights_for_groups(group_id, file_ids, folder_ids=folder_ids)

Remove usage rights

Removes copyright and license information associated with one or more files

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
    api_instance = canvas_lms_python_client.UsageRightsApi(api_client)
    group_id = 'group_id_example' # str | Scope response to group_id
    file_ids = ['file_ids_example'] # List[str] | List of ids of files to remove associated usage rights from.
    folder_ids = ['folder_ids_example'] # List[str] | List of ids of folders. Usage rights will be removed from all files in these folders. (optional)

    try:
        # Remove usage rights
        await api_instance.usage_rights_remove_usage_rights_for_groups(group_id, file_ids, folder_ids=folder_ids)
    except Exception as e:
        print("Exception when calling UsageRightsApi->usage_rights_remove_usage_rights_for_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Scope response to group_id | 
 **file_ids** | [**List[str]**](str.md)| List of ids of files to remove associated usage rights from. | 
 **folder_ids** | [**List[str]**](str.md)| List of ids of folders. Usage rights will be removed from all files in these folders. | [optional] 

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
**0** | Remove usage rights |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **usage_rights_remove_usage_rights_for_users**
> usage_rights_remove_usage_rights_for_users(user_id, file_ids, folder_ids=folder_ids)

Remove usage rights

Removes copyright and license information associated with one or more files

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
    api_instance = canvas_lms_python_client.UsageRightsApi(api_client)
    user_id = 'user_id_example' # str | Scope response to user_id
    file_ids = ['file_ids_example'] # List[str] | List of ids of files to remove associated usage rights from.
    folder_ids = ['folder_ids_example'] # List[str] | List of ids of folders. Usage rights will be removed from all files in these folders. (optional)

    try:
        # Remove usage rights
        await api_instance.usage_rights_remove_usage_rights_for_users(user_id, file_ids, folder_ids=folder_ids)
    except Exception as e:
        print("Exception when calling UsageRightsApi->usage_rights_remove_usage_rights_for_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| Scope response to user_id | 
 **file_ids** | [**List[str]**](str.md)| List of ids of files to remove associated usage rights from. | 
 **folder_ids** | [**List[str]**](str.md)| List of ids of folders. Usage rights will be removed from all files in these folders. | [optional] 

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
**0** | Remove usage rights |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **usage_rights_set_usage_rights**
> UsageRights usage_rights_set_usage_rights(course_id, usage_rights_set_usage_rights_request=usage_rights_set_usage_rights_request)

Set usage rights

Sets copyright and license information for one or more files

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.usage_rights import UsageRights
from canvas_lms_python_client.models.usage_rights_set_usage_rights_request import UsageRightsSetUsageRightsRequest
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
    api_instance = canvas_lms_python_client.UsageRightsApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    usage_rights_set_usage_rights_request = canvas_lms_python_client.UsageRightsSetUsageRightsRequest() # UsageRightsSetUsageRightsRequest | Request body parameters (optional)

    try:
        # Set usage rights
        api_response = await api_instance.usage_rights_set_usage_rights(course_id, usage_rights_set_usage_rights_request=usage_rights_set_usage_rights_request)
        print("The response of UsageRightsApi->usage_rights_set_usage_rights:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsageRightsApi->usage_rights_set_usage_rights: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **usage_rights_set_usage_rights_request** | [**UsageRightsSetUsageRightsRequest**](UsageRightsSetUsageRightsRequest.md)| Request body parameters | [optional] 

### Return type

[**UsageRights**](UsageRights.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | UsageRights |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **usage_rights_set_usage_rights_for_groups**
> UsageRights usage_rights_set_usage_rights_for_groups(group_id, usage_rights_set_usage_rights_request=usage_rights_set_usage_rights_request)

Set usage rights

Sets copyright and license information for one or more files

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.usage_rights import UsageRights
from canvas_lms_python_client.models.usage_rights_set_usage_rights_request import UsageRightsSetUsageRightsRequest
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
    api_instance = canvas_lms_python_client.UsageRightsApi(api_client)
    group_id = 'group_id_example' # str | Scope response to group_id
    usage_rights_set_usage_rights_request = canvas_lms_python_client.UsageRightsSetUsageRightsRequest() # UsageRightsSetUsageRightsRequest | Request body parameters (optional)

    try:
        # Set usage rights
        api_response = await api_instance.usage_rights_set_usage_rights_for_groups(group_id, usage_rights_set_usage_rights_request=usage_rights_set_usage_rights_request)
        print("The response of UsageRightsApi->usage_rights_set_usage_rights_for_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsageRightsApi->usage_rights_set_usage_rights_for_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Scope response to group_id | 
 **usage_rights_set_usage_rights_request** | [**UsageRightsSetUsageRightsRequest**](UsageRightsSetUsageRightsRequest.md)| Request body parameters | [optional] 

### Return type

[**UsageRights**](UsageRights.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | UsageRights |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **usage_rights_set_usage_rights_for_users**
> UsageRights usage_rights_set_usage_rights_for_users(user_id, usage_rights_set_usage_rights_request=usage_rights_set_usage_rights_request)

Set usage rights

Sets copyright and license information for one or more files

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.usage_rights import UsageRights
from canvas_lms_python_client.models.usage_rights_set_usage_rights_request import UsageRightsSetUsageRightsRequest
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
    api_instance = canvas_lms_python_client.UsageRightsApi(api_client)
    user_id = 'user_id_example' # str | Scope response to user_id
    usage_rights_set_usage_rights_request = canvas_lms_python_client.UsageRightsSetUsageRightsRequest() # UsageRightsSetUsageRightsRequest | Request body parameters (optional)

    try:
        # Set usage rights
        api_response = await api_instance.usage_rights_set_usage_rights_for_users(user_id, usage_rights_set_usage_rights_request=usage_rights_set_usage_rights_request)
        print("The response of UsageRightsApi->usage_rights_set_usage_rights_for_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsageRightsApi->usage_rights_set_usage_rights_for_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| Scope response to user_id | 
 **usage_rights_set_usage_rights_request** | [**UsageRightsSetUsageRightsRequest**](UsageRightsSetUsageRightsRequest.md)| Request body parameters | [optional] 

### Return type

[**UsageRights**](UsageRights.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | UsageRights |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

