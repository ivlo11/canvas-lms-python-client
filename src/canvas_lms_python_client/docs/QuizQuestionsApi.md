# canvas_lms_python_client.QuizQuestionsApi

All URIs are relative to *https://canvas.instructure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**quiz_questions_create**](QuizQuestionsApi.md#quiz_questions_create) | **POST** /api/v1/courses/{course_id}/quizzes/{quiz_id}/questions | Create a single quiz question
[**quiz_questions_destroy**](QuizQuestionsApi.md#quiz_questions_destroy) | **DELETE** /api/v1/courses/{course_id}/quizzes/{quiz_id}/questions/{id} | Delete a quiz question
[**quiz_questions_index**](QuizQuestionsApi.md#quiz_questions_index) | **GET** /api/v1/courses/{course_id}/quizzes/{quiz_id}/questions | List questions in a quiz or a submission
[**quiz_questions_show**](QuizQuestionsApi.md#quiz_questions_show) | **GET** /api/v1/courses/{course_id}/quizzes/{quiz_id}/questions/{id} | Get a single quiz question
[**quiz_questions_update**](QuizQuestionsApi.md#quiz_questions_update) | **PUT** /api/v1/courses/{course_id}/quizzes/{quiz_id}/questions/{id} | Update an existing quiz question


# **quiz_questions_create**
> QuizQuestion quiz_questions_create(course_id, quiz_id, quiz_questions_create_request=quiz_questions_create_request)

Create a single quiz question

Create a new quiz question for this quiz

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.quiz_question import QuizQuestion
from canvas_lms_python_client.models.quiz_questions_create_request import QuizQuestionsCreateRequest
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
    api_instance = canvas_lms_python_client.QuizQuestionsApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    quiz_id = 'quiz_id_example' # str | Scope response to quiz_id
    quiz_questions_create_request = canvas_lms_python_client.QuizQuestionsCreateRequest() # QuizQuestionsCreateRequest | Request body parameters (optional)

    try:
        # Create a single quiz question
        api_response = await api_instance.quiz_questions_create(course_id, quiz_id, quiz_questions_create_request=quiz_questions_create_request)
        print("The response of QuizQuestionsApi->quiz_questions_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuizQuestionsApi->quiz_questions_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **quiz_id** | **str**| Scope response to quiz_id | 
 **quiz_questions_create_request** | [**QuizQuestionsCreateRequest**](QuizQuestionsCreateRequest.md)| Request body parameters | [optional] 

### Return type

[**QuizQuestion**](QuizQuestion.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | QuizQuestion |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **quiz_questions_destroy**
> quiz_questions_destroy(course_id, id, quiz_id)

Delete a quiz question

<b>204 No Content</b> response code is returned if the deletion was successful.

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
    api_instance = canvas_lms_python_client.QuizQuestionsApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    id = 'id_example' # str | The quiz question's unique identifier
    quiz_id = 'quiz_id_example' # str | The associated quiz's unique identifier

    try:
        # Delete a quiz question
        await api_instance.quiz_questions_destroy(course_id, id, quiz_id)
    except Exception as e:
        print("Exception when calling QuizQuestionsApi->quiz_questions_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **id** | **str**| The quiz question&#39;s unique identifier | 
 **quiz_id** | **str**| The associated quiz&#39;s unique identifier | 

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
**0** | Delete a quiz question |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **quiz_questions_index**
> List[QuizQuestion] quiz_questions_index(course_id, quiz_id, quiz_submission_id=quiz_submission_id, quiz_submission_attempt=quiz_submission_attempt, page=page, per_page=per_page)

List questions in a quiz or a submission

Returns the paginated list of QuizQuestions in this quiz.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.quiz_question import QuizQuestion
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
    api_instance = canvas_lms_python_client.QuizQuestionsApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    quiz_id = 'quiz_id_example' # str | Scope response to quiz_id
    quiz_submission_id = 56 # int | If specified, the endpoint will return the questions that were presented for that submission. This is useful if the quiz has been modified after the submission was created and the latest quiz version's set of questions does not match the submission's. NOTE: you must specify quiz_submission_attempt as well if you specify this parameter. (optional)
    quiz_submission_attempt = 56 # int | The attempt of the submission you want the questions for. (optional)
    page = 56 # int | The page number to return. Defaults to 1. (optional)
    per_page = 56 # int | The number of items to return per page. Defaults to 10. Maximum is 100. (optional)

    try:
        # List questions in a quiz or a submission
        api_response = await api_instance.quiz_questions_index(course_id, quiz_id, quiz_submission_id=quiz_submission_id, quiz_submission_attempt=quiz_submission_attempt, page=page, per_page=per_page)
        print("The response of QuizQuestionsApi->quiz_questions_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuizQuestionsApi->quiz_questions_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **quiz_id** | **str**| Scope response to quiz_id | 
 **quiz_submission_id** | **int**| If specified, the endpoint will return the questions that were presented for that submission. This is useful if the quiz has been modified after the submission was created and the latest quiz version&#39;s set of questions does not match the submission&#39;s. NOTE: you must specify quiz_submission_attempt as well if you specify this parameter. | [optional] 
 **quiz_submission_attempt** | **int**| The attempt of the submission you want the questions for. | [optional] 
 **page** | **int**| The page number to return. Defaults to 1. | [optional] 
 **per_page** | **int**| The number of items to return per page. Defaults to 10. Maximum is 100. | [optional] 

### Return type

[**List[QuizQuestion]**](QuizQuestion.md)

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

# **quiz_questions_show**
> QuizQuestion quiz_questions_show(course_id, id, quiz_id)

Get a single quiz question

Returns the quiz question with the given id

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.quiz_question import QuizQuestion
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
    api_instance = canvas_lms_python_client.QuizQuestionsApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    id = 'id_example' # str | The quiz question unique identifier.
    quiz_id = 'quiz_id_example' # str | Scope response to quiz_id

    try:
        # Get a single quiz question
        api_response = await api_instance.quiz_questions_show(course_id, id, quiz_id)
        print("The response of QuizQuestionsApi->quiz_questions_show:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuizQuestionsApi->quiz_questions_show: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **id** | **str**| The quiz question unique identifier. | 
 **quiz_id** | **str**| Scope response to quiz_id | 

### Return type

[**QuizQuestion**](QuizQuestion.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | QuizQuestion |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **quiz_questions_update**
> QuizQuestion quiz_questions_update(course_id, id, quiz_id, quiz_questions_create_request=quiz_questions_create_request)

Update an existing quiz question

Updates an existing quiz question for this quiz

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.quiz_question import QuizQuestion
from canvas_lms_python_client.models.quiz_questions_create_request import QuizQuestionsCreateRequest
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
    api_instance = canvas_lms_python_client.QuizQuestionsApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    id = 'id_example' # str | The quiz question's unique identifier.
    quiz_id = 'quiz_id_example' # str | The associated quiz's unique identifier.
    quiz_questions_create_request = canvas_lms_python_client.QuizQuestionsCreateRequest() # QuizQuestionsCreateRequest | Request body parameters (optional)

    try:
        # Update an existing quiz question
        api_response = await api_instance.quiz_questions_update(course_id, id, quiz_id, quiz_questions_create_request=quiz_questions_create_request)
        print("The response of QuizQuestionsApi->quiz_questions_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuizQuestionsApi->quiz_questions_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **id** | **str**| The quiz question&#39;s unique identifier. | 
 **quiz_id** | **str**| The associated quiz&#39;s unique identifier. | 
 **quiz_questions_create_request** | [**QuizQuestionsCreateRequest**](QuizQuestionsCreateRequest.md)| Request body parameters | [optional] 

### Return type

[**QuizQuestion**](QuizQuestion.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | QuizQuestion |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

