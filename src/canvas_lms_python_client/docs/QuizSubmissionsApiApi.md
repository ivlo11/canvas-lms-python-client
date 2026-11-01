# canvas_lms_python_client.QuizSubmissionsApiApi

All URIs are relative to *https://canvas.instructure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**quiz_submissions_api_complete**](QuizSubmissionsApiApi.md#quiz_submissions_api_complete) | **POST** /api/v1/courses/{course_id}/quizzes/{quiz_id}/submissions/{id}/complete | Complete the quiz submission (turn it in).
[**quiz_submissions_api_create**](QuizSubmissionsApiApi.md#quiz_submissions_api_create) | **POST** /api/v1/courses/{course_id}/quizzes/{quiz_id}/submissions | Create the quiz submission (start a quiz-taking session)
[**quiz_submissions_api_index**](QuizSubmissionsApiApi.md#quiz_submissions_api_index) | **GET** /api/v1/courses/{course_id}/quizzes/{quiz_id}/submissions | Get all quiz submissions.
[**quiz_submissions_api_show**](QuizSubmissionsApiApi.md#quiz_submissions_api_show) | **GET** /api/v1/courses/{course_id}/quizzes/{quiz_id}/submissions/{id} | Get a single quiz submission.
[**quiz_submissions_api_submission**](QuizSubmissionsApiApi.md#quiz_submissions_api_submission) | **GET** /api/v1/courses/{course_id}/quizzes/{quiz_id}/submission | Get the quiz submission.
[**quiz_submissions_api_time**](QuizSubmissionsApiApi.md#quiz_submissions_api_time) | **GET** /api/v1/courses/{course_id}/quizzes/{quiz_id}/submissions/{id}/time | Get current quiz submission times.
[**quiz_submissions_api_update**](QuizSubmissionsApiApi.md#quiz_submissions_api_update) | **PUT** /api/v1/courses/{course_id}/quizzes/{quiz_id}/submissions/{id} | Update student question scores and comments.


# **quiz_submissions_api_complete**
> QuizSubmissionsResponse quiz_submissions_api_complete(course_id, id, quiz_id, quiz_submissions_api_complete_request=quiz_submissions_api_complete_request)

Complete the quiz submission (turn it in).

Complete the quiz submission by marking it as complete and grading it. When
the quiz submission has been marked as complete, no further modifications
will be allowed.

<b>Responses</b>

* <b>200 OK</b> if the request was successful
* <b>403 Forbidden</b> if an invalid access code is specified
* <b>403 Forbidden</b> if the Quiz's IP filter restriction does not pass
* <b>403 Forbidden</b> if an invalid token is specified
* <b>400 Bad Request</b> if the QS is already complete
* <b>400 Bad Request</b> if the attempt parameter is missing
* <b>400 Bad Request</b> if the attempt parameter is not the latest attempt

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.quiz_submissions_api_complete_request import QuizSubmissionsApiCompleteRequest
from canvas_lms_python_client.models.quiz_submissions_response import QuizSubmissionsResponse
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
    api_instance = canvas_lms_python_client.QuizSubmissionsApiApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    id = 'id_example' # str | Scope response to id
    quiz_id = 'quiz_id_example' # str | Scope response to quiz_id
    quiz_submissions_api_complete_request = canvas_lms_python_client.QuizSubmissionsApiCompleteRequest() # QuizSubmissionsApiCompleteRequest | Request body parameters (optional)

    try:
        # Complete the quiz submission (turn it in).
        api_response = await api_instance.quiz_submissions_api_complete(course_id, id, quiz_id, quiz_submissions_api_complete_request=quiz_submissions_api_complete_request)
        print("The response of QuizSubmissionsApiApi->quiz_submissions_api_complete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuizSubmissionsApiApi->quiz_submissions_api_complete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **id** | **str**| Scope response to id | 
 **quiz_id** | **str**| Scope response to quiz_id | 
 **quiz_submissions_api_complete_request** | [**QuizSubmissionsApiCompleteRequest**](QuizSubmissionsApiCompleteRequest.md)| Request body parameters | [optional] 

### Return type

[**QuizSubmissionsResponse**](QuizSubmissionsResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Complete the quiz submission (turn it in). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **quiz_submissions_api_create**
> QuizSubmissionsResponse quiz_submissions_api_create(course_id, quiz_id, quiz_submissions_api_create_request=quiz_submissions_api_create_request)

Create the quiz submission (start a quiz-taking session)

Start taking a Quiz by creating a QuizSubmission which you can use to answer
questions and submit your answers.

<b>Responses</b>

* <b>200 OK</b> if the request was successful
* <b>400 Bad Request</b> if the quiz is locked
* <b>403 Forbidden</b> if an invalid access code is specified
* <b>403 Forbidden</b> if the Quiz's IP filter restriction does not pass
* <b>409 Conflict</b> if a QuizSubmission already exists for this user and quiz

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.quiz_submissions_api_create_request import QuizSubmissionsApiCreateRequest
from canvas_lms_python_client.models.quiz_submissions_response import QuizSubmissionsResponse
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
    api_instance = canvas_lms_python_client.QuizSubmissionsApiApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    quiz_id = 'quiz_id_example' # str | Scope response to quiz_id
    quiz_submissions_api_create_request = canvas_lms_python_client.QuizSubmissionsApiCreateRequest() # QuizSubmissionsApiCreateRequest | Request body parameters (optional)

    try:
        # Create the quiz submission (start a quiz-taking session)
        api_response = await api_instance.quiz_submissions_api_create(course_id, quiz_id, quiz_submissions_api_create_request=quiz_submissions_api_create_request)
        print("The response of QuizSubmissionsApiApi->quiz_submissions_api_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuizSubmissionsApiApi->quiz_submissions_api_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **quiz_id** | **str**| Scope response to quiz_id | 
 **quiz_submissions_api_create_request** | [**QuizSubmissionsApiCreateRequest**](QuizSubmissionsApiCreateRequest.md)| Request body parameters | [optional] 

### Return type

[**QuizSubmissionsResponse**](QuizSubmissionsResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Create the quiz submission (start a quiz-taking session) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **quiz_submissions_api_index**
> QuizSubmissionsResponse quiz_submissions_api_index(course_id, quiz_id, include=include, page=page, per_page=per_page)

Get all quiz submissions.

Get a list of all submissions for this quiz. Users who can view or manage
grades for a course will have submissions from multiple users returned. A
user who can only submit will have only their own submissions returned. When
a user has an in-progress submission, only that submission is returned. When
there isn't an in-progress quiz_submission, all completed submissions,
including previous attempts, are returned.

<b>200 OK</b> response code is returned if the request was successful.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.quiz_submissions_response import QuizSubmissionsResponse
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
    api_instance = canvas_lms_python_client.QuizSubmissionsApiApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    quiz_id = 'quiz_id_example' # str | Scope response to quiz_id
    include = ['include_example'] # List[str] | Associations to include with the quiz submission. (optional)
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # Get all quiz submissions.
        api_response = await api_instance.quiz_submissions_api_index(course_id, quiz_id, include=include, page=page, per_page=per_page)
        print("The response of QuizSubmissionsApiApi->quiz_submissions_api_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuizSubmissionsApiApi->quiz_submissions_api_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **quiz_id** | **str**| Scope response to quiz_id | 
 **include** | [**List[str]**](str.md)| Associations to include with the quiz submission. | [optional] 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**QuizSubmissionsResponse**](QuizSubmissionsResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Get all quiz submissions. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **quiz_submissions_api_show**
> QuizSubmissionsResponse quiz_submissions_api_show(course_id, id, quiz_id, include=include)

Get a single quiz submission.

Get a single quiz submission.

<b>200 OK</b> response code is returned if the request was successful.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.quiz_submissions_response import QuizSubmissionsResponse
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
    api_instance = canvas_lms_python_client.QuizSubmissionsApiApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    id = 'id_example' # str | Scope response to id
    quiz_id = 'quiz_id_example' # str | Scope response to quiz_id
    include = ['include_example'] # List[str] | Associations to include with the quiz submission. (optional)

    try:
        # Get a single quiz submission.
        api_response = await api_instance.quiz_submissions_api_show(course_id, id, quiz_id, include=include)
        print("The response of QuizSubmissionsApiApi->quiz_submissions_api_show:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuizSubmissionsApiApi->quiz_submissions_api_show: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **id** | **str**| Scope response to id | 
 **quiz_id** | **str**| Scope response to quiz_id | 
 **include** | [**List[str]**](str.md)| Associations to include with the quiz submission. | [optional] 

### Return type

[**QuizSubmissionsResponse**](QuizSubmissionsResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Get a single quiz submission. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **quiz_submissions_api_submission**
> QuizSubmissionsResponse quiz_submissions_api_submission(course_id, quiz_id, include=include)

Get the quiz submission.

Get the submission for this quiz for the current user.

<b>200 OK</b> response code is returned if the request was successful.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.quiz_submissions_response import QuizSubmissionsResponse
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
    api_instance = canvas_lms_python_client.QuizSubmissionsApiApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    quiz_id = 'quiz_id_example' # str | Scope response to quiz_id
    include = ['include_example'] # List[str] | Associations to include with the quiz submission. (optional)

    try:
        # Get the quiz submission.
        api_response = await api_instance.quiz_submissions_api_submission(course_id, quiz_id, include=include)
        print("The response of QuizSubmissionsApiApi->quiz_submissions_api_submission:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuizSubmissionsApiApi->quiz_submissions_api_submission: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **quiz_id** | **str**| Scope response to quiz_id | 
 **include** | [**List[str]**](str.md)| Associations to include with the quiz submission. | [optional] 

### Return type

[**QuizSubmissionsResponse**](QuizSubmissionsResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Get the quiz submission. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **quiz_submissions_api_time**
> quiz_submissions_api_time(course_id, id, quiz_id)

Get current quiz submission times.

Get the current timing data for the quiz attempt, both the end_at timestamp
and the time_left parameter.

<b>Responses</b>

* <b>200 OK</b> if the request was successful

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
    api_instance = canvas_lms_python_client.QuizSubmissionsApiApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    id = 'id_example' # str | Scope response to id
    quiz_id = 'quiz_id_example' # str | Scope response to quiz_id

    try:
        # Get current quiz submission times.
        await api_instance.quiz_submissions_api_time(course_id, id, quiz_id)
    except Exception as e:
        print("Exception when calling QuizSubmissionsApiApi->quiz_submissions_api_time: %s\n" % e)
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
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Get current quiz submission times. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **quiz_submissions_api_update**
> QuizSubmissionsResponse quiz_submissions_api_update(course_id, id, quiz_id, quiz_submissions_api_update_request=quiz_submissions_api_update_request)

Update student question scores and comments.

Update the amount of points a student has scored for questions they've
answered, provide comments for the student about their answer(s), or simply
fudge the total score by a specific amount of points.

<b>Responses</b>

* <b>200 OK</b> if the request was successful
* <b>403 Forbidden</b> if you are not a teacher in this course
* <b>400 Bad Request</b> if the attempt parameter is missing or invalid
* <b>400 Bad Request</b> if the specified QS attempt is not yet complete

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.quiz_submissions_api_update_request import QuizSubmissionsApiUpdateRequest
from canvas_lms_python_client.models.quiz_submissions_response import QuizSubmissionsResponse
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
    api_instance = canvas_lms_python_client.QuizSubmissionsApiApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    id = 'id_example' # str | Scope response to id
    quiz_id = 'quiz_id_example' # str | Scope response to quiz_id
    quiz_submissions_api_update_request = canvas_lms_python_client.QuizSubmissionsApiUpdateRequest() # QuizSubmissionsApiUpdateRequest | Request body parameters  **Example Request:** ``` {   \"quiz_submissions\": [{     \"attempt\": 1,     \"fudge_points\": -2.4,     \"questions\": {       \"1\": {         \"score\": 2.5,         \"comment\": \"This can't be right, but I'll let it pass this one time.\"       },       \"2\": {         \"score\": 0,         \"comment\": \"Good thinking. Almost!\"       }     }   }] } ``` (optional)

    try:
        # Update student question scores and comments.
        api_response = await api_instance.quiz_submissions_api_update(course_id, id, quiz_id, quiz_submissions_api_update_request=quiz_submissions_api_update_request)
        print("The response of QuizSubmissionsApiApi->quiz_submissions_api_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuizSubmissionsApiApi->quiz_submissions_api_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **id** | **str**| Scope response to id | 
 **quiz_id** | **str**| Scope response to quiz_id | 
 **quiz_submissions_api_update_request** | [**QuizSubmissionsApiUpdateRequest**](QuizSubmissionsApiUpdateRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; {   \&quot;quiz_submissions\&quot;: [{     \&quot;attempt\&quot;: 1,     \&quot;fudge_points\&quot;: -2.4,     \&quot;questions\&quot;: {       \&quot;1\&quot;: {         \&quot;score\&quot;: 2.5,         \&quot;comment\&quot;: \&quot;This can&#39;t be right, but I&#39;ll let it pass this one time.\&quot;       },       \&quot;2\&quot;: {         \&quot;score\&quot;: 0,         \&quot;comment\&quot;: \&quot;Good thinking. Almost!\&quot;       }     }   }] } &#x60;&#x60;&#x60; | [optional] 

### Return type

[**QuizSubmissionsResponse**](QuizSubmissionsResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Update student question scores and comments. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

