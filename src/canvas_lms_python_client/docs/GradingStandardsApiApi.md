# canvas_lms_python_client.GradingStandardsApiApi

All URIs are relative to *https://canvas.instructure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**grading_standards_api_context_index**](GradingStandardsApiApi.md#grading_standards_api_context_index) | **GET** /api/v1/courses/{course_id}/grading_standards | List the grading standards available in a context.
[**grading_standards_api_context_index_for_accounts**](GradingStandardsApiApi.md#grading_standards_api_context_index_for_accounts) | **GET** /api/v1/accounts/{account_id}/grading_standards | List the grading standards available in a context.
[**grading_standards_api_context_show**](GradingStandardsApiApi.md#grading_standards_api_context_show) | **GET** /api/v1/courses/{course_id}/grading_standards/{grading_standard_id} | Get a single grading standard in a context.
[**grading_standards_api_context_show_for_accounts**](GradingStandardsApiApi.md#grading_standards_api_context_show_for_accounts) | **GET** /api/v1/accounts/{account_id}/grading_standards/{grading_standard_id} | Get a single grading standard in a context.
[**grading_standards_api_create**](GradingStandardsApiApi.md#grading_standards_api_create) | **POST** /api/v1/accounts/{account_id}/grading_standards | Create a new grading standard
[**grading_standards_api_create_for_courses**](GradingStandardsApiApi.md#grading_standards_api_create_for_courses) | **POST** /api/v1/courses/{course_id}/grading_standards | Create a new grading standard
[**grading_standards_api_destroy**](GradingStandardsApiApi.md#grading_standards_api_destroy) | **DELETE** /api/v1/courses/{course_id}/grading_standards/{grading_standard_id} | Delete a grading standard
[**grading_standards_api_destroy_for_accounts**](GradingStandardsApiApi.md#grading_standards_api_destroy_for_accounts) | **DELETE** /api/v1/accounts/{account_id}/grading_standards/{grading_standard_id} | Delete a grading standard
[**grading_standards_api_update**](GradingStandardsApiApi.md#grading_standards_api_update) | **PUT** /api/v1/courses/{course_id}/grading_standards/{grading_standard_id} | Update a grading standard
[**grading_standards_api_update_for_accounts**](GradingStandardsApiApi.md#grading_standards_api_update_for_accounts) | **PUT** /api/v1/accounts/{account_id}/grading_standards/{grading_standard_id} | Update a grading standard


# **grading_standards_api_context_index**
> List[GradingStandard] grading_standards_api_context_index(course_id)

List the grading standards available in a context.

Returns the paginated list of grading standards for the given context that are visible to the user.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.grading_standard import GradingStandard
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
    api_instance = canvas_lms_python_client.GradingStandardsApiApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id

    try:
        # List the grading standards available in a context.
        api_response = await api_instance.grading_standards_api_context_index(course_id)
        print("The response of GradingStandardsApiApi->grading_standards_api_context_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GradingStandardsApiApi->grading_standards_api_context_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 

### Return type

[**List[GradingStandard]**](GradingStandard.md)

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

# **grading_standards_api_context_index_for_accounts**
> List[GradingStandard] grading_standards_api_context_index_for_accounts(account_id)

List the grading standards available in a context.

Returns the paginated list of grading standards for the given context that are visible to the user.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.grading_standard import GradingStandard
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
    api_instance = canvas_lms_python_client.GradingStandardsApiApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id

    try:
        # List the grading standards available in a context.
        api_response = await api_instance.grading_standards_api_context_index_for_accounts(account_id)
        print("The response of GradingStandardsApiApi->grading_standards_api_context_index_for_accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GradingStandardsApiApi->grading_standards_api_context_index_for_accounts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 

### Return type

[**List[GradingStandard]**](GradingStandard.md)

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

# **grading_standards_api_context_show**
> GradingStandard grading_standards_api_context_show(course_id, grading_standard_id)

Get a single grading standard in a context.

Returns a grading standard for the given context that is visible to the user.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.grading_standard import GradingStandard
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
    api_instance = canvas_lms_python_client.GradingStandardsApiApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    grading_standard_id = 'grading_standard_id_example' # str | Scope response to grading_standard_id

    try:
        # Get a single grading standard in a context.
        api_response = await api_instance.grading_standards_api_context_show(course_id, grading_standard_id)
        print("The response of GradingStandardsApiApi->grading_standards_api_context_show:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GradingStandardsApiApi->grading_standards_api_context_show: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **grading_standard_id** | **str**| Scope response to grading_standard_id | 

### Return type

[**GradingStandard**](GradingStandard.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | GradingStandard |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grading_standards_api_context_show_for_accounts**
> GradingStandard grading_standards_api_context_show_for_accounts(account_id, grading_standard_id)

Get a single grading standard in a context.

Returns a grading standard for the given context that is visible to the user.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.grading_standard import GradingStandard
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
    api_instance = canvas_lms_python_client.GradingStandardsApiApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    grading_standard_id = 'grading_standard_id_example' # str | Scope response to grading_standard_id

    try:
        # Get a single grading standard in a context.
        api_response = await api_instance.grading_standards_api_context_show_for_accounts(account_id, grading_standard_id)
        print("The response of GradingStandardsApiApi->grading_standards_api_context_show_for_accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GradingStandardsApiApi->grading_standards_api_context_show_for_accounts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **grading_standard_id** | **str**| Scope response to grading_standard_id | 

### Return type

[**GradingStandard**](GradingStandard.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | GradingStandard |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grading_standards_api_create**
> GradingStandard grading_standards_api_create(account_id, grading_standards_api_create_request=grading_standards_api_create_request)

Create a new grading standard

Create a new grading standard

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.grading_standard import GradingStandard
from canvas_lms_python_client.models.grading_standards_api_create_request import GradingStandardsApiCreateRequest
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
    api_instance = canvas_lms_python_client.GradingStandardsApiApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    grading_standards_api_create_request = canvas_lms_python_client.GradingStandardsApiCreateRequest() # GradingStandardsApiCreateRequest | Request body parameters  **Example Request:** ``` curl https://<canvas>/api/v1/courses/<course_id>/grading_standards \\   -X POST \\   -H 'Authorization: Bearer <token>' \\   -d 'title=New standard name' \\   -d 'points_based=false' \\   -d 'scaling_factor=1.0' \\   -d 'grading_scheme_entry[][name]=A' \\   -d 'grading_scheme_entry[][value]=94' \\   -d 'grading_scheme_entry[][name]=A-' \\   -d 'grading_scheme_entry[][value]=90' \\   -d 'grading_scheme_entry[][name]=B+' \\   -d 'grading_scheme_entry[][value]=87' \\   -d 'grading_scheme_entry[][name]=B' \\   -d 'grading_scheme_entry[][value]=84' \\   -d 'grading_scheme_entry[][name]=B-' \\   -d 'grading_scheme_entry[][value]=80' \\   -d 'grading_scheme_entry[][name]=C+' \\   -d 'grading_scheme_entry[][value]=77' \\   -d 'grading_scheme_entry[][name]=C' \\   -d 'grading_scheme_entry[][value]=74' \\   -d 'grading_scheme_entry[][name]=C-' \\   -d 'grading_scheme_entry[][value]=70' \\   -d 'grading_scheme_entry[][name]=D+' \\   -d 'grading_scheme_entry[][value]=67' \\   -d 'grading_scheme_entry[][name]=D' \\   -d 'grading_scheme_entry[][value]=64' \\   -d 'grading_scheme_entry[][name]=D-' \\   -d 'grading_scheme_entry[][value]=61' \\   -d 'grading_scheme_entry[][name]=F' \\   -d 'grading_scheme_entry[][value]=0' ``` (optional)

    try:
        # Create a new grading standard
        api_response = await api_instance.grading_standards_api_create(account_id, grading_standards_api_create_request=grading_standards_api_create_request)
        print("The response of GradingStandardsApiApi->grading_standards_api_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GradingStandardsApiApi->grading_standards_api_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **grading_standards_api_create_request** | [**GradingStandardsApiCreateRequest**](GradingStandardsApiCreateRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl https://&lt;canvas&gt;/api/v1/courses/&lt;course_id&gt;/grading_standards \\   -X POST \\   -H &#39;Authorization: Bearer &lt;token&gt;&#39; \\   -d &#39;title&#x3D;New standard name&#39; \\   -d &#39;points_based&#x3D;false&#39; \\   -d &#39;scaling_factor&#x3D;1.0&#39; \\   -d &#39;grading_scheme_entry[][name]&#x3D;A&#39; \\   -d &#39;grading_scheme_entry[][value]&#x3D;94&#39; \\   -d &#39;grading_scheme_entry[][name]&#x3D;A-&#39; \\   -d &#39;grading_scheme_entry[][value]&#x3D;90&#39; \\   -d &#39;grading_scheme_entry[][name]&#x3D;B+&#39; \\   -d &#39;grading_scheme_entry[][value]&#x3D;87&#39; \\   -d &#39;grading_scheme_entry[][name]&#x3D;B&#39; \\   -d &#39;grading_scheme_entry[][value]&#x3D;84&#39; \\   -d &#39;grading_scheme_entry[][name]&#x3D;B-&#39; \\   -d &#39;grading_scheme_entry[][value]&#x3D;80&#39; \\   -d &#39;grading_scheme_entry[][name]&#x3D;C+&#39; \\   -d &#39;grading_scheme_entry[][value]&#x3D;77&#39; \\   -d &#39;grading_scheme_entry[][name]&#x3D;C&#39; \\   -d &#39;grading_scheme_entry[][value]&#x3D;74&#39; \\   -d &#39;grading_scheme_entry[][name]&#x3D;C-&#39; \\   -d &#39;grading_scheme_entry[][value]&#x3D;70&#39; \\   -d &#39;grading_scheme_entry[][name]&#x3D;D+&#39; \\   -d &#39;grading_scheme_entry[][value]&#x3D;67&#39; \\   -d &#39;grading_scheme_entry[][name]&#x3D;D&#39; \\   -d &#39;grading_scheme_entry[][value]&#x3D;64&#39; \\   -d &#39;grading_scheme_entry[][name]&#x3D;D-&#39; \\   -d &#39;grading_scheme_entry[][value]&#x3D;61&#39; \\   -d &#39;grading_scheme_entry[][name]&#x3D;F&#39; \\   -d &#39;grading_scheme_entry[][value]&#x3D;0&#39; &#x60;&#x60;&#x60; | [optional] 

### Return type

[**GradingStandard**](GradingStandard.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | GradingStandard |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grading_standards_api_create_for_courses**
> GradingStandard grading_standards_api_create_for_courses(course_id, grading_standards_api_create_request=grading_standards_api_create_request)

Create a new grading standard

Create a new grading standard

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.grading_standard import GradingStandard
from canvas_lms_python_client.models.grading_standards_api_create_request import GradingStandardsApiCreateRequest
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
    api_instance = canvas_lms_python_client.GradingStandardsApiApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    grading_standards_api_create_request = canvas_lms_python_client.GradingStandardsApiCreateRequest() # GradingStandardsApiCreateRequest | Request body parameters  **Example Request:** ``` curl https://<canvas>/api/v1/courses/<course_id>/grading_standards \\   -X POST \\   -H 'Authorization: Bearer <token>' \\   -d 'title=New standard name' \\   -d 'points_based=false' \\   -d 'scaling_factor=1.0' \\   -d 'grading_scheme_entry[][name]=A' \\   -d 'grading_scheme_entry[][value]=94' \\   -d 'grading_scheme_entry[][name]=A-' \\   -d 'grading_scheme_entry[][value]=90' \\   -d 'grading_scheme_entry[][name]=B+' \\   -d 'grading_scheme_entry[][value]=87' \\   -d 'grading_scheme_entry[][name]=B' \\   -d 'grading_scheme_entry[][value]=84' \\   -d 'grading_scheme_entry[][name]=B-' \\   -d 'grading_scheme_entry[][value]=80' \\   -d 'grading_scheme_entry[][name]=C+' \\   -d 'grading_scheme_entry[][value]=77' \\   -d 'grading_scheme_entry[][name]=C' \\   -d 'grading_scheme_entry[][value]=74' \\   -d 'grading_scheme_entry[][name]=C-' \\   -d 'grading_scheme_entry[][value]=70' \\   -d 'grading_scheme_entry[][name]=D+' \\   -d 'grading_scheme_entry[][value]=67' \\   -d 'grading_scheme_entry[][name]=D' \\   -d 'grading_scheme_entry[][value]=64' \\   -d 'grading_scheme_entry[][name]=D-' \\   -d 'grading_scheme_entry[][value]=61' \\   -d 'grading_scheme_entry[][name]=F' \\   -d 'grading_scheme_entry[][value]=0' ``` (optional)

    try:
        # Create a new grading standard
        api_response = await api_instance.grading_standards_api_create_for_courses(course_id, grading_standards_api_create_request=grading_standards_api_create_request)
        print("The response of GradingStandardsApiApi->grading_standards_api_create_for_courses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GradingStandardsApiApi->grading_standards_api_create_for_courses: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **grading_standards_api_create_request** | [**GradingStandardsApiCreateRequest**](GradingStandardsApiCreateRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl https://&lt;canvas&gt;/api/v1/courses/&lt;course_id&gt;/grading_standards \\   -X POST \\   -H &#39;Authorization: Bearer &lt;token&gt;&#39; \\   -d &#39;title&#x3D;New standard name&#39; \\   -d &#39;points_based&#x3D;false&#39; \\   -d &#39;scaling_factor&#x3D;1.0&#39; \\   -d &#39;grading_scheme_entry[][name]&#x3D;A&#39; \\   -d &#39;grading_scheme_entry[][value]&#x3D;94&#39; \\   -d &#39;grading_scheme_entry[][name]&#x3D;A-&#39; \\   -d &#39;grading_scheme_entry[][value]&#x3D;90&#39; \\   -d &#39;grading_scheme_entry[][name]&#x3D;B+&#39; \\   -d &#39;grading_scheme_entry[][value]&#x3D;87&#39; \\   -d &#39;grading_scheme_entry[][name]&#x3D;B&#39; \\   -d &#39;grading_scheme_entry[][value]&#x3D;84&#39; \\   -d &#39;grading_scheme_entry[][name]&#x3D;B-&#39; \\   -d &#39;grading_scheme_entry[][value]&#x3D;80&#39; \\   -d &#39;grading_scheme_entry[][name]&#x3D;C+&#39; \\   -d &#39;grading_scheme_entry[][value]&#x3D;77&#39; \\   -d &#39;grading_scheme_entry[][name]&#x3D;C&#39; \\   -d &#39;grading_scheme_entry[][value]&#x3D;74&#39; \\   -d &#39;grading_scheme_entry[][name]&#x3D;C-&#39; \\   -d &#39;grading_scheme_entry[][value]&#x3D;70&#39; \\   -d &#39;grading_scheme_entry[][name]&#x3D;D+&#39; \\   -d &#39;grading_scheme_entry[][value]&#x3D;67&#39; \\   -d &#39;grading_scheme_entry[][name]&#x3D;D&#39; \\   -d &#39;grading_scheme_entry[][value]&#x3D;64&#39; \\   -d &#39;grading_scheme_entry[][name]&#x3D;D-&#39; \\   -d &#39;grading_scheme_entry[][value]&#x3D;61&#39; \\   -d &#39;grading_scheme_entry[][name]&#x3D;F&#39; \\   -d &#39;grading_scheme_entry[][value]&#x3D;0&#39; &#x60;&#x60;&#x60; | [optional] 

### Return type

[**GradingStandard**](GradingStandard.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | GradingStandard |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grading_standards_api_destroy**
> GradingStandard grading_standards_api_destroy(course_id, grading_standard_id)

Delete a grading standard

Deletes the grading standard with the given id

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.grading_standard import GradingStandard
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
    api_instance = canvas_lms_python_client.GradingStandardsApiApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    grading_standard_id = 'grading_standard_id_example' # str | Scope response to grading_standard_id

    try:
        # Delete a grading standard
        api_response = await api_instance.grading_standards_api_destroy(course_id, grading_standard_id)
        print("The response of GradingStandardsApiApi->grading_standards_api_destroy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GradingStandardsApiApi->grading_standards_api_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **grading_standard_id** | **str**| Scope response to grading_standard_id | 

### Return type

[**GradingStandard**](GradingStandard.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | GradingStandard |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grading_standards_api_destroy_for_accounts**
> GradingStandard grading_standards_api_destroy_for_accounts(account_id, grading_standard_id)

Delete a grading standard

Deletes the grading standard with the given id

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.grading_standard import GradingStandard
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
    api_instance = canvas_lms_python_client.GradingStandardsApiApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    grading_standard_id = 'grading_standard_id_example' # str | Scope response to grading_standard_id

    try:
        # Delete a grading standard
        api_response = await api_instance.grading_standards_api_destroy_for_accounts(account_id, grading_standard_id)
        print("The response of GradingStandardsApiApi->grading_standards_api_destroy_for_accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GradingStandardsApiApi->grading_standards_api_destroy_for_accounts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **grading_standard_id** | **str**| Scope response to grading_standard_id | 

### Return type

[**GradingStandard**](GradingStandard.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | GradingStandard |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grading_standards_api_update**
> GradingStandard grading_standards_api_update(course_id, grading_standard_id, grading_standards_api_update_request=grading_standards_api_update_request)

Update a grading standard

Updates the grading standard with the given id

If the grading standard has been used for grading, only the title can be updated.
The data, points_based, and scaling_factor cannot be modified once the grading
standard has been used to grade assignments.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.grading_standard import GradingStandard
from canvas_lms_python_client.models.grading_standards_api_update_request import GradingStandardsApiUpdateRequest
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
    api_instance = canvas_lms_python_client.GradingStandardsApiApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    grading_standard_id = 'grading_standard_id_example' # str | Scope response to grading_standard_id
    grading_standards_api_update_request = canvas_lms_python_client.GradingStandardsApiUpdateRequest() # GradingStandardsApiUpdateRequest | Request body parameters  **Example Request:** ``` curl https://<canvas>/api/v1/courses/1/grading_standards/5 \\   -X PUT \\   -H 'Authorization: Bearer <token>' \\   -d 'title=Updated+Grading+Standard'   -d 'points_based=false' \\   -d 'scaling_factor=1.0' \\   -d 'grading_scheme_entry[][name]=A' \\   -d 'grading_scheme_entry[][value]=94' \\   -d 'grading_scheme_entry[][name]=A-' \\   -d 'grading_scheme_entry[][value]=90' \\   -d 'grading_scheme_entry[][name]=B+' \\   -d 'grading_scheme_entry[][value]=87' \\   -d 'grading_scheme_entry[][name]=B' \\   -d 'grading_scheme_entry[][value]=84' \\   -d 'grading_scheme_entry[][name]=B-' \\   -d 'grading_scheme_entry[][value]=80' \\   -d 'grading_scheme_entry[][name]=C+' \\   -d 'grading_scheme_entry[][value]=77' \\   -d 'grading_scheme_entry[][name]=C' \\   -d 'grading_scheme_entry[][value]=74' \\   -d 'grading_scheme_entry[][name]=C-' \\   -d 'grading_scheme_entry[][value]=70' \\   -d 'grading_scheme_entry[][name]=D+' \\   -d 'grading_scheme_entry[][value]=67' \\   -d 'grading_scheme_entry[][name]=D' \\   -d 'grading_scheme_entry[][value]=64' \\   -d 'grading_scheme_entry[][name]=D-' \\   -d 'grading_scheme_entry[][value]=61' \\   -d 'grading_scheme_entry[][name]=F' \\   -d 'grading_scheme_entry[][value]=0' ``` (optional)

    try:
        # Update a grading standard
        api_response = await api_instance.grading_standards_api_update(course_id, grading_standard_id, grading_standards_api_update_request=grading_standards_api_update_request)
        print("The response of GradingStandardsApiApi->grading_standards_api_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GradingStandardsApiApi->grading_standards_api_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **grading_standard_id** | **str**| Scope response to grading_standard_id | 
 **grading_standards_api_update_request** | [**GradingStandardsApiUpdateRequest**](GradingStandardsApiUpdateRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl https://&lt;canvas&gt;/api/v1/courses/1/grading_standards/5 \\   -X PUT \\   -H &#39;Authorization: Bearer &lt;token&gt;&#39; \\   -d &#39;title&#x3D;Updated+Grading+Standard&#39;   -d &#39;points_based&#x3D;false&#39; \\   -d &#39;scaling_factor&#x3D;1.0&#39; \\   -d &#39;grading_scheme_entry[][name]&#x3D;A&#39; \\   -d &#39;grading_scheme_entry[][value]&#x3D;94&#39; \\   -d &#39;grading_scheme_entry[][name]&#x3D;A-&#39; \\   -d &#39;grading_scheme_entry[][value]&#x3D;90&#39; \\   -d &#39;grading_scheme_entry[][name]&#x3D;B+&#39; \\   -d &#39;grading_scheme_entry[][value]&#x3D;87&#39; \\   -d &#39;grading_scheme_entry[][name]&#x3D;B&#39; \\   -d &#39;grading_scheme_entry[][value]&#x3D;84&#39; \\   -d &#39;grading_scheme_entry[][name]&#x3D;B-&#39; \\   -d &#39;grading_scheme_entry[][value]&#x3D;80&#39; \\   -d &#39;grading_scheme_entry[][name]&#x3D;C+&#39; \\   -d &#39;grading_scheme_entry[][value]&#x3D;77&#39; \\   -d &#39;grading_scheme_entry[][name]&#x3D;C&#39; \\   -d &#39;grading_scheme_entry[][value]&#x3D;74&#39; \\   -d &#39;grading_scheme_entry[][name]&#x3D;C-&#39; \\   -d &#39;grading_scheme_entry[][value]&#x3D;70&#39; \\   -d &#39;grading_scheme_entry[][name]&#x3D;D+&#39; \\   -d &#39;grading_scheme_entry[][value]&#x3D;67&#39; \\   -d &#39;grading_scheme_entry[][name]&#x3D;D&#39; \\   -d &#39;grading_scheme_entry[][value]&#x3D;64&#39; \\   -d &#39;grading_scheme_entry[][name]&#x3D;D-&#39; \\   -d &#39;grading_scheme_entry[][value]&#x3D;61&#39; \\   -d &#39;grading_scheme_entry[][name]&#x3D;F&#39; \\   -d &#39;grading_scheme_entry[][value]&#x3D;0&#39; &#x60;&#x60;&#x60; | [optional] 

### Return type

[**GradingStandard**](GradingStandard.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | GradingStandard |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grading_standards_api_update_for_accounts**
> GradingStandard grading_standards_api_update_for_accounts(account_id, grading_standard_id, grading_standards_api_update_request=grading_standards_api_update_request)

Update a grading standard

Updates the grading standard with the given id

If the grading standard has been used for grading, only the title can be updated.
The data, points_based, and scaling_factor cannot be modified once the grading
standard has been used to grade assignments.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.grading_standard import GradingStandard
from canvas_lms_python_client.models.grading_standards_api_update_request import GradingStandardsApiUpdateRequest
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
    api_instance = canvas_lms_python_client.GradingStandardsApiApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    grading_standard_id = 'grading_standard_id_example' # str | Scope response to grading_standard_id
    grading_standards_api_update_request = canvas_lms_python_client.GradingStandardsApiUpdateRequest() # GradingStandardsApiUpdateRequest | Request body parameters  **Example Request:** ``` curl https://<canvas>/api/v1/courses/1/grading_standards/5 \\   -X PUT \\   -H 'Authorization: Bearer <token>' \\   -d 'title=Updated+Grading+Standard'   -d 'points_based=false' \\   -d 'scaling_factor=1.0' \\   -d 'grading_scheme_entry[][name]=A' \\   -d 'grading_scheme_entry[][value]=94' \\   -d 'grading_scheme_entry[][name]=A-' \\   -d 'grading_scheme_entry[][value]=90' \\   -d 'grading_scheme_entry[][name]=B+' \\   -d 'grading_scheme_entry[][value]=87' \\   -d 'grading_scheme_entry[][name]=B' \\   -d 'grading_scheme_entry[][value]=84' \\   -d 'grading_scheme_entry[][name]=B-' \\   -d 'grading_scheme_entry[][value]=80' \\   -d 'grading_scheme_entry[][name]=C+' \\   -d 'grading_scheme_entry[][value]=77' \\   -d 'grading_scheme_entry[][name]=C' \\   -d 'grading_scheme_entry[][value]=74' \\   -d 'grading_scheme_entry[][name]=C-' \\   -d 'grading_scheme_entry[][value]=70' \\   -d 'grading_scheme_entry[][name]=D+' \\   -d 'grading_scheme_entry[][value]=67' \\   -d 'grading_scheme_entry[][name]=D' \\   -d 'grading_scheme_entry[][value]=64' \\   -d 'grading_scheme_entry[][name]=D-' \\   -d 'grading_scheme_entry[][value]=61' \\   -d 'grading_scheme_entry[][name]=F' \\   -d 'grading_scheme_entry[][value]=0' ``` (optional)

    try:
        # Update a grading standard
        api_response = await api_instance.grading_standards_api_update_for_accounts(account_id, grading_standard_id, grading_standards_api_update_request=grading_standards_api_update_request)
        print("The response of GradingStandardsApiApi->grading_standards_api_update_for_accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GradingStandardsApiApi->grading_standards_api_update_for_accounts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **grading_standard_id** | **str**| Scope response to grading_standard_id | 
 **grading_standards_api_update_request** | [**GradingStandardsApiUpdateRequest**](GradingStandardsApiUpdateRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; curl https://&lt;canvas&gt;/api/v1/courses/1/grading_standards/5 \\   -X PUT \\   -H &#39;Authorization: Bearer &lt;token&gt;&#39; \\   -d &#39;title&#x3D;Updated+Grading+Standard&#39;   -d &#39;points_based&#x3D;false&#39; \\   -d &#39;scaling_factor&#x3D;1.0&#39; \\   -d &#39;grading_scheme_entry[][name]&#x3D;A&#39; \\   -d &#39;grading_scheme_entry[][value]&#x3D;94&#39; \\   -d &#39;grading_scheme_entry[][name]&#x3D;A-&#39; \\   -d &#39;grading_scheme_entry[][value]&#x3D;90&#39; \\   -d &#39;grading_scheme_entry[][name]&#x3D;B+&#39; \\   -d &#39;grading_scheme_entry[][value]&#x3D;87&#39; \\   -d &#39;grading_scheme_entry[][name]&#x3D;B&#39; \\   -d &#39;grading_scheme_entry[][value]&#x3D;84&#39; \\   -d &#39;grading_scheme_entry[][name]&#x3D;B-&#39; \\   -d &#39;grading_scheme_entry[][value]&#x3D;80&#39; \\   -d &#39;grading_scheme_entry[][name]&#x3D;C+&#39; \\   -d &#39;grading_scheme_entry[][value]&#x3D;77&#39; \\   -d &#39;grading_scheme_entry[][name]&#x3D;C&#39; \\   -d &#39;grading_scheme_entry[][value]&#x3D;74&#39; \\   -d &#39;grading_scheme_entry[][name]&#x3D;C-&#39; \\   -d &#39;grading_scheme_entry[][value]&#x3D;70&#39; \\   -d &#39;grading_scheme_entry[][name]&#x3D;D+&#39; \\   -d &#39;grading_scheme_entry[][value]&#x3D;67&#39; \\   -d &#39;grading_scheme_entry[][name]&#x3D;D&#39; \\   -d &#39;grading_scheme_entry[][value]&#x3D;64&#39; \\   -d &#39;grading_scheme_entry[][name]&#x3D;D-&#39; \\   -d &#39;grading_scheme_entry[][value]&#x3D;61&#39; \\   -d &#39;grading_scheme_entry[][name]&#x3D;F&#39; \\   -d &#39;grading_scheme_entry[][value]&#x3D;0&#39; &#x60;&#x60;&#x60; | [optional] 

### Return type

[**GradingStandard**](GradingStandard.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | GradingStandard |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

