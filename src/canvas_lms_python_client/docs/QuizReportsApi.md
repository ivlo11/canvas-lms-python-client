# canvas_lms_python_client.QuizReportsApi

All URIs are relative to *https://canvas.instructure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**quiz_reports_abort**](QuizReportsApi.md#quiz_reports_abort) | **DELETE** /api/v1/courses/{course_id}/quizzes/{quiz_id}/reports/{id} | Abort the generation of a report, or remove a previously generated one
[**quiz_reports_create**](QuizReportsApi.md#quiz_reports_create) | **POST** /api/v1/courses/{course_id}/quizzes/{quiz_id}/reports | Create a quiz report
[**quiz_reports_index**](QuizReportsApi.md#quiz_reports_index) | **GET** /api/v1/courses/{course_id}/quizzes/{quiz_id}/reports | Retrieve all quiz reports
[**quiz_reports_show**](QuizReportsApi.md#quiz_reports_show) | **GET** /api/v1/courses/{course_id}/quizzes/{quiz_id}/reports/{id} | Get a quiz report


# **quiz_reports_abort**
> quiz_reports_abort(course_id, id, quiz_id)

Abort the generation of a report, or remove a previously generated one

This API allows you to cancel a previous request you issued for a report to
be generated. Or in the case of an already generated report, you'd like to
remove it, perhaps to generate it another time with an updated version that
provides new features.

You must check the report's generation status before attempting to use this
interface. See the "workflow_state" property of the QuizReport's Progress
object for more information. Only when the progress reports itself in a
"queued" state can the generation be aborted.

*Responses*

- <code>204 No Content</code> if your request was accepted
- <code>422 Unprocessable Entity</code> if the report is not being generated
  or can not be aborted at this stage

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
    api_instance = canvas_lms_python_client.QuizReportsApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    id = 'id_example' # str | Scope response to id
    quiz_id = 'quiz_id_example' # str | Scope response to quiz_id

    try:
        # Abort the generation of a report, or remove a previously generated one
        await api_instance.quiz_reports_abort(course_id, id, quiz_id)
    except Exception as e:
        print("Exception when calling QuizReportsApi->quiz_reports_abort: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **id** | **str**| Scope response to id | 
 **quiz_id** | **str**| Scope response to quiz_id | 

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
**0** | Abort the generation of a report, or remove a previously generated one |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **quiz_reports_create**
> QuizReport quiz_reports_create(course_id, quiz_id, quiz_reports_create_request=quiz_reports_create_request)

Create a quiz report

Create and return a new report for this quiz. If a previously
generated report matches the arguments and is still current (i.e.
there have been no new submissions), it will be returned.

*Responses*

* <code>400 Bad Request</code> if the specified report type is invalid
* <code>409 Conflict</code> if a quiz report of the specified type is already being
  generated

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.quiz_report import QuizReport
from canvas_lms_python_client.models.quiz_reports_create_request import QuizReportsCreateRequest
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
    api_instance = canvas_lms_python_client.QuizReportsApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    quiz_id = 'quiz_id_example' # str | Scope response to quiz_id
    quiz_reports_create_request = canvas_lms_python_client.QuizReportsCreateRequest() # QuizReportsCreateRequest | Request body parameters (optional)

    try:
        # Create a quiz report
        api_response = await api_instance.quiz_reports_create(course_id, quiz_id, quiz_reports_create_request=quiz_reports_create_request)
        print("The response of QuizReportsApi->quiz_reports_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuizReportsApi->quiz_reports_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **quiz_id** | **str**| Scope response to quiz_id | 
 **quiz_reports_create_request** | [**QuizReportsCreateRequest**](QuizReportsCreateRequest.md)| Request body parameters | [optional] 

### Return type

[**QuizReport**](QuizReport.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | QuizReport |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **quiz_reports_index**
> List[QuizReport] quiz_reports_index(course_id, quiz_id, includes_all_versions=includes_all_versions)

Retrieve all quiz reports

Returns a list of all available reports.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.quiz_report import QuizReport
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
    api_instance = canvas_lms_python_client.QuizReportsApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    quiz_id = 'quiz_id_example' # str | Scope response to quiz_id
    includes_all_versions = True # bool | Whether to retrieve reports that consider all the submissions or only the most recent. Defaults to false, ignored for item_analysis reports. (optional)

    try:
        # Retrieve all quiz reports
        api_response = await api_instance.quiz_reports_index(course_id, quiz_id, includes_all_versions=includes_all_versions)
        print("The response of QuizReportsApi->quiz_reports_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuizReportsApi->quiz_reports_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **quiz_id** | **str**| Scope response to quiz_id | 
 **includes_all_versions** | **bool**| Whether to retrieve reports that consider all the submissions or only the most recent. Defaults to false, ignored for item_analysis reports. | [optional] 

### Return type

[**List[QuizReport]**](QuizReport.md)

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

# **quiz_reports_show**
> QuizReport quiz_reports_show(course_id, id, quiz_id, include_string=include_string)

Get a quiz report

Returns the data for a single quiz report.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.quiz_report import QuizReport
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
    api_instance = canvas_lms_python_client.QuizReportsApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    id = 'id_example' # str | Scope response to id
    quiz_id = 'quiz_id_example' # str | Scope response to quiz_id
    include_string = 'include_string_example' # str | Whether the output should include documents for the file and/or progress objects associated with this report. (Note: JSON-API only) (optional)

    try:
        # Get a quiz report
        api_response = await api_instance.quiz_reports_show(course_id, id, quiz_id, include_string=include_string)
        print("The response of QuizReportsApi->quiz_reports_show:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuizReportsApi->quiz_reports_show: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **id** | **str**| Scope response to id | 
 **quiz_id** | **str**| Scope response to quiz_id | 
 **include_string** | **str**| Whether the output should include documents for the file and/or progress objects associated with this report. (Note: JSON-API only) | [optional] 

### Return type

[**QuizReport**](QuizReport.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | QuizReport |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

