# canvas_lms_python_client.SyllabusApiApi

All URIs are relative to *https://canvas.instructure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**syllabus_api_accessibility_queue_scan**](SyllabusApiApi.md#syllabus_api_accessibility_queue_scan) | **POST** /api/v1/courses/{course_id}/syllabus/accessibility/queue_scan | Queue syllabus accessibility scan
[**syllabus_api_accessibility_scan**](SyllabusApiApi.md#syllabus_api_accessibility_scan) | **POST** /api/v1/courses/{course_id}/syllabus/accessibility/scan | Scan syllabus for accessibility issues


# **syllabus_api_accessibility_queue_scan**
> object syllabus_api_accessibility_queue_scan(course_id)

Queue syllabus accessibility scan

Queues a course syllabus for accessibility scanning.

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
    api_instance = canvas_lms_python_client.SyllabusApiApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id

    try:
        # Queue syllabus accessibility scan
        api_response = await api_instance.syllabus_api_accessibility_queue_scan(course_id)
        print("The response of SyllabusApiApi->syllabus_api_accessibility_queue_scan:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SyllabusApiApi->syllabus_api_accessibility_queue_scan: %s\n" % e)
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
**0** | AccessibilityResourceScan |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **syllabus_api_accessibility_scan**
> object syllabus_api_accessibility_scan(course_id)

Scan syllabus for accessibility issues

Scans a course syllabus for accessibility issues and returns the results.

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
    api_instance = canvas_lms_python_client.SyllabusApiApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id

    try:
        # Scan syllabus for accessibility issues
        api_response = await api_instance.syllabus_api_accessibility_scan(course_id)
        print("The response of SyllabusApiApi->syllabus_api_accessibility_scan:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SyllabusApiApi->syllabus_api_accessibility_scan: %s\n" % e)
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
**0** | AccessibilityResourceScan |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

