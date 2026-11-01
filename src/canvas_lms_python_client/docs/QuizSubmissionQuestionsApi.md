# canvas_lms_python_client.QuizSubmissionQuestionsApi

All URIs are relative to *https://canvas.instructure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**quiz_submission_questions_answer**](QuizSubmissionQuestionsApi.md#quiz_submission_questions_answer) | **POST** /api/v1/quiz_submissions/{quiz_submission_id}/questions | Answering questions
[**quiz_submission_questions_flag**](QuizSubmissionQuestionsApi.md#quiz_submission_questions_flag) | **PUT** /api/v1/quiz_submissions/{quiz_submission_id}/questions/{id}/flag | Flagging a question.
[**quiz_submission_questions_formatted_answer**](QuizSubmissionQuestionsApi.md#quiz_submission_questions_formatted_answer) | **GET** /api/v1/quiz_submissions/{quiz_submission_id}/questions/{id}/formatted_answer | Get a formatted student numerical answer.
[**quiz_submission_questions_index**](QuizSubmissionQuestionsApi.md#quiz_submission_questions_index) | **GET** /api/v1/quiz_submissions/{quiz_submission_id}/questions | Get all quiz submission questions.
[**quiz_submission_questions_unflag**](QuizSubmissionQuestionsApi.md#quiz_submission_questions_unflag) | **PUT** /api/v1/quiz_submissions/{quiz_submission_id}/questions/{id}/unflag | Unflagging a question.


# **quiz_submission_questions_answer**
> List[QuizSubmissionQuestion] quiz_submission_questions_answer(quiz_submission_id, quiz_submission_questions_answer_request=quiz_submission_questions_answer_request)

Answering questions

Provide or update an answer to one or more QuizQuestions.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.quiz_submission_question import QuizSubmissionQuestion
from canvas_lms_python_client.models.quiz_submission_questions_answer_request import QuizSubmissionQuestionsAnswerRequest
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
    api_instance = canvas_lms_python_client.QuizSubmissionQuestionsApi(api_client)
    quiz_submission_id = 'quiz_submission_id_example' # str | Scope response to quiz_submission_id
    quiz_submission_questions_answer_request = canvas_lms_python_client.QuizSubmissionQuestionsAnswerRequest() # QuizSubmissionQuestionsAnswerRequest | Request body parameters  **Example Request:** ``` {   \"attempt\": 1,   \"validation_token\": \"YOUR_VALIDATION_TOKEN\",   \"access_code\": null,   \"quiz_questions\": [{     \"id\": \"1\",     \"answer\": \"Hello World!\"   }, {     \"id\": \"2\",     \"answer\": 42.0   }] } ``` (optional)

    try:
        # Answering questions
        api_response = await api_instance.quiz_submission_questions_answer(quiz_submission_id, quiz_submission_questions_answer_request=quiz_submission_questions_answer_request)
        print("The response of QuizSubmissionQuestionsApi->quiz_submission_questions_answer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuizSubmissionQuestionsApi->quiz_submission_questions_answer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quiz_submission_id** | **str**| Scope response to quiz_submission_id | 
 **quiz_submission_questions_answer_request** | [**QuizSubmissionQuestionsAnswerRequest**](QuizSubmissionQuestionsAnswerRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; {   \&quot;attempt\&quot;: 1,   \&quot;validation_token\&quot;: \&quot;YOUR_VALIDATION_TOKEN\&quot;,   \&quot;access_code\&quot;: null,   \&quot;quiz_questions\&quot;: [{     \&quot;id\&quot;: \&quot;1\&quot;,     \&quot;answer\&quot;: \&quot;Hello World!\&quot;   }, {     \&quot;id\&quot;: \&quot;2\&quot;,     \&quot;answer\&quot;: 42.0   }] } &#x60;&#x60;&#x60; | [optional] 

### Return type

[**List[QuizSubmissionQuestion]**](QuizSubmissionQuestion.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **quiz_submission_questions_flag**
> quiz_submission_questions_flag(id, quiz_submission_id, quiz_submission_questions_flag_request=quiz_submission_questions_flag_request)

Flagging a question.

Set a flag on a quiz question to indicate that you want to return to it
later.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.quiz_submission_questions_flag_request import QuizSubmissionQuestionsFlagRequest
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
    api_instance = canvas_lms_python_client.QuizSubmissionQuestionsApi(api_client)
    id = 'id_example' # str | Scope response to id
    quiz_submission_id = 'quiz_submission_id_example' # str | Scope response to quiz_submission_id
    quiz_submission_questions_flag_request = canvas_lms_python_client.QuizSubmissionQuestionsFlagRequest() # QuizSubmissionQuestionsFlagRequest | Request body parameters  **Example Request:** ``` {   \"attempt\": 1,   \"validation_token\": \"YOUR_VALIDATION_TOKEN\",   \"access_code\": null } ``` (optional)

    try:
        # Flagging a question.
        await api_instance.quiz_submission_questions_flag(id, quiz_submission_id, quiz_submission_questions_flag_request=quiz_submission_questions_flag_request)
    except Exception as e:
        print("Exception when calling QuizSubmissionQuestionsApi->quiz_submission_questions_flag: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Scope response to id | 
 **quiz_submission_id** | **str**| Scope response to quiz_submission_id | 
 **quiz_submission_questions_flag_request** | [**QuizSubmissionQuestionsFlagRequest**](QuizSubmissionQuestionsFlagRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; {   \&quot;attempt\&quot;: 1,   \&quot;validation_token\&quot;: \&quot;YOUR_VALIDATION_TOKEN\&quot;,   \&quot;access_code\&quot;: null } &#x60;&#x60;&#x60; | [optional] 

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
**0** | Flagging a question. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **quiz_submission_questions_formatted_answer**
> quiz_submission_questions_formatted_answer(id, quiz_submission_id, answer)

Get a formatted student numerical answer.

Matches the intended behavior of the UI when a numerical answer is entered
and returns the resulting formatted number

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
    api_instance = canvas_lms_python_client.QuizSubmissionQuestionsApi(api_client)
    id = 'id_example' # str | Scope response to id
    quiz_submission_id = 'quiz_submission_id_example' # str | Scope response to quiz_submission_id
    answer = 3.4 # float | 

    try:
        # Get a formatted student numerical answer.
        await api_instance.quiz_submission_questions_formatted_answer(id, quiz_submission_id, answer)
    except Exception as e:
        print("Exception when calling QuizSubmissionQuestionsApi->quiz_submission_questions_formatted_answer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Scope response to id | 
 **quiz_submission_id** | **str**| Scope response to quiz_submission_id | 
 **answer** | **float**|  | 

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
**0** | Get a formatted student numerical answer. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **quiz_submission_questions_index**
> QuizSubmissionQuestionsResponse quiz_submission_questions_index(quiz_submission_id, include=include)

Get all quiz submission questions.

Get a list of all the question records for this quiz submission.

<b>200 OK</b> response code is returned if the request was successful.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.quiz_submission_questions_response import QuizSubmissionQuestionsResponse
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
    api_instance = canvas_lms_python_client.QuizSubmissionQuestionsApi(api_client)
    quiz_submission_id = 'quiz_submission_id_example' # str | Scope response to quiz_submission_id
    include = ['include_example'] # List[str] | Associations to include with the quiz submission question. (optional)

    try:
        # Get all quiz submission questions.
        api_response = await api_instance.quiz_submission_questions_index(quiz_submission_id, include=include)
        print("The response of QuizSubmissionQuestionsApi->quiz_submission_questions_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuizSubmissionQuestionsApi->quiz_submission_questions_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quiz_submission_id** | **str**| Scope response to quiz_submission_id | 
 **include** | [**List[str]**](str.md)| Associations to include with the quiz submission question. | [optional] 

### Return type

[**QuizSubmissionQuestionsResponse**](QuizSubmissionQuestionsResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Get all quiz submission questions. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **quiz_submission_questions_unflag**
> quiz_submission_questions_unflag(id, quiz_submission_id, quiz_submission_questions_flag_request=quiz_submission_questions_flag_request)

Unflagging a question.

Remove the flag that you previously set on a quiz question after you've
returned to it.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.quiz_submission_questions_flag_request import QuizSubmissionQuestionsFlagRequest
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
    api_instance = canvas_lms_python_client.QuizSubmissionQuestionsApi(api_client)
    id = 'id_example' # str | Scope response to id
    quiz_submission_id = 'quiz_submission_id_example' # str | Scope response to quiz_submission_id
    quiz_submission_questions_flag_request = canvas_lms_python_client.QuizSubmissionQuestionsFlagRequest() # QuizSubmissionQuestionsFlagRequest | Request body parameters  **Example Request:** ``` {   \"attempt\": 1,   \"validation_token\": \"YOUR_VALIDATION_TOKEN\",   \"access_code\": null } ``` (optional)

    try:
        # Unflagging a question.
        await api_instance.quiz_submission_questions_unflag(id, quiz_submission_id, quiz_submission_questions_flag_request=quiz_submission_questions_flag_request)
    except Exception as e:
        print("Exception when calling QuizSubmissionQuestionsApi->quiz_submission_questions_unflag: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Scope response to id | 
 **quiz_submission_id** | **str**| Scope response to quiz_submission_id | 
 **quiz_submission_questions_flag_request** | [**QuizSubmissionQuestionsFlagRequest**](QuizSubmissionQuestionsFlagRequest.md)| Request body parameters  **Example Request:** &#x60;&#x60;&#x60; {   \&quot;attempt\&quot;: 1,   \&quot;validation_token\&quot;: \&quot;YOUR_VALIDATION_TOKEN\&quot;,   \&quot;access_code\&quot;: null } &#x60;&#x60;&#x60; | [optional] 

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
**0** | Unflagging a question. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

