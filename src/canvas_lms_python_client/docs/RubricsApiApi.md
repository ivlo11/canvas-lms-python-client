# canvas_lms_python_client.RubricsApiApi

All URIs are relative to *https://canvas.instructure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rubrics_api_index**](RubricsApiApi.md#rubrics_api_index) | **GET** /api/v1/accounts/{account_id}/rubrics | List rubrics
[**rubrics_api_index_for_courses**](RubricsApiApi.md#rubrics_api_index_for_courses) | **GET** /api/v1/courses/{course_id}/rubrics | List rubrics
[**rubrics_api_show**](RubricsApiApi.md#rubrics_api_show) | **GET** /api/v1/accounts/{account_id}/rubrics/{id} | Get a single rubric
[**rubrics_api_show_for_courses**](RubricsApiApi.md#rubrics_api_show_for_courses) | **GET** /api/v1/courses/{course_id}/rubrics/{id} | Get a single rubric
[**rubrics_api_upload**](RubricsApiApi.md#rubrics_api_upload) | **POST** /api/v1/courses/{course_id}/rubrics/upload | Creates a rubric using a CSV file
[**rubrics_api_upload_for_accounts**](RubricsApiApi.md#rubrics_api_upload_for_accounts) | **POST** /api/v1/accounts/{account_id}/rubrics/upload | Creates a rubric using a CSV file
[**rubrics_api_upload_status**](RubricsApiApi.md#rubrics_api_upload_status) | **GET** /api/v1/courses/{course_id}/rubrics/upload/{id} | Get the status of a rubric import
[**rubrics_api_upload_status_for_accounts**](RubricsApiApi.md#rubrics_api_upload_status_for_accounts) | **GET** /api/v1/accounts/{account_id}/rubrics/upload/{id} | Get the status of a rubric import
[**rubrics_api_upload_template**](RubricsApiApi.md#rubrics_api_upload_template) | **GET** /api/v1/rubrics/upload_template | Templated file for importing a rubric
[**rubrics_api_used_locations**](RubricsApiApi.md#rubrics_api_used_locations) | **GET** /api/v1/courses/{course_id}/rubrics/{id}/used_locations | Get the courses and assignments for a rubric
[**rubrics_api_used_locations_for_accounts**](RubricsApiApi.md#rubrics_api_used_locations_for_accounts) | **GET** /api/v1/accounts/{account_id}/rubrics/{id}/used_locations | Get the courses and assignments for a rubric


# **rubrics_api_index**
> List[Rubric] rubrics_api_index(account_id, page=page, per_page=per_page)

List rubrics

Returns the paginated list of active rubrics for the current context.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.rubric import Rubric
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
    api_instance = canvas_lms_python_client.RubricsApiApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # List rubrics
        api_response = await api_instance.rubrics_api_index(account_id, page=page, per_page=per_page)
        print("The response of RubricsApiApi->rubrics_api_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RubricsApiApi->rubrics_api_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**List[Rubric]**](Rubric.md)

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

# **rubrics_api_index_for_courses**
> List[Rubric] rubrics_api_index_for_courses(course_id, page=page, per_page=per_page)

List rubrics

Returns the paginated list of active rubrics for the current context.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.rubric import Rubric
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
    api_instance = canvas_lms_python_client.RubricsApiApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # List rubrics
        api_response = await api_instance.rubrics_api_index_for_courses(course_id, page=page, per_page=per_page)
        print("The response of RubricsApiApi->rubrics_api_index_for_courses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RubricsApiApi->rubrics_api_index_for_courses: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**List[Rubric]**](Rubric.md)

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

# **rubrics_api_show**
> Rubric rubrics_api_show(account_id, id, include=include, style=style)

Get a single rubric

Returns the rubric with the given id.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.rubric import Rubric
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
    api_instance = canvas_lms_python_client.RubricsApiApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    id = 'id_example' # str | Scope response to id
    include = ['include_example'] # List[str] | Related records to include in the response. (optional)
    style = 'style_example' # str | Applicable only if assessments are being returned. If included, returns either all criteria data associated with the assessment, or just the comments. If not included, both data and comments are omitted. (optional)

    try:
        # Get a single rubric
        api_response = await api_instance.rubrics_api_show(account_id, id, include=include, style=style)
        print("The response of RubricsApiApi->rubrics_api_show:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RubricsApiApi->rubrics_api_show: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **id** | **str**| Scope response to id | 
 **include** | [**List[str]**](str.md)| Related records to include in the response. | [optional] 
 **style** | **str**| Applicable only if assessments are being returned. If included, returns either all criteria data associated with the assessment, or just the comments. If not included, both data and comments are omitted. | [optional] 

### Return type

[**Rubric**](Rubric.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Rubric |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rubrics_api_show_for_courses**
> Rubric rubrics_api_show_for_courses(course_id, id, include=include, style=style)

Get a single rubric

Returns the rubric with the given id.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.rubric import Rubric
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
    api_instance = canvas_lms_python_client.RubricsApiApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    id = 'id_example' # str | Scope response to id
    include = ['include_example'] # List[str] | Related records to include in the response. (optional)
    style = 'style_example' # str | Applicable only if assessments are being returned. If included, returns either all criteria data associated with the assessment, or just the comments. If not included, both data and comments are omitted. (optional)

    try:
        # Get a single rubric
        api_response = await api_instance.rubrics_api_show_for_courses(course_id, id, include=include, style=style)
        print("The response of RubricsApiApi->rubrics_api_show_for_courses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RubricsApiApi->rubrics_api_show_for_courses: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **id** | **str**| Scope response to id | 
 **include** | [**List[str]**](str.md)| Related records to include in the response. | [optional] 
 **style** | **str**| Applicable only if assessments are being returned. If included, returns either all criteria data associated with the assessment, or just the comments. If not included, both data and comments are omitted. | [optional] 

### Return type

[**Rubric**](Rubric.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Rubric |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rubrics_api_upload**
> object rubrics_api_upload(course_id)

Creates a rubric using a CSV file

Returns the rubric import object that was created

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
    api_instance = canvas_lms_python_client.RubricsApiApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id

    try:
        # Creates a rubric using a CSV file
        api_response = await api_instance.rubrics_api_upload(course_id)
        print("The response of RubricsApiApi->rubrics_api_upload:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RubricsApiApi->rubrics_api_upload: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 

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
**0** | RubricImport |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rubrics_api_upload_for_accounts**
> object rubrics_api_upload_for_accounts(account_id)

Creates a rubric using a CSV file

Returns the rubric import object that was created

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
    api_instance = canvas_lms_python_client.RubricsApiApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id

    try:
        # Creates a rubric using a CSV file
        api_response = await api_instance.rubrics_api_upload_for_accounts(account_id)
        print("The response of RubricsApiApi->rubrics_api_upload_for_accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RubricsApiApi->rubrics_api_upload_for_accounts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 

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
**0** | RubricImport |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rubrics_api_upload_status**
> object rubrics_api_upload_status(course_id, id)

Get the status of a rubric import

Can return the latest rubric import for an account or course, or a specific import by id

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
    api_instance = canvas_lms_python_client.RubricsApiApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    id = 'id_example' # str | Scope response to id

    try:
        # Get the status of a rubric import
        api_response = await api_instance.rubrics_api_upload_status(course_id, id)
        print("The response of RubricsApiApi->rubrics_api_upload_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RubricsApiApi->rubrics_api_upload_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **id** | **str**| Scope response to id | 

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
**0** | RubricImport |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rubrics_api_upload_status_for_accounts**
> object rubrics_api_upload_status_for_accounts(account_id, id)

Get the status of a rubric import

Can return the latest rubric import for an account or course, or a specific import by id

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
    api_instance = canvas_lms_python_client.RubricsApiApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    id = 'id_example' # str | Scope response to id

    try:
        # Get the status of a rubric import
        api_response = await api_instance.rubrics_api_upload_status_for_accounts(account_id, id)
        print("The response of RubricsApiApi->rubrics_api_upload_status_for_accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RubricsApiApi->rubrics_api_upload_status_for_accounts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **id** | **str**| Scope response to id | 

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
**0** | RubricImport |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rubrics_api_upload_template**
> object rubrics_api_upload_template()

Templated file for importing a rubric

Returns a CSV template file that can be used to import rubrics into Canvas.

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
    api_instance = canvas_lms_python_client.RubricsApiApi(api_client)

    try:
        # Templated file for importing a rubric
        api_response = await api_instance.rubrics_api_upload_template()
        print("The response of RubricsApiApi->rubrics_api_upload_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RubricsApiApi->rubrics_api_upload_template: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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
**0** | a CSV file in the format that can be imported |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rubrics_api_used_locations**
> List[RubricUsedLocation] rubrics_api_used_locations(course_id, id, page=page, per_page=per_page)

Get the courses and assignments for a rubric

Returns the courses and assignments where a rubric is being used

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.rubric_used_location import RubricUsedLocation
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
    api_instance = canvas_lms_python_client.RubricsApiApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    id = 'id_example' # str | Scope response to id
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # Get the courses and assignments for a rubric
        api_response = await api_instance.rubrics_api_used_locations(course_id, id, page=page, per_page=per_page)
        print("The response of RubricsApiApi->rubrics_api_used_locations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RubricsApiApi->rubrics_api_used_locations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **id** | **str**| Scope response to id | 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**List[RubricUsedLocation]**](RubricUsedLocation.md)

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

# **rubrics_api_used_locations_for_accounts**
> List[RubricUsedLocation] rubrics_api_used_locations_for_accounts(account_id, id, page=page, per_page=per_page)

Get the courses and assignments for a rubric

Returns the courses and assignments where a rubric is being used

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.rubric_used_location import RubricUsedLocation
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
    api_instance = canvas_lms_python_client.RubricsApiApi(api_client)
    account_id = 'account_id_example' # str | Scope response to account_id
    id = 'id_example' # str | Scope response to id
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # Get the courses and assignments for a rubric
        api_response = await api_instance.rubrics_api_used_locations_for_accounts(account_id, id, page=page, per_page=per_page)
        print("The response of RubricsApiApi->rubrics_api_used_locations_for_accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RubricsApiApi->rubrics_api_used_locations_for_accounts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Scope response to account_id | 
 **id** | **str**| Scope response to id | 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**List[RubricUsedLocation]**](RubricUsedLocation.md)

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

