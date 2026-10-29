# canvas_lms_python_client.ContextModulesApiApi

All URIs are relative to *https://canvas.instructure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**context_modules_api_create**](ContextModulesApiApi.md#context_modules_api_create) | **POST** /api/v1/courses/{course_id}/modules | Create a module
[**context_modules_api_destroy**](ContextModulesApiApi.md#context_modules_api_destroy) | **DELETE** /api/v1/courses/{course_id}/modules/{id} | Delete module
[**context_modules_api_index**](ContextModulesApiApi.md#context_modules_api_index) | **GET** /api/v1/courses/{course_id}/modules | List modules
[**context_modules_api_relock**](ContextModulesApiApi.md#context_modules_api_relock) | **PUT** /api/v1/courses/{course_id}/modules/{id}/relock | Re-lock module progressions
[**context_modules_api_show**](ContextModulesApiApi.md#context_modules_api_show) | **GET** /api/v1/courses/{course_id}/modules/{id} | Show module
[**context_modules_api_update**](ContextModulesApiApi.md#context_modules_api_update) | **PUT** /api/v1/courses/{course_id}/modules/{id} | Update a module


# **context_modules_api_create**
> Module context_modules_api_create(course_id, context_modules_api_create_request=context_modules_api_create_request)

Create a module

Create and return a new module

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.context_modules_api_create_request import ContextModulesApiCreateRequest
from canvas_lms_python_client.models.module import Module
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
    api_instance = canvas_lms_python_client.ContextModulesApiApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    context_modules_api_create_request = canvas_lms_python_client.ContextModulesApiCreateRequest() # ContextModulesApiCreateRequest | Request body parameters  **Example Request:** ``` curl https://<canvas>/api/v1/courses/<course_id>/modules \\   -X POST \\   -H 'Authorization: Bearer <token>' \\   -d 'module[name]=module' \\   -d 'module[position]=2' \\   -d 'module[prerequisite_module_ids][]=121' \\   -d 'module[prerequisite_module_ids][]=122' ``` (optional)

    try:
        # Create a module
        api_response = await api_instance.context_modules_api_create(course_id, context_modules_api_create_request=context_modules_api_create_request)
        print("The response of ContextModulesApiApi->context_modules_api_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContextModulesApiApi->context_modules_api_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **context_modules_api_create_request** | [**ContextModulesApiCreateRequest**](ContextModulesApiCreateRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl https://&lt;canvas&gt;/api/v1/courses/&lt;course_id&gt;/modules \\   -X POST \\   -H &#39;Authorization: Bearer &lt;token&gt;&#39; \\   -d &#39;module[name]&#x3D;module&#39; \\   -d &#39;module[position]&#x3D;2&#39; \\   -d &#39;module[prerequisite_module_ids][]&#x3D;121&#39; \\   -d &#39;module[prerequisite_module_ids][]&#x3D;122&#39; &#x60;&#x60;&#x60; | [optional] 

### Return type

[**Module**](Module.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Module |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **context_modules_api_destroy**
> Module context_modules_api_destroy(course_id, id)

Delete module

Delete a module

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.module import Module
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
    api_instance = canvas_lms_python_client.ContextModulesApiApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    id = 'id_example' # str | Scope response to id

    try:
        # Delete module
        api_response = await api_instance.context_modules_api_destroy(course_id, id)
        print("The response of ContextModulesApiApi->context_modules_api_destroy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContextModulesApiApi->context_modules_api_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **id** | **str**| Scope response to id | 

### Return type

[**Module**](Module.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Module |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **context_modules_api_index**
> List[Module] context_modules_api_index(course_id, include=include, search_term=search_term, student_id=student_id, page=page, per_page=per_page)

List modules

A paginated list of the modules in a course

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.module import Module
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
    api_instance = canvas_lms_python_client.ContextModulesApiApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    include = ['include_example'] # List[str] | - \"items\": Return module items inline if possible.   This parameter suggests that Canvas return module items directly   in the Module object JSON, to avoid having to make separate API   requests for each module when enumerating modules and items. Canvas   is free to omit 'items' for any particular module if it deems them   too numerous to return inline. Callers must be prepared to use the   {api:ContextModuleItemsApiController#index List Module Items API}   if items are not returned. - \"content_details\": Requires 'items'. Returns additional   details with module items specific to their associated content items.   Includes standard lock information for each item. (optional)
    search_term = 'search_term_example' # str | The partial name of the modules (and module items, if 'items' is specified with include[]) to match and return. (optional)
    student_id = 'student_id_example' # str | Returns module completion information for the student with this id. (optional)
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # List modules
        api_response = await api_instance.context_modules_api_index(course_id, include=include, search_term=search_term, student_id=student_id, page=page, per_page=per_page)
        print("The response of ContextModulesApiApi->context_modules_api_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContextModulesApiApi->context_modules_api_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **include** | [**List[str]**](str.md)| - \&quot;items\&quot;: Return module items inline if possible.   This parameter suggests that Canvas return module items directly   in the Module object JSON, to avoid having to make separate API   requests for each module when enumerating modules and items. Canvas   is free to omit &#39;items&#39; for any particular module if it deems them   too numerous to return inline. Callers must be prepared to use the   {api:ContextModuleItemsApiController#index List Module Items API}   if items are not returned. - \&quot;content_details\&quot;: Requires &#39;items&#39;. Returns additional   details with module items specific to their associated content items.   Includes standard lock information for each item. | [optional] 
 **search_term** | **str**| The partial name of the modules (and module items, if &#39;items&#39; is specified with include[]) to match and return. | [optional] 
 **student_id** | **str**| Returns module completion information for the student with this id. | [optional] 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**List[Module]**](Module.md)

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

# **context_modules_api_relock**
> Module context_modules_api_relock(course_id, id)

Re-lock module progressions

Resets module progressions to their default locked state and
recalculates them based on the current requirements.

Adding progression requirements to an active course will not lock students
out of modules they have already unlocked unless this action is called.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.module import Module
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
    api_instance = canvas_lms_python_client.ContextModulesApiApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    id = 'id_example' # str | Scope response to id

    try:
        # Re-lock module progressions
        api_response = await api_instance.context_modules_api_relock(course_id, id)
        print("The response of ContextModulesApiApi->context_modules_api_relock:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContextModulesApiApi->context_modules_api_relock: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **id** | **str**| Scope response to id | 

### Return type

[**Module**](Module.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Module |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **context_modules_api_show**
> Module context_modules_api_show(course_id, id, include=include, student_id=student_id)

Show module

Get information about a single module

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.module import Module
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
    api_instance = canvas_lms_python_client.ContextModulesApiApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    id = 'id_example' # str | Scope response to id
    include = ['include_example'] # List[str] | - \"items\": Return module items inline if possible.   This parameter suggests that Canvas return module items directly   in the Module object JSON, to avoid having to make separate API   requests for each module when enumerating modules and items. Canvas   is free to omit 'items' for any particular module if it deems them   too numerous to return inline. Callers must be prepared to use the   {api:ContextModuleItemsApiController#index List Module Items API}   if items are not returned. - \"content_details\": Requires 'items'. Returns additional   details with module items specific to their associated content items.   Includes standard lock information for each item. (optional)
    student_id = 'student_id_example' # str | Returns module completion information for the student with this id. (optional)

    try:
        # Show module
        api_response = await api_instance.context_modules_api_show(course_id, id, include=include, student_id=student_id)
        print("The response of ContextModulesApiApi->context_modules_api_show:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContextModulesApiApi->context_modules_api_show: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **id** | **str**| Scope response to id | 
 **include** | [**List[str]**](str.md)| - \&quot;items\&quot;: Return module items inline if possible.   This parameter suggests that Canvas return module items directly   in the Module object JSON, to avoid having to make separate API   requests for each module when enumerating modules and items. Canvas   is free to omit &#39;items&#39; for any particular module if it deems them   too numerous to return inline. Callers must be prepared to use the   {api:ContextModuleItemsApiController#index List Module Items API}   if items are not returned. - \&quot;content_details\&quot;: Requires &#39;items&#39;. Returns additional   details with module items specific to their associated content items.   Includes standard lock information for each item. | [optional] 
 **student_id** | **str**| Returns module completion information for the student with this id. | [optional] 

### Return type

[**Module**](Module.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Module |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **context_modules_api_update**
> Module context_modules_api_update(course_id, id, context_modules_api_update_request=context_modules_api_update_request)

Update a module

Update and return an existing module

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.context_modules_api_update_request import ContextModulesApiUpdateRequest
from canvas_lms_python_client.models.module import Module
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
    api_instance = canvas_lms_python_client.ContextModulesApiApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    id = 'id_example' # str | Scope response to id
    context_modules_api_update_request = canvas_lms_python_client.ContextModulesApiUpdateRequest() # ContextModulesApiUpdateRequest | Request body parameters  **Example Request:** ``` curl https://<canvas>/api/v1/courses/<course_id>/modules/<module_id> \\   -X PUT \\   -H 'Authorization: Bearer <token>' \\   -d 'module[name]=module' \\   -d 'module[position]=2' \\   -d 'module[prerequisite_module_ids][]=121' \\   -d 'module[prerequisite_module_ids][]=122' ``` (optional)

    try:
        # Update a module
        api_response = await api_instance.context_modules_api_update(course_id, id, context_modules_api_update_request=context_modules_api_update_request)
        print("The response of ContextModulesApiApi->context_modules_api_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContextModulesApiApi->context_modules_api_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **id** | **str**| Scope response to id | 
 **context_modules_api_update_request** | [**ContextModulesApiUpdateRequest**](ContextModulesApiUpdateRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl https://&lt;canvas&gt;/api/v1/courses/&lt;course_id&gt;/modules/&lt;module_id&gt; \\   -X PUT \\   -H &#39;Authorization: Bearer &lt;token&gt;&#39; \\   -d &#39;module[name]&#x3D;module&#39; \\   -d &#39;module[position]&#x3D;2&#39; \\   -d &#39;module[prerequisite_module_ids][]&#x3D;121&#39; \\   -d &#39;module[prerequisite_module_ids][]&#x3D;122&#39; &#x60;&#x60;&#x60; | [optional] 

### Return type

[**Module**](Module.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Module |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

