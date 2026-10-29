# canvas_lms_python_client.QuizStatisticsApi

All URIs are relative to *https://canvas.instructure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**quiz_statistics_index**](QuizStatisticsApi.md#quiz_statistics_index) | **GET** /api/v1/courses/{course_id}/quizzes/{quiz_id}/statistics | Fetching the latest quiz statistics


# **quiz_statistics_index**
> quiz_statistics_index(course_id, quiz_id, all_versions=all_versions)

Fetching the latest quiz statistics

This endpoint provides statistics for all quiz versions, or for a specific
quiz version, in which case the output is guaranteed to represent the
_latest_ and most current version of the quiz.

<b>200 OK</b> response code is returned if the request was successful.

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
    api_instance = canvas_lms_python_client.QuizStatisticsApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    quiz_id = 'quiz_id_example' # str | Scope response to quiz_id
    all_versions = True # bool | Whether the statistics report should include all submissions attempts. (optional)

    try:
        # Fetching the latest quiz statistics
        await api_instance.quiz_statistics_index(course_id, quiz_id, all_versions=all_versions)
    except Exception as e:
        print("Exception when calling QuizStatisticsApi->quiz_statistics_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **quiz_id** | **str**| Scope response to quiz_id | 
 **all_versions** | **bool**| Whether the statistics report should include all submissions attempts. | [optional] 

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Fetching the latest quiz statistics |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

