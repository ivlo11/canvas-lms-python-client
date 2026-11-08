# canvas_lms_python_client.ExternalToolsApi

All URIs are relative to *https://canvas.instructure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**external_tools_add_top_nav_favorite**](ExternalToolsApi.md#external_tools_add_top_nav_favorite) | **POST** /api/v1/accounts/{account_id}/external_tools/top_nav_favorites/{id} | Add tool to Top Navigation Favorites
[**external_tools_all_visible_nav_tools**](ExternalToolsApi.md#external_tools_all_visible_nav_tools) | **GET** /api/v1/external_tools/visible_course_nav_tools | Get visible course navigation tools
[**external_tools_create**](ExternalToolsApi.md#external_tools_create) | **POST** /api/v1/courses/{course_id}/external_tools | Create an external tool
[**external_tools_create_for_accounts**](ExternalToolsApi.md#external_tools_create_for_accounts) | **POST** /api/v1/accounts/{account_id}/external_tools | Create an external tool
[**external_tools_destroy**](ExternalToolsApi.md#external_tools_destroy) | **DELETE** /api/v1/courses/{course_id}/external_tools/{external_tool_id} | Delete an external tool
[**external_tools_destroy_for_accounts**](ExternalToolsApi.md#external_tools_destroy_for_accounts) | **DELETE** /api/v1/accounts/{account_id}/external_tools/{external_tool_id} | Delete an external tool
[**external_tools_generate_sessionless_launch**](ExternalToolsApi.md#external_tools_generate_sessionless_launch) | **GET** /api/v1/courses/{course_id}/external_tools/sessionless_launch | Get a sessionless launch url for an external tool.
[**external_tools_generate_sessionless_launch_for_accounts**](ExternalToolsApi.md#external_tools_generate_sessionless_launch_for_accounts) | **GET** /api/v1/accounts/{account_id}/external_tools/sessionless_launch | Get a sessionless launch url for an external tool.
[**external_tools_index**](ExternalToolsApi.md#external_tools_index) | **GET** /api/v1/courses/{course_id}/external_tools | List external tools
[**external_tools_index_for_accounts**](ExternalToolsApi.md#external_tools_index_for_accounts) | **GET** /api/v1/accounts/{account_id}/external_tools | List external tools
[**external_tools_index_for_groups**](ExternalToolsApi.md#external_tools_index_for_groups) | **GET** /api/v1/groups/{group_id}/external_tools | List external tools
[**external_tools_mark_rce_favorite**](ExternalToolsApi.md#external_tools_mark_rce_favorite) | **POST** /api/v1/accounts/{account_id}/external_tools/rce_favorites/{id} | Mark tool as RCE Favorite
[**external_tools_remove_top_nav_favorite**](ExternalToolsApi.md#external_tools_remove_top_nav_favorite) | **DELETE** /api/v1/accounts/{account_id}/external_tools/top_nav_favorites/{id} | Remove tool from Top Navigation Favorites
[**external_tools_show**](ExternalToolsApi.md#external_tools_show) | **GET** /api/v1/courses/{course_id}/external_tools/{external_tool_id} | Get a single external tool
[**external_tools_show_for_accounts**](ExternalToolsApi.md#external_tools_show_for_accounts) | **GET** /api/v1/accounts/{account_id}/external_tools/{external_tool_id} | Get a single external tool
[**external_tools_unmark_rce_favorite**](ExternalToolsApi.md#external_tools_unmark_rce_favorite) | **DELETE** /api/v1/accounts/{account_id}/external_tools/rce_favorites/{id} | Unmark tool as RCE Favorite
[**external_tools_update**](ExternalToolsApi.md#external_tools_update) | **PUT** /api/v1/courses/{course_id}/external_tools/{external_tool_id} | Edit an external tool
[**external_tools_update_for_accounts**](ExternalToolsApi.md#external_tools_update_for_accounts) | **PUT** /api/v1/accounts/{account_id}/external_tools/{external_tool_id} | Edit an external tool
[**external_tools_visible_course_nav_tools**](ExternalToolsApi.md#external_tools_visible_course_nav_tools) | **GET** /api/v1/courses/{course_id}/external_tools/visible_course_nav_tools | Get visible course navigation tools for a single course


# **external_tools_add_top_nav_favorite**
> external_tools_add_top_nav_favorite(account_id, id)

Add tool to Top Navigation Favorites

Adds a dedicated button in Top Navigation for the specified tool for the given account.
Cannot set more than 2 top_navigation Favorites.

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
    api_instance = canvas_lms_python_client.ExternalToolsApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    id = 'id_example' # str | Scope response to id

    try:
        # Add tool to Top Navigation Favorites
        await api_instance.external_tools_add_top_nav_favorite(account_id, id)
    except Exception as e:
        print("Exception when calling ExternalToolsApi->external_tools_add_top_nav_favorite: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **id** | **str**| Scope response to id | 

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
**0** | Add tool to Top Navigation Favorites |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **external_tools_all_visible_nav_tools**
> List[ContextExternalTool] external_tools_all_visible_nav_tools(context_codes)

Get visible course navigation tools

Get a list of external tools with the course_navigation placement that have not been hidden in
course settings and whose visibility settings apply to the requesting user. These tools are the
same that appear in the course navigation.

The response format is the same as for List external tools, but with additional context_id and
context_name fields on each element in the array.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.context_external_tool import ContextExternalTool
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
    api_instance = canvas_lms_python_client.ExternalToolsApi(api_client)
    context_codes = ['context_codes_example'] # List[str] | List of context_codes to retrieve visible course nav tools for (for example, +course_123+). Only courses are presently supported.

    try:
        # Get visible course navigation tools
        api_response = await api_instance.external_tools_all_visible_nav_tools(context_codes)
        print("The response of ExternalToolsApi->external_tools_all_visible_nav_tools:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExternalToolsApi->external_tools_all_visible_nav_tools: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **context_codes** | [**List[str]**](str.md)| List of context_codes to retrieve visible course nav tools for (for example, +course_123+). Only courses are presently supported. | 

### Return type

[**List[ContextExternalTool]**](ContextExternalTool.md)

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

# **external_tools_create**
> ContextExternalTool external_tools_create(course_id, external_tools_create_request=external_tools_create_request)

Create an external tool

Create an external tool in the specified course/account.
The created tool will be returned, see the "show" endpoint for an example.
If a client ID is supplied canvas will attempt to create a context external
tool using the LTI 1.3 standard.

See the <a href="file.lti_dev_key_config.html#placements-params">Placements Documentation</a> for more information on what
placements are available, the possible fields, and their accepted values.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.context_external_tool import ContextExternalTool
from canvas_lms_python_client.models.external_tools_create_request import ExternalToolsCreateRequest
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
    api_instance = canvas_lms_python_client.ExternalToolsApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    external_tools_create_request = canvas_lms_python_client.ExternalToolsCreateRequest() # ExternalToolsCreateRequest | Request body parameters  **Example Request:** ``` This would create a tool on this course with two custom fields and a course navigation tab curl -X POST 'https://<canvas>/api/v1/courses/<course_id>/external_tools' \\      -H \"Authorization: Bearer <token>\" \\      -F 'name=LTI Example' \\      -F 'consumer_key=asdfg' \\      -F 'shared_secret=lkjh' \\      -F 'url=https://example.com/ims/lti' \\      -F 'privacy_level=name_only' \\      -F 'custom_fields[key1]=value1' \\      -F 'custom_fields[key2]=value2' \\      -F 'course_navigation[text]=Course Materials' \\      -F 'course_navigation[enabled]=true' ``` (optional)

    try:
        # Create an external tool
        api_response = await api_instance.external_tools_create(course_id, external_tools_create_request=external_tools_create_request)
        print("The response of ExternalToolsApi->external_tools_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExternalToolsApi->external_tools_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **external_tools_create_request** | [**ExternalToolsCreateRequest**](ExternalToolsCreateRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; This would create a tool on this course with two custom fields and a course navigation tab curl -X POST &#39;https://&lt;canvas&gt;/api/v1/courses/&lt;course_id&gt;/external_tools&#39; \\      -H \&quot;Authorization: Bearer &lt;token&gt;\&quot; \\      -F &#39;name&#x3D;LTI Example&#39; \\      -F &#39;consumer_key&#x3D;asdfg&#39; \\      -F &#39;shared_secret&#x3D;lkjh&#39; \\      -F &#39;url&#x3D;https://example.com/ims/lti&#39; \\      -F &#39;privacy_level&#x3D;name_only&#39; \\      -F &#39;custom_fields[key1]&#x3D;value1&#39; \\      -F &#39;custom_fields[key2]&#x3D;value2&#39; \\      -F &#39;course_navigation[text]&#x3D;Course Materials&#39; \\      -F &#39;course_navigation[enabled]&#x3D;true&#39; &#x60;&#x60;&#x60; | [optional] 

### Return type

[**ContextExternalTool**](ContextExternalTool.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | ContextExternalTool |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **external_tools_create_for_accounts**
> ContextExternalTool external_tools_create_for_accounts(account_id, external_tools_create_request=external_tools_create_request)

Create an external tool

Create an external tool in the specified course/account.
The created tool will be returned, see the "show" endpoint for an example.
If a client ID is supplied canvas will attempt to create a context external
tool using the LTI 1.3 standard.

See the <a href="file.lti_dev_key_config.html#placements-params">Placements Documentation</a> for more information on what
placements are available, the possible fields, and their accepted values.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.context_external_tool import ContextExternalTool
from canvas_lms_python_client.models.external_tools_create_request import ExternalToolsCreateRequest
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
    api_instance = canvas_lms_python_client.ExternalToolsApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    external_tools_create_request = canvas_lms_python_client.ExternalToolsCreateRequest() # ExternalToolsCreateRequest | Request body parameters  **Example Request:** ``` This would create a tool on this course with two custom fields and a course navigation tab curl -X POST 'https://<canvas>/api/v1/courses/<course_id>/external_tools' \\      -H \"Authorization: Bearer <token>\" \\      -F 'name=LTI Example' \\      -F 'consumer_key=asdfg' \\      -F 'shared_secret=lkjh' \\      -F 'url=https://example.com/ims/lti' \\      -F 'privacy_level=name_only' \\      -F 'custom_fields[key1]=value1' \\      -F 'custom_fields[key2]=value2' \\      -F 'course_navigation[text]=Course Materials' \\      -F 'course_navigation[enabled]=true' ``` (optional)

    try:
        # Create an external tool
        api_response = await api_instance.external_tools_create_for_accounts(account_id, external_tools_create_request=external_tools_create_request)
        print("The response of ExternalToolsApi->external_tools_create_for_accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExternalToolsApi->external_tools_create_for_accounts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **external_tools_create_request** | [**ExternalToolsCreateRequest**](ExternalToolsCreateRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; This would create a tool on this course with two custom fields and a course navigation tab curl -X POST &#39;https://&lt;canvas&gt;/api/v1/courses/&lt;course_id&gt;/external_tools&#39; \\      -H \&quot;Authorization: Bearer &lt;token&gt;\&quot; \\      -F &#39;name&#x3D;LTI Example&#39; \\      -F &#39;consumer_key&#x3D;asdfg&#39; \\      -F &#39;shared_secret&#x3D;lkjh&#39; \\      -F &#39;url&#x3D;https://example.com/ims/lti&#39; \\      -F &#39;privacy_level&#x3D;name_only&#39; \\      -F &#39;custom_fields[key1]&#x3D;value1&#39; \\      -F &#39;custom_fields[key2]&#x3D;value2&#39; \\      -F &#39;course_navigation[text]&#x3D;Course Materials&#39; \\      -F &#39;course_navigation[enabled]&#x3D;true&#39; &#x60;&#x60;&#x60; | [optional] 

### Return type

[**ContextExternalTool**](ContextExternalTool.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | ContextExternalTool |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **external_tools_destroy**
> ContextExternalTool external_tools_destroy(course_id, external_tool_id)

Delete an external tool

Remove the specified external tool

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.context_external_tool import ContextExternalTool
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
    api_instance = canvas_lms_python_client.ExternalToolsApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    external_tool_id = 'external_tool_id_example' # str | Scope response to external_tool_id

    try:
        # Delete an external tool
        api_response = await api_instance.external_tools_destroy(course_id, external_tool_id)
        print("The response of ExternalToolsApi->external_tools_destroy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExternalToolsApi->external_tools_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **external_tool_id** | **str**| Scope response to external_tool_id | 

### Return type

[**ContextExternalTool**](ContextExternalTool.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | ContextExternalTool |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **external_tools_destroy_for_accounts**
> ContextExternalTool external_tools_destroy_for_accounts(account_id, external_tool_id)

Delete an external tool

Remove the specified external tool

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.context_external_tool import ContextExternalTool
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
    api_instance = canvas_lms_python_client.ExternalToolsApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    external_tool_id = 'external_tool_id_example' # str | Scope response to external_tool_id

    try:
        # Delete an external tool
        api_response = await api_instance.external_tools_destroy_for_accounts(account_id, external_tool_id)
        print("The response of ExternalToolsApi->external_tools_destroy_for_accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExternalToolsApi->external_tools_destroy_for_accounts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **external_tool_id** | **str**| Scope response to external_tool_id | 

### Return type

[**ContextExternalTool**](ContextExternalTool.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | ContextExternalTool |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **external_tools_generate_sessionless_launch**
> external_tools_generate_sessionless_launch(course_id, id=id, url=url, assignment_id=assignment_id, module_item_id=module_item_id, launch_type=launch_type, resource_link_lookup_uuid=resource_link_lookup_uuid)

Get a sessionless launch url for an external tool.

Returns a sessionless launch url for an external tool.
Prefers the resource_link_lookup_uuid, but defaults to the other passed
  parameters id, url, and launch_type

NOTE: Either the resource_link_lookup_uuid, id, or url must be provided unless launch_type is assessment or module_item.

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
    api_instance = canvas_lms_python_client.ExternalToolsApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    id = 'id_example' # str | The external id of the tool to launch. (optional)
    url = 'url_example' # str | The LTI launch url for the external tool. (optional)
    assignment_id = 'assignment_id_example' # str | The assignment id for an assignment launch. Required if launch_type is set to \"assessment\". (optional)
    module_item_id = 'module_item_id_example' # str | The assignment id for a module item launch. Required if launch_type is set to \"module_item\". (optional)
    launch_type = 'launch_type_example' # str | The type of launch to perform on the external tool. Placement names (eg. \"course_navigation\") can also be specified to use the custom launch url for that placement; if done, the tool id must be provided. (optional)
    resource_link_lookup_uuid = 'resource_link_lookup_uuid_example' # str | The identifier to lookup a resource link. (optional)

    try:
        # Get a sessionless launch url for an external tool.
        await api_instance.external_tools_generate_sessionless_launch(course_id, id=id, url=url, assignment_id=assignment_id, module_item_id=module_item_id, launch_type=launch_type, resource_link_lookup_uuid=resource_link_lookup_uuid)
    except Exception as e:
        print("Exception when calling ExternalToolsApi->external_tools_generate_sessionless_launch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **id** | **str**| The external id of the tool to launch. | [optional] 
 **url** | **str**| The LTI launch url for the external tool. | [optional] 
 **assignment_id** | **str**| The assignment id for an assignment launch. Required if launch_type is set to \&quot;assessment\&quot;. | [optional] 
 **module_item_id** | **str**| The assignment id for a module item launch. Required if launch_type is set to \&quot;module_item\&quot;. | [optional] 
 **launch_type** | **str**| The type of launch to perform on the external tool. Placement names (eg. \&quot;course_navigation\&quot;) can also be specified to use the custom launch url for that placement; if done, the tool id must be provided. | [optional] 
 **resource_link_lookup_uuid** | **str**| The identifier to lookup a resource link. | [optional] 

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
**0** | Get a sessionless launch url for an external tool. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **external_tools_generate_sessionless_launch_for_accounts**
> external_tools_generate_sessionless_launch_for_accounts(account_id, id=id, url=url, assignment_id=assignment_id, module_item_id=module_item_id, launch_type=launch_type, resource_link_lookup_uuid=resource_link_lookup_uuid)

Get a sessionless launch url for an external tool.

Returns a sessionless launch url for an external tool.
Prefers the resource_link_lookup_uuid, but defaults to the other passed
  parameters id, url, and launch_type

NOTE: Either the resource_link_lookup_uuid, id, or url must be provided unless launch_type is assessment or module_item.

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
    api_instance = canvas_lms_python_client.ExternalToolsApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    id = 'id_example' # str | The external id of the tool to launch. (optional)
    url = 'url_example' # str | The LTI launch url for the external tool. (optional)
    assignment_id = 'assignment_id_example' # str | The assignment id for an assignment launch. Required if launch_type is set to \"assessment\". (optional)
    module_item_id = 'module_item_id_example' # str | The assignment id for a module item launch. Required if launch_type is set to \"module_item\". (optional)
    launch_type = 'launch_type_example' # str | The type of launch to perform on the external tool. Placement names (eg. \"course_navigation\") can also be specified to use the custom launch url for that placement; if done, the tool id must be provided. (optional)
    resource_link_lookup_uuid = 'resource_link_lookup_uuid_example' # str | The identifier to lookup a resource link. (optional)

    try:
        # Get a sessionless launch url for an external tool.
        await api_instance.external_tools_generate_sessionless_launch_for_accounts(account_id, id=id, url=url, assignment_id=assignment_id, module_item_id=module_item_id, launch_type=launch_type, resource_link_lookup_uuid=resource_link_lookup_uuid)
    except Exception as e:
        print("Exception when calling ExternalToolsApi->external_tools_generate_sessionless_launch_for_accounts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **id** | **str**| The external id of the tool to launch. | [optional] 
 **url** | **str**| The LTI launch url for the external tool. | [optional] 
 **assignment_id** | **str**| The assignment id for an assignment launch. Required if launch_type is set to \&quot;assessment\&quot;. | [optional] 
 **module_item_id** | **str**| The assignment id for a module item launch. Required if launch_type is set to \&quot;module_item\&quot;. | [optional] 
 **launch_type** | **str**| The type of launch to perform on the external tool. Placement names (eg. \&quot;course_navigation\&quot;) can also be specified to use the custom launch url for that placement; if done, the tool id must be provided. | [optional] 
 **resource_link_lookup_uuid** | **str**| The identifier to lookup a resource link. | [optional] 

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
**0** | Get a sessionless launch url for an external tool. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **external_tools_index**
> List[ContextExternalTool] external_tools_index(course_id, search_term=search_term, selectable=selectable, include_parents=include_parents, placement=placement, page=page, per_page=per_page)

List external tools

Returns the paginated list of external tools for the current context.
See the get request docs for a single tool for a list of properties on an external tool.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.context_external_tool import ContextExternalTool
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
    api_instance = canvas_lms_python_client.ExternalToolsApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    search_term = 'search_term_example' # str | The partial name of the tools to match and return. (optional)
    selectable = True # bool | If true, then only tools that are meant to be selectable are returned. (optional)
    include_parents = True # bool | If true, then include tools installed in all accounts above the current context (optional)
    placement = 'placement_example' # str | The placement type to filter by.  Return all tools at the current context as well as all tools from the parent, and filter the tools list to only those with a placement of 'editor_button' (optional)
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # List external tools
        api_response = await api_instance.external_tools_index(course_id, search_term=search_term, selectable=selectable, include_parents=include_parents, placement=placement, page=page, per_page=per_page)
        print("The response of ExternalToolsApi->external_tools_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExternalToolsApi->external_tools_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **search_term** | **str**| The partial name of the tools to match and return. | [optional] 
 **selectable** | **bool**| If true, then only tools that are meant to be selectable are returned. | [optional] 
 **include_parents** | **bool**| If true, then include tools installed in all accounts above the current context | [optional] 
 **placement** | **str**| The placement type to filter by.  Return all tools at the current context as well as all tools from the parent, and filter the tools list to only those with a placement of &#39;editor_button&#39; | [optional] 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**List[ContextExternalTool]**](ContextExternalTool.md)

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

# **external_tools_index_for_accounts**
> List[ContextExternalTool] external_tools_index_for_accounts(account_id, search_term=search_term, selectable=selectable, include_parents=include_parents, placement=placement, page=page, per_page=per_page)

List external tools

Returns the paginated list of external tools for the current context.
See the get request docs for a single tool for a list of properties on an external tool.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.context_external_tool import ContextExternalTool
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
    api_instance = canvas_lms_python_client.ExternalToolsApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    search_term = 'search_term_example' # str | The partial name of the tools to match and return. (optional)
    selectable = True # bool | If true, then only tools that are meant to be selectable are returned. (optional)
    include_parents = True # bool | If true, then include tools installed in all accounts above the current context (optional)
    placement = 'placement_example' # str | The placement type to filter by.  Return all tools at the current context as well as all tools from the parent, and filter the tools list to only those with a placement of 'editor_button' (optional)
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # List external tools
        api_response = await api_instance.external_tools_index_for_accounts(account_id, search_term=search_term, selectable=selectable, include_parents=include_parents, placement=placement, page=page, per_page=per_page)
        print("The response of ExternalToolsApi->external_tools_index_for_accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExternalToolsApi->external_tools_index_for_accounts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **search_term** | **str**| The partial name of the tools to match and return. | [optional] 
 **selectable** | **bool**| If true, then only tools that are meant to be selectable are returned. | [optional] 
 **include_parents** | **bool**| If true, then include tools installed in all accounts above the current context | [optional] 
 **placement** | **str**| The placement type to filter by.  Return all tools at the current context as well as all tools from the parent, and filter the tools list to only those with a placement of &#39;editor_button&#39; | [optional] 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**List[ContextExternalTool]**](ContextExternalTool.md)

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

# **external_tools_index_for_groups**
> List[ContextExternalTool] external_tools_index_for_groups(group_id, search_term=search_term, selectable=selectable, include_parents=include_parents, placement=placement, page=page, per_page=per_page)

List external tools

Returns the paginated list of external tools for the current context.
See the get request docs for a single tool for a list of properties on an external tool.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.context_external_tool import ContextExternalTool
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
    api_instance = canvas_lms_python_client.ExternalToolsApi(api_client)
    group_id = 'group_id_example' # str | Scope response to group_id
    search_term = 'search_term_example' # str | The partial name of the tools to match and return. (optional)
    selectable = True # bool | If true, then only tools that are meant to be selectable are returned. (optional)
    include_parents = True # bool | If true, then include tools installed in all accounts above the current context (optional)
    placement = 'placement_example' # str | The placement type to filter by.  Return all tools at the current context as well as all tools from the parent, and filter the tools list to only those with a placement of 'editor_button' (optional)
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # List external tools
        api_response = await api_instance.external_tools_index_for_groups(group_id, search_term=search_term, selectable=selectable, include_parents=include_parents, placement=placement, page=page, per_page=per_page)
        print("The response of ExternalToolsApi->external_tools_index_for_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExternalToolsApi->external_tools_index_for_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Scope response to group_id | 
 **search_term** | **str**| The partial name of the tools to match and return. | [optional] 
 **selectable** | **bool**| If true, then only tools that are meant to be selectable are returned. | [optional] 
 **include_parents** | **bool**| If true, then include tools installed in all accounts above the current context | [optional] 
 **placement** | **str**| The placement type to filter by.  Return all tools at the current context as well as all tools from the parent, and filter the tools list to only those with a placement of &#39;editor_button&#39; | [optional] 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**List[ContextExternalTool]**](ContextExternalTool.md)

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

# **external_tools_mark_rce_favorite**
> ExternalToolsMarkRceFavoriteResponse external_tools_mark_rce_favorite(account_id, id)

Mark tool as RCE Favorite

Mark the specified editor_button external tool as a favorite in the RCE editor
for courses in the given account and its subaccounts (if the subaccounts
haven't set their own RCE Favorites). This places the tool in a preferred location
in the RCE. Cannot mark more than 2 tools as RCE Favorites.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.external_tools_mark_rce_favorite_response import ExternalToolsMarkRceFavoriteResponse
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
    api_instance = canvas_lms_python_client.ExternalToolsApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    id = 'id_example' # str | Scope response to id

    try:
        # Mark tool as RCE Favorite
        api_response = await api_instance.external_tools_mark_rce_favorite(account_id, id)
        print("The response of ExternalToolsApi->external_tools_mark_rce_favorite:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExternalToolsApi->external_tools_mark_rce_favorite: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **id** | **str**| Scope response to id | 

### Return type

[**ExternalToolsMarkRceFavoriteResponse**](ExternalToolsMarkRceFavoriteResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | ExternalToolsMarkRceFavoriteResponse |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **external_tools_remove_top_nav_favorite**
> external_tools_remove_top_nav_favorite(account_id, id)

Remove tool from Top Navigation Favorites

Removes the dedicated button in Top Navigation for the specified tool for the given account.

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
    api_instance = canvas_lms_python_client.ExternalToolsApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    id = 'id_example' # str | Scope response to id

    try:
        # Remove tool from Top Navigation Favorites
        await api_instance.external_tools_remove_top_nav_favorite(account_id, id)
    except Exception as e:
        print("Exception when calling ExternalToolsApi->external_tools_remove_top_nav_favorite: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **id** | **str**| Scope response to id | 

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
**0** | Remove tool from Top Navigation Favorites |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **external_tools_show**
> ContextExternalTool external_tools_show(course_id, external_tool_id)

Get a single external tool

Returns the specified external tool.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.context_external_tool import ContextExternalTool
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
    api_instance = canvas_lms_python_client.ExternalToolsApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    external_tool_id = 'external_tool_id_example' # str | Scope response to external_tool_id

    try:
        # Get a single external tool
        api_response = await api_instance.external_tools_show(course_id, external_tool_id)
        print("The response of ExternalToolsApi->external_tools_show:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExternalToolsApi->external_tools_show: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **external_tool_id** | **str**| Scope response to external_tool_id | 

### Return type

[**ContextExternalTool**](ContextExternalTool.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | ContextExternalTool |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **external_tools_show_for_accounts**
> ContextExternalTool external_tools_show_for_accounts(account_id, external_tool_id)

Get a single external tool

Returns the specified external tool.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.context_external_tool import ContextExternalTool
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
    api_instance = canvas_lms_python_client.ExternalToolsApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    external_tool_id = 'external_tool_id_example' # str | Scope response to external_tool_id

    try:
        # Get a single external tool
        api_response = await api_instance.external_tools_show_for_accounts(account_id, external_tool_id)
        print("The response of ExternalToolsApi->external_tools_show_for_accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExternalToolsApi->external_tools_show_for_accounts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **external_tool_id** | **str**| Scope response to external_tool_id | 

### Return type

[**ContextExternalTool**](ContextExternalTool.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | ContextExternalTool |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **external_tools_unmark_rce_favorite**
> ExternalToolsMarkRceFavoriteResponse external_tools_unmark_rce_favorite(account_id, id)

Unmark tool as RCE Favorite

Unmark the specified external tool as a favorite in the RCE editor
for the given account. The tool will remain available but will no longer
appear in the preferred favorites location.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.external_tools_mark_rce_favorite_response import ExternalToolsMarkRceFavoriteResponse
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
    api_instance = canvas_lms_python_client.ExternalToolsApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    id = 'id_example' # str | Scope response to id

    try:
        # Unmark tool as RCE Favorite
        api_response = await api_instance.external_tools_unmark_rce_favorite(account_id, id)
        print("The response of ExternalToolsApi->external_tools_unmark_rce_favorite:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExternalToolsApi->external_tools_unmark_rce_favorite: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **id** | **str**| Scope response to id | 

### Return type

[**ExternalToolsMarkRceFavoriteResponse**](ExternalToolsMarkRceFavoriteResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | ExternalToolsMarkRceFavoriteResponse |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **external_tools_update**
> ContextExternalTool external_tools_update(course_id, external_tool_id)

Edit an external tool

Update the specified external tool. Uses same parameters as create. Returns the updated tool.

NOTE: Any updates made to LTI 1.3 tools with this API will be overridden if any changes are
made to the tool's associated LTI Registration/Developer Key configuration. In almost all cases,
changes should be made to the tool's associated LTI Registration configuration, not individual tools.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.context_external_tool import ContextExternalTool
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
    api_instance = canvas_lms_python_client.ExternalToolsApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    external_tool_id = 'external_tool_id_example' # str | Scope response to external_tool_id

    try:
        # Edit an external tool
        api_response = await api_instance.external_tools_update(course_id, external_tool_id)
        print("The response of ExternalToolsApi->external_tools_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExternalToolsApi->external_tools_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **external_tool_id** | **str**| Scope response to external_tool_id | 

### Return type

[**ContextExternalTool**](ContextExternalTool.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | ContextExternalTool |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **external_tools_update_for_accounts**
> ContextExternalTool external_tools_update_for_accounts(account_id, external_tool_id)

Edit an external tool

Update the specified external tool. Uses same parameters as create. Returns the updated tool.

NOTE: Any updates made to LTI 1.3 tools with this API will be overridden if any changes are
made to the tool's associated LTI Registration/Developer Key configuration. In almost all cases,
changes should be made to the tool's associated LTI Registration configuration, not individual tools.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.context_external_tool import ContextExternalTool
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
    api_instance = canvas_lms_python_client.ExternalToolsApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    external_tool_id = 'external_tool_id_example' # str | Scope response to external_tool_id

    try:
        # Edit an external tool
        api_response = await api_instance.external_tools_update_for_accounts(account_id, external_tool_id)
        print("The response of ExternalToolsApi->external_tools_update_for_accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExternalToolsApi->external_tools_update_for_accounts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **external_tool_id** | **str**| Scope response to external_tool_id | 

### Return type

[**ContextExternalTool**](ContextExternalTool.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | ContextExternalTool |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **external_tools_visible_course_nav_tools**
> List[ContextExternalTool] external_tools_visible_course_nav_tools(course_id)

Get visible course navigation tools for a single course

Get a list of external tools with the course_navigation placement that have not been hidden in
course settings and whose visibility settings apply to the requesting user. These tools are the
same that appear in the course navigation.

The response format is the same as Get visible course navigation tools.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.context_external_tool import ContextExternalTool
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
    api_instance = canvas_lms_python_client.ExternalToolsApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id

    try:
        # Get visible course navigation tools for a single course
        api_response = await api_instance.external_tools_visible_course_nav_tools(course_id)
        print("The response of ExternalToolsApi->external_tools_visible_course_nav_tools:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExternalToolsApi->external_tools_visible_course_nav_tools: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 

### Return type

[**List[ContextExternalTool]**](ContextExternalTool.md)

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

