# canvas_lms_python_client.CourseReportsApi

All URIs are relative to *https://canvas.instructure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**course_reports_create**](CourseReportsApi.md#course_reports_create) | **POST** /api/v1/courses/{course_id}/reports/{report_type} | Start a Report
[**course_reports_last**](CourseReportsApi.md#course_reports_last) | **GET** /api/v1/courses/{course_id}/reports/{report_type} | Status of last Report
[**course_reports_show**](CourseReportsApi.md#course_reports_show) | **GET** /api/v1/courses/{course_id}/reports/{report_type}/{id} | Status of a Report


# **course_reports_create**
> Report course_reports_create(course_id, report_type, course_reports_create_request=course_reports_create_request)

Start a Report

Generates a report instance for the account. Note that "report" in the
request must match one of the available report names.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.course_reports_create_request import CourseReportsCreateRequest
from canvas_lms_python_client.models.report import Report
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
    api_instance = canvas_lms_python_client.CourseReportsApi(api_client)
    course_id = 'course_id_example' # str | The id of the course to report on.
    report_type = 'report_type_example' # str | The type of report to generate.
    course_reports_create_request = canvas_lms_python_client.CourseReportsCreateRequest() # CourseReportsCreateRequest | Request body parameters (optional)

    try:
        # Start a Report
        api_response = await api_instance.course_reports_create(course_id, report_type, course_reports_create_request=course_reports_create_request)
        print("The response of CourseReportsApi->course_reports_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CourseReportsApi->course_reports_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| The id of the course to report on. | 
 **report_type** | **str**| The type of report to generate. | 
 **course_reports_create_request** | [**CourseReportsCreateRequest**](CourseReportsCreateRequest.md)| Request body parameters | [optional] 

### Return type

[**Report**](Report.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Report |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **course_reports_last**
> Report course_reports_last(course_id, report_type)

Status of last Report

Returns the status of the last report initiated by the current user.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.report import Report
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
    api_instance = canvas_lms_python_client.CourseReportsApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    report_type = 'report_type_example' # str | Scope response to report_type

    try:
        # Status of last Report
        api_response = await api_instance.course_reports_last(course_id, report_type)
        print("The response of CourseReportsApi->course_reports_last:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CourseReportsApi->course_reports_last: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **report_type** | **str**| Scope response to report_type | 

### Return type

[**Report**](Report.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Report |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **course_reports_show**
> Report course_reports_show(course_id, id, report_type)

Status of a Report

Returns the status of a report.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.report import Report
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
    api_instance = canvas_lms_python_client.CourseReportsApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    id = 'id_example' # str | Scope response to id
    report_type = 'report_type_example' # str | Scope response to report_type

    try:
        # Status of a Report
        api_response = await api_instance.course_reports_show(course_id, id, report_type)
        print("The response of CourseReportsApi->course_reports_show:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CourseReportsApi->course_reports_show: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **id** | **str**| Scope response to id | 
 **report_type** | **str**| Scope response to report_type | 

### Return type

[**Report**](Report.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Report |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

