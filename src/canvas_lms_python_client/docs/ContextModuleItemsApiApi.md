# canvas_lms_python_client.ContextModuleItemsApiApi

All URIs are relative to *https://canvas.instructure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**context_module_items_api_create**](ContextModuleItemsApiApi.md#context_module_items_api_create) | **POST** /api/v1/courses/{course_id}/modules/{module_id}/items | Create a module item
[**context_module_items_api_destroy**](ContextModuleItemsApiApi.md#context_module_items_api_destroy) | **DELETE** /api/v1/courses/{course_id}/modules/{module_id}/items/{id} | Delete module item
[**context_module_items_api_index**](ContextModuleItemsApiApi.md#context_module_items_api_index) | **GET** /api/v1/courses/{course_id}/modules/{module_id}/items | List module items
[**context_module_items_api_item_sequence**](ContextModuleItemsApiApi.md#context_module_items_api_item_sequence) | **GET** /api/v1/courses/{course_id}/module_item_sequence | Get module item sequence
[**context_module_items_api_mark_as_done**](ContextModuleItemsApiApi.md#context_module_items_api_mark_as_done) | **PUT** /api/v1/courses/{course_id}/modules/{module_id}/items/{id}/done | Mark module item as done/not done
[**context_module_items_api_mark_item_read**](ContextModuleItemsApiApi.md#context_module_items_api_mark_item_read) | **POST** /api/v1/courses/{course_id}/modules/{module_id}/items/{id}/mark_read | Mark module item read
[**context_module_items_api_select_mastery_path**](ContextModuleItemsApiApi.md#context_module_items_api_select_mastery_path) | **POST** /api/v1/courses/{course_id}/modules/{module_id}/items/{id}/select_mastery_path | Select a mastery path
[**context_module_items_api_show**](ContextModuleItemsApiApi.md#context_module_items_api_show) | **GET** /api/v1/courses/{course_id}/modules/{module_id}/items/{id} | Show module item
[**context_module_items_api_update**](ContextModuleItemsApiApi.md#context_module_items_api_update) | **PUT** /api/v1/courses/{course_id}/modules/{module_id}/items/{id} | Update a module item


# **context_module_items_api_create**
> ModuleItem context_module_items_api_create(course_id, module_id, context_module_items_api_create_request=context_module_items_api_create_request)

Create a module item

Create and return a new module item

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.context_module_items_api_create_request import ContextModuleItemsApiCreateRequest
from canvas_lms_python_client.models.module_item import ModuleItem
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
    api_instance = canvas_lms_python_client.ContextModuleItemsApiApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    module_id = 'module_id_example' # str | Scope response to module_id
    context_module_items_api_create_request = canvas_lms_python_client.ContextModuleItemsApiCreateRequest() # ContextModuleItemsApiCreateRequest | Request body parameters  **Example Request:** ``` curl https://<canvas>/api/v1/courses/<course_id>/modules/<module_id>/items \\   -X POST \\   -H 'Authorization: Bearer <token>' \\   -d 'module_item[title]=module item' \\   -d 'module_item[type]=ExternalTool' \\   -d 'module_item[content_id]=10' \\   -d 'module_item[position]=2' \\   -d 'module_item[indent]=1' \\   -d 'module_item[new_tab]=true' \\   -d 'module_item[iframe][width]=300' \\   -d 'module_item[iframe][height]=200' ``` (optional)

    try:
        # Create a module item
        api_response = await api_instance.context_module_items_api_create(course_id, module_id, context_module_items_api_create_request=context_module_items_api_create_request)
        print("The response of ContextModuleItemsApiApi->context_module_items_api_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContextModuleItemsApiApi->context_module_items_api_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **module_id** | **str**| Scope response to module_id | 
 **context_module_items_api_create_request** | [**ContextModuleItemsApiCreateRequest**](ContextModuleItemsApiCreateRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl https://&lt;canvas&gt;/api/v1/courses/&lt;course_id&gt;/modules/&lt;module_id&gt;/items \\   -X POST \\   -H &#39;Authorization: Bearer &lt;token&gt;&#39; \\   -d &#39;module_item[title]&#x3D;module item&#39; \\   -d &#39;module_item[type]&#x3D;ExternalTool&#39; \\   -d &#39;module_item[content_id]&#x3D;10&#39; \\   -d &#39;module_item[position]&#x3D;2&#39; \\   -d &#39;module_item[indent]&#x3D;1&#39; \\   -d &#39;module_item[new_tab]&#x3D;true&#39; \\   -d &#39;module_item[iframe][width]&#x3D;300&#39; \\   -d &#39;module_item[iframe][height]&#x3D;200&#39; &#x60;&#x60;&#x60; | [optional] 

### Return type

[**ModuleItem**](ModuleItem.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | ModuleItem |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **context_module_items_api_destroy**
> ModuleItem context_module_items_api_destroy(course_id, id, module_id)

Delete module item

Delete a module item

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.module_item import ModuleItem
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
    api_instance = canvas_lms_python_client.ContextModuleItemsApiApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    id = 'id_example' # str | Scope response to id
    module_id = 'module_id_example' # str | Scope response to module_id

    try:
        # Delete module item
        api_response = await api_instance.context_module_items_api_destroy(course_id, id, module_id)
        print("The response of ContextModuleItemsApiApi->context_module_items_api_destroy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContextModuleItemsApiApi->context_module_items_api_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **id** | **str**| Scope response to id | 
 **module_id** | **str**| Scope response to module_id | 

### Return type

[**ModuleItem**](ModuleItem.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | ModuleItem |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **context_module_items_api_index**
> List[ModuleItem] context_module_items_api_index(course_id, module_id, include=include, search_term=search_term, student_id=student_id, page=page, per_page=per_page)

List module items

A paginated list of the items in a module

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.module_item import ModuleItem
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
    api_instance = canvas_lms_python_client.ContextModuleItemsApiApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    module_id = 'module_id_example' # str | Scope response to module_id
    include = ['include_example'] # List[str] | If included, will return additional details specific to the content associated with each item. Refer to the {api:Modules:Module%20Item Module Item specification} for more details. Includes standard lock information for each item. (optional)
    search_term = 'search_term_example' # str | The partial title of the items to match and return. (optional)
    student_id = 'student_id_example' # str | Returns module completion information for the student with this id. (optional)
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # List module items
        api_response = await api_instance.context_module_items_api_index(course_id, module_id, include=include, search_term=search_term, student_id=student_id, page=page, per_page=per_page)
        print("The response of ContextModuleItemsApiApi->context_module_items_api_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContextModuleItemsApiApi->context_module_items_api_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **module_id** | **str**| Scope response to module_id | 
 **include** | [**List[str]**](str.md)| If included, will return additional details specific to the content associated with each item. Refer to the {api:Modules:Module%20Item Module Item specification} for more details. Includes standard lock information for each item. | [optional] 
 **search_term** | **str**| The partial title of the items to match and return. | [optional] 
 **student_id** | **str**| Returns module completion information for the student with this id. | [optional] 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**List[ModuleItem]**](ModuleItem.md)

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

# **context_module_items_api_item_sequence**
> ModuleItemSequence context_module_items_api_item_sequence(course_id, asset_type=asset_type, asset_id=asset_id)

Get module item sequence

Given an asset in a course, find the ModuleItem it belongs to, the previous and next Module Items
in the course sequence, and also any applicable mastery path rules

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.module_item_sequence import ModuleItemSequence
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
    api_instance = canvas_lms_python_client.ContextModuleItemsApiApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    asset_type = 'asset_type_example' # str | The type of asset to find module sequence information for. Use the ModuleItem if it is known (e.g., the user navigated from a module item), since this will avoid ambiguity if the asset appears more than once in the module sequence. (optional)
    asset_id = 56 # int | The id of the asset (or the url in the case of a Page) (optional)

    try:
        # Get module item sequence
        api_response = await api_instance.context_module_items_api_item_sequence(course_id, asset_type=asset_type, asset_id=asset_id)
        print("The response of ContextModuleItemsApiApi->context_module_items_api_item_sequence:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContextModuleItemsApiApi->context_module_items_api_item_sequence: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **asset_type** | **str**| The type of asset to find module sequence information for. Use the ModuleItem if it is known (e.g., the user navigated from a module item), since this will avoid ambiguity if the asset appears more than once in the module sequence. | [optional] 
 **asset_id** | **int**| The id of the asset (or the url in the case of a Page) | [optional] 

### Return type

[**ModuleItemSequence**](ModuleItemSequence.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | ModuleItemSequence |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **context_module_items_api_mark_as_done**
> context_module_items_api_mark_as_done(course_id, id, module_id)

Mark module item as done/not done

Mark a module item as done/not done. Use HTTP method PUT to mark as done,
and DELETE to mark as not done.

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
    api_instance = canvas_lms_python_client.ContextModuleItemsApiApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    id = 'id_example' # str | Scope response to id
    module_id = 'module_id_example' # str | Scope response to module_id

    try:
        # Mark module item as done/not done
        await api_instance.context_module_items_api_mark_as_done(course_id, id, module_id)
    except Exception as e:
        print("Exception when calling ContextModuleItemsApiApi->context_module_items_api_mark_as_done: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **id** | **str**| Scope response to id | 
 **module_id** | **str**| Scope response to module_id | 

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
**0** | Mark module item as done/not done |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **context_module_items_api_mark_item_read**
> context_module_items_api_mark_item_read(course_id, id, module_id)

Mark module item read

Fulfills "must view" requirement for a module item. It is generally not necessary to do this explicitly,
but it is provided for applications that need to access external content directly (bypassing the html_url
redirect that normally allows Canvas to fulfill "must view" requirements).

This endpoint cannot be used to complete requirements on locked or unpublished module items.

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
    api_instance = canvas_lms_python_client.ContextModuleItemsApiApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    id = 'id_example' # str | Scope response to id
    module_id = 'module_id_example' # str | Scope response to module_id

    try:
        # Mark module item read
        await api_instance.context_module_items_api_mark_item_read(course_id, id, module_id)
    except Exception as e:
        print("Exception when calling ContextModuleItemsApiApi->context_module_items_api_mark_item_read: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **id** | **str**| Scope response to id | 
 **module_id** | **str**| Scope response to module_id | 

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
**0** | Mark module item read |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **context_module_items_api_select_mastery_path**
> context_module_items_api_select_mastery_path(course_id, id, module_id, context_module_items_api_select_mastery_path_request=context_module_items_api_select_mastery_path_request)

Select a mastery path

Select a mastery path when module item includes several possible paths.
Requires Mastery Paths feature to be enabled.  Returns a compound document
with the assignments included in the given path and any module items
related to those assignments

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.context_module_items_api_select_mastery_path_request import ContextModuleItemsApiSelectMasteryPathRequest
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
    api_instance = canvas_lms_python_client.ContextModuleItemsApiApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    id = 'id_example' # str | Scope response to id
    module_id = 'module_id_example' # str | Scope response to module_id
    context_module_items_api_select_mastery_path_request = canvas_lms_python_client.ContextModuleItemsApiSelectMasteryPathRequest() # ContextModuleItemsApiSelectMasteryPathRequest | Request body parameters  **Example Request:** ``` curl https://<canvas>/api/v1/courses/<course_id>/modules/<module_id>/items/<item_id>/select_master_path \\   -X POST \\   -H 'Authorization: Bearer <token>' \\   -d 'assignment_set_id=2992' ``` (optional)

    try:
        # Select a mastery path
        await api_instance.context_module_items_api_select_mastery_path(course_id, id, module_id, context_module_items_api_select_mastery_path_request=context_module_items_api_select_mastery_path_request)
    except Exception as e:
        print("Exception when calling ContextModuleItemsApiApi->context_module_items_api_select_mastery_path: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **id** | **str**| Scope response to id | 
 **module_id** | **str**| Scope response to module_id | 
 **context_module_items_api_select_mastery_path_request** | [**ContextModuleItemsApiSelectMasteryPathRequest**](ContextModuleItemsApiSelectMasteryPathRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl https://&lt;canvas&gt;/api/v1/courses/&lt;course_id&gt;/modules/&lt;module_id&gt;/items/&lt;item_id&gt;/select_master_path \\   -X POST \\   -H &#39;Authorization: Bearer &lt;token&gt;&#39; \\   -d &#39;assignment_set_id&#x3D;2992&#39; &#x60;&#x60;&#x60; | [optional] 

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
**0** | Select a mastery path |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **context_module_items_api_show**
> ModuleItem context_module_items_api_show(course_id, id, module_id, include=include, student_id=student_id)

Show module item

Get information about a single module item

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.module_item import ModuleItem
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
    api_instance = canvas_lms_python_client.ContextModuleItemsApiApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    id = 'id_example' # str | Scope response to id
    module_id = 'module_id_example' # str | Scope response to module_id
    include = ['include_example'] # List[str] | If included, will return additional details specific to the content associated with this item. Refer to the {api:Modules:Module%20Item Module Item specification} for more details. Includes standard lock information for each item. (optional)
    student_id = 'student_id_example' # str | Returns module completion information for the student with this id. (optional)

    try:
        # Show module item
        api_response = await api_instance.context_module_items_api_show(course_id, id, module_id, include=include, student_id=student_id)
        print("The response of ContextModuleItemsApiApi->context_module_items_api_show:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContextModuleItemsApiApi->context_module_items_api_show: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **id** | **str**| Scope response to id | 
 **module_id** | **str**| Scope response to module_id | 
 **include** | [**List[str]**](str.md)| If included, will return additional details specific to the content associated with this item. Refer to the {api:Modules:Module%20Item Module Item specification} for more details. Includes standard lock information for each item. | [optional] 
 **student_id** | **str**| Returns module completion information for the student with this id. | [optional] 

### Return type

[**ModuleItem**](ModuleItem.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | ModuleItem |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **context_module_items_api_update**
> ModuleItem context_module_items_api_update(course_id, id, module_id, context_module_items_api_update_request=context_module_items_api_update_request)

Update a module item

Update and return an existing module item

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.context_module_items_api_update_request import ContextModuleItemsApiUpdateRequest
from canvas_lms_python_client.models.module_item import ModuleItem
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
    api_instance = canvas_lms_python_client.ContextModuleItemsApiApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    id = 'id_example' # str | Scope response to id
    module_id = 'module_id_example' # str | Scope response to module_id
    context_module_items_api_update_request = canvas_lms_python_client.ContextModuleItemsApiUpdateRequest() # ContextModuleItemsApiUpdateRequest | Request body parameters  **Example Request:** ``` curl https://<canvas>/api/v1/courses/<course_id>/modules/<module_id>/items/<item_id> \\   -X PUT \\   -H 'Authorization: Bearer <token>' \\   -d 'module_item[position]=2' \\   -d 'module_item[indent]=1' \\   -d 'module_item[new_tab]=true' ``` (optional)

    try:
        # Update a module item
        api_response = await api_instance.context_module_items_api_update(course_id, id, module_id, context_module_items_api_update_request=context_module_items_api_update_request)
        print("The response of ContextModuleItemsApiApi->context_module_items_api_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContextModuleItemsApiApi->context_module_items_api_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **id** | **str**| Scope response to id | 
 **module_id** | **str**| Scope response to module_id | 
 **context_module_items_api_update_request** | [**ContextModuleItemsApiUpdateRequest**](ContextModuleItemsApiUpdateRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl https://&lt;canvas&gt;/api/v1/courses/&lt;course_id&gt;/modules/&lt;module_id&gt;/items/&lt;item_id&gt; \\   -X PUT \\   -H &#39;Authorization: Bearer &lt;token&gt;&#39; \\   -d &#39;module_item[position]&#x3D;2&#39; \\   -d &#39;module_item[indent]&#x3D;1&#39; \\   -d &#39;module_item[new_tab]&#x3D;true&#39; &#x60;&#x60;&#x60; | [optional] 

### Return type

[**ModuleItem**](ModuleItem.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | ModuleItem |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

