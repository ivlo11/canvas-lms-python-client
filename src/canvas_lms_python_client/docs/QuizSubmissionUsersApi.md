# canvas_lms_python_client.QuizSubmissionUsersApi

All URIs are relative to *https://canvas.instructure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**quiz_submission_users_message**](QuizSubmissionUsersApi.md#quiz_submission_users_message) | **POST** /api/v1/courses/{course_id}/quizzes/{id}/submission_users/message | Send a message to unsubmitted or submitted users for the quiz


# **quiz_submission_users_message**
> QuizzesQuizSubmissionUsersMessageResponse quiz_submission_users_message(course_id, id, quiz_submission_users_message_request=quiz_submission_users_message_request)

Send a message to unsubmitted or submitted users for the quiz

{
  "body": {
    "type": "string",
    "description": "message body of the conversation to be created",
    "example": "Please take the quiz."
  },
  "recipients": {
    "type": "string",
    "description": "Who to send the message to. May be either 'submitted' or 'unsubmitted'",
    "example": "submitted"
  },
  "subject": {
    "type": "string",
    "description": "Subject of the new Conversation created",
    "example": "ATTN: Quiz 101 Students"
  }
}

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.quiz_submission_users_message_request import QuizSubmissionUsersMessageRequest
from canvas_lms_python_client.models.quizzes_quiz_submission_users_message_response import QuizzesQuizSubmissionUsersMessageResponse
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
    api_instance = canvas_lms_python_client.QuizSubmissionUsersApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    id = 'id_example' # str | Scope response to id
    quiz_submission_users_message_request = canvas_lms_python_client.QuizSubmissionUsersMessageRequest() # QuizSubmissionUsersMessageRequest | Request body parameters (optional)

    try:
        # Send a message to unsubmitted or submitted users for the quiz
        api_response = await api_instance.quiz_submission_users_message(course_id, id, quiz_submission_users_message_request=quiz_submission_users_message_request)
        print("The response of QuizSubmissionUsersApi->quiz_submission_users_message:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuizSubmissionUsersApi->quiz_submission_users_message: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **id** | **str**| Scope response to id | 
 **quiz_submission_users_message_request** | [**QuizSubmissionUsersMessageRequest**](QuizSubmissionUsersMessageRequest.md)| Request body parameters | [optional] 

### Return type

[**QuizzesQuizSubmissionUsersMessageResponse**](QuizzesQuizSubmissionUsersMessageResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | QuizzesQuizSubmissionUsersMessageResponse |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

