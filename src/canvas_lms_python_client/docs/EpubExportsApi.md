# canvas_lms_python_client.EpubExportsApi

All URIs are relative to *https://canvas.instructure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**epub_exports_create**](EpubExportsApi.md#epub_exports_create) | **POST** /api/v1/courses/{course_id}/epub_exports | Create ePub Export
[**epub_exports_index**](EpubExportsApi.md#epub_exports_index) | **GET** /api/v1/epub_exports | List courses with their latest ePub export
[**epub_exports_show**](EpubExportsApi.md#epub_exports_show) | **GET** /api/v1/courses/{course_id}/epub_exports/{id} | Show ePub export


# **epub_exports_create**
> EpubExport epub_exports_create(course_id)

Create ePub Export

Begin an ePub export for a course.

You can use the {api:ProgressController#show Progress API} to track the
progress of the export. The export's progress is linked to with the
_progress_url_ value.

When the export completes, use the {api:EpubExportsController#show Show content export} endpoint
to retrieve a download URL for the exported content.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.epub_export import EpubExport
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
    api_instance = canvas_lms_python_client.EpubExportsApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id

    try:
        # Create ePub Export
        api_response = await api_instance.epub_exports_create(course_id)
        print("The response of EpubExportsApi->epub_exports_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EpubExportsApi->epub_exports_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 

### Return type

[**EpubExport**](EpubExport.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | EpubExport |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **epub_exports_index**
> List[CourseEpubExport] epub_exports_index()

List courses with their latest ePub export

A paginated list of all courses a user is actively participating in, and
the latest ePub export associated with the user & course.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.course_epub_export import CourseEpubExport
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
    api_instance = canvas_lms_python_client.EpubExportsApi(api_client)

    try:
        # List courses with their latest ePub export
        api_response = await api_instance.epub_exports_index()
        print("The response of EpubExportsApi->epub_exports_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EpubExportsApi->epub_exports_index: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[CourseEpubExport]**](CourseEpubExport.md)

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

# **epub_exports_show**
> EpubExport epub_exports_show(course_id, id)

Show ePub export

Get information about a single ePub export.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.epub_export import EpubExport
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
    api_instance = canvas_lms_python_client.EpubExportsApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    id = 'id_example' # str | Scope response to id

    try:
        # Show ePub export
        api_response = await api_instance.epub_exports_show(course_id, id)
        print("The response of EpubExportsApi->epub_exports_show:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EpubExportsApi->epub_exports_show: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **id** | **str**| Scope response to id | 

### Return type

[**EpubExport**](EpubExport.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | EpubExport |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

