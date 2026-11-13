# canvas_lms_python_client.QuizSubmissionEventsApiApi

All URIs are relative to *https://canvas.instructure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**quiz_submission_events_api_create**](QuizSubmissionEventsApiApi.md#quiz_submission_events_api_create) | **POST** /api/v1/courses/{course_id}/quizzes/{quiz_id}/submissions/{id}/events | Submit captured events
[**quiz_submission_events_api_index**](QuizSubmissionEventsApiApi.md#quiz_submission_events_api_index) | **GET** /api/v1/courses/{course_id}/quizzes/{quiz_id}/submissions/{id}/events | Retrieve captured events


# **quiz_submission_events_api_create**
> quiz_submission_events_api_create(course_id, id, quiz_id, quiz_submission_events_api_create_request=quiz_submission_events_api_create_request)

Submit captured events

Store a set of events which were captured during a quiz taking session.

On success, the response will be 204 No Content with an empty body.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.quiz_submission_events_api_create_request import QuizSubmissionEventsApiCreateRequest
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
    api_instance = canvas_lms_python_client.QuizSubmissionEventsApiApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    id = 'id_example' # str | Scope response to id
    quiz_id = 'quiz_id_example' # str | Scope response to quiz_id
    quiz_submission_events_api_create_request = canvas_lms_python_client.QuizSubmissionEventsApiCreateRequest() # QuizSubmissionEventsApiCreateRequest | Request body parameters  **Example Request:** ``` {   \"quiz_submission_events\":   [     {       \"client_timestamp\": \"2014-10-08T19:29:58Z\",       \"event_type\": \"question_answered\",       \"event_data\" : {\"answer\": \"42\"}     }, {       \"client_timestamp\": \"2014-10-08T19:30:17Z\",       \"event_type\": \"question_flagged\",       \"event_data\" : { \"question_id\": \"1\", \"flagged\": true }     }   ] } ``` (optional)

    try:
        # Submit captured events
        await api_instance.quiz_submission_events_api_create(course_id, id, quiz_id, quiz_submission_events_api_create_request=quiz_submission_events_api_create_request)
    except Exception as e:
        print("Exception when calling QuizSubmissionEventsApiApi->quiz_submission_events_api_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **id** | **str**| Scope response to id | 
 **quiz_id** | **str**| Scope response to quiz_id | 
 **quiz_submission_events_api_create_request** | [**QuizSubmissionEventsApiCreateRequest**](QuizSubmissionEventsApiCreateRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; {   \&quot;quiz_submission_events\&quot;:   [     {       \&quot;client_timestamp\&quot;: \&quot;2014-10-08T19:29:58Z\&quot;,       \&quot;event_type\&quot;: \&quot;question_answered\&quot;,       \&quot;event_data\&quot; : {\&quot;answer\&quot;: \&quot;42\&quot;}     }, {       \&quot;client_timestamp\&quot;: \&quot;2014-10-08T19:30:17Z\&quot;,       \&quot;event_type\&quot;: \&quot;question_flagged\&quot;,       \&quot;event_data\&quot; : { \&quot;question_id\&quot;: \&quot;1\&quot;, \&quot;flagged\&quot;: true }     }   ] } &#x60;&#x60;&#x60; | [optional] 

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Submit captured events |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **quiz_submission_events_api_index**
> QuizSubmissionEventsApiIndexResponse quiz_submission_events_api_index(course_id, id, quiz_id, attempt=attempt, page=page, per_page=per_page)

Retrieve captured events

Retrieve the set of events captured during a specific submission attempt.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.quiz_submission_events_api_index_response import QuizSubmissionEventsApiIndexResponse
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
    api_instance = canvas_lms_python_client.QuizSubmissionEventsApiApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    id = 'id_example' # str | Scope response to id
    quiz_id = 'quiz_id_example' # str | Scope response to quiz_id
    attempt = 56 # int | The specific submission attempt to look up the events for. If unspecified, the latest attempt will be used. (optional)
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # Retrieve captured events
        api_response = await api_instance.quiz_submission_events_api_index(course_id, id, quiz_id, attempt=attempt, page=page, per_page=per_page)
        print("The response of QuizSubmissionEventsApiApi->quiz_submission_events_api_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuizSubmissionEventsApiApi->quiz_submission_events_api_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **id** | **str**| Scope response to id | 
 **quiz_id** | **str**| Scope response to quiz_id | 
 **attempt** | **int**| The specific submission attempt to look up the events for. If unspecified, the latest attempt will be used. | [optional] 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**QuizSubmissionEventsApiIndexResponse**](QuizSubmissionEventsApiIndexResponse.md)

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

