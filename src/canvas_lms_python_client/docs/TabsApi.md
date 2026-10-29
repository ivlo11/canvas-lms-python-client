# canvas_lms_python_client.TabsApi

All URIs are relative to *https://canvas.instructure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tabs_index**](TabsApi.md#tabs_index) | **GET** /api/v1/accounts/{account_id}/tabs | List available tabs for a course or group
[**tabs_index_for_courses**](TabsApi.md#tabs_index_for_courses) | **GET** /api/v1/courses/{course_id}/tabs | List available tabs for a course or group
[**tabs_index_for_groups**](TabsApi.md#tabs_index_for_groups) | **GET** /api/v1/groups/{group_id}/tabs | List available tabs for a course or group
[**tabs_index_for_users**](TabsApi.md#tabs_index_for_users) | **GET** /api/v1/users/{user_id}/tabs | List available tabs for a course or group
[**tabs_update**](TabsApi.md#tabs_update) | **PUT** /api/v1/courses/{course_id}/tabs/{tab_id} | Update a tab for a course


# **tabs_index**
> tabs_index(account_id, include=include)

List available tabs for a course or group

Returns a paginated list of navigation tabs available in the current context.

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
    api_instance = canvas_lms_python_client.TabsApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    include = ['include_example'] # List[str] | - \"course_subject_tabs\": Optional flag to return the tabs associated with a canvas_for_elementary subject course's   home page instead of the typical sidebar navigation. Only takes effect if this request is for a course context   in a canvas_for_elementary-enabled account or sub-account. (optional)

    try:
        # List available tabs for a course or group
        await api_instance.tabs_index(account_id, include=include)
    except Exception as e:
        print("Exception when calling TabsApi->tabs_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **include** | [**List[str]**](str.md)| - \&quot;course_subject_tabs\&quot;: Optional flag to return the tabs associated with a canvas_for_elementary subject course&#39;s   home page instead of the typical sidebar navigation. Only takes effect if this request is for a course context   in a canvas_for_elementary-enabled account or sub-account. | [optional] 

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
**0** | List available tabs for a course or group |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tabs_index_for_courses**
> tabs_index_for_courses(course_id, include=include)

List available tabs for a course or group

Returns a paginated list of navigation tabs available in the current context.

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
    api_instance = canvas_lms_python_client.TabsApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    include = ['include_example'] # List[str] | - \"course_subject_tabs\": Optional flag to return the tabs associated with a canvas_for_elementary subject course's   home page instead of the typical sidebar navigation. Only takes effect if this request is for a course context   in a canvas_for_elementary-enabled account or sub-account. (optional)

    try:
        # List available tabs for a course or group
        await api_instance.tabs_index_for_courses(course_id, include=include)
    except Exception as e:
        print("Exception when calling TabsApi->tabs_index_for_courses: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **include** | [**List[str]**](str.md)| - \&quot;course_subject_tabs\&quot;: Optional flag to return the tabs associated with a canvas_for_elementary subject course&#39;s   home page instead of the typical sidebar navigation. Only takes effect if this request is for a course context   in a canvas_for_elementary-enabled account or sub-account. | [optional] 

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
**0** | List available tabs for a course or group |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tabs_index_for_groups**
> tabs_index_for_groups(group_id, include=include)

List available tabs for a course or group

Returns a paginated list of navigation tabs available in the current context.

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
    api_instance = canvas_lms_python_client.TabsApi(api_client)
    group_id = 'group_id_example' # str | Scope response to group_id
    include = ['include_example'] # List[str] | - \"course_subject_tabs\": Optional flag to return the tabs associated with a canvas_for_elementary subject course's   home page instead of the typical sidebar navigation. Only takes effect if this request is for a course context   in a canvas_for_elementary-enabled account or sub-account. (optional)

    try:
        # List available tabs for a course or group
        await api_instance.tabs_index_for_groups(group_id, include=include)
    except Exception as e:
        print("Exception when calling TabsApi->tabs_index_for_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Scope response to group_id | 
 **include** | [**List[str]**](str.md)| - \&quot;course_subject_tabs\&quot;: Optional flag to return the tabs associated with a canvas_for_elementary subject course&#39;s   home page instead of the typical sidebar navigation. Only takes effect if this request is for a course context   in a canvas_for_elementary-enabled account or sub-account. | [optional] 

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
**0** | List available tabs for a course or group |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tabs_index_for_users**
> tabs_index_for_users(user_id, include=include)

List available tabs for a course or group

Returns a paginated list of navigation tabs available in the current context.

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
    api_instance = canvas_lms_python_client.TabsApi(api_client)
    user_id = 'user_id_example' # str | Scope response to user_id
    include = ['include_example'] # List[str] | - \"course_subject_tabs\": Optional flag to return the tabs associated with a canvas_for_elementary subject course's   home page instead of the typical sidebar navigation. Only takes effect if this request is for a course context   in a canvas_for_elementary-enabled account or sub-account. (optional)

    try:
        # List available tabs for a course or group
        await api_instance.tabs_index_for_users(user_id, include=include)
    except Exception as e:
        print("Exception when calling TabsApi->tabs_index_for_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| Scope response to user_id | 
 **include** | [**List[str]**](str.md)| - \&quot;course_subject_tabs\&quot;: Optional flag to return the tabs associated with a canvas_for_elementary subject course&#39;s   home page instead of the typical sidebar navigation. Only takes effect if this request is for a course context   in a canvas_for_elementary-enabled account or sub-account. | [optional] 

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
**0** | List available tabs for a course or group |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tabs_update**
> Tab tabs_update(course_id, tab_id, tabs_update_request=tabs_update_request)

Update a tab for a course

Home and Settings tabs are not manageable, and can't be hidden or moved

Returns a tab object

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.tab import Tab
from canvas_lms_python_client.models.tabs_update_request import TabsUpdateRequest
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
    api_instance = canvas_lms_python_client.TabsApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    tab_id = 'tab_id_example' # str | Scope response to tab_id
    tabs_update_request = canvas_lms_python_client.TabsUpdateRequest() # TabsUpdateRequest | Request body parameters  **Example Request:** ``` curl https://<canvas>/api/v1/courses/<course_id>/tabs/tab_id \\   -X PUT \\   -H 'Authorization: Bearer <token>' \\   -d 'hidden=true' \\   -d 'position=2' // 1 based ``` (optional)

    try:
        # Update a tab for a course
        api_response = await api_instance.tabs_update(course_id, tab_id, tabs_update_request=tabs_update_request)
        print("The response of TabsApi->tabs_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TabsApi->tabs_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **tab_id** | **str**| Scope response to tab_id | 
 **tabs_update_request** | [**TabsUpdateRequest**](TabsUpdateRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl https://&lt;canvas&gt;/api/v1/courses/&lt;course_id&gt;/tabs/tab_id \\   -X PUT \\   -H &#39;Authorization: Bearer &lt;token&gt;&#39; \\   -d &#39;hidden&#x3D;true&#39; \\   -d &#39;position&#x3D;2&#39; // 1 based &#x60;&#x60;&#x60; | [optional] 

### Return type

[**Tab**](Tab.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Tab |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

