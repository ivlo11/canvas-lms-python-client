# canvas_lms_python_client.ContentImportsApi

All URIs are relative to *https://canvas.instructure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**content_imports_copy_course_content**](ContentImportsApi.md#content_imports_copy_course_content) | **POST** /api/v1/courses/{course_id}/course_copy | Copy course content
[**content_imports_copy_course_status**](ContentImportsApi.md#content_imports_copy_course_status) | **GET** /api/v1/courses/{course_id}/course_copy/{id} | Get course copy status


# **content_imports_copy_course_content**
> ContentImportsCopyCourseStatusResponse content_imports_copy_course_content(course_id, content_imports_copy_course_content_request=content_imports_copy_course_content_request)

Copy course content

DEPRECATED: Please use the {api:ContentMigrationsController#create Content Migrations API}

Copies content from one course into another. The default is to copy all course
content. You can control specific types to copy by using either the 'except' option
or the 'only' option.

The response is the same as the course copy status endpoint

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.content_imports_copy_course_content_request import ContentImportsCopyCourseContentRequest
from canvas_lms_python_client.models.content_imports_copy_course_status_response import ContentImportsCopyCourseStatusResponse
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
    api_instance = canvas_lms_python_client.ContentImportsApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    content_imports_copy_course_content_request = canvas_lms_python_client.ContentImportsCopyCourseContentRequest() # ContentImportsCopyCourseContentRequest | Request body parameters (optional)

    try:
        # Copy course content
        api_response = await api_instance.content_imports_copy_course_content(course_id, content_imports_copy_course_content_request=content_imports_copy_course_content_request)
        print("The response of ContentImportsApi->content_imports_copy_course_content:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContentImportsApi->content_imports_copy_course_content: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **content_imports_copy_course_content_request** | [**ContentImportsCopyCourseContentRequest**](ContentImportsCopyCourseContentRequest.md)| Request body parameters | [optional] 

### Return type

[**ContentImportsCopyCourseStatusResponse**](ContentImportsCopyCourseStatusResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | ContentImportsCopyCourseStatusResponse |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **content_imports_copy_course_status**
> ContentImportsCopyCourseStatusResponse content_imports_copy_course_status(course_id, id)

Get course copy status

DEPRECATED: Please use the {api:ContentMigrationsController#create Content Migrations API}

Retrieve the status of a course copy

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.content_imports_copy_course_status_response import ContentImportsCopyCourseStatusResponse
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
    api_instance = canvas_lms_python_client.ContentImportsApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    id = 'id_example' # str | Scope response to id

    try:
        # Get course copy status
        api_response = await api_instance.content_imports_copy_course_status(course_id, id)
        print("The response of ContentImportsApi->content_imports_copy_course_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContentImportsApi->content_imports_copy_course_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **id** | **str**| Scope response to id | 

### Return type

[**ContentImportsCopyCourseStatusResponse**](ContentImportsCopyCourseStatusResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | ContentImportsCopyCourseStatusResponse |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

