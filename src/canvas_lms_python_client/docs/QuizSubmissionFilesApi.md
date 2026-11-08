# canvas_lms_python_client.QuizSubmissionFilesApi

All URIs are relative to *https://canvas.instructure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**quiz_submission_files_create**](QuizSubmissionFilesApi.md#quiz_submission_files_create) | **POST** /api/v1/courses/{course_id}/quizzes/{quiz_id}/submissions/self/files | Upload a file


# **quiz_submission_files_create**
> QuizzesQuizSubmissionFilesCreateResponse quiz_submission_files_create(course_id, quiz_id, quiz_submission_files_create_request=quiz_submission_files_create_request)

Upload a file

Associate a new quiz submission file

This API endpoint is the first step in uploading a quiz submission file.
See the {file:file.file_uploads.html File Upload Documentation} for details on
the file upload workflow as these parameters are interpreted as per the
documentation there.

### Example

* Bearer (token) Authentication (bearer):

```python
import canvas_lms_python_client
from canvas_lms_python_client.models.quiz_submission_files_create_request import QuizSubmissionFilesCreateRequest
from canvas_lms_python_client.models.quizzes_quiz_submission_files_create_response import QuizzesQuizSubmissionFilesCreateResponse
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
    api_instance = canvas_lms_python_client.QuizSubmissionFilesApi(api_client)
    course_id = 'course_id_example' # str | Scope response to course_id
    quiz_id = 'quiz_id_example' # str | Scope response to quiz_id
    quiz_submission_files_create_request = canvas_lms_python_client.QuizSubmissionFilesCreateRequest() # QuizSubmissionFilesCreateRequest | Request body parameters (optional)

    try:
        # Upload a file
        api_response = await api_instance.quiz_submission_files_create(course_id, quiz_id, quiz_submission_files_create_request=quiz_submission_files_create_request)
        print("The response of QuizSubmissionFilesApi->quiz_submission_files_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuizSubmissionFilesApi->quiz_submission_files_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Scope response to course_id | 
 **quiz_id** | **str**| Scope response to quiz_id | 
 **quiz_submission_files_create_request** | [**QuizSubmissionFilesCreateRequest**](QuizSubmissionFilesCreateRequest.md)| Request body parameters | [optional] 

### Return type

[**QuizzesQuizSubmissionFilesCreateResponse**](QuizzesQuizSubmissionFilesCreateResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | QuizzesQuizSubmissionFilesCreateResponse |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

