# canvas_lms_python_client.CourseQuizExtensionsApi

All URIs are relative to *https://canvas.instructure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**course_quiz_extensions_create**](CourseQuizExtensionsApi.md#course_quiz_extensions_create) | **POST** /api/v1/courses/{course_id}/quiz_extensions | Set extensions for student quiz submissions


# **course_quiz_extensions_create**
> QuizExtensionsResponse course_quiz_extensions_create(course_id, course_quiz_extensions_create_request=course_quiz_extensions_create_request)

Set extensions for student quiz submissions

<b>Responses</b>

* <b>200 OK</b> if the request was successful
* <b>403 Forbidden</b> if you are not allowed to extend quizzes for this course

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.course_quiz_extensions_create_request import CourseQuizExtensionsCreateRequest
from canvas_lms_python_client.models.quiz_extensions_response import QuizExtensionsResponse
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
    api_instance = canvas_lms_python_client.CourseQuizExtensionsApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    course_quiz_extensions_create_request = canvas_lms_python_client.CourseQuizExtensionsCreateRequest() # CourseQuizExtensionsCreateRequest | Request body parameters  **Example Request:** ``` {   \"quiz_extensions\": [{     \"user_id\": 3,     \"extra_attempts\": 2,     \"extra_time\": 20,     \"manually_unlocked\": true   },{     \"user_id\": 2,     \"extra_attempts\": 2,     \"extra_time\": 20,     \"manually_unlocked\": false   }] } ``` (optional)

    try:
        # Set extensions for student quiz submissions
        api_response = await api_instance.course_quiz_extensions_create(course_id, course_quiz_extensions_create_request=course_quiz_extensions_create_request)
        print("The response of CourseQuizExtensionsApi->course_quiz_extensions_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CourseQuizExtensionsApi->course_quiz_extensions_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **course_quiz_extensions_create_request** | [**CourseQuizExtensionsCreateRequest**](CourseQuizExtensionsCreateRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; {   \&quot;quiz_extensions\&quot;: [{     \&quot;user_id\&quot;: 3,     \&quot;extra_attempts\&quot;: 2,     \&quot;extra_time\&quot;: 20,     \&quot;manually_unlocked\&quot;: true   },{     \&quot;user_id\&quot;: 2,     \&quot;extra_attempts\&quot;: 2,     \&quot;extra_time\&quot;: 20,     \&quot;manually_unlocked\&quot;: false   }] } &#x60;&#x60;&#x60; | [optional] 

### Return type

[**QuizExtensionsResponse**](QuizExtensionsResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Set extensions for student quiz submissions |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

